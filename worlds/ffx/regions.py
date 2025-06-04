from BaseClasses import Entrance, ItemClassification, Region, Location, LocationProgressType, CollectionState
import json
import pkgutil
from typing import NamedTuple

from .locations import FFXLocation, FFXTreasureLocations, FFXPartyMemberLocations, FFXBossLocations, \
    FFXOverdriveLocations, FFXOtherLocations, FFXSphereGridLocations, FFXLocationData
from .rules import ruleDict
from .items import party_members
from worlds.generic.Rules import add_rule
from ..AutoWorld import World

class RegionData(dict):
    @property
    def name(self) -> str:
        return self["name"]
    @property
    def id(self) -> int:
        return self["id"]
    @property
    def treasures(self) -> list[int]:
        return self["treasures"]
    @property
    def party_members(self) -> list[int]:
        return self["party_members"]
    @property
    def bosses(self) -> list[int]:
        return self["bosses"]
    @property
    def overdrives(self) -> list[int]:
        return self["overdrives"]
    @property
    def other(self) -> list[int]:
        return self["other"]
    @property
    def leads_to(self) -> list[int]:
        return self["leads_to"]
    @property
    def rules(self) -> list[str]:
        return self["rules"]


def create_regions(world, player) -> None:
    def create_region_locations(region_name, treasures):
        region = Region(region_name, player, world.multiworld)
        for treasure_id in treasures:
            location = [x for x in FFXTreasureLocations if x.location_id == treasure_id][0]
            new_location = FFXLocation(player, location.name, location.rom_address, region)
            if location.missable:
                new_location.progress_type = LocationProgressType.EXCLUDED
            region.locations.append(new_location)
        return region

    def add_locations_by_ids(region: Region, location_ids: list[int], location_data: list[FFXLocationData]):
        for id in location_ids:
            location = [x for x in location_data if x.location_id == id][0]
            new_location = FFXLocation(player, location.name, location.rom_address, region)
            if location.missable:
                new_location.progress_type = LocationProgressType.EXCLUDED
            region.locations.append(new_location)
            all_locations.append(new_location)



    menu_region = Region("Menu", player, world.multiworld)
    world.multiworld.regions.append(menu_region)

    region_file = pkgutil.get_data(__name__, "data/regions.json")
    #region_data_list = [RegionData(x) for x in json.loads(region_file)]
    region_data_list = json.loads(region_file)
    region_data_list = [RegionData(x) for x in region_data_list]

    region_dict: dict[int, Region] = dict()
    region_rules: dict[int, list[str]] = dict()

    all_locations = []

    for region_data in region_data_list:
        new_region = Region(region_data.name, player, world.multiworld)
        region_dict[region_data.id] = new_region
        world.multiworld.regions.append(new_region)
        if len(region_data.rules) > 0:
            region_rules[region_data.id] = region_data.rules

        add_locations_by_ids(new_region, region_data.treasures, FFXTreasureLocations)
        # for id in region_data.treasures:
        #     print(region_data.name, id)
        #     location = [x for x in FFXTreasureLocations if x.location_id == id][0]
        #     new_location = FFXLocation(player, location.name, location.rom_address, new_region)
        #     if location.missable:
        #         new_location.progress_type = LocationProgressType.EXCLUDED
        #     new_region.locations.append(new_location)
        #     all_locations.append(new_location)

        add_locations_by_ids(new_region, region_data.party_members, FFXPartyMemberLocations)
        # for id in region_data.party_members:
        #     print(region_data.name, id)
        #     location = [x for x in FFXPartyMemberLocations if x.location_id == id][0]
        #     new_location = FFXLocation(player, location.name, location.rom_address, new_region)
        #     if location.missable:
        #         new_location.progress_type = LocationProgressType.EXCLUDED
        #     new_region.locations.append(new_location)
        #     all_locations.append(new_location)

        add_locations_by_ids(new_region, region_data.bosses, FFXBossLocations)
        # for id in region_data.bosses:
        #     print(region_data.name, id)
        #     location = [x for x in FFXBossLocations if x.location_id == id][0]
        #     new_location = FFXLocation(player, location.name, location.rom_address, new_region)
        #     if location.missable:
        #         new_location.progress_type = LocationProgressType.EXCLUDED
        #     new_region.locations.append(new_location)
        #     all_locations.append(new_location)

        add_locations_by_ids(new_region, region_data.overdrives, FFXOverdriveLocations)
        # for id in region_data.overdrives:
        #     print(region_data.name, id)
        #     location = [x for x in FFXOverdriveLocations if x.location_id == id][0]
        #     new_location = FFXLocation(player, location.name, location.rom_address, new_region)
        #     if location.missable:
        #         new_location.progress_type = LocationProgressType.EXCLUDED
        #     new_region.locations.append(new_location)
        #     all_locations.append(new_location)

        add_locations_by_ids(new_region, region_data.other, FFXOtherLocations)
        # for id in region_data.other:
        #     print(region_data.name, id)
        #     location = [x for x in FFXOtherLocations if x.location_id == id][0]
        #     new_location = FFXLocation(player, location.name, location.rom_address, new_region)
        #     if location.missable:
        #         new_location.progress_type = LocationProgressType.EXCLUDED
        #     new_region.locations.append(new_location)
        #     all_locations.append(new_location)

    for region_data in region_data_list:
        curr_region = region_dict[region_data.id]
        for region_id in region_data.leads_to:
            other_region = region_dict[region_id]
            rules = region_rules.get(region_id)
            if rules is not None:
                rule_lambdas = [ruleDict[x](world) for x in rules]
                new_rule = lambda state, rule_list=rule_lambdas: all([rule(state) for rule in rule_list])
            else:
                new_rule = None
            curr_region.connect(other_region, rule=new_rule)

    for region_id, other_region in region_dict.items():
        if len(other_region.entrances) == 0:
            menu_region.connect(other_region)

    character_names = [
        "Tidus",
        "Yuna",
        "Auron",
        "Kimahri",
        "Wakka",
        "Lulu",
        "Rikku"
    ]

    for character, region in enumerate(FFXSphereGridLocations):
        new_region = Region(f"Sphere Grid: {character_names[character]}", player, world.multiworld)
        for location in region:
            new_location = FFXLocation(player, location.name, location.rom_address, new_region)
            if location.missable:
                new_location.progress_type = LocationProgressType.EXCLUDED
            new_region.locations.append(new_location)
            all_locations.append(new_location)
        menu_region.connect(new_region, rule=lambda state, i=character: state.has(party_members[i].itemName, world.player))


    #test_region = Region("Test", player, world.multiworld)
    #menu_region.connect(test_region)
    #
    #for location in FFXTreasureLocations:
    #    new_location = FFXLocation(player, location.name, location.rom_address, test_region)
    #    new_location.progress_type = LocationProgressType.EXCLUDED
    #    test_region.locations.append(new_location)

    #baaj_1_region = Region("Baaj Temple 1st visit", player, world.multiworld)
    #baaj_1_region = create_region_locations("Baaj Temple 1st visit", [0, 1, 2, 3, 6, 7, 219, 213])  # + Klikk

    #al_bhed_ship_region = Region("Al Bhed Ship", player, world.multiworld)
    #al_bhed_ship_region = create_region_locations("Al Bhed Ship", [296])  # + Tros, Al Bhed Primer I

    #baaj_2_region = Region("Baaj Temple 2nd visit", player, world.multiworld)
    #baaj_2_region = create_region_locations("Baaj Temple 2nd visit", [204, 205, 5])  # + Anima




    #besaid_1_region = Region("Besaid Island 1st visit", player, world.multiworld)
    #besaid_1_region = create_region_locations("Besaid Island 1st visit", [268, 9, 283, 285, 284, 282, 90, 91, 92, 13, 14, 215, 216, 15, 459])  # + Al Bhed Primer II, Yuna, Lulu, Wakka, Valefor, Brotherhood



    #besaid_2_region = Region("Besaid Island 2nd visit", player, world.multiworld)
