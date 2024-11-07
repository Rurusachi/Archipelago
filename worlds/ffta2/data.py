from typing import NamedTuple, List, Tuple
from .quests import (QuestData, questData)
from .bazaar import (BazaarRecipe, bazaarRecipes)
from .items import items_by_id

recruitableUnitNames = [
    "Luso",
    "Nu Mou Black Mage",
    "Viera White Mage",
    "Bangaa Warrior",
    "Hume Archer",
    "Moogle Thief",
    "Adelle",
    "Cid",
    "Hurdy",
    "Vaan",
    "Penelo",
    "Al-Cid",
    "Montblanc",
    "Frimelda",
    "Hume Soldier",
    "Hume Thief",
    "Hume White Mage",
    "Hume Black Mage",
    "Hume Archer",
    "Hume Paladin",
    "Hume Fighter",
    "Hume Parivir",
    "Hume Ninja",
    "Hume Illusionist",
    "Hume Blue Mage",
    "Hume Hunter",
    "Hume Seer",
    "Bangaa Warrior",
    "Bangaa White Monk",
    "Bangaa Dragoon",
    "Bangaa Defender",
    "Bangaa Gladiator",
    "Bangaa Master Monk",
    "Bangaa Bishop",
    "Bangaa Templar",
    "Bangaa Cannoneer",
    "Bangaa Trickster",
    "Nu Mou White Mage",
    "Nu Mou Black Mage",
    "Nu Mou Beastmaster",
    "Nu Mou Time Mage",
    "Nu Mou Illusionist",
    "Nu Mou Alchemist",
    "Nu Mou Arcanist",
    "Nu Mou Sage",
    "Nu Mou Scholar",
    "Nu Mou Keeper",
    "Viera Fencer",
    "Viera White Mage",
    "Viera Green Mage",
    "Viera Archer",
    "Viera Elementalist",
    "Viera Red Mage",
    "Viera Spellblade",
    "Viera Summoner",
    "Viera Assassin",
    "Viera Sniper",
    "Moogle Animist",
    "Moogle Thief",
    "Moogle Black Mage",
    "Moogle Moogle Knight",
    "Moogle Fusilier",
    "Moogle Juggler",
    "Moogle Tinker",
    "Moogle Time Mage",
    "Moogle Chocobo Knight",
    "Moogle Flintlock",
    "Seeq Berserker",
    "Seeq Ranger",
    "Seeq Lanista",
    "Seeq Viking",
    "Gria Hunter",
    "Gria Raptor",
    "Gria Ravager",
    "Gria Geomancer",
]

specialUnitNames: List[str] = [
    "Luso",
    "Adelle",
    "Cid",
    "Hurdy",
    "Vaan",
    "Penelo",
    "Al-Cid",
    "Montblanc",
    "Frimelda",
]

formationLengths = [
    4, 4, 6, 7, 6, 5, 6, 5, 5, 6, 7, 6, 6, 5, 6, 7, 6, 6, 6, 6,
    6, 5, 6, 3, 1, 7, 6, 6, 6, 6, 7, 3, 6, 6, 6, 6, 6, 5, 5, 9,
    5, 4, 11, 6, 10, 5, 6, 8, 6, 5, 7, 4, 5, 5, 5, 5, 6, 6, 6, 6,
    6, 6, 6, 5, 5, 5, 5, 6, 6, 7, 6, 4, 5, 6, 5, 5, 6, 6, 4, 5,
    3, 5, 5, 5, 4, 4, 4, 6, 6, 6, 1, 1, 1, 6, 6, 4, 5, 4, 6, 7,
    6, 7, 4, 6, 4, 6, 6, 6, 4, 6, 6, 4, 6, 3, 4, 6, 6, 6, 16, 9, 
    9, 9, 13, 7, 7, 4, 5, 11, 6, 6, 6, 8, 11, 6, 2, 6, 6, 5, 5, 5,
    5, 2, 8, 2, 2, 2, 3, 2, 2, 4, 4, 2, 8, 3, 4, 7, 1, 5, 4, 4,
    5, 5, 7, 6, 5, 5, 6, 5, 6, 7, 19, 6, 5, 5, 7, 9, 20, 2, 6, 8,
    5, 5, 6, 7, 7, 2, 7, 6, 6, 2, 7, 6, 6, 4, 20, 6, 7, 10, 8, 8,
    7, 6, 3, 6, 10, 6, 6, 5, 11, 12, 12, 12, 3, 7, 6, 4, 1, 1, 1, 1,
    1, 5, 1, 7, 4, 5, 5, 8, 4, 4, 4, 7, 5, 8, 7, 4, 6, 6, 9, 9,
    6, 1, 6, 3, 6, 4, 6, 3, 6, 1, 1, 1, 1, 3, 18, 17, 17, 17, 17, 17,
    17, 17, 17, 17, 17, 17, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
    6, 6, 7, 6, 4, 1, 2, 6, 6, 6, 6, 7, 6, 16, 5, 6, 6, 6, 4, 5,
    6, 6, 6, 6, 6, 6, 9, 6, 6, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6,
    6, 6, 6, 6, 6, 6, 6, 4, 6, 8, 3, 6, 7, 5, 5, 7, 6, 6, 9, 6,
    7, 8, 7, 18, 1, 7, 1, 4, 8, 6, 8, 1, 1, 6, 6, 3, 1, 5, 6, 7,
    8, 9, 10, 1, 12, 6, 3, 3, 6, 20, 25, 31, 31, 31, 10, 3, 6, 6, 6, 6,
    6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 11, 11, 5, 12, 8, 9, 7,
]

