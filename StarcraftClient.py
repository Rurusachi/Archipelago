from __future__ import annotations

import sys
import multiprocessing
import logging
import asyncio
import nest_asyncio

import sc2

from sc2.main import run_game
from sc2.data import Race
from sc2.bot_ai import BotAI
from sc2.player import Bot
from worlds.sc2wol.Items import lookup_id_to_name, item_table
from worlds.sc2wol.Locations import SC2WOL_LOC_ID_OFFSET

from Utils import init_logging

if __name__ == "__main__":
    init_logging("SC2Client", exception_logger="Client")

logger = logging.getLogger("Client")
sc2_logger = logging.getLogger("Starcraft2")

import colorama

from NetUtils import *
from CommonClient import CommonContext, server_loop, console_loop, ClientCommandProcessor, gui_enabled, get_base_parser

nest_asyncio.apply()

class StarcraftClientProcessor(ClientCommandProcessor):
    ctx: Context

    def _cmd_play(self, mission_id: str = "") -> bool:
        """Start a Starcraft 2 mission"""

        options = mission_id.split()
        num_options = len(options)

        if num_options > 0:
            mission_number = int(options[0])

            if is_mission_available(mission_number, self.ctx.checked_locations, mission_req_table):
                asyncio.create_task(starcraft_launch(self.ctx, mission_number), name="Starcraft Launch")
            else:
                sc2_logger.info(
                    "This mission is not currently unlocked.  Use /unfinished or /available to see what is available.")

        else:
            sc2_logger.info("Mission ID needs to be specified.  Use /unfinished or /available to view ids for available missions.")

        return True

    def _cmd_available(self) -> bool:
        """Get what missions are currently available to play"""

        request_available_missions(self.ctx.checked_locations, mission_req_table)
        return True

    def _cmd_unfinished(self) -> bool:
        """Get what missions are currently available to play and have not had all locations checked"""

        request_unfinished_missions(self.ctx.checked_locations, mission_req_table)
        return True


class Context(CommonContext):
    command_processor = StarcraftClientProcessor
    game = "Starcraft 2 Wings of Liberty"
    items_handling = 0b111
    difficulty = -1
    all_in_choice = 0
    items_rec_to_announce = []
    rec_announce_pos = 0
    items_sent_to_announce = []
    sent_announce_pos = 0
    announcements = []
    announcement_pos = 0

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(Context, self).server_auth(password_requested)
        if not self.auth:
            logger.info('Enter slot name:')
            self.auth = await self.console_input()

        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd in {"Connected"}:
            self.difficulty = args["slot_data"]["game_difficulty"]
            self.all_in_choice = args["slot_data"]["all_in_map"]
        if cmd in {"PrintJSON"}:
            noted = False
            if "receiving" in args:
                if args["receiving"] == self.slot:
                    self.announcements.append(args["data"])
                    noted = True
            if not noted and "item" in args:
                if args["item"].player == self.slot:
                    self.announcements.append(args["data"])

    def run_gui(self):
        from kvui import GameManager

        class SC2Manager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago"),
                ("Starcraft2", "Starcraft2"),
            ]
            base_title = "Archipelago Starcraft 2 Client"

        self.ui = SC2Manager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


async def main():
    multiprocessing.freeze_support()
    parser = get_base_parser()
    parser.add_argument('--loglevel', default='info', choices=['debug', 'info', 'warning', 'error', 'critical'])
    args = parser.parse_args()

    ctx = Context(args.connect, args.password)
    if ctx.server_task is None:
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")

    input_task = None
    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()

    if sys.stdin:
        input_task = asyncio.create_task(console_loop(ctx), name="Input")

    await ctx.exit_event.wait()

    ctx.server_address = None
    ctx.snes_reconnect_address = None
    await ctx.shutdown()

    if ui_task:
        await ui_task

    if input_task:
        input_task.cancel()

maps_table = ["ap_traynor01", "ap_traynor02", "ap_traynor03", "ap_thanson01", "ap_thanson02", "ap_thanson03a", "ap_thanson03b", "ap_ttychus01",
              "ap_ttychus02", "ap_ttychus03", "ap_ttychus04", "ap_ttychus05", "ap_ttosh01", "ap_ttosh02", "ap_ttosh03a", "ap_ttosh03b",
              "ap_thorner01", "ap_thorner02", "ap_thorner03", "ap_thorner04", "ap_thorner05s", "ap_tzeratul01", "ap_tzeratul02",
              "ap_tzeratul03", "ap_tzeratul04", "ap_tvalerian01", "ap_tvalerian02a", "ap_tvalerian02b", "ap_tvalerian03"]


