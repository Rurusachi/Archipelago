import os
import pkgutil
import struct
from typing import Tuple, Dict

from settings import get_settings
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes


def get_base_takara_as_bytes() -> bytes:
    with open(get_settings().ffx_options.takara_file, "rb") as infile:
        base_takara_bytes = bytes(infile.read())

    return base_takara_bytes


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


def generate_output(world, player: int, output_directory: str) -> None:
    patch = FFXProcedurePatch(player=player, player_name=world.multiworld.player_name[player])

    set_items(world, world.multiworld, player, patch)

    patch.write_file("token_data.bin", patch.get_token_binary())

    out_file_name = world.multiworld.get_out_file_name_base(world.player)
    patch.write(
        os.path.join(output_directory,
                     f"{out_file_name}{patch.patch_file_ending}"))


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

                if item_id >= 0x2000 and item_id <= 0x206F:
                    # Normal item
                    amount = 10
                    item_type = 0x02
                elif item_id >= 0xA000 and item_id <= 0xA03F:
                    # Key item
                    amount = 1
                    item_type = 0x0A
                elif item_id >= 0x5000 and item_id <= 0x5085:
                    # Weapon
                    amount = 1
                    item_type = 0x05
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
