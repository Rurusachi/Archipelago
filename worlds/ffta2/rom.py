import os
import pkgutil
import struct
from typing import Tuple

from settings import get_settings

from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes

from .data import (FFTA2Data, ffta2_data, QuestOffsets, FormationOffsets, Formations, UnitOffsets, RecruitableUnitOffsets, JobRequirementOffsets, FlagOffsets, MemoryAddresses, jobUnlockList, get_flag, recruitableUnitNames)
from .items import (GateItems, jobUnlockOffset, jobUnlockItems)
from .locations import (FFTA2Locations)
from .options import (JobUnlockRequirements, DispatchQuests)


def get_base_rom_as_bytes() -> bytes:
    with open(get_settings().ffta2_options.rom_file, "rb") as infile:
        base_rom_bytes = bytes(infile.read())

    return base_rom_bytes


class FFTA2ProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Final Fantasy Tactics A2"
    hash = "aaffeb638f1ac98ed3a954264ad1bf2e"
    patch_file_ending = ".apffta2"
    result_file_ending = ".nds"

    procedure = [
        ("apply_bsdiff4", ["base_patch.bsdiff4"]),
        ("apply_tokens", ["token_data.bin"]),
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_as_bytes()


def unlock_quest(ffta2_data, index: int, patch: FFTA2ProcedurePatch):
    patch.write_token(APTokenTypes.WRITE, ffta2_data.quests[index].memory + QuestOffsets.story_requirement,
                      struct.pack("<H", 0x1))


def generate_output(world, player: int, output_directory: str) -> None:
    patch = FFTA2ProcedurePatch(player=player, player_name=world.multiworld.player_name[player])

    patch.write_file("base_patch.bsdiff4", pkgutil.get_data(__name__, "ffta2_data/base_patch.bsdiff4"))

    for index, quest in enumerate(ffta2_data.quests):

        patch.write_token(APTokenTypes.OR_8, quest.memory + QuestOffsets.region, 0x7e)

        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.story_requirement, struct.pack("<H", 0x0))
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.flag_requirement, struct.pack("<H", 0x0))
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.unknown_requirement, struct.pack("<HB", 0x0, 0x0))

        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.month, struct.pack("<B", 0x0))
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.available_period, struct.pack("<B", 0x0))
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.days, struct.pack("<B", 0x0))
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.repeat_failed_days, struct.pack("<B", 0x0))
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.repeat_completed_days, struct.pack("<B", 0xFE))  # FE = Never?
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.fee, struct.pack("<B", 0x0))

        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.required_item1, struct.pack("<H", 0x0))
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.required_item_amount1, struct.pack("<B", 0x0))
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.required_item2, struct.pack("<H", 0x0))
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.required_item_amount2, struct.pack("<B", 0x0))

        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.negotiation, struct.pack("<B", 0x0))
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.aptitude, struct.pack("<B", 0x0))
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.teamwork, struct.pack("<B", 0x0))
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.adaptability, struct.pack("<B", 0x0))

        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.reward_1, struct.pack("<H", 0x0))
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.reward_2, struct.pack("<H", 0x0))
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.reward_3, struct.pack("<H", 0x0))

        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.exp, struct.pack("<B", world.options.quest_exp.value))
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.ap, struct.pack("<B", world.options.quest_ap.value))
        patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.cp, struct.pack("<B", 0x0))

        if world.options.quest_gil.value != -1:
            patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.gil_reward, struct.pack("<H", world.options.quest_gil.value))

        if world.options.dispatch_quests.value == DispatchQuests.option_no_dispatch:
            patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.is_dispatch, struct.pack("<H", 0x0))

        if quest.name in ["Wanted: Woodcutter", "Clan Mates recruit"]:
            # Move out of locked location in Targ
            patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.location, struct.pack("<B", 0x4))
        elif quest.name in ["Seeding the Harvest", "A Harvest Hand"] or index == 0x1a6:
            # Move out of locked location in Camoa
            patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.location, struct.pack("<B", 0xa))
        elif quest.name == "Brightmoon Tor":
            patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.location, struct.pack("<B", 0x22))

        if quest.name == "The Two Grimoires" and world.options.final_quests.value == 1:
            # Put the final quest near Targ so it's actually accessible
            patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.location, struct.pack("<B", 0x2))
        elif quest.name.endswith("recruit") or quest.name.endswith("random"):
            patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.story_requirement, struct.pack("<H", 0x1))
            patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.days, struct.pack("<B", 5))
            patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.repeat_failed_days, struct.pack("<B", 20))
            patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.repeat_completed_days, struct.pack("<B", 20))
            if quest.name.endswith("recruit"):
                patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.exp, struct.pack("<B", 0))
                patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.ap, struct.pack("<B", 0))
                patch.write_token(APTokenTypes.WRITE, quest.memory + QuestOffsets.gil_reward, struct.pack("<H", 0))

    for formation in ffta2_data.formations:
        for unit in range(formation.units):
            unitMemory = formation.memory + Formations.byteSize + Formations.unitSize * unit

            # Enemies scale with average(?) level
            patch.write_token(APTokenTypes.WRITE, unitMemory + UnitOffsets.min_level, struct.pack("<H", 1))
            patch.write_token(APTokenTypes.WRITE, unitMemory + UnitOffsets.max_level, struct.pack("<H", 99))

            # Set loot to consumables(?)
            patch.write_token(APTokenTypes.WRITE, unitMemory + UnitOffsets.loot_lvl1, struct.pack("<H", 0x38))
            patch.write_token(APTokenTypes.WRITE, unitMemory + UnitOffsets.loot_lvl2, struct.pack("<H", 0x38))
            patch.write_token(APTokenTypes.WRITE, unitMemory + UnitOffsets.loot_lvl3, struct.pack("<H", 0x38))
            patch.write_token(APTokenTypes.WRITE, unitMemory + UnitOffsets.loot_lvl4, struct.pack("<H", 0x38))

    if world.options.job_unlock_req.value == JobUnlockRequirements.option_job_items:
        for job_item in jobUnlockItems:
            job_id_list = jobUnlockList[job_item.itemID - jobUnlockOffset - 1]
            for id in job_id_list:
                job = ffta2_data.jobRequirements[id-1]

                job_flag_pointer = get_flag(job_item.itemID - jobUnlockOffset - 1, FlagOffsets.JobItems)[2]
                # print(hex(flag))
                patch.write_token(APTokenTypes.WRITE, job.memory + JobRequirementOffsets.quest_requirement, struct.pack("<H", job_flag_pointer))
                patch.write_token(APTokenTypes.WRITE, job.memory + JobRequirementOffsets.job1, struct.pack("<BB", 0x0, 0x0))
                patch.write_token(APTokenTypes.WRITE, job.memory + JobRequirementOffsets.job2, struct.pack("<BB", 0x0, 0x0))
                patch.write_token(APTokenTypes.WRITE, job.memory + JobRequirementOffsets.job3, struct.pack("<BB", 0x0, 0x0))
    else:
        for i, job in enumerate(ffta2_data.jobRequirements):
            if world.options.job_unlock_req.value == JobUnlockRequirements.option_no_quests:
                patch.write_token(APTokenTypes.WRITE, job.memory + JobRequirementOffsets.quest_requirement, struct.pack("<H", 0x0))
            elif world.options.job_unlock_req.value == JobUnlockRequirements.option_all_unlocked:
                patch.write_token(APTokenTypes.WRITE, job.memory + JobRequirementOffsets.quest_requirement, struct.pack("<H", 0x0))
                patch.write_token(APTokenTypes.WRITE, job.memory + JobRequirementOffsets.job1, struct.pack("<BB", 0x0, 0x0))
                patch.write_token(APTokenTypes.WRITE, job.memory + JobRequirementOffsets.job2, struct.pack("<BB", 0x0, 0x0))
                patch.write_token(APTokenTypes.WRITE, job.memory + JobRequirementOffsets.job3, struct.pack("<BB", 0x0, 0x0))
            elif world.options.job_unlock_req.value == JobUnlockRequirements.option_all_locked:
                job_flag_pointer = 0x168  # 2D bytes, 0 bits (0x0212d761, should always be 0, otherwise item events break)
                patch.write_token(APTokenTypes.WRITE, job.memory + JobRequirementOffsets.quest_requirement, struct.pack("<H", job_flag_pointer))

    for i in range(1, 6):
        patch.write_token(APTokenTypes.WRITE, ffta2_data.recruitableUnits[i].memory + RecruitableUnitOffsets.starter, struct.pack("<B", 0x0))

    for unit_name in world.options.starting_units.value:
        unit_index = recruitableUnitNames.index(unit_name)
        patch.write_token(APTokenTypes.WRITE, ffta2_data.recruitableUnits[unit_index].memory + RecruitableUnitOffsets.starter, struct.pack("<B", 0x8))
        patch.write_token(APTokenTypes.WRITE, ffta2_data.recruitableUnits[unit_index].memory + RecruitableUnitOffsets.min_level, struct.pack("<B", 0x3))

    gate_number = world.options.gate_num.value
    if gate_number > 30 and world.options.goal.value == 1:
        gate_number = 30

    set_up_gates(ffta2_data, gate_number, world, patch)

    set_items(world.multiworld, player, patch)

    patch.write_file("token_data.bin", patch.get_token_binary())

    # Write Output
    out_file_name = world.multiworld.get_out_file_name_base(world.player)

    patch.write(
        os.path.join(output_directory,
                     f"{out_file_name}{patch.patch_file_ending}"))


