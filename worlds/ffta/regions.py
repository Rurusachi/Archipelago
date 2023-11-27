from BaseClasses import Entrance, ItemClassification, Region, Location

from .data import FFTAData
from .items import FFTAItem
from .locations import FFTALocations, FFTALocation, MissionGroups, FFTALocationData

#FFTAValidLocations = []
#FFTALocationGroup = []
#gates = []
#valid_gates = []


def create_gates(num_gate: int, gate: Region, world, last_gate: bool, FFTAValidLocations):

    if last_gate:
        world.multiworld.regions.append(gate)
        location_index = (num_gate - 1) * 8 + 6
        gate.locations.append(FFTAValidLocations[location_index])
        FFTAValidLocations[location_index].parent_region = gate
        gate.locations.append(FFTAValidLocations[location_index + 1])
        FFTAValidLocations[location_index + 1].parent_region = gate

        return

    num_missions: int

    if num_gate == 0:
        num_missions = 6
        location_index = 0

    elif num_gate == 1:
        num_missions = 8
        location_index = num_gate * 6

    else:
        location_index = (num_gate - 1) * 8 + 6
        num_missions = 8

    world.multiworld.regions.append(gate)

    for i in range(num_missions):
        index = location_index + i
        #print("\nindex of the location being created: " + (str)(index))
        #print("\nthis is what i is now being added to location index: " + (str)(i))
        gate.locations.append(FFTAValidLocations[index])
        FFTAValidLocations[index].parent_region = gate


