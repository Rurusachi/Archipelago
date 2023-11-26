import os
import pkgutil
import random


import bsdiff4
from settings import get_settings

from BaseClasses import MultiWorld
from worlds.Files import APDeltaPatch

from .data import (FFTAData, randomized_jobs, randomized_weapons, randomized_equip, UnitOffsets, MissionOffsets, JobOffsets,
                   location_ids, randomized_abilities, JobID, randomized_judge, judge_equip, judge_weapon, basic_weapon, basic_equip)
from .items import (MissionUnlockItems)
from .fftaabilities import master_abilities, get_job_abilities
from .locations import MissionGroups


class FFTADeltaPatch(APDeltaPatch):
    game = "Final Fantasy Tactics Advance"
    hash = "cd99cdde3d45554c1b36fbeb8863b7bd"
    patch_file_ending = ".apffta"
    result_file_ending = ".gba"

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_as_bytes()


def get_base_rom_as_bytes() -> bytes:
    with open(get_settings().ffta_settings.rom_file, "rb") as infile:
        base_rom_bytes = bytes(infile.read())

    return base_rom_bytes


def _set_bytes_little_endian(byte_array, address, size, value) -> None:
    offset = 0
    while size > 0:
        byte_array[address + offset] = value & 0xFF
        value = value >> 8
        offset += 1
        size -= 1


def unlock_mission(rom: bytearray, data, index: int):
    _set_bytes_little_endian(rom, data.missions[index].memory + MissionOffsets.unlockflag1, 3, 0x00)
    _set_bytes_little_endian(rom, data.missions[index].memory + MissionOffsets.unlockflag2, 3, 0x00)
    _set_bytes_little_endian(rom, data.missions[index].memory + MissionOffsets.unlockflag3, 3, 0x00)


def randomize_unit(rom: bytearray, data, index: int):
    #These were all 2 before, changing to 1 to see
    _set_bytes_little_endian(rom, data.formations[index].memory + UnitOffsets.job, 2, randomized_jobs[index])
    _set_bytes_little_endian(rom, data.formations[index].memory + UnitOffsets.unit_item1, 2, randomized_weapons[index])
    _set_bytes_little_endian(rom, data.formations[index].memory + UnitOffsets.unit_item2, 2, randomized_equip[index])
    _set_bytes_little_endian(rom, data.formations[index].memory + UnitOffsets.unit_item3, 2, 0x00)


def randomize_judge(rom: bytearray, data, index: int, random_index: int):
    # Randomizing the judge encounters
    _set_bytes_little_endian(rom, data.formations[index].memory + UnitOffsets.job, 2, randomized_judge[random_index])
    _set_bytes_little_endian(rom, data.formations[index].memory + UnitOffsets.unit_item1, 2, judge_weapon[random_index])
    _set_bytes_little_endian(rom, data.formations[index].memory + UnitOffsets.unit_item2, 2, judge_equip[random_index])
    _set_bytes_little_endian(rom, data.formations[index].memory + UnitOffsets.unit_item3, 2, 0x00)


