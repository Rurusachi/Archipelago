import os
import pkgutil
import struct
import zipfile
import json
import typing

from settings import get_settings
from Options import OptionError
from worlds.AutoWorld import World
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes, APPatch
from .locations import location_types, get_location_type

if typing.TYPE_CHECKING:
    from .__init__ import FFXWorld
else:
    FFXWorld = object


class APFFXFile(APPatch):
    game = "Final Fantasy X"
    def get_manifest(self):
        manifest = super().get_manifest()
        manifest["patch_file_ending"] = ".apffx"
        return manifest


def options_validation(world: FFXWorld) -> None:
    if world.options.goal_requirement.value == world.options.goal_requirement.option_nemesis:
        if not world.options.capture_sanity.value:
            raise OptionError(f"[Final Fantasy X - '{world.player_name}'] "
                "Goal Requirement: Nemesis cannot be chosen if Capture Sanity is disabled.")
        elif not world.options.creation_rewards.value == world.options.creation_rewards.option_original:
            raise OptionError(f"[Final Fantasy X - '{world.player_name}'] "
                "Goal Requirement: Nemesis cannot be chosen if Creation Rewards is not set to Original Creations.")
        elif not world.options.arena_bosses.value == world.options.arena_bosses.option_original:
            raise OptionError(f"[Final Fantasy X - '{world.player_name}'] "
                "Goal Requirement: Nemesis cannot be chosen if Arena Bosses is not set to Original Creations.")
    elif world.options.creation_rewards.value and not world.options.capture_sanity.value:
        raise OptionError(f"[Final Fantasy X - '{world.player_name}'] "
                "Creation Rewards cannot be enabled if Capture Sanity is disabled.")
    elif world.options.arena_bosses.value and not world.options.capture_sanity.value:
        raise OptionError(f"[Final Fantasy X - '{world.player_name}'] "
                "Arena Bosses cannot be enabled if Capture Sanity is disabled.")


def generate_output(world: FFXWorld, player: int, output_directory: str) -> None:
    miscellaneous_data = {
        "SeedId": world.multiworld.get_out_file_name_base(world.player),
        "GoalRequirement": world.options.goal_requirement.value,
        "RequiredPartyMembers": world.options.required_party_members.value,
        "RequiredPrimers": world.options.required_primers.value,
        "APMultiplier": world.options.ap_multiplier.value,
    }

    locations: dict[str, list[dict[str, int | str] | int] | str] = {x: list() for x in location_types.values()}

    for location in world.multiworld.get_filled_locations(player):
        if location.is_event:
            continue
        if location.item.player != player:
            item_id = 0
        else:
            item_id = location.item.code
        locations[get_location_type(location.address)].append({"location_name": location.name,
                                                               "location_id": location.address & 0x0FFF,
                                                               "item_id": item_id,
                                                               "item_name": location.item.name,
                                                               "player_name": world.multiworld.get_player_name(location.item.player)})

    starting_items: list[int] = list()

    for item in world.multiworld.precollected_items[player]:
        starting_items.append(item.code)
    locations["StartingItems"] = starting_items


    file_path = os.path.join(output_directory, f"{world.multiworld.get_out_file_name_base(world.player)}.json")
    with open(file_path, "w", encoding="utf-8") as outfile:
        outfile.write(json.dumps(miscellaneous_data | locations, indent=4))

    #file_path = os.path.join(output_directory, f"{world.multiworld.get_out_file_name_base(world.player)}.apffx")
    #APFFX = APFFXFile(file_path, player=world.player, player_name=world.multiworld.player_name[world.player])
    #with zipfile.ZipFile(file_path, mode="w", compression=zipfile.ZIP_DEFLATED,
    #                     compresslevel=9) as zf:
    #    zf.writestr("locations.json", json.dumps(locations))
    #    APFFX.write_contents(zf)