def calculate_items(items):
    unit_unlocks = 0
    armory1_unlocks = 0
    armory2_unlocks = 0
    upgrade_unlocks = 0
    building_unlocks = 0
    merc_unlocks = 0
    lab_unlocks = 0
    protoss_unlock = 0
    minerals = 0
    vespene = 0

    for item in items:
        data = lookup_id_to_name[item.item]

        if item_table[data].type == "Unit":
            unit_unlocks += (1 << item_table[data].number)
        elif item_table[data].type == "Upgrade":
            upgrade_unlocks += (1 << item_table[data].number)
        elif item_table[data].type == "Armory 1":
            armory1_unlocks += (1 << item_table[data].number)
        elif item_table[data].type == "Armory 2":
            armory2_unlocks += (1 << item_table[data].number)
        elif item_table[data].type == "Building":
            building_unlocks += (1 << item_table[data].number)
        elif item_table[data].type == "Mercenary":
            merc_unlocks += (1 << item_table[data].number)
        elif item_table[data].type == "Laboratory":
            lab_unlocks += (1 << item_table[data].number)
        elif item_table[data].type == "Protoss":
            protoss_unlock += (1 << item_table[data].number)
        elif item_table[data].type == "Minerals":
            minerals += item_table[data].number
        elif item_table[data].type == "Vespene":
            vespene += item_table[data].number

    return [unit_unlocks, upgrade_unlocks, armory1_unlocks, armory2_unlocks, building_unlocks, merc_unlocks,
            lab_unlocks, protoss_unlock, minerals, vespene]


def calc_difficulty(difficulty):
    if difficulty == 0:
        return 'C'
    elif difficulty == 1:
        return 'N'
    elif difficulty == 2:
        return 'H'
    elif difficulty == 3:
        return 'B'

    return 'X'


async def starcraft_launch(ctx: Context, mission_id):
    ctx.rec_announce_pos = len(ctx.items_rec_to_announce)
    ctx.sent_announce_pos = len(ctx.items_sent_to_announce)
    ctx.announcements_pos = len(ctx.announcements)

    run_game(sc2.maps.get(maps_table[mission_id-1]), [
        Bot(Race.Terran, ArchipelagoBot(ctx, mission_id), name="Archipelago")], realtime=True)


