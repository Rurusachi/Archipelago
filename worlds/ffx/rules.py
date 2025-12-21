import typing
from collections import Counter
from typing import Callable

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, CollectionRule
from . import key_items
from .items import character_names, stat_abilities, item_to_stat_value, aeon_names, region_unlock_items, equipItemOffset
from .locations import TreasureOffset, OtherOffset, BossOffset, PartyMemberOffset

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
    add_rule(world.get_location(world.location_id_to_name[13 | PartyMemberOffset]), lambda state: (
        state.can_reach_location(world.location_id_to_name[ 15 | TreasureOffset], world.player),  # Besaid
        state.can_reach_location(world.location_id_to_name[ 19 | TreasureOffset], world.player),  # Kilika
        state.can_reach_location(world.location_id_to_name[484 | TreasureOffset], world.player),  # Djose
        state.can_reach_location(world.location_id_to_name[485 | TreasureOffset], world.player),  # Macalania
        state.can_reach_location(world.location_id_to_name[217 | TreasureOffset], world.player),  # Bevelle
        state.can_reach_location(world.location_id_to_name[209 | TreasureOffset], world.player),  # Zanarkand
    ))
    # Magus Sisters
    add_rule(world.get_location(world.location_id_to_name[15 | PartyMemberOffset]), lambda state: state.has_all(["Flower Scepter", "Blossom Crown"], world.player))





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


    # TODO: Implement Other locations
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


    # Complete Al Bhed Primers
    al_bhed_primers = [item.itemName for item in key_items[0x4:0x1D+1]]
    add_rule(world.get_location(world.location_id_to_name[405 | TreasureOffset]),
             lambda state: state.has_all(al_bhed_primers, world.player))