jobUnlockList = [
    [0x1],
    [0x2, 0x2d],
    [0x3, 0x18, 0x23],
    [0x4, 0x19, 0x2e],
    [0x5, 0x25],
    [0x6],
    [0x7],
    [0x8],
    [0x9],
    [0xa, 0x1c],
    [0xb],
    [0xc, 0x3a],
    [0xd],
    [0xe],
    [0xf],
    [0x10],
    [0x11],
    [0x12],
    [0x13],
    [0x14],
    [0x15],
    [0x16],
    [0x17],
    [0x1a],
    [0x1b, 0x33],
    [0x1d],
    [0x1e],
    [0x1f],
    [0x20],
    [0x21],
    [0x22],
    [0x24],
    [0x26],
    [0x27],
    [0x28],
    [0x29],
    [0x2a],
    [0x2b],
    [0x2c],
    [0x2f],
    [0x30],
    [0x31],
    [0x32],
    [0x34],
    [0x35],
    [0x36],
    [0x37],
    [0x38],
    [0x39],
    [0x3b],
    [0x3c],
    [0x3d],
]


class FormationOffsets:
    law: int = 0x0
    units: int = 0x1
    party_limit: int = 0x3


class UnitOffsets:
    character: int = 0x0
    job: int = 0x1
    min_level: int = 0x2
    max_level: int = 0x3
    name: int = 0x4
    ability1: int = 0xe
    ability2: int = 0x10
    ability3: int = 0x12
    ability4: int = 0x14
    ability5: int = 0x16
    ability6: int = 0x18
    reaction: int = 0x24
    passive: int = 0x26
    equip1: int = 0x28
    equip2: int = 0x2a
    equip3: int = 0x2c
    equip4: int = 0x2e
    equip5: int = 0x30
    loot_lvl1: int = 0x34
    loot_lvl2: int = 0x35
    loot_lvl3: int = 0x36
    loot_lvl4: int = 0x37
    loot_consumables: int = 0x38
    loot_gil: int = 0x39
    faction: int = 0x3a


class QuestOffsets:
    type: int = 0x0
    id: int = 0x1  # Id for Multi-part quests maybe? Every multi-part quest has a unique id here (e.g. Camoa cup is 0x13)
    rank: int = 0x2
    region: int = 0x3
    story_requirement: int = 0x4
    flag_requirement: int = 0x6
    unknown_requirement: int = 0x8
    month: int = 0xb
    available_period: int = 0xd  # Maybe?
    days: int = 0x10
    repeat_failed_days: int = 0x11
    repeat_completed_days: int = 0x12  # FE = never?, FF = Instant?
    fee: int = 0x13  # multiplied by 100
    required_item1: int = 0x14
    required_item_amount1: int = 0x16
    required_item2: int = 0x18
    required_item_amount2: int = 0x1a
    negotiation: int = 0x1c
    aptitude: int = 0x1d
    teamwork: int = 0x1e
    adaptability: int = 0x1f
    is_dispatch: int = 0x2a
    recommended_dispatch: int = 0x2f
    location: int = 0x21
    gil_reward: int = 0x4c
    ap: int = 0x4e  # multiplied by 10?
    cp: int = 0x4f
    reward_1: int = 0x50
    reward_2: int = 0x52
    reward_3: int = 0x54
    reward_4: int = 0x56
    exp: int = 0x5e


class BazaarCategoryOffsets:
    item1: int = 0x00
    grade1: int = 0x02
    item2: int = 0x04
    grade2: int = 0x06
    item3: int = 0x08
    grade3: int = 0x0a
    item4: int = 0x0c
    grade4: int = 0x0e
    item5: int = 0x10
    grade5: int = 0x12
    item6: int = 0x14
    grade6: int = 0x16
    item7: int = 0x18
    grade7: int = 0x1a
    item8: int = 0x1c
    grade8: int = 0x1e
    item9: int = 0x20
    grade9: int = 0x22