class ArchipelagoBot(sc2.bot_ai.BotAI):
    game_running = False
    mission_completed = False
    first_bonus = False
    second_bonus = False
    third_bonus = False
    fourth_bonus = False
    fifth_bonus = False
    sixth_bonus = False
    seventh_bonus = False
    eight_bonus = False
    ctx: Context = None
    mission_id = 0

    can_read_game = False

    last_received_update = 0

    def __init__(self, ctx: Context, mission_id):
        self.ctx = ctx
        self.mission_id = mission_id

        super(ArchipelagoBot, self).__init__()

    async def on_step(self, iteration: int):
        game_state = 0
        if iteration == 0:
            start_items = calculate_items(self.ctx.items_received)
            difficulty = calc_difficulty(self.ctx.difficulty)
            await self.chat_send("ArchipelagoLoad {} {} {} {} {} {} {} {} {} {} {} {}".format(
                difficulty, start_items[0], start_items[1], start_items[2], start_items[3], start_items[4], start_items[5],
                start_items[6], start_items[7], start_items[8], start_items[9], self.ctx.all_in_choice))
            self.last_received_update = len(self.ctx.items_received)

        else:
            if self.ctx.announcement_pos < len(self.ctx.announcements):
                index = 0
                message = ""
                while index < len(self.ctx.announcements[self.ctx.announcement_pos]):
                    message += self.ctx.announcements[self.ctx.announcement_pos][index]["text"]
                    index += 1

                index = 0
                start_rem_pos = -1
                # Remove unneeded [Color] tags
                while index < len(message):
                    if message[index] == '[':
                        start_rem_pos = index
                        index += 1
                    elif message[index] == ']' and start_rem_pos > -1:
                        temp_msg = ""

                        if start_rem_pos > 0:
                            temp_msg = message[:start_rem_pos]
                        if index < len(message) - 1:
                            temp_msg += message[index+1:]

                        message = temp_msg
                        index += start_rem_pos - index
                        start_rem_pos = -1
                    else:
                        index += 1

                await self.chat_send("SendMessage " + message)
                self.ctx.announcement_pos += 1

            # Archipelago reads the health
            for unit in self.all_own_units():
                if unit.health_max == 38281:
                    game_state = int(38281 - unit.health)
                    can_read_game = True

            if iteration == 80 and not game_state & 1:
                await self.chat_send("SendMessage Warning: Archipelago unable to connect or has lost connection to " +
                                     "Starcraft 2 (This is likely a map issue)")

            if self.last_received_update < len(self.ctx.items_received):
                current_items = calculate_items(self.ctx.items_received)
                await self.chat_send("UpdateTech {} {} {} {} {} {} {} {}".format(
                    current_items[0], current_items[1], current_items[2], current_items[3], current_items[4], current_items[5],
                    current_items[6], current_items[7]))
                self.last_received_update = len(self.ctx.items_received)

            if game_state & 1:
                if not self.game_running:
                    print("Archipelago Connected")
                    self.game_running = True

                if can_read_game:
                    if game_state & (1 << 1) and not self.mission_completed:
                        if self.mission_id != 29:
                            print("Mission Completed")
                            await self.ctx.send_msgs([
                                {"cmd": 'LocationChecks', "locations": [SC2WOL_LOC_ID_OFFSET + 100 * self.mission_id]}])
                            self.mission_completed = True
                        else:
                            print("Game Complete")
                            await self.ctx.send_msgs([{"cmd": 'StatusUpdate', "status": ClientStatus.CLIENT_GOAL}])
                            self.mission_completed = True

                    if game_state & (1 << 2) and not self.first_bonus:
                        print("1st Bonus Collected")
                        await self.ctx.send_msgs(
                            [{"cmd": 'LocationChecks', "locations": [SC2WOL_LOC_ID_OFFSET + 100 * self.mission_id + 1]}])
                        self.first_bonus = True

                    if not self.second_bonus and game_state & (1 << 3):
                        print("2nd Bonus Collected")
                        await self.ctx.send_msgs(
                            [{"cmd": 'LocationChecks', "locations": [SC2WOL_LOC_ID_OFFSET + 100 * self.mission_id + 2]}])
                        self.second_bonus = True

                    if not self.third_bonus and game_state & (1 << 4):
                        print("3rd Bonus Collected")
                        await self.ctx.send_msgs(
                            [{"cmd": 'LocationChecks', "locations": [SC2WOL_LOC_ID_OFFSET + 100 * self.mission_id + 3]}])
                        self.third_bonus = True

                    if not self.fourth_bonus and game_state & (1 << 5):
                        print("4th Bonus Collected")
                        await self.ctx.send_msgs(
                            [{"cmd": 'LocationChecks', "locations": [SC2WOL_LOC_ID_OFFSET + 100 * self.mission_id + 4]}])
                        self.fourth_bonus = True

                    if not self.fifth_bonus and game_state & (1 << 6):
                        print("5th Bonus Collected")
                        await self.ctx.send_msgs(
                            [{"cmd": 'LocationChecks', "locations": [SC2WOL_LOC_ID_OFFSET + 100 * self.mission_id + 5]}])
                        self.fifth_bonus = True

                    if not self.sixth_bonus and game_state & (1 << 7):
                        print("6th Bonus Collected")
                        await self.ctx.send_msgs(
                            [{"cmd": 'LocationChecks', "locations": [SC2WOL_LOC_ID_OFFSET + 100 * self.mission_id + 6]}])
                        self.sixth_bonus = True

                    if not self.seventh_bonus and game_state & (1 << 8):
                        print("6th Bonus Collected")
                        await self.ctx.send_msgs(
                            [{"cmd": 'LocationChecks', "locations": [SC2WOL_LOC_ID_OFFSET + 100 * self.mission_id + 7]}])
                        self.seventh_bonus = True

                    if not self.eight_bonus and game_state & (1 << 9):
                        print("6th Bonus Collected")
                        await self.ctx.send_msgs(
                            [{"cmd": 'LocationChecks', "locations": [SC2WOL_LOC_ID_OFFSET + 100 * self.mission_id + 8]}])
                        self.eight_bonus = True

                else:
                    await self.chat_send("LostConnection - Lost connection to game.")


class MissionInfo(typing.NamedTuple):
    id: int
    extra_locations: int
    required_world: list[int]
    number: int = 0  # number of worlds need beaten