def set_up_gates(ffta2_data: FFTA2Data, num_gates: int,
                 world, patch: FFTA2ProcedurePatch) -> None:
    unlock_quest(ffta2_data, world.QuestGroups[0][0][0].quest_id, patch)
    unlock_quest(ffta2_data, world.QuestGroups[1][0][0].quest_id, patch)
    unlock_quest(ffta2_data, world.QuestGroups[2][0][0].quest_id, patch)

    # unlock_quest(ffta2_data, world.QuestGroups[3][0][0].quest_id, patch)

    # set_required_items(ffta2_data,
    #                    world.QuestGroups[3][0][0].quest_id, GateItems[0].itemID, patch)

    final_quest_list = [0x16, 0x17]  # "The Ritual", "The Two Grimoires"
    final_quest_id = final_quest_list[world.options.final_quests.value]

    if world.options.final_quests.value == 0:
        set_quest_requirement(ffta2_data, 0x17, 0x16, patch)

    # quest_index = 4
    # quest_unlock = 3
    # item_index = 0

    if num_gates == 1:
        unlock_quest(ffta2_data, world.QuestGroups[3][0][0].quest_id, patch)
        set_required_items(ffta2_data,
                           world.QuestGroups[3][0][0].quest_id, GateItems[0].itemID, patch)
        set_quest_requirement(ffta2_data, final_quest_id, world.QuestGroups[3][0][0].quest_id, patch)
        return

    # if True:
    #     for i in range(2, num_gates + 1):

    #         for j in range(4):
    #             set_quest_requirement(ffta2_data, world.QuestGroups[quest_index][0][0].quest_id,
    #                                     world.QuestGroups[quest_unlock][0][0].quest_id, patch)
    #             quest_index += 1

    #         quest_unlock += 4

    #         set_required_items(ffta2_data, world.QuestGroups[quest_unlock][0][0].quest_id,
    #                            GateItems[item_index].itemID,
    #                            patch)
    #         item_index += 1

    num_paths = len(world.path_quests)

    # Unlock the first gate quest in each path
    for path in world.path_quests:
        unlock_quest(ffta2_data, world.QuestGroups[path[0][0]][0][0].quest_id, patch)

    for path_index, path in enumerate(world.path_quests):
        item_index: int = path_index
        for previous_quest, quests in path:
            for quest_index in quests:
                set_quest_requirement(ffta2_data, world.QuestGroups[quest_index][0][0].quest_id,
                                      world.QuestGroups[previous_quest][0][0].quest_id, patch)

            set_required_items(ffta2_data, world.QuestGroups[previous_quest][0][0].quest_id,
                               GateItems[item_index].itemID,
                               patch)
            item_index += num_paths

    # Set final quest to unlock after all the gates if all quest gates option is selected
    if num_paths == 1:
        set_quest_requirement(ffta2_data, final_quest_id,
                              world.QuestGroups[world.path_quests[0][-1][0]][0][0].quest_id, patch)
    else:
        (byte_index, bit_index, quest_flag) = get_flag(0, FlagOffsets.FinalQuest)
        patch.write_token(APTokenTypes.WRITE, ffta2_data.quests[final_quest_id].memory + QuestOffsets.flag_requirement,
                          struct.pack("<H", quest_flag))
        patch.write_token(APTokenTypes.WRITE, ffta2_data.quests[final_quest_id].memory + QuestOffsets.story_requirement,
                          struct.pack("<H", 0x1))


