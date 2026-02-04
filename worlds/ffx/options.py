"""
Option definitions for Final Fantasy ¨X
"""
from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, Option, Range, Toggle, PerGameCommonOptions

class GoalRequirement(Choice):
    """
    Sets the requirement to start the final battles. Defeating Yu Yevon is always the goal.
    - None: No requirements.
    - Party Members: Requires unlocking a number of party members (not counting Aeons).
    - Party Members and Aeons: Requires unlocking a number of party members (including Aeons).
    - Pilgrimage: Complete all required temples, and defeat the boss in Zanarkand Ruins.
    - Nemesis: Requires defeating Nemesis in the Monster Arena. To enable this option Capture Sanity must be enabled, and Creation Rewards & Arena Bosses must be set to Original Creations
    """
    display_name = "Goal Requirement"
    default = 0
    option_none = 0
    option_party_members = 1
    option_pilgrimage = 2
    option_party_members_and_aeons = 3
    option_nemesis = 4


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


class MiniGames(Toggle):
    """
    Sets whether minigames are included or not. If off they will only have filler items.
    Minigames include;
    - Blitzball (World Champion & Jupiter Sigil)
    - Luca Story Blitzball win
    - Macalania Butterflies (Saturn Sigil)
    - Thunder Plains Lightning Dodging (including Venus Sigil)
    - Bikanel Cactuar Village (Mercury Sigil)
    - Calm Lands Chocobo Training (Dodger, Hyper Dodger, Catcher, Caladbolg & Sun Sigil)
    - Remiem Temple Chocobo Race (Cloudy Mirror)
    Default is off.
    """
    display_name = "Minigames"
    default = 0
    option_off = 0
    option_on = 1


class RecruitSanity(Toggle):
    """
    Sets whether Blitzball Free Agents are included or not. If off they will only have filler items.
    There are 24 Free Agents throughout Spira
    Default is off.
    """
    display_name = "Recruit Sanity"
    default = 0
    option_off = 0
    option_on = 1


class CaptureSanity(Toggle):
    """
    Sets whether Fiend Captures are included or not. If off they will only have filler items.
    A check is included for the first capture of each of the 102 unique capturable fiends
    Default is off.
    """
    display_name = "Capture Sanity"
    default = 0
    option_off = 0
    option_on = 1

    
class MonsterArenaAccess(Choice):
    """
    The Monster Arena will be accessible directly from the Airship menu, instead of via the Calm Lands.
    This option sets how the 'Region: Monster Arena' item will be placed in the multiworld.
    - Normal: The Monster Arena region item will be placed in the multiworld, and captures will come into logic per region once the arena is accessible
    - Early: The Monster Arena region item will be placed globally in sphere 1. Otherwise, the same as 'Normal'
    - Always: Start with the Monster Arena region item, and captures will be in logic immediately per region.
    Default is off.
    """
    display_name = "Monster Arena Access"
    default = 0
    option_normal = 0
    option_early = 1
    option_always = 2


class CreationRewards(Choice):
    """
    ** Requires Capture Sanity **
    Sets whether Monster Arena Creation Rewards are included or not. If off they will only have filler.
    These rewards can be gained from the Monster Arena after completing any Area or Species Conquest, or unlocking an Original Creation
    - Off: All arena rewards will be filler.
    - Area: Only Area Conquest rewards will be in logic. Other rewards will only have filler.
    - Species: Both Area & Species Conquest rewards will be in logic. Other rewards will only have filler.
    - Original: All rewards will be in logic. This can require up to 10 captures of every fiend.
    Default is off.
    """
    display_name = "Creation Rewards"
    default = 0
    option_off = 0
    option_area = 1
    option_species = 2
    option_original = 3


class MonsterArenaBosses(Choice):
    """
    ** Requires Capture Sanity **
    Sets whether Monster Arena boss locations are included or not. If off they will only have filler items.
    Monster Arena bosses include all Area & Species Conquests, as well as the Original Creations.
    - Off: All arena bosses will have filler.
    - Area: Area Conquest bosses will be in logic. Other arena bosses will have filler.
    - Species: Area & Species Conquest bosses will be in logic. Other arena bosses will have filler.
    - Original: All arena bosses will be in logic, up to & including Nemesis.
    Default is off.
    """
    display_name = "Arena Bosses"
    default = 0
    option_off = 0
    option_area = 1
    option_species = 2
    option_original = 3


class SuperBosses(Toggle):
    """
    Sets whether Super Boss locations are included or not. If off they will only have filler items.
    Super Bosses include Omega Weapon, the Dark Aeons & Penance.
    Default is off.
    """
    display_name = "Super Bosses"
    default = 0
    option_off = 0
    option_on = 1


class LogicDifficulty(Range):
    """
    Sets how strict the logic is for region access. Higher is harder / less restrictive.
    Default is 3.
    """
    display_name = "Logic Difficulty"
    default = 3
    range_start = 1
    range_end = 10


class EarlyPartyMembers(Range):
    """
    Sets how many additional party members will be placed globally in sphere 1.
    This will allow players to have access to more characters earlier.
    This value does **NOT** include the starting character
    Default is 0.
    """
    display_name = "Early Party Members"
    default = 0
    range_start = 0
    range_end = 7


class AlwaysSensor(Toggle):
    """
    Sets whether to always have the Sensor ability active, regardless of equipped weapon abilities
    Default is off.
    """
    display_name = "Always Sensor"
    default = 0
    option_off = 0
    option_on = 1


class AlwaysCapture(Toggle):
    """
    Sets whether to always have the Capture ability active, regardless of equipped weapon abilities
    Default is off.
    """
    display_name = "Always Capture"
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


class SphereGridRandomization(Choice):
    """
    Sets whether the Sphere Grid is randomized.
    Default is off.
    """
    display_name = "Sphere Grid Randomization"
    default = 0
    option_off = 0


@dataclass
class FFXOptions(PerGameCommonOptions):
    goal_requirement: GoalRequirement
    required_party_members: RequiredPartyMembers
    required_primers: RequiredPrimers
    ap_multiplier: APMultiplier
    mini_games: MiniGames
    recruit_sanity: RecruitSanity
    capture_sanity: CaptureSanity
    arena_access: MonsterArenaAccess
    creation_rewards: CreationRewards
    arena_bosses: MonsterArenaBosses
    super_bosses: SuperBosses
    trap_percentage: TrapPercentage
    logic_difficulty: LogicDifficulty
    early_party_members: EarlyPartyMembers
    always_sensor: AlwaysSensor
    always_capture: AlwaysCapture
    sphere_grid_randomization: SphereGridRandomization
