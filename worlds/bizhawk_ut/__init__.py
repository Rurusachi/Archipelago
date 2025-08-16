from typing import Tuple, Dict, Any
import traceback
from worlds.LauncherComponents import SuffixIdentifier, components, Component, Type, launch_subprocess
from worlds._bizhawk.client import AutoBizHawkClientRegister


def my_launch_client(*args) -> None:
    from .bizhawk_ut_client import my_launch
    launch_subprocess(my_launch, name="BizHawk Client + Universal Tracker", args=args)


for bizhawk_component in components:
    if bizhawk_component.script_name == "BizHawkClient":
        break

component = Component("BizHawk Client + Universal Tracker",
                      component_type=Type.CLIENT, func=my_launch_client,
                      file_identifier=bizhawk_component.file_identifier)
components.append(component)


old_new = AutoBizHawkClientRegister.__new__


def newUT(cls, name: str, bases: Tuple[type, ...], namespace: Dict[str, Any]) -> AutoBizHawkClientRegister:

    temp = namespace["game_watcher"]

    async def my_game_watcher(self, ctx) -> None:
        if getattr(ctx, "tracker_enabled", False):
            try:
                if ctx.player_id is not None and ctx.multiworld is not None:
                    ctx.updateTracker()
            except Exception:
                tb = traceback.format_exc()
                print(tb)
        await temp(self, ctx)
    namespace["game_watcher"] = my_game_watcher

    new_class = old_new(cls, name, bases, namespace)

    if "patch_suffix" in namespace:
        new_suffixes = [*component.file_identifier.suffixes]
        if type(namespace["patch_suffix"]) is str:
            new_suffixes.append(namespace["patch_suffix"])
        else:
            new_suffixes.extend(namespace["patch_suffix"])
        component.file_identifier = SuffixIdentifier(*new_suffixes)
        bizhawk_component.file_identifier = SuffixIdentifier()

    return new_class


AutoBizHawkClientRegister.__new__ = newUT
