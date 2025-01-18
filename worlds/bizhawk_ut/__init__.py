from worlds.LauncherComponents import SuffixIdentifier, components, Component, Type, launch_subprocess


def my_launch_client(*args) -> None:
    from .bizhawk_ut_client import my_launch
    launch_subprocess(my_launch, name="BizHawkClientUniversalTracker", args=args)


components.append(Component("BizHawk Client + Universal Tracker", "BizHawkClientUniversalTracker",
                            component_type=Type.CLIENT, func=my_launch_client,
                            file_identifier=SuffixIdentifier()))
