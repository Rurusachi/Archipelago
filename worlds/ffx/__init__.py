"""
Archipelago World definition for Final Fantasy X
"""

from typing import ClassVar, Dict, Any, List, Tuple, Set, Optional
from random import Random
import settings

from BaseClasses import Tutorial, Item, ItemClassification
from worlds.AutoWorld import WebWorld, World
from Utils import visualize_regions

from .client import FFXClient

from .items import create_item_label_to_code_map, item_table, key_items, filler_items, AllItems, FFXItem
from .locations import create_location_label_to_id_map
from .regions import create_regions
from .options import FFXOptions
from .generate import generate_output, FFXProcedurePatch


class FFXWebWorld(WebWorld):
    """
    Webhost info for Final Fantasy X
    """
    theme = "grass"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Final Fantasy X with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Rurusachi"]
    )

    tutorials = [setup_en]


class FFXSettings(settings.Group):
    class FFXTakaraFile(settings.UserFilePath):
        """File name of your Final Fantasy X Takara File"""
        description = "Final Fantasy X Takara File"
        copy_to = "takara.bin"
        md5s = [FFXProcedurePatch.hash]

    takara_file: FFXTakaraFile = FFXTakaraFile(FFXTakaraFile.copy_to)


class FFXWorld(World):
    """
    Final Fantasy X is a game
    """
    game = "Final Fantasy X"
    web = FFXWebWorld()
    topology_present = False

    settings_key = "ffx_options"
    settings: ClassVar[FFXSettings]

    options_dataclass = FFXOptions
    options: FFXOptions

    required_client_version = (0, 4, 4)

    item_name_to_id = create_item_label_to_code_map()
    location_name_to_id = create_location_label_to_id_map()

    def get_filler_item_name(self) -> str:
        filler = [x.itemName for x in filler_items]
        return self.random.choice(filler)

    def create_regions(self) -> None:
        create_regions(self, self.player)

    def create_items(self):

        required_items = []

        for item in key_items:
            required_items.append(item.itemName)

        unfilled_locations = len(self.multiworld.get_unfilled_locations(self.player))

        items_remaining = unfilled_locations - len(required_items)

        for itemName in required_items:
            self.multiworld.itempool.append(self.create_item(itemName))

        useful_items = []
        for item in AllItems:
            if item.progression == ItemClassification.useful:
                useful_items += [item.itemName]

        self.random.shuffle(useful_items)

        for i in range(items_remaining):
            if i > len(useful_items) - 1:
                self.multiworld.itempool.append(self.create_filler())
            else:
                self.multiworld.itempool.append(self.create_item(useful_items[i]))

    def create_item(self, name: str) -> Item:
        item = item_table[name]
        return FFXItem(item.itemName, item.progression, item.itemID, self.player)

    def generate_output(self, output_directory: str) -> None:

        # Visualize regions
        visualize_regions(self.multiworld.get_region("Menu", self.player), f"ffx {self.player}.puml", show_entrance_names=True)

        generate_output(self, self.player, output_directory)