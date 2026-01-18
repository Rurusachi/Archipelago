import typing
from collections import Counter
from typing import Callable

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, CollectionRule
from . import key_items
from .items import character_names, stat_abilities, item_to_stat_value, aeon_names, region_unlock_items, equipItemOffset
from .locations import TreasureOffset, OtherOffset, BossOffset, PartyMemberOffset, CaptureOffset

if typing.TYPE_CHECKING:
    from .__init__ import FFXWorld
else:
    FFXWorld = object

world_battle_levels: dict[str, int] = {
"Baaj Temple":                 1,
"Besaid":                      2,
"Kilika":                      3,
"Luca":                        4,
"Mi'ihen Highroad":            5,
"Mushroom Rock Road":          6,
"Djose":                       7,
"Moonflow":                    8,
"Guadosalam":                  1,
"Thunder Plains":              9,
"Macalania":                  10,
"Bikanel":                    11,
"Bevelle":                    12,
"Calm Lands":                 13,
"Cavern of the Stolen Fayth": 13,
"Mt. Gagazet":                14,
"Zanarkand Ruins":            15,
"Sin":                        16,
"Airship":                    12,
"Omega Ruins":                17,
}

region_to_first_visit: dict[str, str] = {
"Baaj Temple":                "Baaj Temple 1st visit",
"Besaid":                     "Besaid Island 1st visit",
"Kilika":                     "Kilika 1st visit: Pre-Geneaux",
"Luca":                       "Luca 1st visit: Pre-Oblitzerator",
"Mi'ihen Highroad":           "Mi'ihen Highroad 1st visit: Pre-Chocobo Eater",
"Mushroom Rock Road":         "Mushroom Rock Road 1st visit: Pre-Sinspawn Gui",
"Djose":                      "Djose 1st visit",
"Moonflow":                   "Moonflow 1st visit: Pre-Extractor",
"Guadosalam":                 "Guadosalam 1st visit",
"Thunder Plains":             "Thunder Plains 1st visit",
"Macalania":                  "Macalania Woods 1st visit: Pre-Spherimorph",
"Bikanel":                    "Bikanel 1st visit",
"Bevelle":                    "Bevelle 1st visit: Pre-Isaaru",
"Calm Lands":                 "Calm Lands 1st visit: Pre-Defender X",
"Cavern of the Stolen Fayth": "Cavern of the Stolen Fayth 1st visit",
"Mt. Gagazet":                "Mt. Gagazet 1st visit: Pre-Biran and Yenke",
"Zanarkand Ruins":            "Zanarkand Ruins 1st visit: Pre-Spectral Keeper",
"Sin":                        "Sin: Pre-Seymour Omnis",
"Airship":                    "Airship 1st visit: Pre-Evrae",
"Omega Ruins":                "Omega Ruins: Pre-Ultima Weapon",
}




def create_region_access_rule(world: FFXWorld, region_name: str):
    region_level = world_battle_levels[region_name]
    if region_level < 5:
        return lambda state: state.has(f"Region: {region_name}", world.player)
    else:
        appropriate_level_regions = [other_region for other_region, other_level in world_battle_levels.items() if
                                     other_region != region_name and region_level > other_level >= region_level - world.options.logic_difficulty.value]

        return lambda state: state.has(f"Region: {region_name}", world.player) and any([state.can_reach_region(region_to_first_visit[other_region], world.player) for other_region in appropriate_level_regions])

def create_level_rule(world: FFXWorld, level: int):
    appropriate_level_regions = [other_region for other_region, other_level in world_battle_levels.items() if
                                 level > other_level >= level - world.options.logic_difficulty.value]

    return lambda state: any([state.can_reach_region(region_to_first_visit[other_region], world.player) for other_region in appropriate_level_regions])