def generate_output(multiworld: MultiWorld, player: int, output_directory: str) -> None:
    base_rom = get_base_rom_as_bytes()
    base_patch = pkgutil.get_data(__name__, "data/base_patch.bsdiff4")
    patched_rom = bytearray(bsdiff4.patch(base_rom, base_patch))

    data = FFTAData(patched_rom)

    # Fix Present day
    _set_bytes_little_endian(patched_rom, 0x563b79, 1, 0x4b)

    # Skip cutscenes, maybe move this into the diff file later
    _set_bytes_little_endian(patched_rom, 0x9a87d9, 2, 0x0517)
    _set_bytes_little_endian(patched_rom, 0x9a8c4c, 8, 0x0517041d0102021a)
    _set_bytes_little_endian(patched_rom, 0x9a9784, 2, 0x0517)

    _set_bytes_little_endian(patched_rom, 0x9a9a7c, 2, 0x0517)
    _set_bytes_little_endian(patched_rom, 0x9a9f48, 8, 0x0517061d0102041a)

    _set_bytes_little_endian(patched_rom, 0x9aa198, 2, 0x0517)
    _set_bytes_little_endian(patched_rom, 0x9aa88a, 8, 0x0517071d0102051a)

    _set_bytes_little_endian(patched_rom, 0x9ab0b9, 8, 0x0517081d0102061a)

    _set_bytes_little_endian(patched_rom, 0x9ab656, 2, 0x0517)
    _set_bytes_little_endian(patched_rom, 0x9abce5, 8, 0x0517091d0102071a)

    _set_bytes_little_endian(patched_rom, 0x9ac2bc, 8, 0x05170a1d0102081a)

    _set_bytes_little_endian(patched_rom, 0x9ac7ef, 8, 0x05170b1d0102091a)

    _set_bytes_little_endian(patched_rom, 0x9ace68, 8, 0x05170c1d01020a1a)

    _set_bytes_little_endian(patched_rom, 0x9ad3dc, 8, 0x05170d1d01020b1a)

    _set_bytes_little_endian(patched_rom, 0x9ad89b, 8, 0x05170e1d01020c1a)

    _set_bytes_little_endian(patched_rom, 0x9adbc3, 2, 0x0517)
    _set_bytes_little_endian(patched_rom, 0x9ae0e6, 2, 0x0517)

    _set_bytes_little_endian(patched_rom, 0x9af115, 8, 0x0517121d01020f1a)

    _set_bytes_little_endian(patched_rom, 0x9af74c, 2, 0x0517)
    _set_bytes_little_endian(patched_rom, 0x9afe8d, 12, 0x021700381c0d131d0102101a)
    _set_bytes_little_endian(patched_rom, 0x9b07e4, 4, 0x0517031e)
    _set_bytes_little_endian(patched_rom, 0x9b0b76, 8, 0x0517141d0102111a)

    _set_bytes_little_endian(patched_rom, 0x9b12b4, 8, 0x0517151d0102121a)

    _set_bytes_little_endian(patched_rom, 0x9b19c8, 8, 0x0517161d0102131a)

    _set_bytes_little_endian(patched_rom, 0x9b2694, 2, 0x0517)

    _set_bytes_little_endian(patched_rom, 0x9b2915, 8, 0x0517181d0102151a)
    _set_bytes_little_endian(patched_rom, 0x9b2915, 8, 0x0517191d0102161a)

    _set_bytes_little_endian(patched_rom, 0x9b45c0, 2, 0x0517)

    _set_bytes_little_endian(patched_rom, 0x9b4750, 8, 0x05171b1d0102181a)
    _set_bytes_little_endian(patched_rom, 0x9b4848, 2, 0x0517)
    _set_bytes_little_endian(patched_rom, 0x9b4e2f, 8, 0x05171c1d0102191a)

    _set_bytes_little_endian(patched_rom, 0x9b52de, 2, 0x0517)
    _set_bytes_little_endian(patched_rom, 0x9b5835, 8, 0x05171d1d01021a1a)

    _set_bytes_little_endian(patched_rom, 0x9b5835, 8, 0x05171e1d01021b1a)



    # Enable random clan battles
    _set_bytes_little_endian(patched_rom, 0xcf802, 2, 0x0428)
    _set_bytes_little_endian(patched_rom, 0xcf807, 1, 0x0F)

    # Set max level to 99
    _set_bytes_little_endian(patched_rom, 0x0c9bae, 1, 0x63)
    _set_bytes_little_endian(patched_rom, 0x0c9baa, 1, 0x63)
    _set_bytes_little_endian(patched_rom, 0x12e672, 1, 0x62)

    # Scale to the highest unit
    if multiworld.scaling[player].value == 1:
        _set_bytes_little_endian(patched_rom, 0xca088, 4, 0x42a07950)
        _set_bytes_little_endian(patched_rom, 0xca08d, 7, 0x000000001c04dd)
        _set_bytes_little_endian(patched_rom, 0xca0aa, 2, 0x1c20)

    # Set quick options to on
    #_set_bytes_little_endian(patched_rom, 0x51ba4e, 2, 0x03c8)

    # Double EXP option
    if multiworld.double_exp[player].value == 1:
        _set_bytes_little_endian(patched_rom, 0x12e658, 2, 0x08e5)

    # Make all missions game over instead of fail
    #_set_bytes_little_endian(patched_rom, 0x122258, 2, 0x2001)

    # This works for removing all missions, maybe do this in the diff file
    for mission in data.missions:
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.unlockflag1, 1, 0x02)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.unlockflag1 + 1, 1, 0x03)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.unlockflag1 + 2, 1, 0x01)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.unlockflag2, 1, 0x02)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.unlockflag2 + 1, 1, 0x03)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.unlockflag2 + 2, 1, 0x00)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.unlockflag3, 1, 0x00)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.unlockflag3 + 1, 1, 0x00)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.unlockflag3 + 2, 1, 0x00)

        #_set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.type, 2, 0x00)
        if patched_rom[mission.memory + MissionOffsets.type] == 0x0D:
            _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.type, 1, 0x0A)

        # Dispatch missions
        elif patched_rom[mission.memory + MissionOffsets.type] == 0x00:
            _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.type, 1, 0x00)
        #    _set_bytes_little_endian(patched_rom, mission.memory + 0x10, 1, 0x03)

        elif patched_rom[mission.memory + MissionOffsets.type] == 0x02:
            _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.type, 1, 0x02)

        else:
            # was 0x0A before
            _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.type, 1, 0x0A)

        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.rank, 2, 0x30)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.ap_reward, 1, 0x05)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.gil_reward, 1, 0x05)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.rewardItem1, 2, 0x0000)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.rewardItem2, 2, 0x0000)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.cardItem1, 2, 0x00)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.cardItem2, 2, 0x00)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.clan_reward, 2, 0x0A)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.clan_reward + 0x07, 1, 0x0A)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.required_item1, 1, 0x00)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.required_item2, 1, 0x00)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.price, 2, 0x00)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.pub_visibility, 1, 0x00)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.days_available, 1, 0x00)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.timeout_days, 1, 0x00)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.required_job, 2, 0x00)
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.required_skill, 2, 0x00)

        # Hiding mission rewards with ??? bags, also making missions not cancelable
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.mission_display, 1, 0xC0)

        # Hide ??? cards
        _set_bytes_little_endian(patched_rom, mission.memory + MissionOffsets.mission_display + 1, 1, 0x00)

