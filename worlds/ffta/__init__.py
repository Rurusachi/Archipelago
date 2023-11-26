"""
Archipelago World definition for Final Fantasy Tactics Advance
"""

import os
from typing import ClassVar, Dict, Any
import settings
import sys
import logging

if "worlds._bizhawk" not in sys.modules:
    bh_apworld_path = os.path.join(os.path.dirname(
        sys.modules["worlds"].__file__), "_bizhawk.apworld")
    if not os.path.isfile(bh_apworld_path) and not os.path.isdir(os.path.splitext(bh_apworld_path)[0]):
        logging.warning(
            "Did not find _bizhawk.apworld required to play Final Fantasy Tactics Advance. Still able to generate.")
    else:
        # Unused, but required to register with BizHawkClient
        from .client import FFTAClient
else:
    # Unused, but required to register with BizHawkClient
    from .client import FFTAClient

from BaseClasses import ItemClassification, MultiWorld, Tutorial
from worlds.AutoWorld import WebWorld, World
from .data import get_random_job, randomized_jobs, randomized_judge, randomized_weapons, randomized_equip, JobID, location_ids, \
    judge_weapon, judge_equip, basic_weapon, basic_equip
from .regions import create_regions
from .rules import set_rules

from .options import option_definitions
from .items import (create_item_label_to_code_map, AllItems, item_table, FFTAItem, WeaponBlades,
                    WeaponSabers, WeaponKatanas, WeaponBows, WeaponGreatBows, WeaponRods, WeaponStaves, WeaponKnuckles,
                    WeaponMaces, WeaponInstruments, WeaponSouls, WeaponRapiers, WeaponGuns, WeaponKnives, ItemData,
                    EquipArmor, EquipRobes, EquipClothing, MissionUnlockItems, TotemaUnlockItems,
                    SoldierWeapons, PaladinWeapons, WarriorWeapons, DefenderWeapons, TemplarWeapons, AssassinWeapons,
                    DragoonWeapons)
from .locations import (create_location_label_to_id_map)
from .rom import FFTADeltaPatch, generate_output


class FFTASettings(settings.Group):
    class FFTARomFile(settings.UserFilePath):
        """File name of your Final Fantasy Tactics Advance ROM"""
        description = "Final Fantasy Tactics Advance ROM File"
        copy_to = "Final Fantasy Tactics Advance (USA).gba"
        md5s = [FFTADeltaPatch.hash]

    rom_file: FFTARomFile = FFTARomFile(FFTARomFile.copy_to)


class FFTAWebWorld(WebWorld):
    """
    Webhost info for Final Fantasy Tactics Advance
    """
    theme = "grass"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Final Fantasy Tactics Advance with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Spicynun"]
    )

    tutorials = [setup_en]