def create_ability_rule(world: FFXWorld, ability_name: str):
    #return lambda state: state.has_any([f"{name} Ability: {ability_name}" for name in character_names], world.player)
    #return lambda state: True;               "       Ability: Fire"
    #temp = [(f"{name} Ability: {ability_name}", f"Party Member: {name}") for name in character_names]
    #for ability, character in temp:
    #    print(world.item_name_to_id[ability])
    #    print(world.item_name_to_id[character])
    #print(temp)
    if world.options.sphere_grid_randomization.value == world.options.sphere_grid_randomization.option_on:
        return lambda state: any([state.has_all([f"{name} Ability: {ability_name}", f"Party Member: {name}"], world.player) for name in character_names])
    else:
        return lambda state: True


#def create_stat_rule(world: World, stat_total: int):
#    return lambda state: state.has
def create_stat_total_rule(world: FFXWorld, num_party_members: int, stat_total: int) -> CollectionRule:
    def has_stat_total(state: CollectionState) -> bool:
        player_prog_items = state.prog_items[world.player]
        totals = Counter()
        for item, count in player_prog_items.items():
            if item in stat_abilities:
                character, value = item_to_stat_value[item]
                totals[character] += value*count

        return len([total for total in totals.values() if total > stat_total]) >= num_party_members
        #for total in totals.values():
        #    if total > stat_total:
        #        return True
        #return False
    return has_stat_total

def create_min_party_rule(world: FFXWorld, num_characters: int) -> CollectionRule:
    return lambda state: state.has_from_list_unique([f"Party Member: {name}" for name in character_names], world.player, num_characters)

def create_min_swimmers_rule(world: FFXWorld, num_characters: int) -> CollectionRule:
    return lambda state: state.has_from_list_unique([f"Party Member: {name}" for name in ["Tidus", "Wakka", "Rikku"]], world.player, num_characters)

def create_min_summon_rule(world: FFXWorld, num_aeons: int) -> CollectionRule:
    return lambda state: state.has(f"Party Member: Yuna", world.player) and state.has_from_list_unique([f"Party Member: {name}" for name in aeon_names], world.player, num_aeons)