# Job unlock options
    # Unlock all jobs
    if multiworld.job_unlock_req[player].value == 1:
        for jobs in data.jobs:
            _set_bytes_little_endian(patched_rom, jobs.memory + JobOffsets.job_requirement, 1, 0x00)

    # Lock all jobs
    elif multiworld.job_unlock_req[player].value == 2 or multiworld.job_unlock_req[player].value == 3:
        for jobs in data.jobs:
            _set_bytes_little_endian(patched_rom, jobs.memory + JobOffsets.job_requirement, 1, 0xFF)

    # Unlock starting job based on if the requirements are vanilla and units are randomized
    if multiworld.job_unlock_req[player].value == 0 and multiworld.starting_units[player].value == 1 or \
       multiworld.job_unlock_req[player].value == 0 and multiworld.starting_units[player].value == 2 or \
       multiworld.job_unlock_req[player].value == 0 and multiworld.starting_units[player].value == 3:
        _set_bytes_little_endian(patched_rom, data.jobs[randomized_jobs[0]].memory + JobOffsets.job_requirement, 1,
                                     0x00)
        _set_bytes_little_endian(patched_rom, data.jobs[randomized_jobs[1]].memory + JobOffsets.job_requirement, 1,
                                     0x00)
        _set_bytes_little_endian(patched_rom, data.jobs[randomized_jobs[2]].memory + JobOffsets.job_requirement, 1,
                                     0x00)
        _set_bytes_little_endian(patched_rom, data.jobs[randomized_jobs[3]].memory + JobOffsets.job_requirement, 1,
                                     0x00)
        _set_bytes_little_endian(patched_rom, data.jobs[randomized_jobs[4]].memory + JobOffsets.job_requirement, 1,
                                     0x00)
        _set_bytes_little_endian(patched_rom, data.jobs[randomized_jobs[5]].memory + JobOffsets.job_requirement, 1,
                                     0x00)

    # TO DO: Randomize abilities
    #for ability in data.human_abilities:
    #    _set_bytes_little_endian(patched_rom, ability.memory, 8, patched_rom[data.viera_abilities[5].memory])

    # All abilities cost 0
    #for abilities in data.abilities:
    #    _set_bytes_little_endian(patched_rom, abilities.memory + AbilityOffsets.mp_cost, 1, 0x00)

    gate_number = multiworld.gate_num[player].value
    if gate_number > 30 and multiworld.final_unlock[player].value == 1:
        gate_number = 30

    set_up_gates(patched_rom, data, gate_number, multiworld.gate_items[player].value,
                 multiworld.final_unlock[player].value, multiworld.final_mission[player].value)