class FFTAWorld(World):
    """
    Final Fantasy Tactics Advance is a game
    """
    game = "Final Fantasy Tactics Advance"
    web = FFTAWebWorld()
    option_definitions = option_definitions
    topology_present = True

    settings_key = "ffta_settings"
    settings: ClassVar[FFTASettings]

    data_version = 0
    required_client_version = (0, 4, 3)

    item_name_to_id = create_item_label_to_code_map()
    location_name_to_id = create_location_label_to_id_map()

    def get_filler_item_name(self) -> str:
        return "Phoenix Down"

    def _get_ffta_data(self):
        return {
            'world_seed': self.multiworld.per_slot_randoms[self.player].getrandbits(32),
            'seed_name': self.multiworld.seed_name,
            'player_name': self.multiworld.get_player_name(self.player),
            'player_id': self.player,
            'race': self.multiworld.is_race,
        }

    def create_regions(self) -> None:
        create_regions(self, self.player)

    def create_items(self):

        required_items = []

        item_index = 0
        for i in range(0, self.multiworld.gate_num[self.player].value):
            required_items.append(MissionUnlockItems[item_index].itemName)

            # Add second item for the gate unlock
            if self.multiworld.gate_items[self.player].value == 1:
                required_items.append(MissionUnlockItems[item_index + 1].itemName)

            item_index = item_index + 2

        # Add totema unlock items to pool if option is selected
        if self.multiworld.final_unlock[self.player].value == 1:
            for i in range(0, len(TotemaUnlockItems)):
                required_items.append(TotemaUnlockItems[i].itemName)

        # Adding required items to the pool first
        for itemName in required_items:
            self.multiworld.itempool.append(self.create_item(itemName))

        # Count number of mission reward locations, account for totema goal
        gate_number = self.multiworld.gate_num[self.player].value
        if gate_number > 30 and self.multiworld.final_unlock[self.player].value == 1:
            gate_number = 30

        unfilled_locations = gate_number * 8 + 1

        # Add totema mission locations to unfilled location count
        if self.multiworld.final_unlock[self.player].value == 1:
            unfilled_locations = unfilled_locations + 10

        useful_items = []
        for item in AllItems:
            if item.progression == ItemClassification.useful:

                if item.itemID >= 0x521aac and self.multiworld.job_unlock_req[self.player].value != 3:
                    continue
                else:
                    useful_items += [item.itemName]

        # Shuffle the useful items to be added to the pool based on the locations remaining
        self.random.shuffle(useful_items)

        items_remaining = unfilled_locations - len(required_items)

        for i in range(items_remaining - 1):
            self.multiworld.itempool.append(self.create_item(useful_items[i]))

        #filler_spots = len(self.multiworld.get_filled_locations()) - len(self.multiworld.get_unfilled_locations())
        #for i in range(filler_spots):
        #    self.multiworld.itempool.append(self.create_filler())

    def set_rules(self) -> None:
        set_rules(self)

    def generate_basic(self) -> None:
        # Setting the victory item at the victory location
        victory_event = FFTAItem('Victory', ItemClassification.progression, None, self.player)

        if self.multiworld.final_mission[self.player].value == 0:
            self.multiworld.get_location("Royal Valley", self.player)\
                .place_locked_item(victory_event)

        elif self.multiworld.final_mission[self.player].value == 1:
            self.multiworld.get_location("Decision Time", self.player) \
                .place_locked_item(victory_event)

        self.multiworld.completion_condition[self.player] =\
            lambda state: state.has("Victory", self.player)

    @classmethod
    def stage_assert_generate(cls, multiworld: MultiWorld):
        if not os.path.exists(cls.settings.rom_file):
            raise FileNotFoundError(cls.settings.rom_file)

    def fill_slot_data(self) -> Dict[str, Any]:

        slot_data = {}

        options = [
            "final_mission",
            "job_unlock_req"
        ]
        for option_name in options:
            option = getattr(self.multiworld, option_name)[self.player]
            slot_data[option_name] = option.value

        return slot_data

    def create_item(self, name: str) -> "Item":
        item = item_table[name]
        # Maybe remove this later
        offset = 41234532
        return FFTAItem(item.itemName, item.progression, item.itemID + offset, self.player)

    def generate_output(self, output_directory: str) -> None:
        # Get rid of this later
        human = 0
        bangaa = 1
        mou = 2
        viera = 3
        moogle = 4
        monster = 5
        all = 6
        all_with_monster = 7

        def randomize_starting(random_choice: int):

            # Randomize job for Marche
            randomized_jobs.append(get_random_job(self.random, random_choice))

            if self.multiworld.starting_unit_equip[self.player].value == 0:
                basic_weapon.append(get_basic_weapon(randomized_jobs[0]))
                basic_equip.append(get_basic_equip(randomized_jobs[0]))

            randomized_weapons.append(get_valid_weapon(randomized_jobs[0]))
            randomized_equip.append(get_valid_equip(randomized_jobs[0]))

            # Randomize job for Montblanc
            randomized_jobs.append(get_random_job(self.random, random_choice))

            if self.multiworld.starting_unit_equip[self.player].value == 0:
                basic_weapon.append(get_basic_weapon(randomized_jobs[1]))
                basic_equip.append(get_basic_equip(randomized_jobs[1]))

            randomized_weapons.append(get_valid_weapon(randomized_jobs[1]))
            randomized_equip.append(get_valid_equip(randomized_jobs[1]))

            # Randomize job for third clan member
            randomized_jobs.append(get_random_job(self.random, random_choice))

            if self.multiworld.starting_unit_equip[self.player].value == 0:
                basic_weapon.append(get_basic_weapon(randomized_jobs[2]))
                basic_equip.append(get_basic_equip(randomized_jobs[2]))

            randomized_weapons.append(get_valid_weapon(randomized_jobs[2]))
            randomized_equip.append(get_valid_equip(randomized_jobs[2]))

            # Randomize job for fourth clan member
            randomized_jobs.append(get_random_job(self.random, random_choice))

            if self.multiworld.starting_unit_equip[self.player].value == 0:
                basic_weapon.append(get_basic_weapon(randomized_jobs[3]))
                basic_equip.append(get_basic_equip(randomized_jobs[3]))

            randomized_weapons.append(get_valid_weapon(randomized_jobs[3]))
            randomized_equip.append(get_valid_equip(randomized_jobs[3]))

            # Randomize job for fifth clan member
            randomized_jobs.append(get_random_job(self.random, random_choice))

            if self.multiworld.starting_unit_equip[self.player].value == 0:
                basic_weapon.append(get_basic_weapon(randomized_jobs[4]))
                basic_equip.append(get_basic_equip(randomized_jobs[4]))

            randomized_weapons.append(get_valid_weapon(randomized_jobs[4]))
            randomized_equip.append(get_valid_equip(randomized_jobs[4]))

            # Randomize job for sixth clan member
            randomized_jobs.append(get_random_job(self.random, random_choice))

            if self.multiworld.starting_unit_equip[self.player].value == 0:
                basic_weapon.append(get_basic_weapon(randomized_jobs[5]))
                basic_equip.append(get_basic_equip(randomized_jobs[5]))

            randomized_weapons.append(get_valid_weapon(randomized_jobs[5]))
            randomized_equip.append(get_valid_equip(randomized_jobs[5]))

        def get_valid_weapon(job: int):

            weapon: ItemData

            # Soldier
            if job == JobID.soldier:
                weapon = self.random.choice(SoldierWeapons)
                return weapon.itemID

            # Paladin
            elif job == JobID.paladin:
                weapon = self.random.choice(PaladinWeapons)
                return weapon.itemID

            # Fighter
            elif job == JobID.fighter:
                weapon = self.random.choice(WeaponBlades)
                return weapon.itemID

            # Thief
            elif job == JobID.thiefhum or job == JobID.thiefmog or job == JobID.juggler:
                weapon = self.random.choice(WeaponKnives)
                return weapon.itemID

            # Ninja and assassins
            elif job == JobID.ninja:
                weapon = self.random.choice(WeaponKatanas)
                return weapon.itemID

            # White mage
            elif job == JobID.whitemagehum or job == JobID.whitemagemou or job == JobID.whitemagevra or job == JobID.summoner:
                weapon = self.random.choice(WeaponStaves)
                return weapon.itemID

            # Rod users
            elif job == JobID.blackmagehum or job == JobID.illusionisthum or job == JobID.blackmagemou \
                    or job == JobID.timemagemou or job == JobID.illusionistmou or job == JobID.blackmagemog or job == JobID.timemagemog:
                weapon = self.random.choice(WeaponRods)
                return weapon.itemID

            # Blue mage
            elif job == JobID.bluemage:
                weapon = self.random.choice(WeaponSabers)
                return weapon.itemID

            # Archer
            elif job == JobID.archerhum or job == JobID.archervra:
                weapon = self.random.choice(WeaponBows)
                return weapon.itemID

            # Hunter or Snipers
            elif job == JobID.hunter or job == JobID.sniper:
                weapon = self.random.choice(WeaponGreatBows)
                return weapon.itemID

            # Warrior
            elif job == JobID.warrior:
                weapon = self.random.choice(WarriorWeapons)
                return weapon.itemID

            # Dragoon
            elif job == JobID.dragoon:
                weapon = self.random.choice(DragoonWeapons)
                return weapon.itemID

            # Defender
            elif job == JobID.defender:
                weapon = self.random.choice(DefenderWeapons)
                return weapon.itemID

            # Gladiator and Mog Knight
            elif job == JobID.gladiator or job == JobID.mogknight:
                weapon = self.random.choice(WeaponBlades)
                return weapon.itemID

            # White monk and gadgeteer
            elif job == JobID.whitemonk or job == JobID.gadgeteer:
                weapon = self.random.choice(WeaponKnuckles)
                return weapon.itemID

            # Bishop
            elif job == JobID.bishop:
                weapon = self.random.choice(WeaponStaves)
                return weapon.itemID

            # Templar
            elif job == JobID.templar:
                weapon = self.random.choice(TemplarWeapons)
                return weapon.itemID

            # Alchemist and sage
            elif job == JobID.alchemist or job == JobID.sage:
                weapon = self.random.choice(WeaponMaces)
                return weapon.itemID

            # Beasmaster or animist
            elif job == JobID.beastmaster or job == JobID.animist:
                weapon = self.random.choice(WeaponInstruments)
                return weapon.itemID

            # Morpher
            elif job == JobID.morpher:
                weapon = self.random.choice(WeaponSouls)
                return weapon.itemID

            # Fencer, red mage and Elementalist
            elif job == JobID.fencer or job == JobID.elementalist or job == JobID.redmage:
                weapon = self.random.choice(WeaponRapiers)
                return weapon.itemID

            # Assassin
            elif job == JobID.assassin:
                weapon = self.random.choice(AssassinWeapons)
                return weapon.itemID

            # Gunner
            elif job == JobID.gunner:
                weapon = self.random.choice(WeaponGuns)
                return weapon.itemID

            else:
                weapon = 0
                return weapon

        def get_basic_weapon(job: int):

            weapon: ItemData

            # Soldier
            if job == JobID.soldier:
                return SoldierWeapons[0].itemID

            # Paladin
            elif job == JobID.paladin:
                return PaladinWeapons[0].itemID

            # Fighter
            elif job == JobID.fighter:
                return WeaponBlades[0].itemID

            # Thief
            elif job == JobID.thiefhum or job == JobID.thiefmog or job == JobID.juggler:
                return WeaponKnives[0].itemID

            # Ninja
            elif job == JobID.ninja:
                return WeaponKatanas[0].itemID

            # White mage
            elif job == JobID.whitemagehum or job == JobID.whitemagemou or job == JobID.whitemagevra or job == JobID.summoner:
                return WeaponStaves[0].itemID

            # Rod users
            elif job == JobID.blackmagehum or job == JobID.illusionisthum or job == JobID.blackmagemou \
                    or job == JobID.timemagemou or job == JobID.illusionistmou or job == JobID.blackmagemog or job == JobID.timemagemog:
                return WeaponRods[0].itemID

            # Blue mage
            elif job == JobID.bluemage:
                return WeaponSabers[0].itemID

            # Archer
            elif job == JobID.archerhum or job == JobID.archervra:
                return WeaponBows[0].itemID

            # Hunter or Snipers
            elif job == JobID.hunter or job == JobID.sniper:
                return WeaponGreatBows[0].itemID

            # Warrior
            elif job == JobID.warrior:
                return WarriorWeapons[0].itemID

            # Dragoon
            elif job == JobID.dragoon:
                return DragoonWeapons[0].itemID

            # Defender
            elif job == JobID.defender:
                return DefenderWeapons[0].itemID

            # Gladiator and Mog Knight
            elif job == JobID.gladiator or job == JobID.mogknight:
                return WeaponBlades[0].itemID

            # White monk and gadgeteer
            elif job == JobID.whitemonk or job == JobID.gadgeteer:
                return WeaponKnuckles[0].itemID

            # Bishop
            elif job == JobID.bishop:
                return WeaponStaves[0].itemID

            # Templar
            elif job == JobID.templar:
                return TemplarWeapons[0].itemID

            # Alchemist and sage
            elif job == JobID.alchemist or job == JobID.sage:
                return WeaponMaces[0].itemID

            # Beasmaster or animist
            elif job == JobID.beastmaster or job == JobID.animist:
                return WeaponInstruments[0].itemID

            # Morpher
            elif job == JobID.morpher:
                return WeaponSouls[0].itemID

            # Fencer, red mage and Elementalist
            elif job == JobID.fencer or job == JobID.elementalist or job == JobID.redmage:
                return WeaponRapiers[0].itemID

            # Assassin
            elif job == JobID.assassin:
                return AssassinWeapons[0].itemID

            # Gunner
            elif job == JobID.gunner:
                return WeaponGuns[0].itemID

            else:
                weapon = 0
                return weapon

        def get_valid_equip(job: int):
            equip: ItemData

            armor_valid_jobs = [JobID.soldier, JobID.paladin, JobID.warrior, JobID.templar, JobID.dragoon,
                                JobID.defender, JobID.mogknight]

            robe_valid_jobs = [JobID.paladin, JobID.whitemagehum, JobID.whitemagevra, JobID.whitemagevra,
                               JobID.blackmagehum, JobID.blackmagemou, JobID.blackmagemog, JobID.illusionisthum,
                               JobID.illusionistmou, JobID.bluemage, JobID.defender,
                               JobID.bishop, JobID.templar, JobID.timemagemou, JobID.timemagemog, JobID.morpher,
                               JobID.sage, JobID.elementalist, JobID.redmage, JobID.summoner]

            for x in armor_valid_jobs:
                if job == x:
                    equip = self.random.choice(EquipArmor)
                    return equip.itemID

            for x in robe_valid_jobs:
                if job == x:
                    equip = self.random.choice(EquipRobes)
                    return equip.itemID

            if job < 0x2B:
                equip = self.random.choice(EquipClothing)
                return equip.itemID

            else:
                equip = 0
                return equip

        def get_basic_equip(job: int):
            equip: ItemData

            armor_valid_jobs = [JobID.soldier, JobID.paladin, JobID.warrior, JobID.templar, JobID.dragoon,
                                JobID.defender, JobID.mogknight]

            robe_valid_jobs = [JobID.paladin, JobID.whitemagehum, JobID.whitemagevra, JobID.whitemagevra,
                               JobID.blackmagehum, JobID.blackmagemou, JobID.blackmagemog, JobID.illusionisthum,
                               JobID.illusionistmou, JobID.bluemage, JobID.defender,
                               JobID.bishop, JobID.templar, JobID.timemagemou, JobID.timemagemog, JobID.morpher,
                               JobID.sage, JobID.elementalist, JobID.redmage, JobID.summoner]

            for x in armor_valid_jobs:
                if job == x:
                    return EquipArmor[0].itemID

            for x in robe_valid_jobs:
                if job == x:
                    return EquipRobes[0].itemID

            if job < 0x2B:
                return EquipClothing[0].itemID

            else:
                equip = 0
                return equip

        # Append randomized units even if randomization is turned off to allow for random enemies to work
        if self.multiworld.starting_units[self.player].value == 2 or \
           self.multiworld.starting_units[self.player].value == 0:
            randomize_starting(all)

        # Shuffle starting unit jobs within their race
        elif self.multiworld.starting_units[self.player].value == 1:
            randomized_jobs.append(get_random_job(self.random, human))

            if self.multiworld.starting_unit_equip[self.player].value == 0:
                basic_weapon.append(get_basic_weapon(randomized_jobs[0]))
                basic_equip.append(get_basic_equip(randomized_jobs[0]))

            randomized_weapons.append(get_valid_weapon(randomized_jobs[0]))
            randomized_equip.append(get_valid_equip(randomized_jobs[0]))

            # Randomize job for Montblanc
            randomized_jobs.append(get_random_job(self.random, moogle))

            if self.multiworld.starting_unit_equip[self.player].value == 0:
                basic_weapon.append(get_basic_weapon(randomized_jobs[1]))
                basic_equip.append(get_basic_equip(randomized_jobs[1]))

            randomized_weapons.append(get_valid_weapon(randomized_jobs[1]))
            randomized_equip.append(get_valid_equip(randomized_jobs[1]))

            # Randomize job for third clan member
            randomized_jobs.append(get_random_job(self.random, human))

            if self.multiworld.starting_unit_equip[self.player].value == 0:
                basic_weapon.append(get_basic_weapon(randomized_jobs[2]))
                basic_equip.append(get_basic_equip(randomized_jobs[2]))

            randomized_weapons.append(get_valid_weapon(randomized_jobs[2]))
            randomized_equip.append(get_valid_equip(randomized_jobs[2]))

            # Randomize job for fourth clan member
            randomized_jobs.append(get_random_job(self.random, bangaa))

            if self.multiworld.starting_unit_equip[self.player].value == 0:
                basic_weapon.append(get_basic_weapon(randomized_jobs[3]))
                basic_equip.append(get_basic_equip(randomized_jobs[3]))

            randomized_weapons.append(get_valid_weapon(randomized_jobs[3]))
            randomized_equip.append(get_valid_equip(randomized_jobs[3]))

            # Randomize job for fifth clan member
            randomized_jobs.append(get_random_job(self.random, mou))

            if self.multiworld.starting_unit_equip[self.player].value == 0:
                basic_weapon.append(get_basic_weapon(randomized_jobs[4]))
                basic_equip.append(get_basic_equip(randomized_jobs[4]))

            randomized_weapons.append(get_valid_weapon(randomized_jobs[4]))
            randomized_equip.append(get_valid_equip(randomized_jobs[4]))

            # Randomize job for sixth clan member
            randomized_jobs.append(get_random_job(self.random, viera))

            if self.multiworld.starting_unit_equip[self.player].value == 0:
                basic_weapon.append(get_basic_weapon(randomized_jobs[5]))
                basic_equip.append(get_basic_equip(randomized_jobs[5]))

            randomized_weapons.append(get_valid_weapon(randomized_jobs[5]))
            randomized_equip.append(get_valid_equip(randomized_jobs[5]))

        elif self.multiworld.starting_units[self.player].value == 3:
            randomize_starting(all_with_monster)

        if self.multiworld.randomize_enemies[self.player].value == 1:
            for index in range(6, 0xA46):
                randomized_jobs.append(get_random_job(self.random, all_with_monster))
                randomized_weapons.append(get_valid_weapon(randomized_jobs[index]))
                randomized_equip.append(get_valid_equip(randomized_jobs[index]))

        # Always randomize the judge encounters for now
        for index in range(0, 5):
            randomized_judge.append(get_random_job(self.random, all))
            judge_weapon.append(get_valid_weapon(randomized_judge[index]))
            judge_equip.append(get_valid_equip(randomized_judge[index]))

        # print(self.random_data.all_abilities)
        # self.random.shuffle(self.random_data.all_abilities)

        # Randomize location nodes on map
        self.random.shuffle(location_ids)
        generate_output(self.multiworld, self.player, output_directory)