ruleDict: dict[str, Callable[[FFXWorld], CollectionRule]] = {
    "Sin Fin":             lambda world: lambda state: create_level_rule(world,  2)(state) and create_min_party_rule   (world, 3)(state) and state.has("Party Member: Wakka", world.player),
    "Sinspawn Echuilles":  lambda world: lambda state: create_level_rule(world,  2)(state) and create_min_swimmers_rule(world, 2)(state),
    "Sinspawn Geneaux":    lambda world: lambda state: create_level_rule(world,  3)(state) and create_min_party_rule   (world, 3)(state),
    "Oblitzerator":        lambda world: lambda state: create_level_rule(world,  4)(state) and create_min_party_rule   (world, 3)(state),
    "Chocobo Eater":       lambda world: lambda state: create_level_rule(world,  5)(state) and create_min_party_rule   (world, 3)(state),
    "Sinspawn Gui":        lambda world: lambda state: create_level_rule(world,  6)(state) and create_min_party_rule   (world, 3)(state),
    "Extractor":           lambda world: lambda state: create_level_rule(world,  8)(state) and create_min_swimmers_rule(world, 2)(state), # At least 2 swimmers
    "Spherimorph":         lambda world: lambda state: create_level_rule(world, 10)(state) and create_min_party_rule   (world, 3)(state),
    "Crawler":             lambda world: lambda state: create_level_rule(world, 10)(state) and create_min_party_rule   (world, 3)(state),
    "Seymour/Anima":       lambda world: lambda state: create_level_rule(world, 10)(state) and create_min_party_rule   (world, 3)(state),
    "Wendigo":             lambda world: lambda state: create_level_rule(world, 10)(state) and create_min_party_rule   (world, 3)(state),
    "Evrae":               lambda world: lambda state: create_level_rule(world, 12)(state) and create_min_party_rule   (world, 3)(state),
    "Airship Sin":         lambda world: lambda state: create_level_rule(world, 16)(state) and create_min_party_rule   (world, 3)(state),
    "Overdrive Sin":       lambda world: lambda state: create_level_rule(world, 16)(state) and create_min_party_rule   (world, 3)(state),
    "Penance":             lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Isaaru":              lambda world: lambda state: create_level_rule(world, 12)(state) and create_min_summon_rule  (world, 2)(state),    # Yuna + 2 summons
    "Evrae Altana":        lambda world: lambda state: create_level_rule(world, 12)(state) and create_min_swimmers_rule(world, 3)(state), # All swimmers
    "Seymour Natus":       lambda world: lambda state: create_level_rule(world, 12)(state) and create_min_party_rule   (world, 3)(state),
    "Defender X":          lambda world: lambda state: create_level_rule(world, 13)(state) and create_min_party_rule   (world, 3)(state),
    "Biran and Yenke":     lambda world: lambda state: create_level_rule(world, 14)(state) and create_min_party_rule   (world, 3)(state),
    "Seymour Flux":        lambda world: lambda state: create_level_rule(world, 14)(state) and create_min_party_rule   (world, 3)(state),
    "Sanctuary Keeper":    lambda world: lambda state: create_level_rule(world, 14)(state) and create_min_party_rule   (world, 3)(state),
    "Spectral Keeper":     lambda world: lambda state: create_level_rule(world, 15)(state) and create_min_party_rule   (world, 3)(state),
    "Yunalesca":           lambda world: lambda state: create_level_rule(world, 15)(state) and create_min_party_rule   (world, 3)(state),
    "Seymour Omnis":       lambda world: lambda state: create_level_rule(world, 16)(state) and create_min_party_rule   (world, 3)(state),
    "Braska's Final Aeon": lambda world: lambda state: create_level_rule(world, 16)(state) and create_min_party_rule   (world, 3)(state),
    "Ultima Weapon":       lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Omega Weapon":        lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_party_rule   (world, 3)(state),
    "Geosgaeno":           lambda world: lambda state: create_level_rule(world, 15)(state) and create_min_swimmers_rule(world, 3)(state),

    "Dark Valefor":        lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_party_rule   (world, 3)(state) and state.has("Party Member: Yuna", world.player),
    "Dark Ifrit":          lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_party_rule   (world, 3)(state),
    "Dark Ixion":          lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_party_rule   (world, 3)(state),
    "Dark Shiva":          lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_party_rule   (world, 3)(state),
    "Dark Bahamut":        lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_party_rule   (world, 3)(state),
    "Dark Anima":          lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_party_rule   (world, 3)(state),
    "Dark Yojimbo":        lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_party_rule   (world, 3)(state),
    "Dark Magus Sisters":  lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_party_rule   (world, 3)(state),

    "Monster Arena: Stratoavis":          lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Malboro Menace":      lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Kottos":              lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Coeurlregina":        lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Jormungand":          lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Cactuar King":        lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Espada":              lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Abyss Worm":          lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Chimerageist":        lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Don Tonberry":        lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Catoblepas":          lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Abaddon":             lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Vorban":              lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),

    "Monster Arena: Fenrir":              lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Ornitholestes":       lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Pteryx":              lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Hornet":              lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Vidatu":              lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: One-Eye":             lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Jumbo Flan":          lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Nega Elemental":      lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Tanket":              lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Fafnir":              lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Sleep Sprout":        lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Bomb King":           lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Juggernaut":          lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Ironclad":            lambda world: lambda state: create_level_rule(world, 17)(state) and create_min_party_rule   (world, 3)(state),
    
    "Monster Arena: Earth Eater":         lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Greater Sphere":      lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Catastrophe":         lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Th'uban":             lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Neslug":              lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Ultima Buster":       lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_party_rule   (world, 3)(state),
    "Monster Arena: Shinryu":             lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_swimmers_rule(world, 3)(state),
    "Monster Arena: Nemesis":             lambda world: lambda state: create_level_rule(world, 18)(state) and create_min_party_rule   (world, 3)(state),

    "Baaj Temple":                lambda world: create_region_access_rule(world, "Baaj Temple"), # lambda state: state.has("Region: Baaj Temple", world.player),
    "Besaid":                     lambda world: create_region_access_rule(world, "Besaid"),
    "Kilika":                     lambda world: create_region_access_rule(world, "Kilika"),
    "Luca":                       lambda world: create_region_access_rule(world, "Luca"),
    "Mi'ihen Highroad":           lambda world: create_region_access_rule(world, "Mi'ihen Highroad"),
    "Mushroom Rock Road":         lambda world: create_region_access_rule(world, "Mushroom Rock Road"),
    "Djose":                      lambda world: create_region_access_rule(world, "Djose"),
    "Moonflow":                   lambda world: create_region_access_rule(world, "Moonflow"),
    "Guadosalam":                 lambda world: create_region_access_rule(world, "Guadosalam"),
    "Thunder Plains":             lambda world: create_region_access_rule(world, "Thunder Plains"),
    "Macalania":                  lambda world: create_region_access_rule(world, "Macalania"),
    "Bikanel":                    lambda world: create_region_access_rule(world, "Bikanel"),
    "Bevelle":                    lambda world: create_region_access_rule(world, "Bevelle"),
    "Calm Lands":                 lambda world: create_region_access_rule(world, "Calm Lands"),
    "Cavern of the Stolen Fayth": lambda world: create_region_access_rule(world, "Cavern of the Stolen Fayth"),
    "Mt. Gagazet":                lambda world: create_region_access_rule(world, "Mt. Gagazet"),
    "Zanarkand Ruins":            lambda world: create_region_access_rule(world, "Zanarkand Ruins"),
    "Sin":                        lambda world: create_region_access_rule(world, "Sin"),
    "Airship":                    lambda world: create_region_access_rule(world, "Airship"),
    "Omega Ruins":                lambda world: create_region_access_rule(world, "Omega Ruins"),
}