# Totema goal
    if multiworld.final_unlock[player].value == 1:
        unlock_mission(patched_rom, data, 4)

        # Totema goal required items
        set_required_items(patched_rom, data, 4, 0x1d1, 0x00)
        set_required_items(patched_rom, data, 7, 0x1d0, 0x00)
        set_required_items(patched_rom, data, 10, 0x1d2, 0x00)
        set_required_items(patched_rom, data, 14, 0x1d3, 0x00)
        set_required_items(patched_rom, data, 17, 0x1c9, 0x00)

        set_mission_requirement(patched_rom, data, 7, 4)
        set_mission_requirement(patched_rom, data, 10, 7)
        set_mission_requirement(patched_rom, data, 14, 10)
        set_mission_requirement(patched_rom, data, 17, 14)

        # Set Royal Valley to be the final mission if it is chosen in the options
        if multiworld.final_mission[player].value == 0:
            set_mission_requirement(patched_rom, data, 23, 17)

        # Set Decision Time to be the final mission
        elif multiworld.final_mission[player].value == 1:
            set_mission_requirement(patched_rom, data, 393, 17)

    # Randomize starting units and set mastered abilities
    for index in range(6):
        if multiworld.starting_units[player].value == 1 or \
           multiworld.starting_units[player].value == 2 or \
           multiworld.starting_units[player].value == 3:

            randomize_unit(patched_rom, data, index)

            # Master all abilities if the unit is a monster type
            if randomized_jobs[index] >= 0x2C:
                master_abilities(patched_rom, data, index, get_job_abilities(randomized_jobs[index]),
                                 10)
            else:
                master_abilities(patched_rom, data, index, get_job_abilities(randomized_jobs[index]),
                                 multiworld.starting_abilities[player].value)

            # Set the basic weapons and equipment if the option is selected
            if multiworld.starting_unit_equip[player].value == 0:
                _set_bytes_little_endian(patched_rom, data.formations[index].memory + UnitOffsets.unit_item1, 2,
                                         basic_weapon[index])
                _set_bytes_little_endian(patched_rom, data.formations[index].memory + UnitOffsets.unit_item2, 2,
                                         basic_equip[index])
                _set_bytes_little_endian(patched_rom, data.formations[index].memory + UnitOffsets.unit_item3, 2, 0x00)

    # Master abilities if units aren't randomized
    if multiworld.starting_units[player].value == 0:
        master_abilities(patched_rom, data, 0, get_job_abilities(JobID.soldier),
                         multiworld.starting_abilities[player].value)
        master_abilities(patched_rom, data, 1, get_job_abilities(JobID.blackmagemog),
                         multiworld.starting_abilities[player].value)
        master_abilities(patched_rom, data, 2, get_job_abilities(JobID.soldier),
                         multiworld.starting_abilities[player].value)
        master_abilities(patched_rom, data, 3, get_job_abilities(JobID.whitemonk),
                         multiworld.starting_abilities[player].value)
        master_abilities(patched_rom, data, 4, get_job_abilities(JobID.whitemagemou),
                         multiworld.starting_abilities[player].value)
        master_abilities(patched_rom, data, 5, get_job_abilities(JobID.archervra),
                         multiworld.starting_abilities[player].value)

    # Scale levels
    for index in range(6, 0xA46):
        # changes from 2 to 1 for bytes just to see something if the placement
        _set_bytes_little_endian(patched_rom, data.formations[index].memory + UnitOffsets.level, 2, 0)
        # Randomize enemies
        if multiworld.randomize_enemies[player].value == 1:
            if patched_rom[data.formations[index].memory] == 0x01:

                randomize_unit(patched_rom, data, index)
                master_abilities(patched_rom, data, index, get_job_abilities(randomized_jobs[index]), random.randint(1, 10))

                # Disable reaction and support abilities for now
                _set_bytes_little_endian(patched_rom, data.formations[index].memory + UnitOffsets.ability_reaction, 1,
                                         0x00)
                _set_bytes_little_endian(patched_rom, data.formations[index].memory + UnitOffsets.ability_support, 1,
                                         0x00)



    # TEMPORARY: Randomize judge units since laws aren't accounted for
    randomize_judge(patched_rom, data, 0xa10, 0)
    randomize_judge(patched_rom, data, 0xa21, 1)
    randomize_judge(patched_rom, data, 0xa30, 2)
    randomize_judge(patched_rom, data, 0xa31, 3)
    randomize_judge(patched_rom, data, 0xa32, 4)

    # Have the judges master all the abilities
    master_abilities(patched_rom, data, 0xa10, get_job_abilities(randomized_judge[0]), 10)
    master_abilities(patched_rom, data, 0xa21, get_job_abilities(randomized_judge[1]), 10)
    master_abilities(patched_rom, data, 0xa30, get_job_abilities(randomized_judge[2]), 10)
    master_abilities(patched_rom, data, 0xa31, get_job_abilities(randomized_judge[3]), 10)
    master_abilities(patched_rom, data, 0xa32, get_job_abilities(randomized_judge[4]), 10)


    # Remove Llednar's weapon on present day to make it more survivable
    _set_bytes_little_endian(patched_rom, 0x52eaf8, 2, 0x00)

    # Randomize locations on map
    for i in range(0, len(location_ids)):
        _set_bytes_little_endian(patched_rom, 0xb390dc + i, 1, location_ids[i])

    set_items(patched_rom, multiworld, player)

    outfile_player_name = f"_P{player}"
    outfile_player_name += f"_{multiworld.get_file_safe_player_name(player).replace(' ', '_')}" \
        if multiworld.player_name[player] != f"Player{player}" else ""

    output_path = os.path.join(output_directory, f"AP_{multiworld.seed_name}{outfile_player_name}.gba")
    with open(output_path, "wb") as outfile:
        outfile.write(patched_rom)
    patch = FFTADeltaPatch(os.path.splitext(output_path)[0] + ".apffta"
                                                              ,player=player,
                                                               player_name=multiworld.player_name[player], patched_path=output_path)

    patch.write()

    os.unlink(output_path)


