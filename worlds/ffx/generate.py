import os
import pkgutil
import struct
import zipfile
import json

from settings import get_settings
from worlds.AutoWorld import World
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes, APPatch
from .locations import location_types, get_location_type


def get_base_takara_as_bytes() -> bytes:
    with open(get_settings().ffx_options.takara_file, "rb") as infile:
        base_takara_bytes = bytes(infile.read())

    return base_takara_bytes

class APFFXFile(APPatch):
    game = "Final Fantasy X"
    def get_manifest(self):
        manifest = super().get_manifest()
        manifest["patch_file_ending"] = ".apffx"
        return manifest

class FFXProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Final Fantasy X"
    hash = "eef93ce67302e012a0b0ccaf224921b0"
    patch_file_ending = ".apffx"
    result_file_ending = ".bin"

    procedure = [
        ("apply_tokens", ["token_data.bin"]),
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_takara_as_bytes()


def generate_output(world: World, player: int, output_directory: str) -> None:

    patch_data = dict()

    #locations = []

    locations: dict[str, list[dict[str, int | str] | int]] = {x: list() for x in location_types.values()}
    #locations: dict[str, dict[int, dict[str, int | str]]] = {x: dict() for x in location_types.values()}

    for location in world.multiworld.get_filled_locations(player):
        if location.item.player != player:
            item_id = 0
        else:
            item_id = location.item.code
        #locations[get_location_type(location.address)][location.address & 0x0FFF] = {"location_name": location.name, "item_id": item_id, "item_name": location.item.name}
        locations[get_location_type(location.address)].append({"location_name": location.name, "location_id": location.address & 0x0FFF, "item_id": item_id, "item_name": location.item.name})
        #locations.append({"location_name": location.name, "location_id": location.address, "item": item_id, "item_name": location.item.name})

    starting_items: list[int] = list()

    for item in world.multiworld.precollected_items[player]:
        starting_items.append(item.code)
    locations["StartingItems"] = starting_items

    file_path = os.path.join(output_directory, f"{world.multiworld.get_out_file_name_base(world.player)}.json")
    with open(file_path, "w") as outfile:
        outfile.write(json.dumps(locations, indent=4))
    #file_path = os.path.join(output_directory, f"{world.multiworld.get_out_file_name_base(world.player)}.apffx")
    #APFFX = APFFXFile(file_path, player=world.player, player_name=world.multiworld.player_name[world.player])
    #with zipfile.ZipFile(file_path, mode="w", compression=zipfile.ZIP_DEFLATED,
    #                     compresslevel=9) as zf:
    #    zf.writestr("locations.json", json.dumps(locations))
    #    APFFX.write_contents(zf)


    # patch = FFXProcedurePatch(player=player, player_name=world.multiworld.player_name[player])
    #
    # set_items(world, world.multiworld, player, patch)
    #
    # patch.write_file("token_data.bin", patch.get_token_binary())
    #
    # out_file_name = world.multiworld.get_out_file_name_base(world.player)
    # patch.write(
    #     os.path.join(output_directory,
    #                  f"{out_file_name}{patch.patch_file_ending}"))


def set_items(world, multiworld, player, patch: FFXProcedurePatch) -> None:
    for location in multiworld.get_filled_locations(player):

        if location.item.code is not None:
            if location.item.player != player:
                # item_id = 0x2000  # Potion for testing
                item_id = 0
                item_type = 0
                amount = 0
            else:
                item_id = location.item.code

                if 0x2000 <= item_id <= 0x206F:
                    # Normal item
                    amount = 10
                    item_type = 0x02
                elif 0xA000 <= item_id <= 0xA03F:
                    # Key item
                    amount = 1
                    item_type = 0x0A
                elif 0x5000 <= item_id <= 0x5085:
                    # Weapon
                    amount = 1
                    item_type = 0x05
                    item_id &= 0xff
                elif 0xD000 <= item_id <= 0xDFFF:
                    # Ability
                    amount = 1
                    item_type = 0x0D
                    item_id &= 0xff
                elif item_id == 0x1000:
                    # Gil
                    amount = 10
                    item_type = 0x00
                    item_id = 0

            if location.address & 0x1000 == 0x1000:
                # Takara.bin
                patch.write_token(APTokenTypes.WRITE, (location.address & 0xfff) * 4 + 0x14, struct.pack("<BBH", item_type, amount, item_id))
            else:
                print("Unknown location address")