def set_rules(world: FFXWorld) -> None:
    def can_reach_minimum_locations(state: CollectionState, locations: list, locations_required: int) -> bool:
        sum = 0
        for location in locations:
            if location.can_reach(state):
                sum += 1
                if sum >= locations_required:
                    return True
        return False
    
    ## Remiem
    # Valefor fight
    add_rule(world.get_location(world.location_id_to_name[379 | TreasureOffset]), create_min_summon_rule(world, 2))
    # Ifrit fight
    add_rule(world.get_location(world.location_id_to_name[381 | TreasureOffset]), create_min_summon_rule(world, 2))
    # Ixion fight
    add_rule(world.get_location(world.location_id_to_name[383 | TreasureOffset]), create_min_summon_rule(world, 2))
    # Shiva fight
    add_rule(world.get_location(world.location_id_to_name[385 | TreasureOffset]), create_min_summon_rule(world, 2))
    # Bahamut fight
    add_rule(world.get_location(world.location_id_to_name[334 | TreasureOffset]), create_min_summon_rule(world, 2))
    # Yojimbo fight
    add_rule(world.get_location(world.location_id_to_name[388 | TreasureOffset]), lambda state: create_min_summon_rule(world, 2)(state) and state.has(f"Party Member: Yojimbo", world.player))
    # Anima fight
    add_rule(world.get_location(world.location_id_to_name[390 | TreasureOffset]), lambda state: state.has(f"Party Member: Yuna", world.player) and state.has_all([f"Party Member: {name}" for name in ["Yojimbo", "Anima"]], world.player))
    # Magus Sisters fight
    add_rule(world.get_location(world.location_id_to_name[392 | TreasureOffset]), lambda state: state.has(f"Party Member: Yuna", world.player) and state.has_all([f"Party Member: {name}" for name in ["Yojimbo", "Anima", "Magus Sisters"]], world.player))
    # Send Belgemine? (Moon sigil)
    add_rule(world.get_location(world.location_id_to_name[275 | TreasureOffset]), lambda state: state.has(f"Party Member: Yuna", world.player) and state.has_all([f"Party Member: {name}" for name in ["Yojimbo", "Anima", "Magus Sisters"]], world.player))


    ## Dark Aeons
    dark_aeons = [
        ( 2, "Dark Valefor"      ),  # "Besaid: Dark Valefor
        (13, "Dark Ifrit"        ),  # "Thunder Plains: Dark Ixion
        (18, "Dark Ixion"        ),  # "Lake Macalania: Dark Shiva
        (19, "Dark Shiva"        ),  # "Bikanel: Dark Ifrit
        (31, "Dark Bahamut"      ),  # "Cavern of the Stolen Fayth: Dark Yojimbo
        (34, "Dark Anima"        ),  # "Gagazet (Outside): Dark Anima
        (38, "Dark Yojimbo"      ),  # "Zanarkand: Dark Bahamut
        (45, "Dark Magus Sisters"),  # "Mushroom Rock Road: Dark Mindy
        (46, "Dark Magus Sisters"),  # "Mushroom Rock Road: Dark Sandy
        (47, "Dark Magus Sisters"),  # "Mushroom Rock Road: Dark Cindy
    ]
    for location_id, aeon in dark_aeons:
        add_rule(world.get_location(world.location_id_to_name[location_id | BossOffset]),
                 ruleDict[aeon](world))

    ## Aeons
    # Anima
    add_rule(world.get_location(world.location_id_to_name[13 | PartyMemberOffset]), lambda state: all((
        state.can_reach_location(world.location_id_to_name[ 15 | TreasureOffset], world.player),  # Besaid
        state.can_reach_location(world.location_id_to_name[ 19 | TreasureOffset], world.player),  # Kilika
        state.can_reach_location(world.location_id_to_name[484 | TreasureOffset], world.player),  # Djose
        state.can_reach_location(world.location_id_to_name[485 | TreasureOffset], world.player),  # Macalania
        state.can_reach_location(world.location_id_to_name[217 | TreasureOffset], world.player),  # Bevelle
        state.can_reach_location(world.location_id_to_name[209 | TreasureOffset], world.player),  # Zanarkand
    )))
    # Magus Sisters
    add_rule(world.get_location(world.location_id_to_name[15 | PartyMemberOffset]), lambda state: state.has_all(["Flower Scepter", "Blossom Crown"], world.player))


    ## Captures
    # Fiend Captures
    for location_id in range(104):
        if (not location_id == 43 and not location_id == 59):
            add_rule(world.get_location(world.location_id_to_name[location_id | CaptureOffset]), 
                lambda state: state.can_reach_region("Monster Arena", world.player)
            )


    ## Capture Rewards
    # Area Conquest
    area_conquest = [
        (424, 49, ("Besaid Island 1st visit",                             )),  # Stratoavis
        (425, 50, ("Kilika 1st visit: Pre-Geneaux",                       )),  # Malboro Menace
        (426, 51, ("Mi'ihen Highroad 1st visit: Post-Chocobo Eater",      )),  # Kottos
        (427, 52, ("Mushroom Rock Road 1st visit: Pre-Sinspawn Gui",      )),  # Coeurlregina
        (428, 53, ("Djose 1st visit", "Moonflow 1st visit: Pre-Extractor",)),  # Jormungand
        (429, 54, ("Thunder Plains 1st visit",                            )),  # Cactuar King
        (430, 55, ("Lake Macalania 1st visit: Pre-Crawler",               )),  # Espada
        (431, 56, ("Bikanel 1st visit",                                   )),  # Abyss Worm
        (432, 57, ("Calm Lands 1st visit: Pre-Defender X",                )),  # Chimerageist
        (433, 58, ("Cavern of the Stolen Fayth 1st visit",                )),  # Don Tonberry
        (434, 59, ("Mt. Gagazet 1st visit: Post-Seymour Flux",            )),  # Catoblepas
        (435, 60, ("Sin: Post-Seymour Omnis",                             )),  # Abaddon
        (436, 61, ("Omega Ruins: Pre-Ultima Weapon",                      )),  # Vorban
    ]
    for location_id, boss_id, regions in area_conquest:
        location = world.get_location(world.location_id_to_name[location_id | TreasureOffset])
        boss = world.get_location(world.location_id_to_name[boss_id | BossOffset])
        
        for region in regions:
            add_rule(location, lambda state: state.can_reach_region(region, world.player))
        add_rule(boss, lambda state, location=location: state.can_reach_location(location.name, world.player))
        add_rule(boss, ruleDict[boss.name](world))


    # Species Conquest
    species_conquest = [
        (437, 62, (8, 9, 10, 11, 12, 13, 14    )), # Fenrir
        (438, 63, (21, 22, 23, 24, 25, 26, 100 )), # Ornitholestes
        (439, 64, (27, 28, 29                  )), # Pteryx
        (440, 65, (30, 31, 32, 33              )), # Hornet
        (441, 66, (5, 6, 7                     )), # Vidatu
        (442, 67, (34, 35, 36, 37, 102         )), # One-Eye
        (443, 68, (15, 16, 17, 18, 19, 20      )), # Jumbo Flan
        (444, 69, (61, 62, 63, 64, 65, 66, 67  )), # Nega Elemental
        (445, 69, (0, 1, 2, 3, 4, 101          )), # Tanket
        (446, 70, (50, 51, 52, 53, 54          )), # Fafnir
        (447, 71, (91, 92, 93                  )), # Sleep Sprout
        (448, 72, (85, 86, 95                  )), # Bomb King
        (449, 73, (47, 48, 49                  )), # Juggernaut
        (450, 74, (76, 77, 78                  )), # Ironclad
    ]
    for location_id, boss_id, captures in species_conquest:
        location = world.get_location(world.location_id_to_name[location_id | TreasureOffset])
        boss = world.get_location(world.location_id_to_name[boss_id | BossOffset])
        
        for capture_id in captures:
            add_rule(location, lambda state: state.can_reach_location(world.location_id_to_name[capture_id | CaptureOffset], world.player))
        add_rule(boss, lambda state, location=location: state.can_reach_location(location.name, world.player))
        add_rule(boss, ruleDict[boss.name](world))
 

    # Original Creations    
    original_creation_conquests = [
        (451, 76, area_conquest,    2), # Earth Eather
        (452, 77, species_conquest, 2), # Greater Sphere
        (453, 78, area_conquest,    6), # Catastrophe
        (454, 79, species_conquest, 6), # Th'uban
    ]
    for location_id, boss_id, arena_type, creations_required in original_creation_conquests:
        location = world.get_location(world.location_id_to_name[location_id | TreasureOffset])
        boss = world.get_location(world.location_id_to_name[boss_id | BossOffset])
        capture_locations = [world.get_location(world.location_id_to_name[arena_id | TreasureOffset]) for arena_id, _, _ in arena_type]
        
        add_rule(location, lambda state, capture_locations=capture_locations, creations_required=creations_required: 
                can_reach_minimum_locations(state, capture_locations, creations_required))
        add_rule(boss, lambda state, location=location: state.can_reach_location(location.name, world.player))
        add_rule(boss, ruleDict[boss.name](world))
    

    original_creation_captures = [
        (455, 80), # Neslug (1x Capture)
        (456, 81), # Ultima Buster (5x Captures)
        (458, 83), # Nemesis (10x Captures)
    ]
    capture_regions = [
        "Besaid Island 1st visit",
        "Kilika 1st visit: Pre-Geneaux",
        "Mi'ihen Highroad 1st visit: Post-Chocobo Eater",
        "Mushroom Rock Road 1st visit: Pre-Sinspawn Gui",
        "Djose 1st visit",
        "Moonflow 1st visit: Pre-Extractor",
        "Thunder Plains 1st visit",
        "Lake Macalania 1st visit: Pre-Crawler",
        "Bikanel 1st visit",
        "Calm Lands 1st visit: Pre-Defender X",
        "Cavern of the Stolen Fayth 1st visit",
        "Mt. Gagazet 1st visit: Post-Seymour Flux",
        "Sin: Post-Seymour Omnis",
        "Omega Ruins: Pre-Ultima Weapon"
    ]
    for location_id, boss_id in original_creation_captures:
        location = world.get_location(world.location_id_to_name[location_id | TreasureOffset])
        boss = world.get_location(world.location_id_to_name[boss_id | BossOffset])
        
        for region in capture_regions:
            add_rule(location, lambda state: state.can_reach_region(region, world.player))
        add_rule(boss, lambda state, location=location: state.can_reach_location(location.name, world.player))
        add_rule(boss, ruleDict[boss.name](world))


    # Shinryu (Underwater Captures in Gagazet)
    location = world.get_location(world.location_id_to_name[457 | TreasureOffset])
    boss = world.get_location(world.location_id_to_name[82 | BossOffset])
    add_rule(location, lambda state: state.can_reach_region("Mt. Gagazet 1st visit: Post-Seymour Flux", world.player))
    add_rule(boss, lambda state: state.can_reach_location(location.name, world.player))
    add_rule(boss, ruleDict["Monster Arena: Shinryu"](world))


    # Nemesis requires killing all other creations
    creation_bosses = [
    49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,     # Area Conquest
    62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, # Species Conquest
    76, 77, 78, 79, 80, 81, 82                              # Original Creations
    ]
    nemesis = world.get_location(world.location_id_to_name[83 | BossOffset])
    # creation_bosses = [world.get_location(world.location_id_to_name[boss_id | BossOffset]) for boss_id in range(49, 83)]
    for creation_id in creation_bosses:
        creation_name = world.location_id_to_name[creation_id | BossOffset]
        add_rule(nemesis, lambda state, creation_name=creation_name: state.can_reach_location(creation_name, world.player))
    add_rule(nemesis, ruleDict[nemesis.name](world))


    ## Celestials
    celestial_weapon_locations = [
        5,
        93,
        #99, # Requires Rusty Sword
        113,
        114,
        188,
        #214, # Airship password location
    ]
    for location_id in celestial_weapon_locations:
        add_rule(world.get_location(world.location_id_to_name[location_id | TreasureOffset]),
                 lambda state: state.has("Celestial Mirror", world.player))

    # Masamune
    add_rule(world.get_location(world.location_id_to_name[99 | TreasureOffset]),
             lambda state: state.has_all(["Celestial Mirror", "Rusty Sword"], world.player))

    # Celestial Mirror
    add_rule(world.get_location(world.location_id_to_name[111 | TreasureOffset]),
             lambda state: state.has("Cloudy Mirror", world.player))

    # Mercury Sigil
    add_rule(world.get_location(world.location_id_to_name[279 | TreasureOffset]),
             lambda state: state.can_reach_region("Airship 1st visit: Post-Evrae", world.player))

    celestial_upgrades = [
        (38, 0x25, "Sun"),
        (40, 0x24, "Moon"),
        (42, 0x1e, "Mars"),
        (44, 0x38, "Saturn"),
        (46, 0x1a, "Jupiter"),
        (48, 0x03, "Venus"),
        (50, 0x3d, "Mercury"),
    ]
    for crest_id, weapon_id, celestial in celestial_upgrades:
        add_rule(world.get_location(world.location_id_to_name[crest_id | OtherOffset]),
                 lambda state, weapon_id=weapon_id, celestial=celestial: state.has_all(["Celestial Mirror",
                                              world.item_id_to_name[weapon_id | equipItemOffset],
                                              f"{celestial} Crest",
                                              ], world.player))
        add_rule(world.get_location(world.location_id_to_name[crest_id+1 | OtherOffset]),
                 lambda state, weapon_id=weapon_id, celestial=celestial: state.has_all(["Celestial Mirror",
                                              world.item_id_to_name[weapon_id | equipItemOffset],
                                              f"{celestial} Crest",
                                              f"{celestial} Sigil",
                                              ], world.player))


    ## Primers
    # Complete Al Bhed Primers
    al_bhed_primers = [item.itemName for item in key_items[0x4:0x1D+1]]
    add_rule(world.get_location(world.location_id_to_name[405 | TreasureOffset]),
             lambda state: state.has_all(al_bhed_primers, world.player))

    # TODO: Disabled for now due to multiple bugs related to this location (Ship softlocks + possible Macalania softlock)
    # Clasko S.S. Liki second visit (Talk to Clasko before Crawler and make sure to have him become a Chocobo Breeder)
    #add_rule(world.get_location(world.location_id_to_name[336 | TreasureOffset]),
    #         lambda state: state.can_reach_region("Lake Macalania 1st visit: Pre-Crawler", world.player))