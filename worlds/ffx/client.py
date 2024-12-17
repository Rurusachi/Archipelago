from typing import TYPE_CHECKING, Dict, Set, Tuple, List
import struct

from NetUtils import ClientStatus

import asyncio
import Utils
import Patch
from worlds.LauncherComponents import Component, SuffixIdentifier, Type, components, launch_subprocess


def my_launch(*launch_args) -> None:
    from CommonClient import get_base_parser, server_loop, logger, gui_enabled

    tracker_loaded = False
    try:
        from worlds.tracker.TrackerClient import TrackerGameContext as SuperContext
        from worlds.tracker.TrackerClient import TrackerCommandProcessor as SuperCommandProcessor
        tracker_loaded = True
    except ModuleNotFoundError:
        from CommonClient import CommonContext as SuperContext
        from CommonClient import ClientCommandProcessor as SuperCommandProcessor

    async def _patch_and_run_game(patch_file: str):
        try:
            metadata, output_file = Patch.create_rom_file(patch_file)
        except Exception as exc:
            logger.exception(exc)

    async def main():
        parser = get_base_parser()
        parser.add_argument("patch_file", default="", type=str, nargs="?", help="Path to an Archipelago patch file")
        args = parser.parse_args(launch_args)

        class MyClientCommandProcessor(SuperCommandProcessor):
            pass

        class MyClientContext(SuperContext):
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

        # watcher_task = asyncio.create_task(_game_watcher(ctx), name="GameWatcher")

        # try:
        #     await watcher_task
        # except Exception as e:
        #     logger.exception(e)

        await ctx.exit_event.wait()
        await ctx.shutdown()

    Utils.init_logging("FFXClient", exception_logger="Client")
    import colorama
    colorama.init()
    asyncio.run(main())
    colorama.deinit()


def my_launch_client(*args) -> None:
    launch_subprocess(my_launch, name="BizHawkClientFFTA2", args=args)


component = Component("FFX Client", "FFXClient", component_type=Type.CLIENT, func=my_launch_client,
                      file_identifier=SuffixIdentifier(".apffx"))
components.append(component)


class FFXClient:
    pass
