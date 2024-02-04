import os
import pkgutil
import random


import bsdiff4

import Utils
from settings import get_settings

from .patcher import (APTokenTypes, APTokenMixin, APPatchExtension, APProcedurePatch)

from .data import (FFTAData, UnitOffsets, MissionOffsets, JobOffsets, JobID)
from .items import (MissionUnlockItems)
from .fftaabilities import master_abilities, get_job_abilities


class FFTAProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Final Fantasy Tactics Advance"
    hash = "cd99cdde3d45554c1b36fbeb8863b7bd"
    patch_file_ending = ".apffta"
    result_file_ending = ".gba"

    procedure = [
        ("apply_bsdiff4", ["base_patch.bsdiff4"]),
        ("apply_tokens", ["token_data.bin"]),
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_as_bytes()

class FFTAPatchExtension(APPatchExtension):
    game = "Final Fantasy Tactics Advance"

def get_base_rom_as_bytes() -> bytes:
    with open(get_settings().ffta_options.rom_file, "rb") as infile:
        base_rom_bytes = bytes(infile.read())

    print("get base APTokenTypes.WRITE is called")

    return base_rom_bytes


def unlock_mission(ffta_data, index: int, patch: FFTAProcedurePatch):
    patch.write_token(APTokenTypes.WRITE, ffta_data.missions[index].memory + MissionOffsets.unlockflag1,
                      bytes([0x00, 0x00, 0x00]))
    patch.write_token(APTokenTypes.WRITE, ffta_data.missions[index].memory + MissionOffsets.unlockflag2,
                      bytes([0x00, 0x00, 0x00]))
    patch.write_token(APTokenTypes.WRITE, ffta_data.missions[index].memory + MissionOffsets.unlockflag3,
                      bytes([0x00, 0x00, 0x00]))


def randomize_unit(ffta_data, index: int, world, patch: FFTAProcedurePatch):
    #These were all 2 before, changing to 1 to see
    patch.write_token(APTokenTypes.WRITE, ffta_data.formations[index].memory + UnitOffsets.job, bytes([world.randomized_jobs[index]]))
    patch.write_token(APTokenTypes.WRITE, ffta_data.formations[index].memory + UnitOffsets.unit_item1, bytes([world.randomized_weapons[index]]))
    patch.write_token(APTokenTypes.WRITE, ffta_data.formations[index].memory + UnitOffsets.unit_item2, bytes([world.randomized_equip[index]]))
    patch.write_token(APTokenTypes.WRITE, ffta_data.formations[index].memory + UnitOffsets.unit_item3, bytes([0x00]))


def randomize_judge(ffta_data, index: int, random_index: int, world, patch: FFTAProcedurePatch):
    # Randomizing the judge encounters
    patch.write_token(APTokenTypes.WRITE, ffta_data.formations[index].memory + UnitOffsets.job, world.randomized_judge[random_index])
    patch.write_token(APTokenTypes.WRITE, ffta_data.formations[index].memory + UnitOffsets.unit_item1, world.judge_weapon[random_index])
    patch.write_token(APTokenTypes.WRITE, ffta_data.formations[index].memory + UnitOffsets.unit_item2, world.judge_equip[random_index])
    patch.write_token(APTokenTypes.WRITE, ffta_data.formations[index].memory + UnitOffsets.unit_item3, 0x00)


def generate_output(world, player: int, output_directory: str) -> None:
    patch = FFTAProcedurePatch()
    patch_extension = FFTAPatchExtension()

    patch.write_file("base_patch.bsdiff4", pkgutil.get_data(__name__, "ffta_data/base_patch.bsdiff4"))

    base_rom = bytes(get_base_rom_as_bytes())

    ffta_data = FFTAData(base_rom)
    
    #if world.options.dispatch.value > 0:
    #    for i in range(125, 330):
    #        patch.write_token(APTokenTypes.WRITE, ffta_data.missions[i].memory + MissionOffsets.dispatch_ability, 1, 0x0)

    # Fix Present day
    patch.write_token(APTokenTypes.WRITE, 0x563b79, bytes([0x4b]))
    
    # Skip cutscenes, maybe move this into the diff file later
    patch.write_token(APTokenTypes.WRITE, 0x9a87d9, bytes([0x05, 0x17]))

    patch.write_file("token_data.bin", patch.get_token_binary())

    

    # Write Output
    outfile_player_name = f"_P{player}"
    outfile_player_name += f"_{world.multiworld.get_file_safe_player_name(player).replace(' ', '_')}" \
        if world.multiworld.player_name[player] != f"Player{player}" else ""

    patched_rom = patch_extension.apply_tokens(patch, base_rom, "token_data.bin")
    fully_patched = patch_extension.apply_bsdiff4(patch, bytes(patched_rom), "base_patch.bsdiff4")
    
    patch.write(
        os.path.join(output_directory,
                     f"AP_{world.multiworld.seed_name}{outfile_player_name}{patch.patch_file_ending}"))
                     
    out_file_name = world.multiworld.get_out_file_name_base(world.player)
    output_path = os.path.join(output_directory, f"{out_file_name}.gba")
    patch.patch(output_path)
                     

                     

""""
    # Skip cutscenes, maybe move this into the diff file later
    patch.write_token(APTokenTypes.WRITE, 0x9a87d9, bytes([0x05, 0x17]))
    patch.write_token(APTokenTypes.WRITE, 0x9a8c4c, 0x0517041d0102021a)
    patch.write_token(APTokenTypes.WRITE, 0x9a9784, 0x0517)

    patch.write_token(APTokenTypes.WRITE, 0x9a9a7c, 0x0517)
    patch.write_token(APTokenTypes.WRITE, 0x9a9f48, 0x0517061d0102041a)

    patch.write_token(APTokenTypes.WRITE, 0x9aa198, 0x0517)
    patch.write_token(APTokenTypes.WRITE, 0x9aa88a, 0x0517071d0102051a)

    patch.write_token(APTokenTypes.WRITE, 0x9ab0b9, 0x0517081d0102061a)

    patch.write_token(APTokenTypes.WRITE, 0x9ab656, 0x0517)
    patch.write_token(APTokenTypes.WRITE, 0x9abce5, 0x0517091d0102071a)

    patch.write_token(APTokenTypes.WRITE, 0x9ac2bc, 0x05170a1d0102081a)

    patch.write_token(APTokenTypes.WRITE, 0x9ac7ef, 0x05170b1d0102091a)

    patch.write_token(APTokenTypes.WRITE, 0x9ace68, 0x05170c1d01020a1a)

    patch.write_token(APTokenTypes.WRITE, 0x9ad3dc, 0x05170d1d01020b1a)

    patch.write_token(APTokenTypes.WRITE, 0x9ad89b, 0x05170e1d01020c1a)

    patch.write_token(APTokenTypes.WRITE, 0x9adbc3, 0x0517)
    patch.write_token(APTokenTypes.WRITE, 0x9ae0e6, 0x0517)

    patch.write_token(APTokenTypes.WRITE, 0x9af115, 0x0517121d01020f1a)

    patch.write_token(APTokenTypes.WRITE, 0x9af74c, 0x0517)
    patch.write_token(APTokenTypes.WRITE, 0x9afe8d, 0x021700381c0d131d0102101a)
    patch.write_token(APTokenTypes.WRITE, 0x9b07e4, 0x0517031e)
    patch.write_token(APTokenTypes.WRITE, 0x9b0b76, 0x0517141d0102111a)

    patch.write_token(APTokenTypes.WRITE, 0x9b12b4, 0x0517151d0102121a)

    patch.write_token(APTokenTypes.WRITE, 0x9b19c8, 0x0517161d0102131a)

    patch.write_token(APTokenTypes.WRITE, 0x9b2694, 0x0517)

    patch.write_token(APTokenTypes.WRITE, 0x9b2915, 0x0517181d0102151a)
    patch.write_token(APTokenTypes.WRITE, 0x9b2915, 0x0517191d0102161a)

    patch.write_token(APTokenTypes.WRITE, 0x9b45c0, 0x0517)

    patch.write_token(APTokenTypes.WRITE, 0x9b4750, 0x05171b1d0102181a)
    patch.write_token(APTokenTypes.WRITE, 0x9b4848, 0x0517)
    patch.write_token(APTokenTypes.WRITE, 0x9b4e2f, 0x05171c1d0102191a)

    patch.write_token(APTokenTypes.WRITE, 0x9b52de, 0x0517)
    patch.write_token(APTokenTypes.WRITE, 0x9b5835, 0x05171d1d01021a1a)

    patch.write_token(APTokenTypes.WRITE, 0x9b5835, 0x05171e1d01021b1a)



    # Enable random clan battles
    patch.write_token(APTokenTypes.WRITE, 0xcf802, 0x0428)
    patch.write_token(APTokenTypes.WRITE, 0xcf807, 0x0F)

    # Set max level to 99
    patch.write_token(APTokenTypes.WRITE, 0x0c9bae, 0x63)
    patch.write_token(APTokenTypes.WRITE, 0x0c9baa, 0x63)
    patch.write_token(APTokenTypes.WRITE, 0x12e672, 0x62)
    
    # Set quick options to on
    if world.options.quick_options.value == 1:
        patch.write_token(APTokenTypes.WRITE, 0x51ba4e, 0x03c8)
        
    # Guarantee recruitment option
    if world.options.force_recruitment.value == 1:
        patch.write_token(APTokenTypes.WRITE, 0xd2494, 0x2000)

    # Scale to the highest unit
    if world.options.scaling.value == 1:
        patch.write_token(APTokenTypes.WRITE, 0xca088, 0x42a07950)
        patch.write_token(APTokenTypes.WRITE, 0xca08d, 0x000000001c04dd)
        patch.write_token(APTokenTypes.WRITE, 0xca0aa, 0x1c20)


    # Double EXP option
    if world.options.double_exp.value == 1:
        patch.write_token(APTokenTypes.WRITE, 0x12e658, 0x08e5)

    # Make all missions game over instead of fail
    #patch.write_token(APTokenTypes.WRITE, 0x122258, 2, 0x2001)
    
    
     # This works for removing all missions, maybe do this in the diff file
    for mission in ffta_data.missions:
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.unlockflag1, 0x02)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.unlockflag1 + 1, 0x03)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.unlockflag1 + 2, 0x01)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.unlockflag2, 0x02)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.unlockflag2 + 1, 0x03)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.unlockflag2 + 2, 0x00)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.unlockflag3, 0x00)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.unlockflag3 + 1, 0x00)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.unlockflag3 + 2, 0x00)

        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.rank, 0x30)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.ap_reward, 0x05)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.gil_reward, 0x05)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.rewardItem1, 0x0000)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.rewardItem2, 0x0000)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.cardItem1, 0x00)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.cardItem2, 0x00)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.clan_reward, 0x0A)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.clan_reward + 0x07, 0x0A)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.required_item1, 0x00)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.required_item2, 0x00)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.price, 0x00)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.pub_visibility, 0x00)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.days_available, 0x00)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.timeout_days, 0x00)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.required_job, 0x00)
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.required_skill, 0x00)

        # Make all dispatch missions guarantee success
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.dispatch_ability, 0x00)

        # Hiding mission rewards with ??? bags, also making missions not cancelable
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.mission_display, 0xC0)

        # Hide ??? cards
        patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.mission_display + 1, 0x00)

        # patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.type, 2, 0x00)
        if base_rom[mission.memory + MissionOffsets.type] == 0x0D:
            patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.type, 0x0A)

        # Dispatch missions
        elif base_rom[mission.memory + MissionOffsets.type] == 0x00:
            patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.type, 0x00)
            patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.dispatch_ability, 0x0)
        #    patch.write_token(APTokenTypes.WRITE, mission.memory + 0x10, 1, 0x03)

        elif base_rom[mission.memory + MissionOffsets.type] == 0x02:
            patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.type, 0x02)

        # Make free missions all dispatch missions for now
        elif base_rom[mission.memory + MissionOffsets.type] >= 0x10 and base_rom[mission.memory] >= 0x7D:
            patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.type, 0x00)
            patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.dispatch_ability, 0x0)

        else:
            # was 0x0A before
            patch.write_token(APTokenTypes.WRITE, mission.memory + MissionOffsets.type, 0x0A)


# Job unlock options
    # Unlock all jobs
    if world.options.job_unlock_req.value == 1:
        for jobs in ffta_data.jobs:
            patch.write_token(APTokenTypes.WRITE, jobs.memory + JobOffsets.job_requirement, 0x00)

    # Lock all jobs
    elif world.options.job_unlock_req.value == 2 or world.options.job_unlock_req.value == 3:
        for jobs in ffta_data.jobs:
            patch.write_token(APTokenTypes.WRITE, jobs.memory + JobOffsets.job_requirement, 0xFF)

    # Unlock starting job based on if the requirements are vanilla and units are randomized
    if world.options.job_unlock_req.value == 0 and world.options.starting_units.value == 1 or \
       world.options.job_unlock_req.value == 0 and world.options.starting_units.value == 2 or \
       world.options.job_unlock_req.value == 0 and world.options.starting_units.value == 3:
        patch.write_token(APTokenTypes.WRITE, ffta_data.jobs[world.randomized_jobs[0]].memory + JobOffsets.job_requirement,
                                     0x00)
        patch.write_token(APTokenTypes.WRITE, ffta_data.jobs[world.randomized_jobs[1]].memory + JobOffsets.job_requirement,
                                     0x00)
        patch.write_token(APTokenTypes.WRITE, ffta_data.jobs[world.randomized_jobs[2]].memory + JobOffsets.job_requirement,
                                     0x00)
        patch.write_token(APTokenTypes.WRITE, ffta_data.jobs[world.randomized_jobs[3]].memory + JobOffsets.job_requirement,
                                     0x00)
        patch.write_token(APTokenTypes.WRITE, ffta_data.jobs[world.randomized_jobs[4]].memory + JobOffsets.job_requirement,
                                     0x00)
        patch.write_token(APTokenTypes.WRITE, ffta_data.jobs[world.randomized_jobs[5]].memory + JobOffsets.job_requirement,
                                     0x00)

    # TO DO: Randomize abilities
    #for ability in ffta_data.human_abilities:
    #    patch.write_token(APTokenTypes.WRITE, ability.memory, 8, base_rom[ffta_data.viera_abilities[5].memory])

    # All abilities cost 0
    #for abilities in ffta_data.abilities:
    #    patch.write_token(APTokenTypes.WRITE, abilities.memory + AbilityOffsets.mp_cost, 1, 0x00)
    
    gate_number = world.options.gate_num.value
    if gate_number > 30 and world.options.final_unlock.value == 1:
        gate_number = 30

    set_up_gates(ffta_data, gate_number, world.options.gate_items.value,
                 world.options.final_unlock.value, world.options.final_mission.value,
                 world.options.dispatch.value, world, patch)


# Totema goal
    if world.options.final_unlock.value == 1:
        unlock_mission(ffta_data, 4, patch)

        # Totema goal required items
        set_required_items(ffta_data, 4, 0x1d1, 0x00, patch)
        set_required_items(ffta_data, 7, 0x1d0, 0x00, patch)
        set_required_items(ffta_data, 10, 0x1d2, 0x00, patch)
        set_required_items(ffta_data, 14, 0x1d3, 0x00, patch)
        set_required_items(ffta_data, 17, 0x1c9, 0x00, patch)

        set_mission_requirement(ffta_data, 7, 4, patch)
        set_mission_requirement(ffta_data, 10, 7, patch)
        set_mission_requirement(ffta_data, 14, 10, patch)
        set_mission_requirement(ffta_data, 17, 14, patch)

        # Set Royal Valley to be the final mission if it is chosen in the options
        if world.options.final_mission.value == 0:
            set_mission_requirement(ffta_data, 23, 17, patch)

        # Set Decision Time to be the final mission
        elif world.options.final_mission.value == 1:
            set_mission_requirement(ffta_data, 393, 17, patch)

    # Randomize starting units and set mastered abilities
    if world.options.starting_units.value != 0:
        for index in range(6):

            randomize_unit(ffta_data, index, world, patch)

            # Master all abilities if the unit is a monster type
            if world.randomized_jobs[index] >= 0x2C:
                master_abilities(base_rom, ffta_data, index, get_job_abilities(world.randomized_jobs[index]),
                                 10)
            else:
                master_abilities(base_rom, ffta_data, index, get_job_abilities(world.randomized_jobs[index]),
                                 world.options.starting_abilities.value)

            # Set the basic weapons and equipment if the option is selected
            if world.options.starting_unit_equip.value == 0:
                patch.write_token(APTokenTypes.WRITE, ffta_data.formations[index].memory + UnitOffsets.unit_item1,
                                         world.basic_weapon[index])
                patch.write_token(APTokenTypes.WRITE, ffta_data.formations[index].memory + UnitOffsets.unit_item2,
                                         world.basic_equip[index])
                patch.write_token(APTokenTypes.WRITE, ffta_data.formations[index].memory + UnitOffsets.unit_item3, 0x00)

    # Master abilities if units aren't randomized
    if world.options.starting_units.value == 0:
        master_abilities(base_rom, ffta_data, 0, get_job_abilities(JobID.soldier),
                         world.options.starting_abilities.value)
        master_abilities(base_rom, ffta_data, 1, get_job_abilities(JobID.blackmagemog),
                         world.options.starting_abilities.value)
        master_abilities(base_rom, ffta_data, 2, get_job_abilities(JobID.soldier),
                         world.options.starting_abilities.value)
        master_abilities(base_rom, ffta_data, 3, get_job_abilities(JobID.whitemonk),
                         world.options.starting_abilities.value)
        master_abilities(base_rom, ffta_data, 4, get_job_abilities(JobID.whitemagemou),
                         world.options.starting_abilities.value)
        master_abilities(base_rom, ffta_data, 5, get_job_abilities(JobID.archervra),
                         world.options.starting_abilities.value)

    # Randomize enemies
    
    for index in range(6, 0xA46):
    
        patch.write_token(APTokenTypes.WRITE, ffta_data.formations[index].memory + UnitOffsets.level, 0)
        
        if world.options.randomize_enemies.value == 1:
            if base_rom[ffta_data.formations[index].memory] == 0x01:

                randomize_unit(ffta_data, index, world, patch)
                master_abilities(base_rom, ffta_data, index, get_job_abilities(world.randomized_jobs[index]), random.randint(1, 10))

                # Disable reaction and support abilities for now
                patch.write_token(APTokenTypes.WRITE, ffta_data.formations[index].memory + UnitOffsets.ability_reaction,
                          0x00)
                patch.write_token(APTokenTypes.WRITE, ffta_data.formations[index].memory + UnitOffsets.ability_support,
                          0x00)



    # TEMPORARY: Randomize judge units since laws aren't accounted for
    randomize_judge(ffta_data, 0xa10, 0, world, patch)
    randomize_judge(ffta_data, 0xa21, 1, world, patch)
    randomize_judge(ffta_data, 0xa30, 2, world, patch)
    randomize_judge(ffta_data, 0xa31, 3, world, patch)
    randomize_judge(ffta_data, 0xa32, 4, world, patch)

    # Have the judges master all the abilities
    master_abilities(base_rom, ffta_data, 0xa10, get_job_abilities(world.randomized_judge[0]), 10)
    master_abilities(base_rom, ffta_data, 0xa21, get_job_abilities(world.randomized_judge[1]), 10)
    master_abilities(base_rom, ffta_data, 0xa30, get_job_abilities(world.randomized_judge[2]), 10)
    master_abilities(base_rom, ffta_data, 0xa31, get_job_abilities(world.randomized_judge[3]), 10)
    master_abilities(base_rom, ffta_data, 0xa32, get_job_abilities(world.randomized_judge[4]), 10)


    # Remove Llednar's weapon on present day to make it more survivable
    patch.write_token(APTokenTypes.WRITE, 0x52eaf8, 0x00)

    # Set option for job items in the ROM
    #if world.options.job_unlock_req.value == 3:
    #    patch.write_token(APTokenTypes.WRITE, 0xAAAAD0, 1, 0x01)

    # Randomize locations on map
    for i in range(0, len(world.location_ids)):
        patch.write_token(APTokenTypes.WRITE, 0xb390dc + i, world.location_ids[i])

    set_items(world.multiworld, player, patch)

    # Set the starting gil amount
    starting_gil = world.options.starting_gil.value
    patch.write_token(APTokenTypes.WRITE, 0x986c, starting_gil)
 
    player_name = world.multiworld.get_file_safe_player_name(world.player)
    for i, byte in enumerate(player_name.encode("utf-8")):
        patch.write_token(APTokenTypes.WRITE, 0xAAABD0 + i, byte)

    patch.write_file("token_data.bin", patch.get_token_binary())

    # Write Output
    outfile_player_name = f"_P{player}"
    outfile_player_name += f"_{world.multiworld.get_file_safe_player_name(player).replace(' ', '_')}" \
        if world.multiworld.player_name[player] != f"Player{player}" else ""

    patch.write(
        os.path.join(output_directory, f"AP_{world.multiworld.seed_name}{outfile_player_name}{patch.patch_file_ending}"))


def set_up_gates(ffta_data: FFTAData, num_gates: int, req_items, final_unlock: int, final_mission: int, dispatch: int,
                 world, patch: FFTAProcedurePatch) -> None:

    unlock_mission(ffta_data, world.MissionGroups[0][0].mission_id, patch)
    unlock_mission(ffta_data, world.MissionGroups[1][0].mission_id, patch)
    unlock_mission(ffta_data, world.MissionGroups[2][0].mission_id, patch)
    unlock_mission(ffta_data, world.MissionGroups[3][0].mission_id, patch)

    if world.options.gate_paths.value == 2:
        unlock_mission(ffta_data, world.MissionGroups[7][0].mission_id, patch)

    elif world.options.gate_paths.value == 3:
        unlock_mission(ffta_data, world.MissionGroups[7][0].mission_id, patch)
        unlock_mission(ffta_data, world.MissionGroups[11][0].mission_id, patch)

    for i in range(0, dispatch):
        unlock_mission(ffta_data, world.DispatchMissionGroups[i][0].mission_id, patch)

    req_item2 = 0

    # Add second required mission item if options are selected
    if req_items == 1 or req_items == 2:
        req_item2 = MissionUnlockItems[1].itemID

    if world.options.gate_items.value == 2:
        set_required_items(ffta_data, world.MissionGroups[3][0].mission_id, MissionUnlockItems[0].itemID,
                           0, patch)
        set_required_items(ffta_data, world.DispatchMissionGroups[dispatch - 1][0].mission_id, req_item2,
                           0, patch)

    else:
        set_required_items(ffta_data, world.MissionGroups[3][0].mission_id, MissionUnlockItems[0].itemID,
                           req_item2, patch)

    if world.options.gate_paths == 2:
        if world.options.gate_items.value == 2:
            set_required_items(ffta_data, world.MissionGroups[7][0].mission_id, MissionUnlockItems[2].itemID,
                               0, patch)
            set_required_items(ffta_data, world.DispatchMissionGroups[dispatch - 1][0].mission_id, req_item2,
                               0, patch)

        else:
            set_required_items(ffta_data, world.MissionGroups[7][0].mission_id, MissionUnlockItems[2].itemID,
                               req_item2, patch)

    if world.options.gate_paths == 3:
        # Setting required item for the start of path 2
        if world.options.gate_items.value == 2:
            set_required_items(ffta_data, world.MissionGroups[7][0].mission_id, MissionUnlockItems[2].itemID,
                               0, patch)
            set_required_items(ffta_data, world.DispatchMissionGroups[dispatch - 1][0].mission_id, req_item2,
                               0, patch)

        else:
            set_required_items(ffta_data, world.MissionGroups[7][0].mission_id, MissionUnlockItems[2].itemID,
                               req_item2, patch)

        # Setting require item for the start of path 3
        if world.options.gate_items.value == 2:
            set_required_items(ffta_data, world.MissionGroups[11][0].mission_id, MissionUnlockItems[4].itemID,
                               0, patch)
            set_required_items(ffta_data, world.DispatchMissionGroups[dispatch - 1][0].mission_id, req_item2,
                               0, patch)

        else:
            set_required_items(ffta_data, world.MissionGroups[11][0].mission_id, MissionUnlockItems[4].itemID,
                               req_item2, patch)

    mission_index = 4
    mission_unlock = 3
    dispatch_index = dispatch
    dispatch_unlock = dispatch - 1
    item_index = 2

    if num_gates == 1 and final_unlock == 0:

        # Unlock Royal Valley for one gate setting
        if final_mission == 0:
            set_mission_requirement(ffta_data, 23, world.MissionGroups[3][0].mission_id, patch)

        # Unlock Decision Time for one gate setting
        elif final_mission == 1:
            set_mission_requirement(ffta_data, 393, world.MissionGroups[3][0].mission_id, patch)

        return

    if world.options.gate_paths.value == 1:
        # It was range(2, num_gates + 1) before
        for i in range(2, num_gates + 1):

            print("Mission unlock: " + str(mission_unlock))

            for j in range(4):
                print("Mission index: " + str(mission_index))
                set_mission_requirement(ffta_data, world.MissionGroups[mission_index][0].mission_id,
                                        world.MissionGroups[mission_unlock][0].mission_id, patch)
                mission_index = mission_index + 1

            # Add dispatch missions based on settings
            for k in range(0, dispatch):

                if world.options.gate_items.value == 2:
                    set_mission_requirement(ffta_data, world.DispatchMissionGroups[dispatch_index][0].mission_id,
                                            world.DispatchMissionGroups[dispatch_unlock][0].mission_id, patch)

                else:
                    set_mission_requirement(ffta_data, world.DispatchMissionGroups[dispatch_index][0].mission_id,
                                            world.MissionGroups[mission_unlock][0].mission_id, patch)

                dispatch_index = dispatch_index + 1

            mission_unlock = mission_unlock + 4
            dispatch_unlock = dispatch_unlock + dispatch

            if req_items == 1 or req_items == 2:
                req_item2 = MissionUnlockItems[item_index + 1].itemID

            # Add required item to dispatch mission gates if option is selected
            if world.options.gate_items.value == 2:
                set_required_items(ffta_data, world.DispatchMissionGroups[dispatch_unlock][0].mission_id,
                                   req_item2,
                                   0, patch)
                set_required_items(ffta_data, world.MissionGroups[mission_unlock][0].mission_id,
                                   MissionUnlockItems[item_index].itemID,
                                   0, patch)

            else:
                set_required_items(ffta_data, world.MissionGroups[mission_unlock][0].mission_id, MissionUnlockItems[item_index].itemID,
                                   req_item2, patch)

            item_index = item_index + 2

    elif world.options.gate_paths.value == 2:
        for i in range(1, num_gates):

            print("Mission unlock: " + str(mission_unlock))
            for j in range(3):
                print("Mission index: " + str(mission_index))
                set_mission_requirement(ffta_data, world.MissionGroups[mission_index][0].mission_id,
                                        world.MissionGroups[mission_unlock][0].mission_id, patch)
                mission_index = mission_index + 1

            print("Mission index: " + str(mission_index + 4))
            set_mission_requirement(ffta_data, world.MissionGroups[mission_index + 4][0].mission_id,
                                    world.MissionGroups[mission_unlock][0].mission_id, patch)

            for k in range(0, dispatch):

                if world.options.gate_items.value == 2:
                    set_mission_requirement(ffta_data, world.DispatchMissionGroups[dispatch_index][0].mission_id,
                                            world.DispatchMissionGroups[dispatch_unlock][0].mission_id, patch)

                else:
                    set_mission_requirement(ffta_data, world.DispatchMissionGroups[dispatch_index][0].mission_id,
                                            world.MissionGroups[mission_unlock][0].mission_id, patch)

                dispatch_index = dispatch_index + 1

            mission_index = mission_index + 1
            mission_unlock = mission_unlock + 4
            dispatch_unlock = dispatch_unlock + dispatch

            if req_items == 1 or req_items == 2:
                req_item2 = MissionUnlockItems[item_index + 1].itemID

            # Add required item to dispatch mission gates if option is selected
            if world.options.gate_items.value == 2:
                set_required_items(ffta_data, world.DispatchMissionGroups[dispatch_unlock][0].mission_id,
                                   req_item2,
                                   0, patch)
                set_required_items(ffta_data, world.MissionGroups[mission_unlock][0].mission_id,
                                   MissionUnlockItems[item_index].itemID,
                                   0, patch)

            else:
                set_required_items(ffta_data, world.MissionGroups[mission_unlock][0].mission_id, MissionUnlockItems[item_index].itemID,
                                   req_item2, patch)

            item_index = item_index + 2

    elif world.options.gate_paths.value == 3:

        path1_index = mission_index
        path2_index = mission_index + 4
        path3_index = mission_index + 8

        path1_unlock = mission_unlock
        path2_unlock = mission_unlock + 4
        path3_unlock = mission_unlock + 8

        path1_item = item_index + 4
        path2_item = item_index + 6
        path3_item = item_index + 8

        print("Path1")
        print(world.path1_length)
        for i in range(1, world.path1_length):
            print(i)
            print("Mission unlock: " + str(path1_unlock))
            for j in range(3):
                print("Mission index: " + str(path1_index))
                set_mission_requirement(ffta_data, world.MissionGroups[path1_index][0].mission_id,
                                        world.MissionGroups[path1_unlock][0].mission_id, patch)
                path1_index = path1_index + 1

            print("Mission index: " + str(path1_index + 8))
            set_mission_requirement(ffta_data, world.MissionGroups[path1_index + 8][0].mission_id,
                                    world.MissionGroups[path1_unlock][0].mission_id, patch)

            for k in range(0, dispatch):

                if world.options.gate_items.value == 2:
                    set_mission_requirement(ffta_data, world.DispatchMissionGroups[dispatch_index][0].mission_id,
                                            world.DispatchMissionGroups[dispatch_unlock][0].mission_id, patch)

                else:
                    set_mission_requirement(ffta_data, world.DispatchMissionGroups[dispatch_index][0].mission_id,
                                            world.MissionGroups[path1_unlock][0].mission_id, patch)

                dispatch_index = dispatch_index + 1

            path1_index = path1_index + 9
            path1_unlock = path1_unlock + 12
            dispatch_unlock = dispatch_unlock + dispatch

            if req_items == 1 or req_items == 2:
                req_item2 = MissionUnlockItems[path1_item + 1].itemID

            # Add required item to dispatch mission gates if option is selected
            if world.options.gate_items.value == 2:
                set_required_items(ffta_data, world.DispatchMissionGroups[dispatch_unlock][0].mission_id,
                                   req_item2,
                                   0, patch)
                set_required_items(ffta_data, world.MissionGroups[mission_unlock][0].mission_id,
                                   MissionUnlockItems[path1_item].itemID,
                                   0, patch)

            else:
                set_required_items(ffta_data, world.MissionGroups[path1_unlock][0].mission_id,
                                   MissionUnlockItems[path1_item].itemID,
                                   req_item2, patch)

            path1_item = path1_item + 6

        print("Path 2")
        print(world.path2_length)
        for i in range(1, world.path2_length):
            print(i)
            print("Mission unlock: " + str(path2_unlock))
            for j in range(3):
                print("Mission index: " + str(path2_index))
                set_mission_requirement(ffta_data, world.MissionGroups[path2_index][0].mission_id,
                                        world.MissionGroups[path2_unlock][0].mission_id, patch)
                path2_index = path2_index + 1

            print("Mission index: " + str(path2_index + 8))
            set_mission_requirement(ffta_data, world.MissionGroups[path2_index + 8][0].mission_id,
                                    world.MissionGroups[path2_unlock][0].mission_id, patch)

            for k in range(0, dispatch):

                if world.options.gate_items.value == 2:
                    set_mission_requirement(ffta_data, world.DispatchMissionGroups[dispatch_index][0].mission_id,
                                            world.DispatchMissionGroups[dispatch_unlock][0].mission_id, patch)

                else:
                    set_mission_requirement(ffta_data, world.DispatchMissionGroups[dispatch_index][0].mission_id,
                                            world.MissionGroups[path2_unlock][0].mission_id, patch)

                dispatch_index = dispatch_index + 1

            path2_index = path2_index + 9
            path2_unlock = path2_unlock + 12
            dispatch_unlock = dispatch_unlock + dispatch

            if req_items == 1 or req_items == 2:
                req_item2 = MissionUnlockItems[item_index + 1].itemID

            # Add required item to dispatch mission gates if option is selected
            if world.options.gate_items.value == 2:
                set_required_items(ffta_data, world.DispatchMissionGroups[dispatch_unlock][0].mission_id,
                                   req_item2,
                                   0, patch)
                set_required_items(ffta_data, world.MissionGroups[mission_unlock][0].mission_id,
                                   MissionUnlockItems[path2_item].itemID,
                                   0, patch)

            else:
                set_required_items(ffta_data, world.MissionGroups[path2_unlock][0].mission_id,
                                   MissionUnlockItems[path2_item].itemID,
                                   req_item2, patch)

            path2_item = path2_item + 6


        print("Path 3")
        print(world.path3_length)
        for i in range(1, world.path3_length):
            print(i)
            print("Mission unlock: " + str(path3_unlock))
            for j in range(3):
                print("Mission index: " + str(path3_index))
                set_mission_requirement(ffta_data, world.MissionGroups[path3_index][0].mission_id,
                                        world.MissionGroups[path3_unlock][0].mission_id, patch)
                path3_index = path3_index + 1

            print("Mission index: " + str(path3_index + 8))
            set_mission_requirement(ffta_data, world.MissionGroups[path3_index + 8][0].mission_id,
                                    world.MissionGroups[path3_unlock][0].mission_id, patch)

            for k in range(0, dispatch):

                if world.options.gate_items.value == 2:
                    set_mission_requirement(ffta_data,
                                            world.DispatchMissionGroups[dispatch_index][0].mission_id,
                                            world.DispatchMissionGroups[dispatch_unlock][0].mission_id, patch)

                else:
                    set_mission_requirement(ffta_data,
                                            world.DispatchMissionGroups[dispatch_index][0].mission_id,
                                            world.MissionGroups[path3_unlock][0].mission_id, patch)

                dispatch_index = dispatch_index + 1

            path3_index = path3_index + 9
            path3_unlock = path3_unlock + 12
            dispatch_unlock = dispatch_unlock + dispatch

            if req_items == 1 or req_items == 2:
                req_item2 = MissionUnlockItems[path3_item + 1].itemID

            # Add required item to dispatch mission gates if option is selected
            if world.options.gate_items.value == 2:
                set_required_items(ffta_data, world.DispatchMissionGroups[dispatch_unlock][0].mission_id,
                                   req_item2,
                                   0, patch)
                set_required_items(ffta_data, world.MissionGroups[mission_unlock][0].mission_id,
                                   MissionUnlockItems[path3_item].itemID,
                                   0, patch)

            else:
                set_required_items(ffta_data, world.MissionGroups[path3_unlock][0].mission_id,
                                   MissionUnlockItems[path3_item].itemID,
                                   req_item2, patch)

            path3_item = path3_item + 6


    # Set final mission to unlock after all the gates if all mission gates option is selected
    if final_unlock == 0:

        if world.options.gate_paths.value == 1:

            # Unlock Royal Valley if it is selected to be the final mission
            if final_mission == 0:
                set_mission_requirement(ffta_data, 23, world.MissionGroups[mission_unlock][0].mission_id, patch)

            # Unlock Decision Time as the final mission
            elif final_mission == 1:
                set_mission_requirement(ffta_data, 393, world.MissionGroups[mission_unlock][0].mission_id, patch)

        # Set all final missions in paths to unlock the final mission
        elif world.options.gate_paths.value == 2:

            # Unlock Royal Valley if it is selected to be the final mission
            if final_mission == 0:
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag1,
                          world.MissionGroups[mission_unlock][0].mission_id + 2)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag1 + 0x01,
                          0x03)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag1 + 0x02,
                          0x01)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag2,
                          world.MissionGroups[mission_unlock + 1][0].mission_id)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag2 + 1,
                          0x04)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag2 + 2,
                          0x01)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag3, 0x00)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag3 + 1,
                          0x05)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag3 + 2,
                          0x01)

            # Unlock Decision Time as the final mission
            elif final_mission == 1:
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag1,
                          world.MissionGroups[mission_unlock][0].mission_id + 2)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag1 + 0x01,
                          0x03)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag1 + 0x02,
                          0x01)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag2,
                          world.MissionGroups[mission_unlock + 1][0].mission_id)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag2 + 1,
                          0x04)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag2 + 2,
                          0x01)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag3, 0x00)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag3 + 1,
                          0x05)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag3 + 2,
                          0x01)

                # Set all final missions in paths to unlock the final mission
        elif world.options.gate_paths.value == 3:

            # Unlock Royal Valley if it is selected to be the final mission
            if final_mission == 0:
                print("path 1 unlock:" + str(world.MissionGroups[path1_unlock][0].mission_id))
                print("path 2 unlock:" + str(world.MissionGroups[path2_unlock][0].mission_id))
                print("path 3 unlock:" + str(world.MissionGroups[path3_unlock][0].mission_id))

                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag1,
                          world.MissionGroups[path1_unlock][0].mission_id + 2)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag1 + 0x01,
                          0x03)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag1 + 0x02,
                          0x01)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag2,
                          world.MissionGroups[path2_unlock][0].mission_id + 2)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag2 + 0x01,
                          0x03)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag2 + 0x02,
                          0x01)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag3,
                          world.MissionGroups[path3_unlock][0].mission_id + 2)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag3 + 0x01,
                          0x03)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[23].memory + MissionOffsets.unlockflag3 + 0x02,
                          0x01)

            # Unlock Decision Time as the final mission
            elif final_mission == 1:
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag1,
                          world.MissionGroups[path1_unlock][0].mission_id + 2)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag1 + 0x01,
                          0x03)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag1 + 0x02,
                          0x01)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag2,
                          world.MissionGroups[path2_unlock][0].mission_id)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag2 + 1,
                          0x03)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag2 + 2,
                          0x01)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag3,
                          world.MissionGroups[path3_unlock][0].mission_id)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag3 + 1,
                          0x00)
                patch.write_token(APTokenTypes.WRITE, ffta_data.missions[393].memory + MissionOffsets.unlockflag3 + 2,
                          0x00)


def set_mission_requirement(ffta_data: FFTAData, current_mission_ID: int, previous_mission_ID: int, patch: FFTAProcedurePatch) -> None:

    # Set the mission requirements to the specified mission ID
    patch.write_token(APTokenTypes.WRITE, ffta_data.missions[current_mission_ID].memory + MissionOffsets.unlockflag1, previous_mission_ID + 2)
    patch.write_token(APTokenTypes.WRITE, ffta_data.missions[current_mission_ID].memory + MissionOffsets.unlockflag1 + 0x01, 0x03)
    patch.write_token(APTokenTypes.WRITE, ffta_data.missions[current_mission_ID].memory + MissionOffsets.unlockflag1 + 0x02, 0x01)
    patch.write_token(APTokenTypes.WRITE, ffta_data.missions[current_mission_ID].memory + MissionOffsets.unlockflag2,  0x00)
    patch.write_token(APTokenTypes.WRITE, ffta_data.missions[current_mission_ID].memory + MissionOffsets.unlockflag2 + 1, 0x00)
    patch.write_token(APTokenTypes.WRITE, ffta_data.missions[current_mission_ID].memory + MissionOffsets.unlockflag2 + 2, 0x00)
    patch.write_token(APTokenTypes.WRITE, ffta_data.missions[current_mission_ID].memory + MissionOffsets.unlockflag3, 0x00)
    patch.write_token(APTokenTypes.WRITE, ffta_data.missions[current_mission_ID].memory + MissionOffsets.unlockflag3 + 1, 0x00)
    patch.write_token(APTokenTypes.WRITE, ffta_data.missions[current_mission_ID].memory + MissionOffsets.unlockflag3 + 2, 0x00)


def set_items(multiworld, player, patch: FFTAProcedurePatch) -> None:
    offset = 41234532

    for location in multiworld.get_filled_locations(player):

        if location.item.code is not None:
            if location.item.player == player:
                if location.item.code - offset >= 0x2ac:
                    patch.write_token(APTokenTypes.WRITE, location.address, 0x1bc)

                else:
                    patch.write_token(APTokenTypes.WRITE, location.address, location.item.code - offset)
            else:
                patch.write_token(APTokenTypes.WRITE, location.address, 0x185)


def set_required_items(ffta_data: FFTAData, index: int, itemid1, itemid2, patch: FFTAProcedurePatch):
    patch.write_token(APTokenTypes.WRITE, ffta_data.missions[index].memory + MissionOffsets.required_item1, itemid1 - 0x177)

    if itemid2 != 0:
        patch.write_token(APTokenTypes.WRITE, ffta_data.missions[index].memory + MissionOffsets.required_item2, itemid2 - 0x177)

    else:
        patch.write_token(APTokenTypes.WRITE, ffta_data.missions[index].memory + MissionOffsets.required_item2, itemid2)

"""

