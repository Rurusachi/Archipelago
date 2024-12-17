from typing import TYPE_CHECKING, Dict, Set, Tuple, List
import struct

from NetUtils import ClientStatus
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient
from .locations import (QuestGroups, BazaarRecipeGroups, bitflags)
from .data import (get_flag, FlagOffsets, MemoryAddresses)
from .items import (jobUnlockOffset)

import asyncio
import Utils
from worlds.LauncherComponents import Component, SuffixIdentifier, Type, components, launch_subprocess


if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext
else:
    BizHawkClientContext = object

clientRegistered = False
for component in components:
    if component.script_name == "BizHawkClientUniversalTracker":
        component.file_identifier = SuffixIdentifier(*(*component.file_identifier.suffixes, ".apffta2"))
        clientRegistered = True
        break

if not clientRegistered:
    def my_launch(*launch_args) -> None:
        from CommonClient import get_base_parser, server_loop, logger, gui_enabled
        from worlds._bizhawk.context import BizHawkClientContext, BizHawkClientCommandProcessor, _patch_and_run_game, _game_watcher

        tracker_loaded = False
        try:
            from worlds.tracker.TrackerClient import TrackerGameContext as SuperContext
            from worlds.tracker.TrackerClient import TrackerCommandProcessor as SuperCommandProcessor
            tracker_loaded = True
        except ModuleNotFoundError:
            from CommonClient import CommonContext as SuperContext
            from CommonClient import ClientCommandProcessor as SuperCommandProcessor

        async def main():
            parser = get_base_parser()
            parser.add_argument("patch_file", default="", type=str, nargs="?", help="Path to an Archipelago patch file")
            args = parser.parse_args(launch_args)

            class MyClientCommandProcessor(BizHawkClientCommandProcessor, SuperCommandProcessor):
                pass

            class MyClientContext(BizHawkClientContext, SuperContext):
                command_processor = MyClientCommandProcessor

                def on_package(self, cmd, args):
                    super().on_package(cmd, args)
                    if tracker_loaded:
                        SuperContext.on_package(self, cmd, args)

            ctx = MyClientContext(args.connect, args.password)
            ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")
            if tracker_loaded:
                ctx.run_generator()
            if gui_enabled:
                ctx.run_gui()
            ctx.run_cli()

            if args.patch_file != "":
                Utils.async_start(_patch_and_run_game(args.patch_file))

            watcher_task = asyncio.create_task(_game_watcher(ctx), name="GameWatcher")

            try:
                await watcher_task
            except Exception as e:
                logger.exception(e)

            await ctx.exit_event.wait()
            await ctx.shutdown()

        Utils.init_logging("BizHawkClientUniversalTracker", exception_logger="Client")
        import colorama
        colorama.init()
        asyncio.run(main())
        colorama.deinit()

    def my_launch_client(*args) -> None:
        launch_subprocess(my_launch, name="BizHawkClientUniversalTracker", args=args)

    component = Component("BizHawk Client + Universal Tracker", "BizHawkClientUniversalTracker",
                          component_type=Type.CLIENT, func=my_launch_client,
                          file_identifier=SuffixIdentifier(".apffta2"))
    components.append(component)


