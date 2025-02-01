import asyncio
import Utils
import sys


def my_launch(*launch_args) -> None:
    from CommonClient import get_base_parser, server_loop, logger, gui_enabled
    from worlds._bizhawk.context import BizHawkClientContext, BizHawkClientCommandProcessor, _patch_and_run_game, _game_watcher
    tracker_loaded = False
    try:
        from worlds.tracker.TrackerClient import (TrackerGameContext as SuperContext,
                                                  TrackerCommandProcessor as SuperCommandProcessor,
                                                  UT_VERSION)
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
            tags = BizHawkClientContext.tags

            def on_package(self, cmd, args):
                super().on_package(cmd, args)
                if tracker_loaded:
                    SuperContext.on_package(self, cmd, args)

            def make_gui(self):
                ui = super().make_gui()
                if tracker_loaded:
                    ui.base_title += f" (with Tracker {UT_VERSION}) for AP version"
                return ui

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
