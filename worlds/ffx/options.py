"""
Option definitions for Final Fantasy ¨X
"""
from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, Option, Range, Toggle, PerGameCommonOptions

class GoalRequirement(Choice):
    """
    Sets the requirement to start the final battles. Defeating Yu Yevon is always the goal.
    None: No requirements.
    Party Members: Requires unlocking a number of party members (not counting Aeons).
    Party Members and Aeons: Requires unlocking a number of party members (including Aeons).
    Pilgrimage: Complete all required temples, and defeat the boss in Zanarkand Ruins.
    """
    display_name = "Goal Requirement"
    default = 0
    option_none = 0
    option_party_members = 1
    option_pilgrimage = 2
    option_party_members_and_aeons = 3


class RequiredPartyMembers(Range):
    """
    Sets how many party members are required if goal_requirement is set to party_members or party_members_and_aeons.
    Default is 7. Max is 8 for party_members, 16 for party_members_and_aeons.
    """
    display_name = "Required Party Members"
    default = 7
    range_start = 1
    range_end = 16


class RequiredPrimers(Range):
    """
    Set how many Al Bhed Primers are required to allow access to the goal.
    This is in addition to the regular goal_requirement, meaning that for example, both Party Members & Primers may be required.
    """
    display_name = "Required Al Bhed Primers"
    default = 0
    range_start = 0
    range_end = 26


class APMultiplier(Range):
    """
    Sets the AP multiplier.
    Default is 2.
    """
    display_name = "AP Multiplier"
    default = 2
    range_start = 1
    range_end = 10


class SphereGridRandomization(Choice):
    """
    Sets whether the Sphere Grid is randomized.
    Default is off.
    """
    display_name = "Sphere Grid Randomization"
    default = 0
    option_off = 0


class SuperBosses(Toggle):
    """
    Sets whether super boss locations are included or not. If off they will only have filler items.
    Default is off.
    """
    display_name = "Super Bosses"
    default = 0
    option_off = 0
    option_on = 1


class MiniGames(Toggle):
    """
    Sets whether minigames (blitzball, lightning dodging, etc.) are included or not. If off they will only have filler items.
    Default is off.
    """
    display_name = "Minigames"
    default = 0
    option_off = 0
    option_on = 1

class RecruitSanity(Toggle):
    """
    Sets whether Blitzball Free Agents are included or not. If off they will only have filler items.
    Default is off.
    """
    display_name = "Recruit Sanity"
    default = 0
    option_off = 0
    option_on = 1


class TrapPercentage(Range):
    """
    Sets the percentage of non-progression items that will be traps.
    Default is 0.
    """
    display_name = "Traps Enabled"
    default = 0
    range_start = 0
    range_end = 100


class LogicDifficulty(Range):
    """
    Sets how strict the logic is for region access. Higher is harder / less restrictive.
    Default is 3.
    """
    display_name = "Logic Difficulty"
    default = 3
    range_start = 1
    range_end = 10

@dataclass
class FFXOptions(PerGameCommonOptions):
    goal_requirement: GoalRequirement
    required_party_members: RequiredPartyMembers
    required_primers: RequiredPrimers
    ap_multiplier: APMultiplier
    sphere_grid_randomization: SphereGridRandomization
    super_bosses: SuperBosses
    mini_games: MiniGames
    recruit_sanity: RecruitSanity
    trap_percentage: TrapPercentage
    logic_difficulty: LogicDifficulty