class FFTA2Client(BizHawkClient):
    game = "Final Fantasy Tactics A2"
    system = "NDS"
    local_checked_locations: Set[int]
    local_set_events: Dict[str, bool]
    goal_flag: Tuple[int, int]  # Byte, bit
    goal_id: int = 0
    path_end_quests: List[Tuple[int, int]]
    paths_required: int

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()
        self.local_set_events = {}
        self.path_end_quests = []
        self.goal_flag = (0, 0)

    async def validate_rom(self, ctx: BizHawkClientContext) -> bool:
        try:
            game_name_bytes = ((await bizhawk.read(ctx.bizhawk_ctx, [(0x3ffa80, 0x8, "Main RAM")]))[0])
            game_name = bytes([byte for byte in game_name_bytes]).decode("ascii")

            print('Game name for validate rom ' + game_name)
            if game_name != "FFTA2-NA":
                return False
        except UnicodeDecodeError:
            return False
        except bizhawk.RequestFailedError:
            return False  # Should verify on the next pass

        ctx.game = self.game
        print('context is registered for FFTA2')
        print(ctx.game)
        ctx.items_handling = 0b101
        ctx.want_slot_data = True
        return True

    async def game_watcher(self, ctx: BizHawkClientContext) -> None:
        if ctx.slot_data is not None:
            self.path_end_quests = ctx.slot_data["path_end_quests"]
            self.paths_required = ctx.slot_data["paths_required"]
            self.goal_flag = ctx.slot_data["goal_flag"]
            self.loot_amount = ctx.slot_data["loot_amount"]

        try:
            flag_list = [(MemoryAddresses.quest_flags, 0x40, "ARM9 System Bus"),
                         (MemoryAddresses.received_items, 2, "ARM9 System Bus"), (MemoryAddresses.event_var, 1, "ARM9 System Bus"),
                         (MemoryAddresses.custom_flags, 0x7, "ARM9 System Bus"),
                         (MemoryAddresses.inventory, 0x27a * 4, "ARM9 System Bus"),
                         (MemoryAddresses.shop_flags, 0x35, "ARM9 System Bus"),
                         #(MemoryAddresses.region_flags, 20, "ARM9 System Bus"),
                         ]
            read_result = await bizhawk.read(ctx.bizhawk_ctx, flag_list)
            quest_flag_bytes = read_result[0]
            received_items = int.from_bytes(read_result[1], "little")
            # inventory_bytes = read_result[4]
            shop_flag_bytes = read_result[5]
            #region_location_flags = read_result[5]

            await bizhawk.write(ctx.bizhawk_ctx,
                                [(MemoryAddresses.region_flags, bytes([0xFF]*20), "ARM9 System Bus"),])

            # inventory_items = [(int.from_bytes(inventory_bytes[i:i+2], "little"), inventory_bytes[i+2], inventory_bytes[i+3]) for i in range(0, len(inventory_bytes), 4)]
            # for i, item in enumerate(inventory_items):
            #     if item[0] in [0x00F5] and (item[1] > 0 or item[2] > 0):
            #         await bizhawk.write(ctx.bizhawk_ctx, [(MemoryAddresses.inventory + i*4 + 2, bytes([0x00, 0x00]), "ARM9 System Bus")])

            local_checked_locations = set()
            game_clear = False

            # Check if goal status is reached
            if quest_flag_bytes[self.goal_flag[0]] & bitflags[self.goal_flag[1]] == bitflags[self.goal_flag[1]]:
                game_clear = True

            # Check set flags
            for byte_i, byte in enumerate(quest_flag_bytes):

                for i in range(8):

                    if byte & (1 << i) == bitflags[i]:

                        for quest in QuestGroups:
                            if byte & (1 << i) == quest[1] and byte_i == quest[2]:
                                for questLocation in quest[0]:
                                    location_id = questLocation.rom_address
                                    if location_id in ctx.server_locations:
                                        local_checked_locations.add(location_id)

            for byte_i, byte in enumerate(shop_flag_bytes):
                for i in range(8):

                    if byte & (1 << i) == bitflags[i]:

                        for recipe in BazaarRecipeGroups:
                            if byte & (1 << i) == recipe[1] and byte_i == recipe[2]:
                                location_id = recipe[0].rom_address
                                if location_id in ctx.server_locations:
                                    local_checked_locations.add(location_id)

            custom_flag_bytes = list(read_result[3])
            # Send locations
            if local_checked_locations != self.local_checked_locations:
                self.local_checked_locations = local_checked_locations
                paths_completed = len([location for location in local_checked_locations if ctx.location_names.lookup_in_game(location) in self.path_end_quests])
                if paths_completed >= self.paths_required:
                    flag = get_flag(0, FlagOffsets.FinalQuest)
                    custom_flag_bytes[flag[0]-FlagOffsets.FinalQuest[0]] |= 1 << flag[1]
                    await bizhawk.write(ctx.bizhawk_ctx,
                                        [(MemoryAddresses.custom_flags, bytes(custom_flag_bytes), "ARM9 System Bus"),])

                if local_checked_locations is not None:
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": list(local_checked_locations)
                    }])

            if not ctx.finished_game and game_clear:
                await ctx.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": ClientStatus.CLIENT_GOAL
                }])

            if received_items < len(ctx.items_received):
                next_item = ctx.items_received[received_items]
                next_item_id = next_item.item

                guard_list = [(MemoryAddresses.event_var, [0x0], "ARM9 System Bus"),
                              (0x021c482c, bytes([0x50, 0x48, 0x1C, 0x02]), "ARM9 System Bus"),
                              (0x0212ef48, bytes([0xff, 0xff, 0xff, 0xff]), "ARM9 System Bus"),]

                if next_item_id > jobUnlockOffset:

                    flag = get_flag(next_item_id - jobUnlockOffset - 1, FlagOffsets.JobItems)
                    custom_flag_bytes[flag[0]-FlagOffsets.JobItems[0]] |= 1 << flag[1]
                    await bizhawk.guarded_write(ctx.bizhawk_ctx,
                                                [(MemoryAddresses.custom_flags, bytes(custom_flag_bytes), "ARM9 System Bus"),
                                                 (MemoryAddresses.received_items, (received_items + 1).to_bytes(2, "little"), "ARM9 System Bus"),
                                                 ], guard_list)
                    next_item_id = 0
                if next_item_id >= 0x01AF and next_item_id <= 0x0265:
                    # Extra loot items
                    amount = self.loot_amount
                else:
                    amount = 1

                item_event = \
                    bytes([0x04, 0x00, 0x00, 0x00, 0x33, 0x00]) + \
                    struct.pack("<HB", next_item_id, amount) + \
                    bytes([0x1e, 0x00, 0xff, 0xff])
                if next_item_id != 0:
                    await bizhawk.guarded_write(ctx.bizhawk_ctx,
                                                [
                                                    (0x212D71C, [0x0], "ARM9 System Bus"),
                                                    (0x0212ef48, struct.pack("<I", 0x0212d760), "ARM9 System Bus"),
                                                    (0x0212d760, item_event, "ARM9 System Bus"),
                                                    (MemoryAddresses.event_var, [0x1], "ARM9 System Bus"),
                                                    (MemoryAddresses.received_items, (received_items + 1).to_bytes(2, "little"), "ARM9 System Bus"),
                                                ], guard_list)

        except bizhawk.RequestFailedError:
            # Exit handler and return to main loop to reconnect
            pass