class BazaarRecipeOffsets:
    loot1: int = 0x0
    loot2: int = 0x2
    loot3: int = 0x4


class JobRequirementOffsets:
    quest_requirement: int = 0x0
    id: int = 0x2
    job_id: int = 0x3
    unique1: int = 0x4
    unique2: int = 0x5
    job1: int = 0x6
    skills1: int = 0x7
    job2: int = 0x8
    skills2: int = 0x9
    job3: int = 0xa
    skills3: int = 0xb


class RecruitableUnitOffsets:
    character: int = 0x0
    starting_job: int = 0x1
    min_level: int = 0x2
    max_level: int = 0x3
    dialogue_role: int = 0x4
    ability1: int = 0xe
    ability2: int = 0x10
    ability3: int = 0x12
    ability4: int = 0x14
    ability5: int = 0x16
    ability6: int = 0x18
    reaction_ability: int = 0x24
    passive_ability: int = 0x26
    equip1: int = 0x28
    equip2: int = 0x2a
    equip3: int = 0x2c
    equip4: int = 0x2e
    equip5: int = 0x30
    starter: int = 0x3a


class EquipmentDataOffsets:
    weapon_type: int = 0x0
    name: int = 0x2
    element: int = 0x4
    range: int = 0x5
    equip_location: int = 0x6
    buy: int = 0xe
    sell: int = 0x10
    bonus_effect: int = 0x12
    attack: int = 0x13
    defense: int = 0x14
    magick: int = 0x15
    resistance: int = 0x16
    speed: int = 0x17
    evasion: int = 0x18
    move: int = 0x19
    jump: int = 0x1a
    job1: int = 0x1b
    job2: int = 0x1c
    job3: int = 0x1d
    ability1: int = 0x1e
    ability2: int = 0x20
    ability3: int = 0x22
    properties: int = 0x24


class EquipmentDataPropertyFlags:
    bladed: int = 0x0
    piercing: int = 0x1
    blunt: int = 0x2
    ranged: int = 0x3
    female: int = 0x4
    limited_stock: int = 0x5
    starts_in_shop: int = 0x6


class MemorySpace(NamedTuple):
    offset: int
    byteSize: int
    length: int


class Quests(MemorySpace):
    offset = 0x053ecf48
    byteSize = 0x64
    length = 0x1ff


class Formations(MemorySpace):
    offset = 0x0512b51c
    byteSize = 0x44
    length = 0x18f
    unitSize = 0x3c


class BazaarCategories(MemorySpace):
    offset = 0x05401BB0  # Skipping an empty slot
    byteSize = 0x2c
    length = 0x66


class BazaarRecipes(MemorySpace):
    offset = 0x05402DC0  # Skipping an empty slot
    byteSize = 0x8
    length = 0x19b


class JobRequirements(MemorySpace):
    offset = 0x53FFEAC  # Skipping an empty slot
    byteSize = 0xc
    length = 64


class RecruitableUnits(MemorySpace):
    offset = 0x0512A388
    byteSize = 0x3c
    length = 0x4b


class EquipmentData(MemorySpace):
    offset = 0x053FB770  # Skipping an empty slot
    byteSize = 0x28
    length = 0x19b


class FFTA2Object:
    memory: int = 0
    name: str = ""

    def __init__(self, memory, name):
        self.memory = memory
        self.name = name


class FFTA2Quest(FFTA2Object):
    battle: int = 0
    region: int = 0
    rank: int = 0

    def __init__(self, memory, data: QuestData):
        self.memory = memory
        self.name = data.name
        self.battle = data.battle
        self.region = data.region
        self.rank = data.rank


class FFTA2Formation(FFTA2Object):
    units: int = 0

    def __init__(self, memory, units):
        self.memory = memory
        self.units = units


class FFTA2BazaarCategory(FFTA2Object):

    def __init__(self, memory, name):
        self.memory = memory
        self.name = name


class FFTA2BazaarRecipe(FFTA2Object):
    item: int
    inVanilla: bool = False

    def __init__(self, memory, name, item, inVanilla):
        self.memory = memory
        self.name = name
        self.item = item
        self.inVanilla = inVanilla


class FFTA2JobRequirement(FFTA2Object):

    def __init__(self, memory, name):
        self.memory = memory
        self.name = name


class FFTA2RecruitableUnit(FFTA2Object):

    def __init__(self, memory, name):
        self.memory = memory
        self.name = name


class FFTA2EquipmentData(FFTA2Object):

    def __init__(self, memory, name):
        self.memory = memory
        self.name = name