mission_req_table = {
    "Liberation Day": MissionInfo(1, 7, []),
    "The Outlaws": MissionInfo(2, 2, [1]),
    "Zero Hour": MissionInfo(3, 4, [2]),
    "Evacuation": MissionInfo(4, 4, [3]),
    "Outbreak": MissionInfo(5, 3, [4]),
    "Safe Haven": MissionInfo(6, 1, [5], number=7),
    "Haven's Fall": MissionInfo(7, 1, [5], number=7),
    "Smash and Grab": MissionInfo(8, 5, [3]),
    "The Dig": MissionInfo(9, 4, [8], number=8),
    "The Moebius Factor": MissionInfo(10, 9, [9], number=11),
    "Supernova": MissionInfo(11, 5, [10], number=14),
    "Maw of the Void": MissionInfo(12, 6, [11]),
    "Devil's Playground": MissionInfo(13, 3, [3], number=4),
    "Welcome to the Jungle": MissionInfo(14, 4, [13]),
    "Breakout": MissionInfo(15, 3, [14], number=8),
    "Ghost of a Chance": MissionInfo(16, 6, [14], number=8),
    "The Great Train Robbery": MissionInfo(17, 4, [3], number=6),
    "Cutthroat": MissionInfo(18, 5, [17]),
    "Engine of Destruction": MissionInfo(19, 6, [18]),
    "Media Blitz": MissionInfo(20, 5, [19]),
    "Piercing the Shroud": MissionInfo(21, 6, [20]),
    "Whispers of Doom": MissionInfo(22, 4, [9]),
    "A Sinister Turn": MissionInfo(23, 4, [22]),
    "Echoes of the Future": MissionInfo(24, 3, [23]),
    "In Utter Darkness": MissionInfo(25, 3, [24]),
    "Gates of Hell": MissionInfo(26, 2, [12]),
    "Belly of the Beast": MissionInfo(27, 4, [26]),
    "Shatter the Sky": MissionInfo(28, 5, [26]),
    "All-In": MissionInfo(29, -1, [27, 28])
}


def calc_objectives_completed(mission, missions_info, locations_done):
    objectives_complete = 0

    if missions_info[mission].extra_locations > 0:
        for i in range(missions_info[mission].extra_locations):
            if (missions_info[mission].id * 100 + SC2WOL_LOC_ID_OFFSET + i) in locations_done:
                objectives_complete += 1

        return objectives_complete

    else:
        return -1


def request_unfinished_missions(locations_done, location_table):
    message = "Unfinished Missions:"

    first_item = True

    unfinished_missions = calc_unfinished_missions(locations_done, location_table)

    for mission in unfinished_missions:
        if first_item:
            message += " {}[{}] ({}/{})".format(mission, location_table[mission].id, unfinished_missions[mission],
                                                location_table[mission].extra_locations)
            first_item = False
        else:
            message += ", {}[{}] ({}/{})".format(mission, location_table[mission].id, unfinished_missions[mission],
                                                 location_table[mission].extra_locations)

    sc2_logger.info(message)


def calc_unfinished_missions(locations_done, locations):
    unfinished_missions = []
    locations_completed = []
    available_missions = calc_available_missions(locations_done, locations)

    for name in available_missions:
        if not locations[name].extra_locations == -1:
            objectives_completed = calc_objectives_completed(name, locations, locations_done)

            if objectives_completed < locations[name].extra_locations:
                unfinished_missions.append(name)
                locations_completed.append(objectives_completed)

        else:
            unfinished_missions.append(name)
            locations_completed.append(-1)

    return {unfinished_missions[i]: locations_completed[i] for i in range(len(unfinished_missions))}


def is_mission_available(mission_id_to_check, locations_done, locations):
    unfinished_missions = calc_available_missions(locations_done, locations)

    for mission in unfinished_missions:
        if locations[mission].id == mission_id_to_check:
            return True

    return False


def request_available_missions(locations_done, location_table):
    message = "Available Missions:"

    first_item = True

    missions = calc_available_missions(locations_done, location_table)

    for mission in missions:
        if first_item:
            message += " {}[{}]".format(mission, location_table[mission].id)
            first_item = False
        else:
            message += ", {}[{}]".format(mission, location_table[mission].id)

    sc2_logger.info(message)


def calc_available_missions(locations_done, locations):
    available_missions = []
    mission_complete = 0

    # Get number of missions completed
    for loc in locations_done:
        if loc % 100 == 0:
            mission_complete += 1

    for name in locations:
        if len(locations[name].required_world) >= 1:
            reqs_complete = True

            for req_mission in locations[name].required_world:
                if not(req_mission * 100 + SC2WOL_LOC_ID_OFFSET) in locations_done:
                    reqs_complete = False
                    break

            if reqs_complete and mission_complete >= locations[name].number:
                available_missions.append(name)
        else:
            available_missions.append(name)

    return available_missions


if __name__ == '__main__':
    colorama.init()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    colorama.deinit()