def set_up_gates(patched_rom: bytearray, data: FFTAData, num_gates: int, req_items, final_unlock: int, final_mission: int) -> None:

    unlock_mission(patched_rom, data, MissionGroups[0][0].mission_id)
    unlock_mission(patched_rom, data, MissionGroups[1][0].mission_id)
    unlock_mission(patched_rom, data, MissionGroups[2][0].mission_id)
    unlock_mission(patched_rom, data, MissionGroups[3][0].mission_id)

    req_item2 = 0

    if req_items == 1:
        req_item2 = MissionUnlockItems[1].itemID

    set_required_items(patched_rom, data, MissionGroups[3][0].mission_id, MissionUnlockItems[0].itemID,
                       req_item2)
    mission_index = 4
    mission_unlock = 3
    item_index = 2

    if num_gates == 1 and final_unlock == 0:

        # Unlock Royal Valley for one gate setting
        if final_mission == 0:
            set_mission_requirement(patched_rom, data, 23, MissionGroups[3][0].mission_id)

        # Unlock Decision Time for one gate setting
        elif final_mission == 1:
            set_mission_requirement(patched_rom, data, 393, MissionGroups[3][0].mission_id)

        return

    for i in range(2, num_gates + 1):

        for j in range(4):

            set_mission_requirement(patched_rom, data, MissionGroups[mission_index][0].mission_id,
                                    MissionGroups[mission_unlock][0].mission_id)
            mission_index = mission_index + 1

        mission_unlock = mission_unlock + 4

        if req_items == 1:
            req_item2 = MissionUnlockItems[item_index + 1].itemID

        set_required_items(patched_rom, data, MissionGroups[mission_unlock][0].mission_id, MissionUnlockItems[item_index].itemID,
                           req_item2)

        item_index = item_index + 2

    # Set final mission to unlock after all the gates if all mission gates option is selected
    if final_unlock == 0:

        # Unlock Royal Valley if it is selected to be the final mission
        if final_mission == 0:
            set_mission_requirement(patched_rom, data, 23, MissionGroups[mission_unlock][0].mission_id)

        # Unlock Decision Time as the final mission
        elif final_mission == 1:
            set_mission_requirement(patched_rom, data, 393, MissionGroups[mission_unlock][0].mission_id)


