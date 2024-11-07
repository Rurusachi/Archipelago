from enum import IntEnum
from typing import List, Tuple, Dict
from math import ceil

from BaseClasses import Entrance, ItemClassification, Region, Location
from .locations import FFTA2Location, QuestGroups, FFTA2BazaarLocations
from .data import ffta2_data
from .items import Loot, LootMagicite, LootMetals, LootSkins, LootBones, LootFlora, LootTimber, LootPhiltres, items_by_id
from .bazaar import bazaarCategories


class GatePosition(IntEnum):
    FIRST = 3
    MIDDLE = 4
    LAST = 1


def create_gates(world, player, gate: Region, gate_quests: List[int]):
    world.multiworld.regions.append(gate)

    for quest_index in gate_quests:
        for locationData in world.QuestGroups[quest_index][0]:
            location = FFTA2Location(player, locationData.name, locationData.rom_address)
            gate.locations.append(location)
            location.parent_region = gate


def create_regions(world, player) -> None:

    # FFTA2ValidLocations: List[List[FFTA2Location]] = []
    gates: List[Region] = []
    valid_gates: List[Region] = []

    # Setting number of locations per quest
    # world.QuestGroups = []
    # ActualQuestGroups = QuestGroups.copy()
    # for i, questGroup in enumerate(ActualQuestGroups):
    #     ActualQuestGroups[i] = (questGroup[0][:world.options.reward_num.value], questGroup[1], questGroup[2])
    # world.QuestGroups = ActualQuestGroups

    world.QuestGroups = [(questGroup[0][:world.options.reward_num.value], questGroup[1], questGroup[2]) for questGroup in QuestGroups]

    menu_region = Region("Menu", player, world.multiworld)
    world.multiworld.regions.append(menu_region)

    # Bazaar recipes
    # Separate loot into types
    # Group bazaar recipes by bazaar categories
    # Select 3 loot types for each category
    if world.options.bazaar_options.value > 1:
        if world.options.bazaar_options.value == 3:
            bazaar_region = Region("Bazaar", player, world.multiworld)
            menu_region.connect(bazaar_region)

        # Loot_max * loot_pool >= 1065 / 7
        loot_max = ceil(153 / world.options.bazaar_loot_pool.value)+1
        world.loot_amount = loot_max
        loot_pool_categories = {
            "Magicite": {loot_item.itemID: loot_max for loot_item in LootMagicite[:world.options.bazaar_loot_pool.value]},
            "Metals": {loot_item.itemID: loot_max for loot_item in LootMetals[:world.options.bazaar_loot_pool.value]},
            "Skins": {loot_item.itemID: loot_max for loot_item in LootSkins[:world.options.bazaar_loot_pool.value]},
            "Bones": {loot_item.itemID: loot_max for loot_item in LootBones[:world.options.bazaar_loot_pool.value]},
            "Flora": {loot_item.itemID: loot_max for loot_item in LootFlora[:world.options.bazaar_loot_pool.value]},
            "Timber": {loot_item.itemID: loot_max for loot_item in LootTimber[:world.options.bazaar_loot_pool.value]},
            "Philtres": {loot_item.itemID: loot_max for loot_item in LootPhiltres[:world.options.bazaar_loot_pool.value]},
        }
        loot_pool_category_keys = list(loot_pool_categories)
        used_loot = set()
        for category in sorted(bazaarCategories, key=lambda x: len([y for y in x.items if y[0] != 0]), reverse=True):
            valid_pools = [k for k in loot_pool_category_keys if sum(loot_pool_categories[k].values()) >= len([i for i in category.items if i[0] != 0])]
            loot_pools = [loot_pool_categories[k] for k in world.random.sample(valid_pools, 3)]
            loot_pool_keys = [[k for k, v in pool.items() if v > 0] for pool in loot_pools]
            print(category.name)
            for item in category.items:
                if item[0] != 0:
                    recipe = ffta2_data.bazaarRecipes[item[0]-1]
                    location_name = f"{recipe.name} Bazaar Recipe"
                    if world.options.bazaar_options.value == 3:
                        bazaar_region.locations.append(FFTA2Location(player, location_name, 0x0542AD48 + recipe.item * 2, bazaar_region))

                    new_recipe = (location_name, item[0], [])
                    for i, pool in enumerate(loot_pools):
                        item_id = world.random.choice(loot_pool_keys[i])
                        new_recipe[2].append(item_id)
                        pool[item_id] -= 1
                        used_loot.add(item_id)
                        if pool[item_id] < 0:
                            raise ValueError(pool)
                        if pool[item_id] == 0:
                            loot_pool_keys[i].remove(item_id)
                            loot_pool_category_keys = [k for k in loot_pool_category_keys if any(loot_pool_categories[k].values())]

                    print(new_recipe[0], [items_by_id[item_id].itemName for item_id in new_recipe[2]])
                    world.bazaar_recipes.append(new_recipe)
        world.bazaar_loot_used_pool = used_loot

    # Set quest order here
    # world.random.shuffle(world.QuestGroups)

    paths: int = world.options.path_num.value
    gate_number: int = world.options.gate_num.value + paths - 1
    gate_balancing: int = world.options.gate_balancing.value

    def calculate_weight(gate, rank):
        '''
            gate and rank should be in range [-1, 1].
            returns value in range [1, 2]. Value is highest when gate and rank are equal.
        '''
        return (gate**2*rank**2 - gate**2 - rank**2 + gate*rank + 1)/2 + 1.5

    chosen_indices = []
    quest_indices = range(len(world.QuestGroups))
    for gate in range(gate_number):
        quest_weights = [calculate_weight(gate / gate_number * 2 - 1, (ffta2_data.quests[x[0][0].quest_id].rank-1) / 98 * 2 - 1)**gate_balancing if i not in chosen_indices else 0 for i, x in enumerate(world.QuestGroups)]
        remaining = 4
        while remaining > 0:
            chosen = world.random.choices(quest_indices, weights=quest_weights, k=remaining)
            for x in chosen:
                if quest_weights[x] != 0:
                    # print(quest_weights[x])
                    chosen_indices.append(x)
                    quest_weights[x] = 0
                    remaining -= 1

    chosen_quests = [world.QuestGroups[i] for i in chosen_indices]
    # print([(ffta2_data.quests[x[0][0].quest_id].rank, x[0][0].name) for x in chosen_quests])
    # print(len(chosen_quests))
    world.QuestGroups = chosen_quests

    # Create region gates
    gates.extend([Region(f"Gate {i+1}", player, world.multiworld) for i in range(30)])

    final_quest = Region("Final Quest Gate", player, world.multiworld)

    final_location = FFTA2Location(player, "The Two Grimoires", None)

    final_quest.locations.append(final_location)
    final_location.parent_region = final_quest
    world.multiworld.regions.append(final_quest)

    path_completion_gates = []
    if paths > 1:
        for i in range(paths):
            path_completion = Region(f"Path {i+1} Completion", player, world.multiworld)
            path_completion_location = FFTA2Location(player, f"Path {i+1} Completion", None)

            path_completion.locations.append(path_completion_location)
            path_completion_location.parent_region = path_completion
            world.multiworld.regions.append(path_completion)
            path_completion.connect(final_quest)

            path_completion_gates.append(path_completion)


    if gate_number > 30 and world.options.goal.value == 1:
        gate_number = 30

    # Add number of gates based on settings
    for i in range(gate_number + 1):
        valid_gates.append(gates[i])

    # Create first gate
    menu_region.connect(valid_gates[0])
    create_gates(world, player, valid_gates[0], [j for j in range(0, GatePosition.FIRST)])

    # location_index: int = GatePosition.FIRST
    # previous_gate: Region = valid_gates[0]
    # for i, gate in enumerate(valid_gates[1:]):
    #     world.multiworld.regions.append(gate)

    #     num_quests: GatePosition = GatePosition.MIDDLE if i < len(valid_gates)-1 else GatePosition.LAST
    #     previous_gate.connect(gate, gate.name)

    #     create_gates(world, FFTA2ValidLocations, gate, num_quests, location_index)
    #     location_index += num_quests
    #     previous_gate = gate

    # valid_gates[gate_number].connect(final_quest)

    path_quests: List[List[Tuple[int, List[int]]]] = []

    path_end_quests: List[Tuple[int, int]] = []

    for path in range(paths):
        path_quests.append([])
        # previous_quest_index: int = GatePosition.FIRST
        quest_index: int = GatePosition.FIRST + path * GatePosition.MIDDLE
        previous_gate: Region = valid_gates[0]
        path_gates = valid_gates[path+1::paths]
        last_quest = len(path_gates)-1
        for i, gate in enumerate(path_gates):
            num_quests: GatePosition = GatePosition.LAST if i == last_quest else GatePosition.MIDDLE
            previous_gate.connect(gate, gate.name)

            gate_quests = [j for j in range(quest_index, quest_index + num_quests)]
            create_gates(world, player, gate, gate_quests)

            path_quests[path].append((gate_quests[0], gate_quests[1:]))
            if i > 0:
                path_quests[path][i-1][1].append(gate_quests[0])
            # previous_quest_index = gate_quests[-1]
            quest_index += num_quests * paths
            previous_gate = gate
        if paths > 1:
            path_gates[last_quest].connect(path_completion_gates[path])
            path_end_quests.append(world.QuestGroups[gate_quests[-1]][0][0].name)

    if paths == 1:
        path_gates[last_quest].connect(final_quest)

    world.path_quests = path_quests
    world.path_end_quests = path_end_quests
