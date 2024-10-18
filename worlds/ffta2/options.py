"""
Option definitions for Final Fantasy Tactics A2
"""
from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, Option, OptionSet, Range, Toggle, FreeText, DeathLink, PerGameCommonOptions, NamedRange, OptionList
from .data import recruitableUnitNames


class GateBalancing(Range):
    """
    Randomizes quests with weights based on gate number and quest rank.
    Low rank quests have higher weights in early gates, and high rank quests have higher weights in late gates.
    A value of 0 means no balancing. Higher values are more heavily weighted.
    """
    display_name = "Gate balancing"
    default = 5
    range_start = 0
    range_end = 20


class GateNumber(Range):
    """
    Sets the number of quest gates. Each gate contains four quests each.
    The Two Grimoires will always be the last quest.
    Amount of locations per gate depends on number of item rewards
    """
    display_name = "Number of quest gates"
    default = 6
    range_start = 1
    range_end = 19


class GatePaths(Range):
    """
    Sets the number of branching gate paths.
    How many must be completed depends on the paths_required option.
    Useful for higher mission gate counts.
    """
    display_name = "Number of gate paths"
    default = 1
    range_start = 1
    range_end = 3


class GatePathsRequired(Range):
    """
    Sets the number of gate paths that must be completed to unlock the final quest.
    """
    display_name = "Number of gate paths required"
    default = 1
    range_start = 1
    range_end = 3


class FinalQuests(Choice):
    """
    Sets the final questline. "The Two Grimoires" leads directly into "From The Rift".

    The Ritual: You must complete "The Ritual", "The Two Grimoires", and "From the Rift" to win.
    The Two Grimoires: You must complete "The Two Grimoires", and "From the Rift" to win.
    """
    display_name = "Final quest"
    default = 0
    option_the_ritual = 0
    option_the_two_grimoires = 1


class QuestRewards(Range):
    """
    Sets the number of locations per quest.
    """
    display_name = "Number of quest rewards"
    default = 3
    range_start = 1
    range_end = 3


class JobUnlockRequirements(Choice):
    """
    Sets job requirements.

    Vanilla: Jobs require mastered abilities and certain quests (not recommended).
    No Quests: Jobs require mastered abilities, but not quests.
    All Unlocked: Jobs have no requirements.
    All Locked: All jobs are locked. Units can only be their starting job.
    Job Items: All jobs start locked. Job unlocks are checks.
    """
    display_name = "Job unlocks"
    default = 1
    option_vanilla = 0
    option_no_quests = 1
    option_all_unlocked = 2
    option_all_locked = 3
    option_job_items = 4


class QuestAP(Range):
    """
    Sets the amount of AP gained from quests.
    The amount is mulitplied by 10. Default is 5 = 50 AP.
    """
    display_name = "AP gained from quests"
    default = 5
    range_start = 1
    range_end = 50


class QuestEXP(Range):
    """
    Sets the base amount of exp gained from quests.
    Default is 60 exp.
    """
    display_name = "Base exp gained from quests"
    default = 60
    range_start = 0
    range_end = 255


class QuestGil(NamedRange):
    """
    Sets the amount of gil gained from quests.
    Special values:
        Vanilla: Default value. Same as the vanilla game
    """
    display_name = "Base exp gained from quests"
    default = -1
    range_start = 0
    range_end = 65535
    special_range_names = {
        "vanilla": -1
        }


class DispatchQuests(Choice):
    """
    Toggle dispatch quests on or off.

    Vanilla: Dispatch quests are the same as vanilla.
    No Dispatch: Dispatch quests are turned turned into normal quests.
    """
    display_name = "Dispatch quests"
    default = 1
    option_vanilla = 0
    option_no_dispatch = 1


class RandomizeStartingUnitRaces(Toggle):
    """
    Randomizes starting unit races.
    """


class RandomizeStartingUnitJobs(Toggle):
    """
    Randomizes starting unit jobs.
    """


class RandomizeStartingUnitEquipment(Toggle):
    """
    Randomizes the starting unit equipment.
    """


class StartingUnits(OptionSet):
    """
    Sets the starting units.
    If starting unit randomization is enabled it will be applied to these units.

    Format:
        ["{Name}", "{Name}", ..., "{Name}"]
        {Name} can be a special unit, or a Race and Job.
        Special units are: Adelle, Cid, Hurdy, Vaan, Penelo, Al-Cid, Montblanc, Frimelda
        Race and Job examples: Hume Archer, Nu Mou Black Mage
        No duplicates allowed.
    """
    display_name = "Dispatch quests"
    default = ["Nu Mou Black Mage",
               "Viera White Mage",
               "Bangaa Warrior",
               "Hume Archer",
               "Moogle Thief",
               ]
    valid_keys = recruitableUnitNames


@dataclass
class FFTA2Options(PerGameCommonOptions):
    gate_balancing: GateBalancing
    gate_num: GateNumber
    path_num: GatePaths
    paths_required: GatePathsRequired
    final_quests: FinalQuests
    reward_num: QuestRewards
    quest_ap: QuestAP
    quest_exp: QuestEXP
    quest_gil: QuestGil
    dispatch_quests: DispatchQuests
    job_unlock_req: JobUnlockRequirements
    #randomize_starting_races: RandomizeStartingUnitRaces
    #randomize_starting_jobs: RandomizeStartingUnitJobs
    #randomize_starting_equipment: RandomizeStartingUnitEquipment
    starting_units: StartingUnits
