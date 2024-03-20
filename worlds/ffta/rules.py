from worlds.generic.Rules import add_rule, set_rule, forbid_item
from .items import MissionUnlockItems


def set_rules(world) -> None:
    # Lambda that returns a lambda rule
    rule_generator = lambda item: (lambda state: state.has(item, world.player))

    # Set final mission unlock to require all paths based on settings
    if world.options.final_unlock.value == 0:
        final_mission_names = ["Royal Valley", "Decision Time"]
        final_mission = final_mission_names[world.options.final_mission.value]
        if world.options.gate_paths.value > 1:
            for path in range(0, world.options.gate_paths.value):
                add_rule(world.multiworld.get_location(final_mission, world.player),
                         rule_generator(f"Path {path+1} Complete"))

    if world.options.final_unlock.value == 1:
        add_rule(world.multiworld.get_entrance("Totema 1", world.player),
                 lambda state: state.has("Water Sigil", world.player))

        add_rule(world.multiworld.get_entrance("Totema 2", world.player),
                 lambda state: state.has("Fire Sigil", world.player))

        add_rule(world.multiworld.get_entrance("Totema 3", world.player),
                 lambda state: state.has("Wind Sigil", world.player))

        add_rule(world.multiworld.get_entrance("Totema 4", world.player),
                 lambda state: state.has("Earth Sigil", world.player))

        add_rule(world.multiworld.get_entrance("Totema 5", world.player),
                 lambda state: state.has("Old Statue", world.player))

    num_gates = world.options.gate_num.value
    num_gates = num_gates + (world.options.gate_paths.value - 1)

    gate_items = [
        ("Magic Trophy", "Fight Trophy"),
        ("Magic Medal", "Ancient Medal"),
        ("Choco Bread", "Choco Gratin"),
        ("Black Thread", "White Thread"),
        ("Thunderstone", "Stormstone"),
        ("Ahriman Eye", "Ahriman Wing"),
        ("Magic Cloth", "Magic Cotton"),
        ("Adaman Alloy", "Mysidia Alloy"),
        ("Elda's Cup", "Gold Vessel"),
        ("Kiddy Bread", "Grownup Bread"),
        ("Danbukwood", "Moonwood"),
        ("Dragon Bone", "Animal Bone"),
        ("Magic Fruit", "Power Fruit"),
        ("Malboro Wine", "Gedegg Soup"),
        ("Encyclopedia", "Dictionary"),
        ("Rat Tail", "Rabbit Tail"),
        ("Stasis Rope", "Mythril Pick"),
        ("Clock Gear", "Gun Gear"),
        ("Blood Shawl", "Blood Apple"),
        ("Eldagusto", "Cyril Ice"),
        ("Crystal", "Trichord"),
        ("Tranquil Box", "Flower Vase"),
        ("Cat's Tears", "Dame's Blush"),
        ("Justice Badge", "Friend Badge"),
        ("Love Potion", "Tonberry Lamp"),
        ("Runba's Tale", "The Hero Gaol"),
        ("Mind Ceffyl", "Body Ceffyl"),
        ("Ancient Bills", "Ancient Coins"),
        ("Blue Rose", "White Flowers"),
        ("Gysahl Greens", "Chocobo Egg"),
        ("Delta Fang", "Esteroth"),
        ("Moon Bloom", "Telaq Flowers"),
    ]

    for i in range(0, num_gates):
        item1 = gate_items[i][0]
        item2 = gate_items[i][1]
        
        add_rule(world.multiworld.get_entrance(f"Gate {i+2}", world.player),
            rule_generator(item1))

        if world.options.gate_items.value == 1:
            add_rule(world.multiworld.get_entrance(f"Gate {i+2}", world.player),
                rule_generator(item2))

        elif world.options.gate_items.value == 2 and i < num_gates - (world.options.gate_paths.value - 1):
            add_rule(world.multiworld.get_entrance(f"Dispatch Gate {i+2}", world.player),
                    rule_generator(item2))
