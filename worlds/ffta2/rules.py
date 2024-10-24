from typing import List
from worlds.generic.Rules import add_rule, CollectionRule
from .items import GateItems


def rule_generator(world, item: str) -> CollectionRule:
    return lambda state: state.has(item, world.player)


def rule_generator_count(world, items: List[str], count: int) -> CollectionRule:
    return lambda state: state.has_from_list_unique(items, world.player, count)


def rule_generator_progressive(world, item: str, num: int) -> CollectionRule:
    return lambda state: state.has(item, world.player, num)


def set_rules(world) -> None:
    num_paths = world.options.path_num.value
    num_gates = world.options.gate_num.value + num_paths - 1

    if num_paths > 1:
        add_rule(world.multiworld.get_location("The Two Grimoires", world.player),
                 rule_generator_count(world,
                                      [f"Path {path+1} Complete" for path in range(num_paths)],
                                      min(world.options.paths_required.value, num_paths)))

    gate_items = [GateItems[i].itemName for i in range(0, len(GateItems))]

    for path in range(0, num_paths):
        for i in range(path, num_gates, num_paths):
            item = gate_items[i]
            add_rule(world.multiworld.get_entrance(f"Gate {i+2}", world.player),
                     rule_generator(world, item))

    # for i in range(0, num_gates):
    #     item = gate_items[i]

    #     add_rule(world.multiworld.get_entrance(f"Gate {i+2}", world.player),
    #              rule_generator(world, item))