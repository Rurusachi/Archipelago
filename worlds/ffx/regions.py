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
    0:   "Mi'ihen Highroad 1st visit: Pre-Chocobo Eater",                   # Raldo
    1:   "Captures: Djose Highroad & Moonflow",                             # Bunyip
    2:   "Macalania Woods 1st visit: Pre-Spherimorph",                      # Murussu
    3:   "Lake Macalania 1st visit: Pre-Crawler",                           # Mafdet
    4:   "Calm Lands 1st visit: Pre-Defender X",                            # Shred
    5:   "Captures: MRR, Djose Highroad & Moonflow",                        # Gandarewa
    6:   "Thunder Plains 1st visit",                                        # Aerouge
    7:   "Captures: Cavern of the Stolen Fayth & Mt. Gagazet",              # Imp
    8:   "Besaid Island 1st visit",                                         # Dingo
    9:   "Mi'ihen Highroad 1st visit: Pre-Chocobo Eater",                   # Mi'ihen Fang
    10:  "Captures: Djose Highroad & Moonflow",                             # Garm
    11:  "Lake Macalania 1st visit: Pre-Crawler",                           # Snow Wolf
    12:  "Bikanel 1st visit: Post-Zu",                                      # Sand Wolf
    13:  "Calm Lands 1st visit: Pre-Defender X",                            # Skoll
    14:  "Mt. Gagazet 1st visit: Post-Biran and Yenke",                     # Bandersnatch
    15:  "Besaid Island 1st visit",                                         # Water Flan
    16:  "Captures: Miihen Oldroad & MRR",                                  # Thunder Flan
    17:  "Captures: Djose Highroad & Moonflow",                             # Snow Flan
    18:  "Lake Macalania 1st visit: Pre-Crawler",                           # Ice Flan
    19:  "Calm Lands 1st visit: Pre-Defender X",                            # Flame Flan
    20:  "Captures: Mt. Gagazet Caves & Zanarkand",                         # Dark Flan
    21:  "Kilika 1st visit: Pre-Geneaux",                                   # Dinonix
    22:  "Captures: Miihen Oldroad & MRR",                                  # Ipiria
    23:  "Captures: MRR & Djose Highroad",                                  # Raptor
    24:  "Thunder Plains 1st visit",                                        # Melusine
    25:  "Macalania Woods 1st visit: Pre-Spherimorph",                      # Iguion
    26:  "Cavern of the Stolen Fayth 1st visit",                            # Yowie
    27:  "Besaid Island 1st visit",                                         # Condor
    28:  "Djose 1st visit",                                                 # Simurgh
    29:  "Bikanel 1st visit: Post-Zu",                                      # Alcyone
    30:  "Kilika 1st visit: Pre-Geneaux",                                   # Killer Bee
    31:  "Captures: Djose Highroad & Moonflow",                             # Bite Bug
    32:  "Macalania Woods 1st visit: Pre-Spherimorph",                      # Wasp
    33:  "Calm Lands 1st visit: Pre-Defender X",                            # Nebiros
    34:  "Captures: Miihen Highroad & MRR",                                 # Floating Eye
    35:  "Thunder Plains 1st visit",                                        # Buer
    36:  "Lake Macalania 1st visit: Pre-Crawler",                           # Evil Eye
    37:  "Captures: Mt. Gagazet Caves, Zanarkand & City of Dying Dreams",   # Ahriman
    38:  "Kilika 1st visit: Pre-Geneaux",                                   # Ragora
    39:  "Mt. Gagazet 1st visit: Post-Biran and Yenke",                     # Grat
    40:  "Mushroom Rock Road 1st visit: Pre-Sinspawn Gui",                  # Garuda
    41:  "Bikanel 1st visit: Post-Zu",                                      # Zu
    42:  "Bikanel 1st visit: Post-Zu",                                      # Sand Worm
  # 43:  "Unused Arena Index",
    44:  "Cavern of the Stolen Fayth 1st visit",                            # Ghost
    45:  "Mt. Gagazet 1st visit: Post-Seymour Flux",                        # Achelous
    46:  "Mt. Gagazet 1st visit: Post-Seymour Flux",                        # Maelspike
    47:  "Captures: Miihen Highroad & MRR",                                 # Dual Horn
    48:  "Cavern of the Stolen Fayth 1st visit",                            # Valaha
    49:  "Captures: Mt. Gagazet Caves & Zanarkand",                         # Grendel
    50:  "Captures: Miihen Oldroad & MRR",                                  # Vouivre
    51:  "Captures: MRR & Djose Highroad",                                  # Lamashtu
    52:  "Thunder Plains 1st visit",                                        # Kusariqqu
    53:  "Bikanel 1st visit: Post-Zu",                                      # Mushussu
    54:  "Captures: Cavern of the Stolen Fayth & Mt. Gagazet",              # Nidhogg
    55:  "Captures: Calm Lands & Cavern of the Stolen Fayth",               # Malboro
    56:  "Captures: City of Dying Dreams & Omega Ruins",                    # Great Malboro
    57:  "Calm Lands 1st visit: Pre-Defender X",                            # Ogre
    58:  "Captures: Mt. Gagazet Slope & Zanarkand",                         # Bashura
  # 59:  "Unused Arena Index",
    60:  "Mt. Gagazet 1st visit: Post-Seymour Flux",                        # Splasher
    61:  "Kilika 1st visit: Pre-Geneaux",                                   # Yellow Element
    62:  "Mi'ihen Highroad 1st visit: Pre-Chocobo Eater",                   # White Element
    63:  "Mushroom Rock Road 1st visit: Pre-Sinspawn Gui",                  # Red Element
    64:  "Thunder Plains 1st visit",                                        # Gold Element
    65:  "Macalania Woods 1st visit: Pre-Spherimorph",                      # Blue Element
    66:  "Cavern of the Stolen Fayth 1st visit",                            # Dark Element
    67:  "Omega Ruins: Pre-Ultima Weapon",                                  # Black Element
    68:  "Cavern of the Stolen Fayth 1st visit",                            # Epaaj
    69:  "Captures: Mt. Gagazet Caves & Zanarkand",                         # Behemoth
    70:  "Sin: Pre-Seymour Omnis",                                          # Behemoth King
    71:  "Macalania Woods 1st visit: Pre-Spherimorph",                      # Chimera
    72:  "Calm Lands 1st visit: Pre-Defender X",                            # Chimera Brain
    73:  "Captures: Calm Lands & Cavern of the Stolen Fayth",               # Coeurl
    74:  "Omega Ruins: Pre-Ultima Weapon",                                  # Master Coeurl
    75:  "Captures: City of Dying Dreams & Omega Ruins",                    # Demonolith
    76:  "Thunder Plains 1st visit",                                        # Iron Giant
    77:  "Sin: Pre-Seymour Omnis",                                          # Gemini Sword
    78:  "Sin: Pre-Seymour Omnis",                                          # Gemini Club
    79:  "Djose 1st visit",                                                 # Basilisk
    80:  "Calm Lands 1st visit: Pre-Defender X",                            # Anacondaur
    81:  "Captures: Inside Sin & Omega Ruins",                              # Adamantoise
    82:  "Captures: City of Dying Dreams & Omega Ruins",                    # Varuna
    83:  "Moonflow 1st visit: Pre-Extractor",                               # Ochu
    84:  "Captures: Mt. Gagazet Caves & Zanarkand",                         # Mandragora
    85:  "Captures: Miihen Highroad & MRR",                                 # Bomb
    86:  "Mt. Gagazet 1st visit: Post-Biran and Yenke",                     # Grenade
    87:  "Thunder Plains 1st visit",                                        # Qactuar
    88:  "Bikanel 1st visit: Post-Zu",                                      # Cactuar
    89:  "Thunder Plains 1st visit",                                        # Larva
    90:  "Sin: Post-Seymour Omnis",                                         # Barbatos
    91:  "Captures: MRR, Djose Highroad & Moonflow",                        # Funguar
    92:  "Cavern of the Stolen Fayth 1st visit",                            # Thorn
    93:  "Sin: Pre-Seymour Omnis",                                          # Exoray
    94:  "Macalania Woods 1st visit: Pre-Spherimorph",                      # Xiphos
    95:  "Omega Ruins: Pre-Ultima Weapon",                                  # Puroboros
    96:  "Omega Ruins: Pre-Ultima Weapon",                                  # Spirit
    97:  "Captures: City of Dying Dreams & Omega Ruins",                    # Wraith    
    98:  "Cavern of the Stolen Fayth 1st visit",                            # Tonberry
    99:  "Omega Ruins: Pre-Ultima Weapon",                                  # Master Tonberry
    100: "Omega Ruins: Pre-Ultima Weapon",                                  # Zaurus
    101: "Omega Ruins: Pre-Ultima Weapon",                                  # Halma
    102: "Omega Ruins: Pre-Ultima Weapon",                                  # Floating Death
    103: "Omega Ruins: Pre-Ultima Weapon",                                  # Machea
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
            world.options.exclude_locations.value.add(location_name)

    if not world.options.recruit_sanity.value:
        recruit_location_ids = []
        for location in FFXRecruitLocations:
            recruit_location_ids.append(location.location_id)
        for id in recruit_location_ids:
            location_name = world.location_id_to_name[id | RecruitOffset]
            world.options.exclude_locations.value.add(location_name)

    if not world.options.capture_sanity.value:
        for location_id, _ in captureDict.items():
            location_name = world.location_id_to_name[location_id | CaptureOffset]
            world.options.exclude_locations.value.add(location_name)

    if not world.options.creation_rewards.value == world.options.creation_rewards.option_original:
        arena_reward_location_ids = [
            424, # Area Conquest - Capture 1 of Each Besaid Fiend (NPC)
            425, # Area Conquest - Capture 1 of Each Kilika Fiend (NPC)
            426, # Area Conquest - Capture 1 of Each Mi'ihen Highraod Fiend (NPC)
            427, # Area Conquest - Capture 1 of Each MRR Fiend (NPC)
            428, # Area Conquest - Capture 1 of Each Djose Highroad Fiend (NPC)
            429, # Area Conquest - Capture 1 of Each Thunder Plains Fiend (NPC)
            430, # Area Conquest - Capture 1 of Each Macalania Fiend (NPC)
            431, # Area Conquest - Capture 1 of Each Bikanel Fiend (NPC)
            432, # Area Conquest - Capture 1 of Each Calm Lands Fiend (NPC)
            433, # Area Conquest - Capture 1 of Each CotSF Fiend (NPC)
            434, # Area Conquest - Capture 1 of Each Gagazet Fiend (NPC)
            435, # Area Conquest - Capture 1 of Each Inside Sin Fiend (NPC)
            436, # Area Conquest - Capture 1 of Each Omega Ruins Fiend (NPC)
            437, # Species Conquest - Capture 3 of Each Wolf Fiend (NPC)
            438, # Species Conquest - Capture 3 of Each Reptile Fiend (NPC)
            439, # Species Conquest - Capture 5 of Each Bird Fiend (NPC)
            440, # Species Conquest - Capture 4 of Each Wasp Fiend (NPC)
            441, # Species Conquest - Capture 4 of Each Imp Fiend (NPC)
            442, # Species Conquest - Capture 4 of Each Eye Fiend (NPC)
            443, # Species Conquest - Capture 3 of Each Flan Fiend (NPC)
            444, # Species Conquest - Capture 3 of Each Elemental Fiend (NPC)
            445, # Species Conquest - Capture 3 of Each Helm Fiend (NPC)
            446, # Species Conquest - Capture 4 of Each Drake Fiend (NPC)
            447, # Species Conquest - Capture 5 of Each Fungi Fiend (NPC)
            448, # Species Conquest - Capture 5 of Each Bomb Fiend (NPC)
            449, # Species Conquest - Capture 5 of Each Ruminant Fiend (NPC)
            450, # Species Conquest - Capture 10 of Each Iron Giant Fiend (NPC)
            451, # Original Creation - Complete 2 Area Conquests (NPC)
            452, # Original Creation - Complete 2 Species Conquests (NPC)
            453, # Original Creation - Complete 6 Area Conquests (NPC)
            454, # Original Creation - Complete 6 Species Conquests (NPC)
            455, # Original Creation - Capture 1 of Each Fiend (NPC)
            456, # Original Creation - Capture 5 of Each Fiend (NPC)
            457, # Original Creation - Capture 2 of Each Gagazet Underwater Fiend (NPC)
            458, # Original Creation - Capture 10 of Each Fiend (NPC)
        ]
        match world.options.creation_rewards.value:
            case world.options.creation_rewards.option_area:
                arena_reward_location_ids = arena_reward_location_ids[14:]
            case world.options.creation_rewards.option_species:
                arena_reward_location_ids = arena_reward_location_ids[28:]
        for id in arena_reward_location_ids:
            location_name = world.location_id_to_name[id | TreasureOffset]
            world.options.exclude_locations.value.add(location_name)
    
    if not world.options.arena_bosses.value == world.options.arena_bosses.option_original:
        arena_boss_location_ids = [
            49, # Stratoavis - Area Conquests
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
            62, # Fenrir - Species Conquests
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
            76, # Earth Eater - Original Creations
            77, # Greater Sphere
            78, # Catastrophe
            79, # Th'uban
            80, # Neslug
            81, # Ultima Buster
            82, # Shinryu
            83, # Nemesis
        ]
        match world.options.arena_bosses.value:
            case world.options.arena_bosses.option_area:
                arena_boss_location_ids = arena_boss_location_ids[13:]
            case world.options.arena_bosses.option_species:
                arena_boss_location_ids = arena_boss_location_ids[27:]       
        for id in arena_boss_location_ids:
            location_name = world.location_id_to_name[id | BossOffset]
            world.options.exclude_locations.value.add(location_name)

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
          # 25, # "Airship: Penance"
            44, # "Omega Ruins: Omega Weapon"
        ]
        for id in super_boss_location_ids:
            location_name = world.location_id_to_name[id | BossOffset]
            world.options.exclude_locations.value.add(location_name)
        location_name = world.location_id_to_name[332 | TreasureOffset]
        world.options.exclude_locations.value.add(location_name)
        
    
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
