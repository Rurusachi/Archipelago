from BaseClasses import Entrance, ItemClassification, Region, Location, LocationProgressType, CollectionState
import json
import pkgutil
import typing
from typing import NamedTuple, List

from .locations import FFXLocation, FFXTreasureLocations, FFXPartyMemberLocations, FFXBossLocations, \
    FFXOverdriveLocations, FFXOtherLocations, FFXRecruitLocations, FFXSphereGridLocations, FFXCaptureLocations, FFXLocationData, TreasureOffset, BossOffset, PartyMemberOffset, RecruitOffset, CaptureOffset
from .rules import ruleDict
from .items import party_member_items, key_items, FFXItem
from worlds.generic.Rules import add_rule
from ..AutoWorld import World

if typing.TYPE_CHECKING:
    from .__init__ import FFXWorld
else:
    FFXWorld = object

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
    def recruits(self) -> list[int]:
        return self["recruits"]
    @property
    def captures(self) -> list[int]:
        return self["captures"]
    @property
    def leads_to(self) -> list[int]:
        return self["leads_to"]
    @property
    def rules(self) -> list[str]:
        return self["rules"]


def create_regions(world: FFXWorld, player) -> None:
    def create_region_locations(region_name, treasures):
        region = Region(region_name, player, world.multiworld)
        for treasure_id in treasures:
            location = [x for x in FFXTreasureLocations if x.location_id == treasure_id][0]
            new_location = FFXLocation(player, location.name, location.rom_address, region)
            if location.missable:
                new_location.progress_type = LocationProgressType.EXCLUDED
            region.locations.append(new_location)
        return region

    def add_locations_by_ids(region: Region, location_ids: list[int], location_data: list[FFXLocationData], location_type: str = ""):
        for id in location_ids:
            locations = [x for x in location_data if x.location_id == id]
            if len(locations) != 1:
                #print(f"Ambiguous or invalid location id {id} ({location_type}) in Region {region.name}. Found {locations}")
                continue
            location = locations[0]
            new_location = FFXLocation(player, location.name, location.rom_address, region)
            if location.missable:
                new_location.progress_type = LocationProgressType.EXCLUDED
            region.locations.append(new_location)
            all_locations.append(new_location)

    def goal_requirement_rule(state):    
        match world.options.goal_requirement.value:
            case world.options.goal_requirement.option_none:
                return True
            case world.options.goal_requirement.option_party_members:
                return state.has_from_list_unique(
                        [character.itemName for character in party_member_items[:8]], world.player, min(world.options.required_party_members.value, 8))
            case world.options.goal_requirement.option_party_members_and_aeons:
                return state.has_from_list_unique(
                        [character.itemName for character in party_member_items], world.player, world.options.required_party_members.value)
            case world.options.goal_requirement.option_pilgrimage:
                return (
                    state.can_reach_location(world.location_id_to_name[ 8 | PartyMemberOffset], world.player) and   # Valefor
                    state.can_reach_location(world.location_id_to_name[ 9 | PartyMemberOffset], world.player) and   # Ifrit
                    state.can_reach_location(world.location_id_to_name[10 | PartyMemberOffset], world.player) and   # Ixion
                    state.can_reach_location(world.location_id_to_name[11 | PartyMemberOffset], world.player) and   # Shiva
                    state.can_reach_location(world.location_id_to_name[12 | PartyMemberOffset], world.player) and   # Bahamut
                    state.can_reach_location(world.location_id_to_name[37 | BossOffset       ], world.player)       # Yunalesca
                )
            case world.options.goal_requirement.option_nemesis:
                return (
                    state.can_reach_location(world.location_id_to_name[83 | BossOffset       ], world.player)       # Nemesis
                )
    
    def primer_requirement_rule(state):
        if world.options.required_primers.value > 0:
            return state.has_from_list_unique(
                [primer.itemName for primer in key_items[4:30]], world.player, world.options.required_primers.value) 
        else:
            return True
        
    captureDict: dict [int, str]= {
    0: "Besaid Island 1st visit",                           # Dingo
    1: "Besaid Island 1st visit",                           # Condor
    2: "Besaid Island 1st visit",                           # Water Flan
    3: "Kilika 1st visit: Pre-Geneaux",                     # Dinonix
    4: "Kilika 1st visit: Pre-Geneaux",                     # Killer Bee
    5: "Kilika 1st visit: Pre-Geneaux",                     # Yellow Element
    6: "Kilika 1st visit: Pre-Geneaux",                     # Ragora
    7: "Mi'ihen Highroad 1st visit: Pre-Chocobo Eater",     # Mi'ihen Fang
    8: "Mi'ihen Highroad 1st visit: Post-Chocobo Eater",    # Ipiria
    9: "Mi'ihen Highroad 1st visit: Pre-Chocobo Eater",     # Floating Eye
    10: "Mi'ihen Highroad 1st visit: Pre-Chocobo Eater",    # White Element
    11: "Mi'ihen Highroad 1st visit: Pre-Chocobo Eater",    # Raldo
    12: "Mi'ihen Highroad 1st visit: Post-Chocobo Eater",   # Vouivre
    13: "Mi'ihen Highroad 1st visit: Pre-Chocobo Eater",    # Bomb
    14: "Mi'ihen Highroad 1st visit: Pre-Chocobo Eater",    # Dual Horn
    15: "Mushroom Rock Road 1st visit: Pre-Sinspawn Gui",   # Raptor
    16: "Mushroom Rock Road 1st visit: Pre-Sinspawn Gui",   # Gandarewa
    17: "Mushroom Rock Road 1st visit: Pre-Sinspawn Gui",   # Thunder Flan
    18: "Mushroom Rock Road 1st visit: Pre-Sinspawn Gui",   # Red Element
    19: "Mushroom Rock Road 1st visit: Pre-Sinspawn Gui",   # Lamashtu
    20: "Mushroom Rock Road 1st visit: Pre-Sinspawn Gui",   # Funguar
    21: "Mushroom Rock Road 1st visit: Pre-Sinspawn Gui",   # Garuda
    22: "Djose 1st visit",                                  # Garm
    23: "Djose 1st visit",                                  # Simurgh
    24: "Djose 1st visit",                                  # Bite Bug
    25: "Djose 1st visit",                                  # Snow Flan
    26: "Djose 1st visit",                                  # Bunyip
    27: "Djose 1st visit",                                  # Basilisk
    28: "Moonflow 1st visit: Pre-Extractor",                # Ochu
    29: "Thunder Plains 1st visit",                         # Melusine
    30: "Thunder Plains 1st visit",                         # Aerouge
    31: "Thunder Plains 1st visit",                         # Buer
    32: "Thunder Plains 1st visit",                         # Gold Element
    33: "Thunder Plains 1st visit",                         # Kusariqqu
    34: "Thunder Plains 1st visit",                         # Larva
    35: "Thunder Plains 1st visit",                         # Iron Giant
    36: "Thunder Plains 1st visit",                         # Qactuar
    37: "Lake Macalania 1st visit: Pre-Crawler",            # Snow Wolf
    38: "Macalania Woods 1st visit: Pre-Spherimorph",       # Iguion
    39: "Macalania Woods 1st visit: Pre-Spherimorph",       # Wasp
    40: "Lake Macalania 1st visit: Pre-Crawler",            # Evil Eye
    41: "Lake Macalania 1st visit: Pre-Crawler",            # Ice Flan
    42: "Macalania Woods 1st visit: Pre-Spherimorph",       # Blue Element
    43: "Macalania Woods 1st visit: Pre-Spherimorph",       # Murussu
    44: "Lake Macalania 1st visit: Pre-Crawler",            # Mafdet
    45: "Macalania Woods 1st visit: Pre-Spherimorph",       # Xiphos
    46: "Macalania Woods 1st visit: Pre-Spherimorph",       # Chimera
    47: "Bikanel 1st visit",                                # Sand Wolf
    48: "Bikanel 1st visit",                                # Alcyone
    49: "Bikanel 1st visit",                                # Mushussu
    50: "Bikanel 1st visit",                                # Zu
    51: "Bikanel 1st visit",                                # Sand Worm
    52: "Bikanel 1st visit",                                # Cactuar
    53: "Calm Lands 1st visit: Pre-Defender X",             # Skoll
    54: "Calm Lands 1st visit: Pre-Defender X",             # Nebiros
    55: "Calm Lands 1st visit: Pre-Defender X",             # Flame Flan
    56: "Calm Lands 1st visit: Pre-Defender X",             # Shred
    57: "Calm Lands 1st visit: Pre-Defender X",             # Anacondaur
    58: "Calm Lands 1st visit: Pre-Defender X",             # Ogre
    59: "Calm Lands 1st visit: Pre-Defender X",             # Coeurl
    60: "Calm Lands 1st visit: Pre-Defender X",             # Chimera Brain
    61: "Calm Lands 1st visit: Pre-Defender X",             # Malboro
    62: "Cavern of the Stolen Fayth 1st visit",             # Yowie
    63: "Cavern of the Stolen Fayth 1st visit",             # Imp
    64: "Cavern of the Stolen Fayth 1st visit",             # Dark Element
    65: "Cavern of the Stolen Fayth 1st visit",             # Nidhogg
    66: "Cavern of the Stolen Fayth 1st visit",             # Thorn
    67: "Cavern of the Stolen Fayth 1st visit",             # Valaha
    68: "Cavern of the Stolen Fayth 1st visit",             # Epaaj
    69: "Cavern of the Stolen Fayth 1st visit",             # Ghost
    70: "Cavern of the Stolen Fayth 1st visit",             # Tonberry
    71: "Mt. Gagazet 1st visit: Post-Biran and Yenke",      # Bandersnatch
    72: "Mt. Gagazet 1st visit: Post-Seymour Flux",         # Ahriman
    73: "Mt. Gagazet 1st visit: Post-Seymour Flux",         # Dark Flan
    74: "Mt. Gagazet 1st visit: Post-Biran and Yenke",      # Grenade
    75: "Mt. Gagazet 1st visit: Post-Biran and Yenke",      # Grat
    76: "Mt. Gagazet 1st visit: Post-Seymour Flux",         # Grendel
    77: "Mt. Gagazet 1st visit: Post-Biran and Yenke",      # Bashura
    78: "Mt. Gagazet 1st visit: Post-Seymour Flux",         # Mandragora
    79: "Mt. Gagazet 1st visit: Post-Seymour Flux",         # Behemoth
    80: "Mt. Gagazet 1st visit: Post-Seymour Flux",         # Splasher
    81: "Mt. Gagazet 1st visit: Post-Seymour Flux",         # Achelous
    82: "Mt. Gagazet 1st visit: Post-Seymour Flux",         # Maelspike
    83: "Sin: Pre-Seymour Omnis",                           # Exoray
    84: "Sin: Post-Seymour Omnis",                          # Wraith
    85: "Sin: Pre-Seymour Omnis",                           # Gemini Sword
    86: "Sin: Pre-Seymour Omnis",                           # Gemini Club
    87: "Sin: Post-Seymour Omnis",                          # Demonolith
    88: "Sin: Post-Seymour Omnis",                          # Great Malboro
    89: "Sin: Post-Seymour Omnis",                          # Barbatos
    90: "Sin: Pre-Seymour Omnis",                           # Adamantoise
    91: "Sin: Pre-Seymour Omnis",                           # Behemoth King
    92: "Omega Ruins: Pre-Ultima Weapon",                   # Zaurus
    93: "Omega Ruins: Pre-Ultima Weapon",                   # Floating Death
    94: "Omega Ruins: Pre-Ultima Weapon",                   # Black Element
    95: "Omega Ruins: Pre-Ultima Weapon",                   # Halma
    96: "Omega Ruins: Pre-Ultima Weapon",                   # Puroboros
    97: "Omega Ruins: Pre-Ultima Weapon",                   # Spirit
    98: "Omega Ruins: Pre-Ultima Weapon",                   # Machea
    99: "Omega Ruins: Pre-Ultima Weapon",                   # Master Coeurl
    100: "Omega Ruins: Pre-Ultima Weapon",                  # Master Tonberry
    101: "Omega Ruins: Pre-Ultima Weapon",                  # Varuna
}


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

        add_locations_by_ids(new_region, region_data.treasures, FFXTreasureLocations, "Treasure")
        # for id in region_data.treasures:
        #     print(region_data.name, id)
        #     location = [x for x in FFXTreasureLocations if x.location_id == id][0]
        #     new_location = FFXLocation(player, location.name, location.rom_address, new_region)
        #     if location.missable:
        #         new_location.progress_type = LocationProgressType.EXCLUDED
        #     new_region.locations.append(new_location)
        #     all_locations.append(new_location)

        add_locations_by_ids(new_region, region_data.party_members, FFXPartyMemberLocations, "Party Member")
        # for id in region_data.party_members:
        #     print(region_data.name, id)
        #     location = [x for x in FFXPartyMemberLocations if x.location_id == id][0]
        #     new_location = FFXLocation(player, location.name, location.rom_address, new_region)
        #     if location.missable:
        #         new_location.progress_type = LocationProgressType.EXCLUDED
        #     new_region.locations.append(new_location)
        #     all_locations.append(new_location)

        add_locations_by_ids(new_region, region_data.bosses, FFXBossLocations, "Boss")
        # for id in region_data.bosses:
        #     print(region_data.name, id)
        #     location = [x for x in FFXBossLocations if x.location_id == id][0]
        #     new_location = FFXLocation(player, location.name, location.rom_address, new_region)
        #     if location.missable:
        #         new_location.progress_type = LocationProgressType.EXCLUDED
        #     new_region.locations.append(new_location)
        #     all_locations.append(new_location)

        # TODO: Implement in client
        # add_locations_by_ids(new_region, region_data.overdrives, FFXOverdriveLocations, "Overdrive")
        # for id in region_data.overdrives:
        #     print(region_data.name, id)
        #     location = [x for x in FFXOverdriveLocations if x.location_id == id][0]
        #     new_location = FFXLocation(player, location.name, location.rom_address, new_region)
        #     if location.missable:
        #         new_location.progress_type = LocationProgressType.EXCLUDED
        #     new_region.locations.append(new_location)
        #     all_locations.append(new_location)

        add_locations_by_ids(new_region, region_data.other, FFXOtherLocations, "Other")
        # for id in region_data.other:
        #     print(region_data.name, id)
        #     location = [x for x in FFXOtherLocations if x.location_id == id][0]
        #     new_location = FFXLocation(player, location.name, location.rom_address, new_region)
        #     if location.missable:
        #         new_location.progress_type = LocationProgressType.EXCLUDED
        #     new_region.locations.append(new_location)
        #     all_locations.append(new_location)

        add_locations_by_ids(new_region, region_data.recruits, FFXRecruitLocations, "Recruit")

        # add_locations_by_ids(new_region, region_data.captures, FFXCaptureLocations, "Capture")

    for location_id, region_name in captureDict.items():
        add_locations_by_ids(world.get_region(region_name), [location_id], FFXCaptureLocations, "Capture")

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

    top_level_regions: list[tuple[Region, Entrance]] = []
    for region_id, other_region in region_dict.items():
        if len(other_region.entrances) == 0:
            rules = region_rules.get(region_id)
            if rules is not None:
                rule_lambdas = [ruleDict[x](world) for x in rules]
                new_rule = lambda state, rule_list=rule_lambdas: all([rule(state) for rule in rule_list])
            else:
                new_rule = None
            menu_entrance: Entrance = menu_region.connect(other_region, rule=new_rule)
            top_level_regions.append((other_region, menu_entrance))

    #for this_region, _ in top_level_regions:
    #    for other_region, menu_entrance in top_level_regions:
    #        if this_region == other_region:
    #            continue
    #        world.multiworld.register_indirect_condition(this_region, menu_entrance)

    if not world.options.super_bosses.value:
        super_boss_location_ids = [
             2, # "Besaid: Dark Valefor"
            19, # "Bikanel: Dark Ifrit"
            13, # "Thunder Plains: Dark Ixion"
            18, # "Lake Macalania: Dark Shiva"
            38, # "Zanarkand: Dark Bahamut"
            31, # "Cavern of the Stolen Fayth: Dark Yojimbo"
            45, # "Mushroom Rock Road: Dark Mindy"
            46, # "Mushroom Rock Road: Dark Sandy"
            47, # "Mushroom Rock Road: Dark Cindy"
            34, # "Gagazet (Outside): Dark Anima"
            25, # "Airship: Penance"
            44, # "Omega Ruins: Omega Weapon"
            49, # Stratoavis
            50, # Malboro Menace
            51, # Kottos
            52, # Coeurlregina
            53, # Jormungand
            54, # Cactuar King
            55, # Espada
            56, # Abyss Worm
            57, # Chimerageist
            58, # Don Tonberry
            59, # Catoblepas
            60, # Abaddon
            61, # Vorban
            62, # Fenrir
            63, # Ornitholestes
            64, # Pteryx
            65, # Hornet
            66, # Vidatu
            67, # One-Eye
            68, # Jumbo Flan
            69, # Nega Elemental
            70, # Tanket
            71, # Fafnir
            72, # Sleep Sprout
            73, # Bomb King
            74, # Juggernaut
            75, # Ironclad
            76, # Earth Eater
            77, # Greater Sphere
            78, # Catastrophe
            79, # Th'uban
            80, # Neslug
            81, # Ultima Buster
            82, # Shinryu
            83, # Nemesis
        ]
        for id in super_boss_location_ids:
            location_name = world.location_id_to_name[id | BossOffset]
            #world.get_location(location_name).progress_type = LocationProgressType.EXCLUDED
            world.options.exclude_locations.value.add(location_name)
        location_name = world.location_id_to_name[332 | TreasureOffset]
        #world.get_location(location_name).progress_type = LocationProgressType.EXCLUDED
        world.options.exclude_locations.value.add(location_name)

    if not world.options.mini_games.value:
        mini_game_location_ids = [
            338, # "Calm Lands: Lv. 1 Key Sphere x1 (Dodger Chocobo Minigame Reward)"
            339, # "Calm Lands: Lv. 2 Key Sphere x1 x1 (Hyper Dodger Chocobo Minigame Reward)"
            340, # "Calm Lands: Lv. 3 Key Sphere x1 x1 (Catcher Chocobo Minigame Reward)"
            417, # "Calm Lands: Elixir x1 (Chocobo Race Reward)"
            418, # "Calm Lands: Megalixir x1 (Chocobo Race Reward)"
            419, # "Calm Lands: Three Stars x60 (Chocobo Race Reward)"
            420, # "Calm Lands: Pendulum x30 (Chocobo Race Reward)"
            421, # "Calm Lands: Wings to Discovery x30 (Chocobo Race Reward)"
            189, # "Thunder Plains: Megalixir x4 (Dodging Minigame Reward)",
            190, # "Thunder Plains: HP Sphere x3 (Dodging Minigame Reward)",
            191, # "Thunder Plains: Strength Sphere x3 (Dodging Minigame Reward)",
            192, # "Thunder Plains: MP Sphere x2 (Dodging Minigame Reward)",
            193, # "Thunder Plains: Mega-Potion x2 (Dodging Minigame Reward)",
            194, # "Thunder Plains: X-Potion x2 (Dodging Minigame Reward)",
            497, # "Story Win vs. Luca Goers Reward",
            274, # "Sun Sigil",
            278, # "Venus Sigil",
            277, # "Saturn Sigil",
            279, # "Mercury Sigil",
            244, # "Jupiter Sigil",
            114, # "Caladbolg",
            93,  # "World Champion",
            176, # "Cloudy Mirror",
        ]
        for id in mini_game_location_ids:
            location_name = world.location_id_to_name[id | TreasureOffset]
            #world.get_location(location_name).progress_type = LocationProgressType.EXCLUDED
            world.options.exclude_locations.value.add(location_name)

    if not world.options.recruit_sanity.value:
        recruit_location_ids = []
        for location in FFXRecruitLocations:
            recruit_location_ids.append(location.location_id)
        for id in recruit_location_ids:
            location_name = world.location_id_to_name[id | RecruitOffset]
            world.options.exclude_locations.value.add(location_name)
    
    if not world.options.capture_sanity.value:
        reward_locations = [
            113, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436,   # Area Conquest
            437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450,   # Species Conquest
            451, 452, 453, 454, 455, 456, 457, 458                                  # Original Creations
        ]
        boss_locations = [
            49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,                     # Area Conquest
            62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,                 # Species Conquest
            76, 77, 78, 79, 80, 81, 82, 83                                          # Original Creations
        ]
        for capture_location in FFXCaptureLocations:
            world.options.exclude_locations.value.add(capture_location.name)
        for reward_id in reward_locations:  # Monster Arena Reward Locations
            reward_name = world.location_id_to_name[reward_id | TreasureOffset]
            world.options.exclude_locations.value.add(reward_name)
        if world.options.super_bosses.value:
            for boss_id in boss_locations: # Monster Arena Super Bosses
                boss_name = world.location_id_to_name[boss_id | BossOffset]
                world.options.exclude_locations.value.add(boss_name)


    final_region = world.get_region("Sin: Braska's Final Aeon")
    final_region.add_event("Sin: Braska's Final Aeon", "Victory", location_type=FFXLocation, item_type=FFXItem)
    final_aeon = world.get_location("Sin: Braska's Final Aeon")

    #final_aeon.place_locked_item(victory_event)

    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)    
    final_aeon.access_rule = lambda state: goal_requirement_rule(state) and primer_requirement_rule(state)


        #world.get_location("Monster Arena: Nemesis"                  ).progress_type = LocationProgressType.EXCLUDED

    # character_names = [
    #     "Tidus",
    #     "Yuna",
    #     "Auron",
    #     "Kimahri",
    #     "Wakka",
    #     "Lulu",
    #     "Rikku"
    # ]
    #
    # for character, region in enumerate(FFXSphereGridLocations):
    #     new_region = Region(f"Sphere Grid: {character_names[character]}", player, world.multiworld)
    #     for location in region:
    #         new_location = FFXLocation(player, location.name, location.rom_address, new_region)
    #         if location.missable:
    #             new_location.progress_type = LocationProgressType.EXCLUDED
    #         new_region.locations.append(new_location)
    #         all_locations.append(new_location)
    #     menu_region.connect(new_region, rule=lambda state, i=character: state.has(party_members[i].itemName, world.player))


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