def set_quest_requirement(ffta2_data: FFTA2Data, current_quest_ID: int, previous_quest_ID: int,
                          patch: FFTA2ProcedurePatch) -> None:

    (byte_index, bit_index, quest_flag) = get_flag(previous_quest_ID, FlagOffsets.Quest)
    # print(f"{previous_quest_ID} -> {current_quest_ID}: ({byte_index}, {bit_index})")

    patch.write_token(APTokenTypes.WRITE, ffta2_data.quests[current_quest_ID].memory + QuestOffsets.flag_requirement,
                      struct.pack("<H", quest_flag))
    patch.write_token(APTokenTypes.WRITE, ffta2_data.quests[current_quest_ID].memory + QuestOffsets.story_requirement,
                      struct.pack("<H", 0x1))


def set_items(multiworld, player, patch: FFTA2ProcedurePatch) -> None:
    offset = 0

    for location in multiworld.get_filled_locations(player):

        if location.item.code is not None:
            if location.item.player != player:
                item_id = 0x00F5
            else:
                item_id = location.item.code - offset

            if item_id > jobUnlockOffset:
                quest_flag = -1
                for quest in FFTA2Locations:
                    for locData in quest:
                        if locData.name == location.name:
                            quest_flag = get_flag(locData.quest_id, FlagOffsets.Quest)[2]
                            break
                    if quest_flag != -1:
                        break
                print(f"{hex(item_id)} -> {hex(quest_flag)}")
                for i in jobUnlockList[item_id - jobUnlockOffset - 1]:
                    patch.write_token(APTokenTypes.WRITE, ffta2_data.jobRequirements[i-1].memory + JobRequirementOffsets.quest_requirement, struct.pack("<H", quest_flag))
                item_id = 0x00F6

            if item_id >= 0x01AF and item_id <= 0x0265:
                # Extra loot items
                amount = 10
            else:
                amount = 1

            item_and_reward = (amount << 0xA) | item_id
            patch.write_token(APTokenTypes.WRITE, location.address, struct.pack("<H", item_and_reward))


def set_required_items(ffta2_data: FFTA2Data, index: int, item_id, patch: FFTA2ProcedurePatch):
    patch.write_token(APTokenTypes.WRITE, ffta2_data.quests[index].memory + QuestOffsets.required_item1,
                      struct.pack("<H", item_id))
    patch.write_token(APTokenTypes.WRITE, ffta2_data.quests[index].memory + QuestOffsets.required_item_amount1,
                      struct.pack("<B", 1))
