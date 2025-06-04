from collections import Counter
from typing import Callable

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, CollectionRule
from .items import character_names, stat_abilities, item_to_stat_value
from ..AutoWorld import World


def create_ability_rule(world: World, ability_name: str):
    #return lambda state: state.has_any([f"{name} Ability: {ability_name}" for name in character_names], world.player)
    #return lambda state: True;               "       Ability: Fire"
    #temp = [(f"{name} Ability: {ability_name}", f"Party Member: {name}") for name in character_names]
    #for ability, character in temp:
    #    print(world.item_name_to_id[ability])
    #    print(world.item_name_to_id[character])
    #print(temp)
    return lambda state: any([state.has_all([f"{name} Ability: {ability_name}", f"Party Member: {name}"], world.player) for name in character_names])


#def create_stat_rule(world: World, stat_total: int):
#    return lambda state: state.has
def create_stat_total_rule(world: World, num_party_members: int, stat_total: int) -> CollectionRule:
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

ruleDict: dict[str, Callable[[World], CollectionRule]] = {
    "Sinspawn Geneaux": lambda world: lambda state: create_ability_rule(world, "Esuna")(state)
                                                    and
                                                    create_ability_rule(world, "Fire")(state)
                                                    and
                                                    (
                                                            create_ability_rule(world, "Silence")(state)
                                                            or
                                                            create_ability_rule(world, "Nul Tide")(state)
                                                    )
                                                    and create_stat_total_rule(world, 3, 50),
    "Oblitzerator": lambda world: lambda state: create_ability_rule(world, "Thunder")(state) or
                                                create_ability_rule(world, "Thundara")(state) or
                                                create_ability_rule(world, "Thundaga")(state),
    "Chocobo Eater": lambda world: lambda state: True,
    "Sinspawn Gui": lambda world: lambda state: True,
    "Extractor": lambda world: lambda state: True,
    "Spherimorph": lambda world: lambda state: True,
    "Crawler": lambda world: lambda state: True,
    "Seymour/Anima": lambda world: lambda state: True,
    "Wendigo": lambda world: lambda state: True,
    "Evrae": lambda world: lambda state: True,
    "Airship Sin": lambda world: lambda state: True,
    "Overdrive Sin": lambda world: lambda state: True,
    "Penance": lambda world: lambda state: True,
    "Isaaru": lambda world: lambda state: True,
    "Evrae Altana": lambda world: lambda state: True,
    "Seymour Natus": lambda world: lambda state: True,
    "Defender X": lambda world: lambda state: True,
    "Biran and Yenke": lambda world: lambda state: True,
    "Seymour Flux": lambda world: lambda state: True,
    "Sanctuary Keeper": lambda world: lambda state: True,
    "Spectral Keeper": lambda world: lambda state: True,
    "Yunalesca": lambda world: lambda state: True,
    "Seymour Omnis": lambda world: lambda state: True,
    "Braska's Final Aeon": lambda world: lambda state: True,
    "Ultima Weapon": lambda world: lambda state: True,
    "Omega Weapon": lambda world: lambda state: True,
}


def set_rules(world: World, player) -> None:
    pass
    #add_rule(world.multiworld.get_region("Kilika 1st visit: Post-Geneaux", player).entrances[0], ruleDict["Sinspawn Geneaux"](world))
