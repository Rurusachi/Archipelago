"""
Archipelago World definition for Final Fantasy Tactics A2
"""

from typing import ClassVar, Dict, Any, List, Tuple
import settings
from Utils import visualize_regions

from .client import FFTA2Client

from BaseClasses import ItemClassification, Tutorial, Item
from worlds.AutoWorld import WebWorld, World
from .regions import create_regions
from .rules import set_rules

from .options import (FFTA2Options, GateNumber, JobUnlockRequirements)
from .items import (create_item_label_to_code_map, AllItems, item_table, FFTA2Item, FillerItems, GateItems, jobUnlockItems)
from .locations import (create_location_label_to_id_map)
from .rom import FFTA2ProcedurePatch, generate_output


class FFTA2WebWorld(WebWorld):
    """
    Webhost info for Final Fantasy Tactics A2
    """
    theme = "grass"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Final Fantasy Tactics A2 with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Rurusachi"]
    )

    tutorials = [setup_en]


class FFTA2Settings(settings.Group):
    class FFTA2RomFile(settings.UserFilePath):
        """File name of your Final Fantasy Tactics A2 ROM"""
        description = "Final Fantasy Tactics A2 ROM File"
        copy_to = "Final Fantasy Tactics A2 - Grimoire of the Rift.nds"
        md5s = [FFTA2ProcedurePatch.hash]

    rom_file: FFTA2RomFile = FFTA2RomFile(FFTA2RomFile.copy_to)


class FFTA2World(World):
    """
    Final Fantasy Tactics A2 is a game
    """
    game = "Final Fantasy Tactics A2"
    web = FFTA2WebWorld()
    topology_present = False

    settings_key = "ffta2_options"
    settings: ClassVar[FFTA2Settings]

    options_dataclass = FFTA2Options
    options: FFTA2Options

    required_client_version = (0, 4, 4)

    item_name_to_id = create_item_label_to_code_map()
    location_name_to_id = create_location_label_to_id_map()

    def __init__(self, multiworld, player):
        super(FFTA2World, self).__init__(multiworld, player)
        self.randomized_weapons = []
        self.randomized_equip = []
        self.basic_weapon = []
        self.basic_equip = []
        self.QuestGroups = []
        self.DispatchQuestGroups = []
        self.location_ids = []
        self.path_quests: List[List[Tuple[int, List[int]]]] = []
        self.path_end_quests: List[Tuple[int, int]] = []

    def get_filler_item_name(self) -> str:
        filler = [x.itemName for x in FillerItems]
        return self.random.choice(filler)

    def create_regions(self) -> None:
        create_regions(self, self.player)

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]) -> None:
        hint_data.update({self.player: {}})
        for location in self.multiworld.get_locations(self.player):
            if location.address is not None:
                hint_data[self.player][location.address] = location.parent_region.hint_text

    def create_items(self):

        required_items = self.get_required_items()

        # Count number of quest reward locations
        # gate_number = self.options.gate_num.value
        # reward_number = self.options.reward_num.value

        # unfilled_locations = gate_number * reward_number * 4 + 1
        # unfilled_locations += (self.options.path_num.value-1) * reward_number

        unfilled_locations = len(self.multiworld.get_unfilled_locations(self.player)) - 1
        if self.options.path_num.value > 1:
            unfilled_locations -= self.options.path_num.value

        items_remaining = unfilled_locations - len(required_items)

        # Adding required items to the pool first
        for itemName in required_items:
            self.multiworld.itempool.append(self.create_item(itemName))

        useful_items = []
        for item in AllItems:
            if item.progression == ItemClassification.useful:
                if self.options.job_unlock_req.value != JobUnlockRequirements.option_job_items:
                    if item in jobUnlockItems:
                        continue

                useful_items += [item.itemName]

        # Shuffle the useful items to be added to the pool based on the locations remaining
        self.random.shuffle(useful_items)

        for i in range(items_remaining):
            if i > len(useful_items) - 1:
                self.multiworld.itempool.append(self.create_filler())
            else:
                self.multiworld.itempool.append(self.create_item(useful_items[i]))

    def set_rules(self) -> None:
        set_rules(self)

    def generate_basic(self) -> None:
        # Setting the victory item at the victory location
        victory_event = FFTA2Item('Victory', ItemClassification.progression, None, self.player)

        self.multiworld.get_location("The Two Grimoires", self.player)\
            .place_locked_item(victory_event)

        self.multiworld.completion_condition[self.player] =\
            lambda state: state.has("Victory", self.player)

        if self.options.path_num.value > 1:
            for i in range(0, self.options.path_num.value):
                path_event = FFTA2Item(f"Path {i+1} Complete", ItemClassification.progression, None, self.player)

                self.multiworld.get_location(f"Path {i+1} Completion", self.player)\
                    .place_locked_item(path_event)

    def get_required_items(self):
        required_items = []

        req_gate_num = self.options.gate_num.value + self.options.path_num.value - 1

        for i in range(0, req_gate_num):
            required_items.append(GateItems[i].itemName)

        return required_items

    def fill_slot_data(self) -> Dict[str, Any]:

        slot_data = self.options.as_dict(
            "gate_num",
            "paths_required",
        )

        slot_data["path_end_quests"] = self.path_end_quests

        return slot_data

    def create_item(self, name: str) -> Item:
        item = item_table[name]
        return FFTA2Item(item.itemName, item.progression, item.itemID, self.player)

    def generate_output(self, output_directory: str) -> None:

        # Visualize regions
        visualize_regions(self.multiworld.get_region("Menu", self.player), f"ffta2 {self.player}.puml", show_entrance_names=True)

        generate_output(self, self.player, output_directory)
