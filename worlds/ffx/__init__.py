"""
Archipelago World definition for Final Fantasy X
"""

from typing import ClassVar, Any, Optional
from random import Random
from settings import Group, FilePath

from BaseClasses import Tutorial, Item, ItemClassification, LocationProgressType
from worlds.AutoWorld import WebWorld, World
from Utils import visualize_regions

from .client import FFXClient

from .items import create_item_label_to_code_map, item_table, key_items, filler_items, AllItems, FFXItem, \
    party_member_items, stat_abilities, skill_abilities, region_unlock_items, trap_items, equip_items
from .locations import create_location_label_to_id_map, FFXLocation, allLocations
from .regions import create_regions
from .options import FFXOptions
from .generate import generate_output, options_validation
from .rules import set_rules, world_battle_levels
from .ut import tracker_world, setup_options_from_slot_data


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


class FFXSettings(Group):
    class UTPoptrackerPath(FilePath):
        """Path to the user's FFX Poptracker Pack."""
        description = "FFX Poptracker Pack zip file"
        required = False

    ut_poptracker_path: UTPoptrackerPath | str = UTPoptrackerPath()


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
    explicit_indirect_conditions = False

    # Universal Tracker
    tracker_world = tracker_world
    ut_can_gen_without_yaml = True
    using_ut: bool

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data

    def generate_early(self) -> None:
        options_validation(self)
        setup_options_from_slot_data(self)

    def get_filler_item_name(self) -> str:
        filler = [x.itemName for x in filler_items]
        return self.random.choice(filler)

    def create_regions(self) -> None:
        create_regions(self, self.player)

    def create_items(self):

        required_items = []

        for item in key_items:
            required_items.append(item.itemName)

        # Progressive celestial weapons and Brotherhood
        for item in equip_items:
            if item.progression == ItemClassification.progression:
                if item.itemID & 0x0FFF == 0x0001:
                    # Brotherhood
                    required_items.extend([item.itemName]*2)
                else:
                    # Celestial
                    required_items.extend([item.itemName]*3)

        # for item in skill_abilities:
        #     required_items.append(item.itemName)
        #
        # for item in stat_abilities:
        #     required_items.extend([item.itemName for _ in range(1)])

        possible_starting_regions = [f"Region: {region}" for region, level in world_battle_levels.items() if
                                     level <= min(self.options.logic_difficulty.value, 3)]
        starting_region = self.random.choice(possible_starting_regions)

        self.multiworld.push_precollected(self.create_item(starting_region))
        for item in region_unlock_items:
            if item.itemName != starting_region:
                required_items.append(item.itemName)

        starting_character = party_member_items[0]

        self.multiworld.push_precollected(self.create_item(starting_character.itemName))
        for party_member in party_member_items:
            if party_member == starting_character:
                continue
            required_items.append(party_member.itemName)

        unfilled_locations = len(self.multiworld.get_unfilled_locations(self.player))

        items_remaining = unfilled_locations - len(required_items)

        for _ in self.options.exclude_locations.value:
            self.multiworld.itempool.append(self.create_filler())
            items_remaining -= 1

        traps_remaining = int(items_remaining * self.options.trap_percentage.value / 100)
        items_remaining = items_remaining - traps_remaining

        for itemName in required_items:
            self.multiworld.itempool.append(self.create_item(itemName))

        useful_items = []
        for item in AllItems:
            if item.progression == ItemClassification.useful:
                useful_items += [item.itemName]

        self.random.shuffle(useful_items)

        traps = [trap.itemName for trap in self.random.choices(trap_items, k=traps_remaining)]

        for trap in traps:
            self.multiworld.itempool.append(self.create_item(trap))

        for i in range(items_remaining):
            if i > len(useful_items) - 1:
                self.multiworld.itempool.append(self.create_filler())
            else:
                self.multiworld.itempool.append(self.create_item(useful_items[i]))

    def create_item(self, name: str) -> Item:
        item = item_table[name]
        return FFXItem(item.itemName, item.progression, item.itemID, self.player)

    def set_rules(self) -> None:
        set_rules(self)

    def generate_basic(self) -> None:
        pass

    def fill_slot_data(self) -> dict[str, Any]:
        slot_data = {
            "SeedId": self.multiworld.get_out_file_name_base(self.player),
            # Options
            "goal_requirement": self.options.goal_requirement.value,
            "required_party_members": self.options.required_party_members.value,
            "required_primers": self.options.required_primers.value,
            "sphere_grid_randomization": self.options.sphere_grid_randomization.value,
            "super_bosses": self.options.super_bosses.value,
            "mini_games": self.options.mini_games.value,
            "logic_difficulty": self.options.logic_difficulty.value,
            "recruit_sanity": self.options.recruit_sanity.value,
            "capture_sanity": self.options.capture_sanity.value
        }
        return slot_data

    def generate_output(self, output_directory: str) -> None:

        # Visualize regions
        visualize_regions(self.multiworld.get_region("Menu", self.player), f"ffx {self.player}.puml", show_entrance_names=True)

        generate_output(self, self.player, output_directory)