class FFTA2Data:
    quests: List[FFTA2Quest]
    formations: List[FFTA2Formation]
    bazaarCategories: List[FFTA2BazaarCategory]
    bazaarRecipes: List[FFTA2BazaarRecipe]
    jobRequirements: List[FFTA2JobRequirement]
    recruitableUnits: List[FFTA2RecruitableUnit]
    equipmentData: List[FFTA2EquipmentData]

    def __init__(self):
        self.quests = self.initializeQuests()
        self.formations = self.initializeFormations()
        self.bazaarCategories = self.initializeBazaarCategories()
        self.bazaarRecipes = self.initializeBazaarRecipes()
        self.jobRequirements = self.initializeJobRequirements()
        self.recruitableUnits = self.initializeRecruitableUnits()
        self.equipmentData = self.initializeEquipmentData()

    def initializeQuests(self) -> List[FFTA2Quest]:
        quests: List[FFTA2Quest] = []
        for n in range(Quests.length):
            memory = Quests.offset + Quests.byteSize * n

            new_item = FFTA2Quest(memory, questData[n])
            quests.append(new_item)

        return quests

    def initializeFormations(self) -> List[FFTA2Formation]:
        formations: List[FFTA2Formation] = []
        memory = Formations.offset
        for n in range(Formations.length):
            new_item = FFTA2Formation(memory, formationLengths[n])
            formations.append(new_item)

            memory += Formations.byteSize + Formations.unitSize * formationLengths[n]

        return formations

    def initializeBazaarCategories(self) -> List[FFTA2BazaarCategory]:
        categories: List[FFTA2BazaarCategory] = []
        for n in range(BazaarCategories.length):
            memory = BazaarCategories.offset + BazaarCategories.byteSize * n

            new_item = FFTA2BazaarCategory(memory, "")
            categories.append(new_item)

        return categories

    def initializeBazaarRecipes(self) -> List[FFTA2BazaarRecipe]:
        recipes: List[FFTA2BazaarRecipe] = []
        for n in range(BazaarRecipes.length):
            memory = BazaarRecipes.offset + BazaarRecipes.byteSize * n

            recipe = bazaarRecipes[n+1]

            new_item = FFTA2BazaarRecipe(memory, recipe.item, n+1, recipe.loot1 != " ")
            recipes.append(new_item)

        return recipes

    def initializeJobRequirements(self) -> List[FFTA2JobRequirement]:
        recipes: List[FFTA2JobRequirement] = []
        for n in range(JobRequirements.length):
            memory = JobRequirements.offset + JobRequirements.byteSize * n

            new_item = FFTA2JobRequirement(memory, "")
            recipes.append(new_item)

        return recipes

    def initializeRecruitableUnits(self) -> List[FFTA2RecruitableUnit]:
        units: List[FFTA2RecruitableUnit] = []
        for n in range(RecruitableUnits.length):
            memory = RecruitableUnits.offset + RecruitableUnits.byteSize * n

            new_item = FFTA2RecruitableUnit(memory, recruitableUnitNames[n])
            units.append(new_item)

        return units

    def initializeEquipmentData(self) -> List[FFTA2EquipmentData]:
        items: List[FFTA2EquipmentData] = []
        for n in range(EquipmentData.length):
            memory = EquipmentData.offset + EquipmentData.byteSize * n

            name = items_by_id.get(n+1).itemName if items_by_id.get(n+1) is not None else "-"
            new_item = FFTA2EquipmentData(memory, name)
            items.append(new_item)

        return items


ffta2_data: FFTA2Data = FFTA2Data()


class MemoryAddresses:
    all_flags: int = 0x0212d734
    region_flags: int = 0x0212d73e
    location_flags: int = 0x0212d741
    job_flags: int = 0x212D784
    quest_flags: int = 0x212D790
    shop_flags: int = 0x0212d6c8
    received_items: int = 0x0212d753
    custom_flags: int = received_items+2
    event_var: int = 0x021c4868
    inventory: int = 0x0212ccdc


class FlagOffsets:
    Rumor = (0x30, 3)
    Notice = (0x40, 3)
    Job = (0x50, 4)
    JobItems = (MemoryAddresses.custom_flags - MemoryAddresses.all_flags, 1)  # Custom job flags
    FinalQuest = (MemoryAddresses.custom_flags - MemoryAddresses.all_flags, 0)  # Custom job flags
    Quest = (0x5C, 0)


def get_flag(id: int, flag_offset: Tuple[int, int]) -> Tuple[int, int, int]:
    '''
    Returns (byte_index, bit_index, flag)
    where flag is the combined byte and bit index (bits 0-2: bit_index, bits 3-10: byte_index)
    '''
    id += flag_offset[1]
    byte_index = (id // 8) + flag_offset[0]
    bit_index = id % 8
    quest_flag = (byte_index << 3) | bit_index
    return (byte_index, bit_index, quest_flag)