def set_mission_requirement(patched_rom: bytearray, data: FFTAData, current_mission_ID: int, previous_mission_ID: int) -> None:

    # Set the mission requirements to the specified mission ID
    _set_bytes_little_endian(patched_rom, data.missions[current_mission_ID].memory + MissionOffsets.unlockflag1, 1, previous_mission_ID + 2)
    _set_bytes_little_endian(patched_rom, data.missions[current_mission_ID].memory + MissionOffsets.unlockflag1 + 0x01, 1, 0x03)
    _set_bytes_little_endian(patched_rom, data.missions[current_mission_ID].memory + MissionOffsets.unlockflag1 + 0x02, 1, 0x01)
    _set_bytes_little_endian(patched_rom, data.missions[current_mission_ID].memory + MissionOffsets.unlockflag2, 1, 0x00)
    _set_bytes_little_endian(patched_rom, data.missions[current_mission_ID].memory + MissionOffsets.unlockflag2 + 1, 1, 0x00)
    _set_bytes_little_endian(patched_rom, data.missions[current_mission_ID].memory + MissionOffsets.unlockflag2 + 2, 1, 0x00)
    _set_bytes_little_endian(patched_rom, data.missions[current_mission_ID].memory + MissionOffsets.unlockflag3, 1, 0x00)
    _set_bytes_little_endian(patched_rom, data.missions[current_mission_ID].memory + MissionOffsets.unlockflag3 + 1, 1, 0x00)
    _set_bytes_little_endian(patched_rom, data.missions[current_mission_ID].memory + MissionOffsets.unlockflag3 + 2, 1, 0x00)


def set_items(patched_rom: bytearray, multiworld, player) -> None:
    offset = 41234532

    for location in multiworld.get_filled_locations(player):

        if location.item.code is not None:
            if location.item.player == player:
                if location.item.code - offset >= 0x521aac:
                    _set_bytes_little_endian(patched_rom, location.address, 2, 0x1bc)

                else:
                    _set_bytes_little_endian(patched_rom, location.address, 2, location.item.code - offset)
            else:
                _set_bytes_little_endian(patched_rom, location.address, 2, 0x185)


def set_required_items(rom: bytearray, data: FFTAData, index: int, itemid1, itemid2):
    _set_bytes_little_endian(rom, data.missions[index].memory + MissionOffsets.required_item1, 2, itemid1 - 0x177)

    if itemid2 != 0:
        _set_bytes_little_endian(rom, data.missions[index].memory + MissionOffsets.required_item2, 2, itemid2 - 0x177)

    else:
        _set_bytes_little_endian(rom, data.missions[index].memory + MissionOffsets.required_item2, 2, itemid2)

# TO DO maybe set up double split gates?