def create_regions(world, player) -> None:
    FFTAValidLocations = []
    gates = []
    valid_gates = []
    TotemaLocations = []
    StoryLocations = []
    menu_region = Region("Menu", player, world.multiworld)
    world.multiworld.regions.append(menu_region)

    #for location in FFTALocations:
    #    location = FFTALocation(player, location.name, location.rom_address)
    #   FFTAValidLocations.append(location)

    # Adding totema missions to list and deleting them from mission groups
    if world.options.final_unlock == 1:
        TotemaLocations.append(FFTALocation(player, MissionGroups[4][0].name, MissionGroups[4][0].rom_address))
        TotemaLocations.append(FFTALocation(player, MissionGroups[4][1].name, MissionGroups[4][1].rom_address))

        del MissionGroups[4]

        TotemaLocations.append(FFTALocation(player, MissionGroups[6][0].name, MissionGroups[6][0].rom_address))
        TotemaLocations.append(FFTALocation(player, MissionGroups[6][1].name, MissionGroups[6][1].rom_address))

        del MissionGroups[6]

        TotemaLocations.append(FFTALocation(player, MissionGroups[8][0].name, MissionGroups[8][0].rom_address))
        TotemaLocations.append(FFTALocation(player, MissionGroups[8][1].name, MissionGroups[8][1].rom_address))

        del MissionGroups[8]

        TotemaLocations.append(FFTALocation(player, MissionGroups[11][0].name, MissionGroups[11][0].rom_address))
        TotemaLocations.append(FFTALocation(player, MissionGroups[11][1].name, MissionGroups[11][1].rom_address))

        del MissionGroups[11]

        TotemaLocations.append(FFTALocation(player, MissionGroups[13][0].name, MissionGroups[13][0].rom_address))
        TotemaLocations.append(FFTALocation(player, MissionGroups[13][1].name, MissionGroups[13][1].rom_address))

        del MissionGroups[13]

    # Having the story missions be the gate unlocks and removing them from the mission pool.
    if world.options.mission_order == 1:

        end_range = 23

        # Account for the removed totema missions if that option is selected
        if world.options.final_unlock == 1:
            end_range = 17

        for index in range(0, end_range):
            StoryLocations.append(MissionGroups[0])
            del MissionGroups[0]

    if world.options.mission_order == 1 or world.options.mission_order == 2:
        world.random.shuffle(MissionGroups)


    # Insert story missions on every fourth mission to be the requirement mission
    if world.options.mission_order == 1:
        story_index = 0
        i = 3
        for gate in range(world.options.gate_num):
            while i < len(MissionGroups) and story_index < len(StoryLocations):
                MissionGroups.insert(i, StoryLocations[story_index])
                i = i + 4
                story_index = story_index + 1

    # Adding missions to valid locations to create the locations
    for index, mission in enumerate(MissionGroups):
        mission_reward_1 = mission[0]
        mission_reward_2 = mission[1]
        reward_location1 = FFTALocation(player, mission_reward_1.name, mission_reward_1.rom_address)
        reward_location2 = FFTALocation(player, mission_reward_2.name, mission_reward_2.rom_address)
        FFTAValidLocations.append(reward_location1)
        FFTAValidLocations.append(reward_location2)

    #for index, mission in enumerate(FFTAValidLocations):
    #    print("This is the locations in valid locations in order: " + mission.name)


    # Create region gates
    gate_1 = Region("Gate 1", player, world.multiworld)
    gate_2 = Region("Gate 2", player, world.multiworld)
    gate_3 = Region("Gate 3", player, world.multiworld)
    gate_4 = Region("Gate 4", player, world.multiworld)
    gate_5 = Region("Gate 5", player, world.multiworld)
    gate_6 = Region("Gate 6", player, world.multiworld)
    gate_7 = Region("Gate 7", player, world.multiworld)
    gate_8 = Region("Gate 8", player, world.multiworld)
    gate_9 = Region("Gate 9", player, world.multiworld)
    gate_10 = Region("Gate 10", player, world.multiworld)
    gate_11 = Region("Gate 11", player, world.multiworld)
    gate_12 = Region("Gate 12", player, world.multiworld)
    gate_13 = Region("Gate 13", player, world.multiworld)
    gate_14 = Region("Gate 14", player, world.multiworld)
    gate_15 = Region("Gate 15", player, world.multiworld)
    gate_16 = Region("Gate 16", player, world.multiworld)
    gate_17 = Region("Gate 17", player, world.multiworld)
    gate_18 = Region("Gate 18", player, world.multiworld)
    gate_19 = Region("Gate 19", player, world.multiworld)
    gate_20 = Region("Gate 20", player, world.multiworld)
    gate_21 = Region("Gate 21", player, world.multiworld)
    gate_22 = Region("Gate 22", player, world.multiworld)
    gate_23 = Region("Gate 23", player, world.multiworld)
    gate_24 = Region("Gate 24", player, world.multiworld)
    gate_25 = Region("Gate 25", player, world.multiworld)
    gate_26 = Region("Gate 26", player, world.multiworld)
    gate_27 = Region("Gate 27", player, world.multiworld)
    gate_28 = Region("Gate 28", player, world.multiworld)
    gate_29 = Region("Gate 29", player, world.multiworld)
    gate_30 = Region("Gate 30", player, world.multiworld)
    gate_31 = Region("Gate 31", player, world.multiworld)
    gate_32 = Region("Gate 32", player, world.multiworld)
    gate_33 = Region("Gate 33", player, world.multiworld)
    final_mission = Region("Final Mission Gate", player, world.multiworld)


    #Add these based on gate settings?
    gates.append(gate_1)
    gates.append(gate_2)
    gates.append(gate_3)
    gates.append(gate_4)
    gates.append(gate_5)
    gates.append(gate_6)
    gates.append(gate_7)
    gates.append(gate_8)
    gates.append(gate_9)
    gates.append(gate_10)
    gates.append(gate_11)
    gates.append(gate_12)
    gates.append(gate_13)
    gates.append(gate_14)
    gates.append(gate_15)
    gates.append(gate_16)
    gates.append(gate_17)
    gates.append(gate_18)
    gates.append(gate_19)
    gates.append(gate_20)
    gates.append(gate_21)
    gates.append(gate_22)
    gates.append(gate_23)
    gates.append(gate_24)
    gates.append(gate_25)
    gates.append(gate_26)
    gates.append(gate_27)
    gates.append(gate_28)
    gates.append(gate_29)
    gates.append(gate_30)
    gates.append(gate_31)
    gates.append(gate_32)
    gates.append(gate_33)

    if world.options.final_mission == 0:
        final_location = FFTALocation(player, 'Royal Valley', None)
    elif world.options.final_mission == 1:
        final_location = FFTALocation(player, 'Decision Time', None)

    final_mission.locations.append(final_location)
    final_location.parent_region = final_mission
    world.multiworld.regions.append(final_mission)

    gate_number = world.options.gate_num

    if gate_number > 30 and world.options.final_unlock == 1:
        gate_number = 30

    for i in range(gate_number + 1):
        valid_gates.append(gates[i])

    last_gate = False
    for x in range(len(valid_gates)):

        if x == len(valid_gates) - 1:
            last_gate = True

        create_gates(x, valid_gates[x], world, last_gate, FFTAValidLocations)

        if x > 0:
            valid_gates[x-1].connect(valid_gates[x], valid_gates[x].name)

    menu_region.connect(gate_1)

    # Set up regions for totema unlock option
    if world.multiworld.final_unlock[player].value == 1:
        totema1 = Region("Totema 1", player, world.multiworld)
        totema2 = Region("Totema 2", player, world.multiworld)
        totema3 = Region("Totema 3", player, world.multiworld)
        totema4 = Region("Totema 4", player, world.multiworld)
        totema5 = Region("Totema 5", player, world.multiworld)

        world.multiworld.regions.append(totema1)
        world.multiworld.regions.append(totema2)
        world.multiworld.regions.append(totema3)
        world.multiworld.regions.append(totema4)
        world.multiworld.regions.append(totema5)

        totema1.locations.append(TotemaLocations[0])
        totema1.locations.append(TotemaLocations[1])
        TotemaLocations[0].parent_region = totema1
        TotemaLocations[1].parent_region = totema1

        totema2.locations.append(TotemaLocations[2])
        totema2.locations.append(TotemaLocations[3])
        TotemaLocations[2].parent_region = totema2
        TotemaLocations[3].parent_region = totema2

        totema3.locations.append(TotemaLocations[4])
        totema3.locations.append(TotemaLocations[5])
        TotemaLocations[4].parent_region = totema3
        TotemaLocations[5].parent_region = totema3

        totema4.locations.append(TotemaLocations[6])
        totema4.locations.append(TotemaLocations[7])
        TotemaLocations[6].parent_region = totema4
        TotemaLocations[7].parent_region = totema4

        totema5.locations.append(TotemaLocations[8])
        totema5.locations.append(TotemaLocations[9])
        TotemaLocations[8].parent_region = totema5
        TotemaLocations[9].parent_region = totema5

        menu_region.connect(totema1, "Totema 1")
        totema1.connect(totema2, "Totema 2")
        totema2.connect(totema3, "Totema 3")
        totema3.connect(totema4, "Totema 4")
        totema4.connect(totema5, "Totema 5")
        totema5.connect(final_mission)

    else:
        # Always connect the last gate to the final mission for the mission gate goal
        valid_gates[gate_number].connect(final_mission)
