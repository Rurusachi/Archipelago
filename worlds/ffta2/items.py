from typing import Dict
import typing
from BaseClasses import Item, ItemClassification


class ItemData(typing.NamedTuple):
    itemName: str
    progression: ItemClassification
    itemID: int = 0x00
    player: int = 0


class FFTA2Item(Item):
    itemName: str
    progression: ItemClassification
    itemID: int = 0x00
    player: int = 0
    game: str = "Final Fantasy Tactics A2"


EquipKnives: typing.List[ItemData] = [
    ItemData("Jackknife", ItemClassification.useful, 0x0001),
    ItemData("Kris", ItemClassification.useful, 0x0002),
    ItemData("Khukuri", ItemClassification.useful, 0x0003),
    ItemData("Kard", ItemClassification.useful, 0x0004),
    ItemData("Scramasax", ItemClassification.useful, 0x0005),
    ItemData("Rondel", ItemClassification.useful, 0x0006),
    ItemData("Jambiya", ItemClassification.useful, 0x0007),
    ItemData("Swordbreaker", ItemClassification.useful, 0x0008),
    ItemData("Orichalcum Dirk", ItemClassification.useful, 0x0009),
    ItemData("Cinquedea", ItemClassification.useful, 0x000A),
    ItemData("Zwillblade", ItemClassification.useful, 0x000B),
    ItemData("Tiptaptwo", ItemClassification.useful, 0x000C),
    ItemData("Tonberrian", ItemClassification.useful, 0x000D),
    ItemData("Dagger", ItemClassification.useful, 0x000E),
]

EquipSwords: typing.List[ItemData] = [
    ItemData("Broadsword", ItemClassification.useful, 0x000F),
    ItemData("Silver Sword", ItemClassification.useful, 0x0010),
    ItemData("Buster Sword", ItemClassification.useful, 0x0011),
    ItemData("Burglar Sword", ItemClassification.useful, 0x0012),
    ItemData("Gale Sword", ItemClassification.useful, 0x0013),
    ItemData("Blood Sword", ItemClassification.useful, 0x0014),
    ItemData("Restorer", ItemClassification.useful, 0x0015),
    ItemData("Vitanova", ItemClassification.useful, 0x0016),
    ItemData("Onion Sword", ItemClassification.useful, 0x0017),
    ItemData("Chirijiraden", ItemClassification.useful, 0x0018),
    ItemData("Shortsword", ItemClassification.useful, 0x0019),
]

EquipBlades: typing.List[ItemData] = [
    ItemData("Sweep Blade", ItemClassification.useful, 0x001A),
    ItemData("Shadow Blade", ItemClassification.useful, 0x001B),
    ItemData("Sun Blade", ItemClassification.useful, 0x001C),
    ItemData("Atomos Blade", ItemClassification.useful, 0x001D),
    ItemData("Flametongue", ItemClassification.useful, 0x001E),
    ItemData("Air Blade", ItemClassification.useful, 0x001F),
    ItemData("Icebrand", ItemClassification.useful, 0x0020),
    ItemData("Kwigon Blade", ItemClassification.useful, 0x0021),
    ItemData("Ogun Blade", ItemClassification.useful, 0x0022),
    ItemData("Pearl Blade", ItemClassification.useful, 0x0023),
    ItemData("Paraiba Blade", ItemClassification.useful, 0x0024),
    ItemData("Venus Blade", ItemClassification.useful, 0x0025),
    ItemData("Materia Blade", ItemClassification.useful, 0x0026),
    ItemData("Ebon Blade", ItemClassification.useful, 0x0027),
    ItemData("Adamant Blade", ItemClassification.useful, 0x0028),
    ItemData("Ayvuir Red", ItemClassification.useful, 0x0029),
    ItemData("Ayvuir Blue", ItemClassification.useful, 0x002A),
    ItemData("Iron Blade", ItemClassification.useful, 0x002B),
]

EquipSabers: typing.List[ItemData] = [
    ItemData("Blue Saber", ItemClassification.useful, 0x002C),
    ItemData("Shamshir", ItemClassification.useful, 0x002D),
    ItemData("Aqua Saber", ItemClassification.useful, 0x002E),
    ItemData("Harpe", ItemClassification.useful, 0x002F),
    ItemData("Manganese Saber", ItemClassification.useful, 0x0030),
    ItemData("Light Saber", ItemClassification.useful, 0x0031),
    ItemData("Talwar", ItemClassification.useful, 0x0032),
    ItemData("Soulsaber", ItemClassification.useful, 0x0033),
]

EquipKnightswords: typing.List[ItemData] = [
    ItemData("Defender", ItemClassification.useful, 0x0034),
    ItemData("Apocalypse", ItemClassification.useful, 0x0035),
    ItemData("Lionheart", ItemClassification.useful, 0x0036),
    ItemData("Ragnarok", ItemClassification.useful, 0x0037),
    ItemData("Lohengrin", ItemClassification.useful, 0x0038),
    ItemData("Save the Queen", ItemClassification.useful, 0x0039),
    ItemData("Arch Sword", ItemClassification.useful, 0x003A),
    ItemData("Excalibur", ItemClassification.useful, 0x003B),
    ItemData("Longsword", ItemClassification.useful, 0x003C),
    ItemData("The Fallen Angel", ItemClassification.useful, 0x003D),
    ItemData("Nagrarok", ItemClassification.useful, 0x003E),
    ItemData("Sequencer", ItemClassification.useful, 0x003F),
]

EquipRapiers: typing.List[ItemData] = [
    ItemData("Stinger", ItemClassification.useful, 0x0040),
    ItemData("Estoc", ItemClassification.useful, 0x0041),
    ItemData("Fleuret", ItemClassification.useful, 0x0042),
    ItemData("Scarlet Rapier", ItemClassification.useful, 0x0043),
    ItemData("Flamberge", ItemClassification.useful, 0x0044),
    ItemData("Silver Rapier", ItemClassification.useful, 0x0045),
    ItemData("Djinn Flyssa", ItemClassification.useful, 0x0046),
    ItemData("Joyeuse", ItemClassification.useful, 0x0047),
    ItemData("Mage Masher", ItemClassification.useful, 0x0048),
    ItemData("Colichemarde", ItemClassification.useful, 0x0049),
    ItemData("Gupti Aga", ItemClassification.useful, 0x004A),
    ItemData("Madu", ItemClassification.useful, 0x004B),
    ItemData("Épée-prisme", ItemClassification.useful, 0x004C),
    ItemData("Battle Rapier", ItemClassification.useful, 0x004D),
    ItemData("Last Letter", ItemClassification.useful, 0x004E),
    ItemData("Diabolique", ItemClassification.useful, 0x004F),
    ItemData("Femme Fatale", ItemClassification.useful, 0x0050),
    ItemData("Windsong Rapier", ItemClassification.useful, 0x0051),
]

EquipGreatswords: typing.List[ItemData] = [
    ItemData("Barong", ItemClassification.useful, 0x0052),
    ItemData("Xankbras", ItemClassification.useful, 0x0053),
    ItemData("Dagriohm", ItemClassification.useful, 0x0054),
    ItemData("Ancient Sword", ItemClassification.useful, 0x0055),
    ItemData("Diamond Sword", ItemClassification.useful, 0x0056),
    ItemData("Oblige", ItemClassification.useful, 0x0057),
    ItemData("Hardedge", ItemClassification.useful, 0x0058),
    ItemData("Ogrenix", ItemClassification.useful, 0x0059),
    ItemData("Zweihander", ItemClassification.useful, 0x005A),
    ItemData("Tournesol", ItemClassification.useful, 0x005B),
    ItemData("Vigilante", ItemClassification.useful, 0x005C),
    ItemData("Master Sword", ItemClassification.useful, 0x005D),
    ItemData("Luabreaker", ItemClassification.useful, 0x005E),
]

EquipBroadswords: typing.List[ItemData] = [
    ItemData("Samson Sword", ItemClassification.useful, 0x005F),
    ItemData("Falchion", ItemClassification.useful, 0x0060),
    ItemData("Predator", ItemClassification.useful, 0x0061),
    ItemData("Stribog", ItemClassification.useful, 0x0062),
    ItemData("El-Cid", ItemClassification.useful, 0x0063),
    ItemData("Beastsword", ItemClassification.useful, 0x0064),
    ItemData("Claymore", ItemClassification.useful, 0x0065),
    ItemData("Vajra", ItemClassification.useful, 0x0066),
    ItemData("Rhomphaia", ItemClassification.useful, 0x0067),
    ItemData("Estrella", ItemClassification.useful, 0x0068),
]

EquipKatanas: typing.List[ItemData] = [
    ItemData("Kunai", ItemClassification.useful, 0x0069),
    ItemData("Murasame", ItemClassification.useful, 0x006A),
    ItemData("Ashura", ItemClassification.useful, 0x006B),
    ItemData("Osafune", ItemClassification.useful, 0x006C),
    ItemData("Adazakura", ItemClassification.useful, 0x006D),
    ItemData("Kotetsu", ItemClassification.useful, 0x006E),
    ItemData("Kiku-ichimonji", ItemClassification.useful, 0x006F),
    ItemData("Ama-no-murakumo", ItemClassification.useful, 0x0070),
    ItemData("Nosada", ItemClassification.useful, 0x0071),
    ItemData("Masamune", ItemClassification.useful, 0x0072),
    ItemData("Zanmato", ItemClassification.useful, 0x0073),
    ItemData("Hyakushiki-masamune", ItemClassification.useful, 0x0074),
    ItemData("Sumihomura", ItemClassification.useful, 0x0075),
    ItemData("Ragetsu-denbu", ItemClassification.useful, 0x0076),
]

EquipSpears: typing.List[ItemData] = [
    ItemData("Javelin", ItemClassification.useful, 0x0077),
    ItemData("Lava Spear", ItemClassification.useful, 0x0078),
    ItemData("Gae Bolg", ItemClassification.useful, 0x0079),
    ItemData("Ice Lance", ItemClassification.useful, 0x007A),
    ItemData("Partisan", ItemClassification.useful, 0x007B),
    ItemData("Kain's Lance", ItemClassification.useful, 0x007C),
    ItemData("Trident", ItemClassification.useful, 0x007D),
    ItemData("Dragon Whisker", ItemClassification.useful, 0x007E),
    ItemData("Short Spear", ItemClassification.useful, 0x007F),
]

EquipRods: typing.List[ItemData] = [
    ItemData("Rod", ItemClassification.useful, 0x0080),
    ItemData("Firewheel Rod", ItemClassification.useful, 0x0081),
    ItemData("Thunder Rod", ItemClassification.useful, 0x0082),
    ItemData("Sleet Rod", ItemClassification.useful, 0x0083),
    ItemData("Terre Rod", ItemClassification.useful, 0x0084),
    ItemData("Force Rod", ItemClassification.useful, 0x0085),
    ItemData("Flame Rod", ItemClassification.useful, 0x0086),
    ItemData("Thor Rod", ItemClassification.useful, 0x0087),
    ItemData("Chill Rod", ItemClassification.useful, 0x0088),
    ItemData("Stardust Rod", ItemClassification.useful, 0x0089),
    ItemData("Lilith Rod", ItemClassification.useful, 0x008A),
    ItemData("Crown Scepter", ItemClassification.useful, 0x008B),
    ItemData("Bomb Arm", ItemClassification.useful, 0x008C),
    ItemData("Heretic Rod", ItemClassification.useful, 0x008D),
]

EquipStaves: typing.List[ItemData] = [
    ItemData("White Staff", ItemClassification.useful, 0x008E),
    ItemData("Staff of Protection", ItemClassification.useful, 0x008F),
    ItemData("Judicer's Staff", ItemClassification.useful, 0x0090),
    ItemData("Healing Staff", ItemClassification.useful, 0x0091),
    ItemData("Cleansing Staff", ItemClassification.useful, 0x0092),
    ItemData("Staff of Blessings", ItemClassification.useful, 0x0093),
    ItemData("Serpent Staff", ItemClassification.useful, 0x0094),
    ItemData("Spring Staff", ItemClassification.useful, 0x0095),
    ItemData("Pomegranate Staff", ItemClassification.useful, 0x0096),
    ItemData("Cheer Staff", ItemClassification.useful, 0x0097),
    ItemData("Nirvana", ItemClassification.useful, 0x0098),
    ItemData("Staff of the Magi", ItemClassification.useful, 0x0099),
]

EquipPoles: typing.List[ItemData] = [
    ItemData("Tonfa", ItemClassification.useful, 0x009A),
    ItemData("Cypress Pole", ItemClassification.useful, 0x009B),
    ItemData("Battle Bamboo", ItemClassification.useful, 0x009C),
    ItemData("Sanjiegun", ItemClassification.useful, 0x009D),
    ItemData("Zephyr Pole", ItemClassification.useful, 0x009E),
    ItemData("Iron Pole", ItemClassification.useful, 0x009F),
    ItemData("Esztam Baton", ItemClassification.useful, 0x00A0),
    ItemData("Gokuu Pole", ItemClassification.useful, 0x00A1),
    ItemData("Fanatic", ItemClassification.useful, 0x00A2),
    ItemData("Ivory Pole", ItemClassification.useful, 0x00A3),
    ItemData("Eight-fluted Pole", ItemClassification.useful, 0x00A4),
    ItemData("Whale Whisker", ItemClassification.useful, 0x00A5),
]

EquipKnuckles: typing.List[ItemData] = [
    ItemData("Metal Knuckles", ItemClassification.useful, 0x00A6),
    ItemData("Rising Sun", ItemClassification.useful, 0x00A7),
    ItemData("Poison Knuckles", ItemClassification.useful, 0x00A8),
    ItemData("Dream Claws", ItemClassification.useful, 0x00A9),
    ItemData("Kaiser Knuckles", ItemClassification.useful, 0x00AA),
    ItemData("Cat Claws", ItemClassification.useful, 0x00AB),
    ItemData("Survivor", ItemClassification.useful, 0x00AC),
    ItemData("White Fangs", ItemClassification.useful, 0x00AD),
    ItemData("Godhand", ItemClassification.useful, 0x00AE),
    ItemData("Tiger Fangs", ItemClassification.useful, 0x00AF),
    ItemData("Death Claws", ItemClassification.useful, 0x00B0),
    ItemData("Leather Knuckles", ItemClassification.useful, 0x00B1),
    ItemData("Gleisburst", ItemClassification.useful, 0x00B2),
    ItemData("Magick Hands", ItemClassification.useful, 0x00B3),
]

EquipBows: typing.List[ItemData] = [
    ItemData("Longbow", ItemClassification.useful, 0x00B4),
    ItemData("Char Bow", ItemClassification.useful, 0x00B5),
    ItemData("Thorn Bow", ItemClassification.useful, 0x00B6),
    ItemData("Nail Bow", ItemClassification.useful, 0x00B7),
    ItemData("Silver Bow", ItemClassification.useful, 0x00B8),
    ItemData("Artemis Bow", ItemClassification.useful, 0x00B9),
    ItemData("Yoichi Bow", ItemClassification.useful, 0x00BA),
    ItemData("Target Bow", ItemClassification.useful, 0x00BB),
    ItemData("Perseus Bow", ItemClassification.useful, 0x00BC),
    ItemData("Shortbow", ItemClassification.useful, 0x00BD),
    ItemData("Crescent Bow", ItemClassification.useful, 0x00BE),
    ItemData("Malbow", ItemClassification.useful, 0x00BF),
]

EquipGreatbows: typing.List[ItemData] = [
    ItemData("Windslash Bow", ItemClassification.useful, 0x00C0),
    ItemData("Huntsman's Bow", ItemClassification.useful, 0x00C1),
    ItemData("Cranequin", ItemClassification.useful, 0x00C2),
    ItemData("Twin Bow", ItemClassification.useful, 0x00C3),
    ItemData("Hunting Bow", ItemClassification.useful, 0x00C4),
    ItemData("Elfin Bow", ItemClassification.useful, 0x00C5),
    ItemData("Hades Bow", ItemClassification.useful, 0x00C6),
    ItemData("Nike Bow", ItemClassification.useful, 0x00C7),
    ItemData("Master Bow", ItemClassification.useful, 0x00C8),
    ItemData("Max's Oathbow", ItemClassification.useful, 0x00C9),
    ItemData("Seventh Heaven", ItemClassification.useful, 0x00CA),
    ItemData("Composite Bow", ItemClassification.useful, 0x00CB),
    ItemData("Marduk", ItemClassification.useful, 0x00CC),
    ItemData("Gastrophetes", ItemClassification.useful, 0x00CD),
    ItemData("Arbalest", ItemClassification.useful, 0x00CE),
]

EquipGuns: typing.List[ItemData] = [
    ItemData("Aiot Gun", ItemClassification.useful, 0x00CF),
    ItemData("Silver Cannon", ItemClassification.useful, 0x00D0),
    ItemData("Riot Gun", ItemClassification.useful, 0x00D1),
    ItemData("Chaos Rifle", ItemClassification.useful, 0x00D2),
    ItemData("Lost Gun", ItemClassification.useful, 0x00D3),
    ItemData("Peacemaker", ItemClassification.useful, 0x00D4),
    ItemData("Giot Gun", ItemClassification.useful, 0x00D5),
    ItemData("Longbarrel", ItemClassification.useful, 0x00D6),
    ItemData("Outsider", ItemClassification.useful, 0x00D7),
    ItemData("Goug Mk 29", ItemClassification.useful, 0x00D8),
]

EquipInstruments: typing.List[ItemData] = [
    ItemData("Demon Bell", ItemClassification.useful, 0x00D9),
    ItemData("Glass Bell", ItemClassification.useful, 0x00DA),
    ItemData("War Trumpet", ItemClassification.useful, 0x00DB),
    ItemData("Conch Shell", ItemClassification.useful, 0x00DC),
    ItemData("Hurdy-gurdy", ItemClassification.useful, 0x00DD),
    ItemData("Black Quena", ItemClassification.useful, 0x00DE),
    ItemData("Satyr Flute", ItemClassification.useful, 0x00DF),
    ItemData("Faerie Harp", ItemClassification.useful, 0x00E0),
    ItemData("Blueleaf Flute", ItemClassification.useful, 0x00E1),
    ItemData("Heal Chime", ItemClassification.useful, 0x00E2),
    ItemData("Shining Lute", ItemClassification.useful, 0x00E3),
    ItemData("Frigid Viol", ItemClassification.useful, 0x00E4),
    ItemData("Brilliant Theorbo", ItemClassification.useful, 0x00E5),
    ItemData("Lamia Harp", ItemClassification.useful, 0x00E6),
]

EquipHandcannons: typing.List[ItemData] = [
    ItemData("Hand Cannon", ItemClassification.useful, 0x00E7),
    ItemData("Omnis Cannon", ItemClassification.useful, 0x00E8),
    ItemData("Diklum", ItemClassification.useful, 0x00E9),
    ItemData("Supernal Ray", ItemClassification.useful, 0x00EA),
    ItemData("Ligatur", ItemClassification.useful, 0x00EB),
    ItemData("Brevis", ItemClassification.useful, 0x00EC),
    ItemData("Massive Bazooka", ItemClassification.useful, 0x00ED),
    ItemData("Guang Cannon", ItemClassification.useful, 0x00EE),
    ItemData("Dromaeo", ItemClassification.useful, 0x00EF),
    ItemData("Rocket Punch", ItemClassification.useful, 0x00F0),
]

EquipAxes: typing.List[ItemData] = [
    ItemData("Broadaxe", ItemClassification.useful, 0x00FC),
    ItemData("Slasher", ItemClassification.useful, 0x00FD),
    ItemData("Hammerhead", ItemClassification.useful, 0x00FE),
    ItemData("Francisca", ItemClassification.useful, 0x00FF),
    ItemData("Greataxe", ItemClassification.useful, 0x0100),
    ItemData("Golden Axe", ItemClassification.useful, 0x0101),
]

EquipHammers: typing.List[ItemData] = [
    ItemData("Iron Hammer", ItemClassification.useful, 0x0102),
    ItemData("War Hammer", ItemClassification.useful, 0x0103),
    ItemData("Sledgehammer", ItemClassification.useful, 0x0104),
    ItemData("Mjolnir", ItemClassification.useful, 0x0105),
]

EquipMaces: typing.List[ItemData] = [
    ItemData("Battle Mace", ItemClassification.useful, 0x0106),
    ItemData("Energy Mace", ItemClassification.useful, 0x0107),
    ItemData("Druid Mace", ItemClassification.useful, 0x0108),
    ItemData("Sage Crosier", ItemClassification.useful, 0x0109),
    ItemData("Morning Star", ItemClassification.useful, 0x010A),
    ItemData("Mandragora", ItemClassification.useful, 0x010B),
    ItemData("Life Crosier", ItemClassification.useful, 0x010C),
    ItemData("Lotus Mace", ItemClassification.useful, 0x010D),
    ItemData("Scorpion Tail", ItemClassification.useful, 0x010E),
    ItemData("Zeus Mace", ItemClassification.useful, 0x010F),
]

EquipCards: typing.List[ItemData] = [
    ItemData("Four of Spades", ItemClassification.useful, 0x0110),
    ItemData("Eight of Hearts", ItemClassification.useful, 0x0111),
    ItemData("Queen of Clubs", ItemClassification.useful, 0x0112),
    ItemData("Jack of Diamonds", ItemClassification.useful, 0x0113),
    ItemData("King of Hearts", ItemClassification.useful, 0x0114),
    ItemData("Ace of Spades", ItemClassification.useful, 0x0115),
    ItemData("Two of Clubs", ItemClassification.useful, 0x0116),
    ItemData("Six of Diamonds", ItemClassification.useful, 0x0117),
    ItemData("Joker", ItemClassification.useful, 0x0118),
]

EquipBooks: typing.List[ItemData] = [
    ItemData("Battle Folio", ItemClassification.useful, 0x0119),
    ItemData("Mage Manual", ItemClassification.useful, 0x011A),
    ItemData("Urutan Annals", ItemClassification.useful, 0x011B),
    ItemData("The Arnath Glyphs", ItemClassification.useful, 0x011C),
    ItemData("Enavia Chronicles", ItemClassification.useful, 0x011D),
    ItemData("Veil of Wiyu", ItemClassification.useful, 0x011E),
    ItemData("Tome of Ending", ItemClassification.useful, 0x011F),
    ItemData("Edaroya Scriptures", ItemClassification.useful, 0x0120),
]

EquipShields: typing.List[ItemData] = [
    ItemData("Bronze Shield", ItemClassification.useful, 0x0121),
    ItemData("Round Shield", ItemClassification.useful, 0x0122),
    ItemData("Platinum Shield", ItemClassification.useful, 0x0123),
    ItemData("Ice Shield", ItemClassification.useful, 0x0124),
    ItemData("Flame Shield", ItemClassification.useful, 0x0125),
    ItemData("Aegis Shield", ItemClassification.useful, 0x0126),
    ItemData("Genji Shield", ItemClassification.useful, 0x0127),
    ItemData("Templar Shield", ItemClassification.useful, 0x0128),
    ItemData("Shield of the Four", ItemClassification.useful, 0x0129),
    ItemData("Chocobo Shield", ItemClassification.useful, 0x012A),
    ItemData("Ensanguined Shield", ItemClassification.useful, 0x012B),
    ItemData("Reverie Shield", ItemClassification.useful, 0x012C),
]

EquipHelmets: typing.List[ItemData] = [
    ItemData("Bronze Helm", ItemClassification.useful, 0x012D),
    ItemData("Iron Helm", ItemClassification.useful, 0x012E),
    ItemData("Barbut", ItemClassification.useful, 0x012F),
    ItemData("Close Helmet", ItemClassification.useful, 0x0130),
    ItemData("Platinum Helm", ItemClassification.useful, 0x0131),
    ItemData("Diamond Helm", ItemClassification.useful, 0x0132),
    ItemData("Hanya Mask", ItemClassification.useful, 0x0133),
    ItemData("Giant's Helmet", ItemClassification.useful, 0x0134),
    ItemData("Genji Helm", ItemClassification.useful, 0x0135),
]

EquipeFemaleHats: typing.List[ItemData] = [
    ItemData("Cachusha", ItemClassification.useful, 0x0136),
    ItemData("Barette", ItemClassification.useful, 0x0137),
    ItemData("Ribbon", ItemClassification.useful, 0x0138),
    ]

EquipHats: typing.List[ItemData] = [
    ItemData("Plumed Hat", ItemClassification.useful, 0x0139),
    ItemData("Green Beret", ItemClassification.useful, 0x013A),
    ItemData("Circlet", ItemClassification.useful, 0x013B),
    ItemData("Headband", ItemClassification.useful, 0x013C),
    ItemData("Wizard's Hat", ItemClassification.useful, 0x013D),
    ItemData("Gold Hairpin", ItemClassification.useful, 0x013E),
    ItemData("Thief's Cap", ItemClassification.useful, 0x013F),
    ItemData("Tiara", ItemClassification.useful, 0x0140),
    ItemData("Black Hat", ItemClassification.useful, 0x0141),
    ItemData("White Hat", ItemClassification.useful, 0x0142),
    ItemData("Golden Skullcap", ItemClassification.useful, 0x0143),
]

EquipHeavyArmor: typing.List[ItemData] = [
    ItemData("Linen Cuirass", ItemClassification.useful, 0x0144),
    ItemData("Bronze Armor", ItemClassification.useful, 0x0145),
    ItemData("Iron Armor", ItemClassification.useful, 0x0146),
    ItemData("Platemail", ItemClassification.useful, 0x0147),
    ItemData("Golden Armor", ItemClassification.useful, 0x0148),
    ItemData("Diamond Armor", ItemClassification.useful, 0x0149),
    ItemData("Platinum Armor", ItemClassification.useful, 0x014A),
    ItemData("Carabineer Mail", ItemClassification.useful, 0x014B),
    ItemData("Mirror Mail", ItemClassification.useful, 0x014C),
    ItemData("Dragon Mail", ItemClassification.useful, 0x014D),
    ItemData("Maximilian", ItemClassification.useful, 0x014E),
    ItemData("Genji Armor", ItemClassification.useful, 0x014F),
    ItemData("Adamant Armor", ItemClassification.useful, 0x0150),
    ItemData("Materia Armor", ItemClassification.useful, 0x0151),
    ItemData("Peytral", ItemClassification.useful, 0x0152),
]

EquipLightArmor: typing.List[ItemData] = [
    ItemData("Leather Clothing", ItemClassification.useful, 0x0153),
    ItemData("Chainmail", ItemClassification.useful, 0x0154),
    ItemData("Adamant Vest", ItemClassification.useful, 0x0155),
    ItemData("Survival Vest", ItemClassification.useful, 0x0156),
    ItemData("Brigandine", ItemClassification.useful, 0x0157),
    ItemData("Jujitsu Gi", ItemClassification.useful, 0x0158),
    ItemData("Power Sash", ItemClassification.useful, 0x0159),
    ItemData("Gaia Gear", ItemClassification.useful, 0x015A),
    ItemData("Minerva Bustier", ItemClassification.useful, 0x015B),
    ItemData("Ninja Gear", ItemClassification.useful, 0x015C),
    ItemData("Black Garb", ItemClassification.useful, 0x015D),
    ItemData("Wygar", ItemClassification.useful, 0x015E),
    ItemData("Mirage Vest", ItemClassification.useful, 0x015F),
    ItemData("Rubber Suit", ItemClassification.useful, 0x0160),
    ItemData("Bone Plate", ItemClassification.useful, 0x0161),
    ItemData("Judicer's Coat", ItemClassification.useful, 0x0162),
]

EquipRobes: typing.List[ItemData] = [
    ItemData("Ever Robe", ItemClassification.useful, 0x0163),
    ItemData("Brint Frock", ItemClassification.useful, 0x0164),
    ItemData("Galmia Frock", ItemClassification.useful, 0x0165),
    ItemData("Templar Cloth", ItemClassification.useful, 0x0166),
    ItemData("Hempen Robe", ItemClassification.useful, 0x0167),
    ItemData("Silken Robe", ItemClassification.useful, 0x0168),
    ItemData("Magus Robe", ItemClassification.useful, 0x0169),
    ItemData("Chameleon Robe", ItemClassification.useful, 0x016A),
    ItemData("Blaze Robe", ItemClassification.useful, 0x016B),
    ItemData("Thunder Robe", ItemClassification.useful, 0x016C),
    ItemData("Flurry Robe", ItemClassification.useful, 0x016D),
    ItemData("White Robe", ItemClassification.useful, 0x016E),
    ItemData("Black Robe", ItemClassification.useful, 0x016F),
    ItemData("Luminous Robe", ItemClassification.useful, 0x0170),
    ItemData("Lordly Robe", ItemClassification.useful, 0x0171),
    ItemData("Samite Coat", ItemClassification.useful, 0x0172),
    ItemData("Red Robe", ItemClassification.useful, 0x0173),
    ItemData("Sage's Robe", ItemClassification.useful, 0x0174),
    ItemData("Magick Robe", ItemClassification.useful, 0x0175),
    ItemData("Reaper's Robe", ItemClassification.useful, 0x0176),
]

EquipShoes: typing.List[ItemData] = [
    ItemData("Battle Boots", ItemClassification.useful, 0x0177),
    ItemData("Spiked Boots", ItemClassification.useful, 0x0178),
    ItemData("Sprint Shoes", ItemClassification.useful, 0x0179),
    ItemData("Red Shoes", ItemClassification.useful, 0x017A),
    ItemData("Winged Boots", ItemClassification.useful, 0x017B),
    ItemData("Germinas Boots", ItemClassification.useful, 0x017C),
    ItemData("Galmia Shoes", ItemClassification.useful, 0x017D),
    ItemData("Faerie Shoes", ItemClassification.useful, 0x017E),
    ItemData("Gaius Caligae", ItemClassification.useful, 0x017F),
    ItemData("Ninja Tabi", ItemClassification.useful, 0x0180),
]

EquipGloves: typing.List[ItemData] = [
    ItemData("Armguards", ItemClassification.useful, 0x0181),
    ItemData("Brigand's Gloves", ItemClassification.useful, 0x0182),
    ItemData("Bracers", ItemClassification.useful, 0x0183),
    ItemData("Genji Gloves", ItemClassification.useful, 0x0184),
    ItemData("Gauntlets", ItemClassification.useful, 0x0185),
    ItemData("Bone Armlets", ItemClassification.useful, 0x0186),
]

EquipRings: typing.List[ItemData] = [
    ItemData("Crimson Tear", ItemClassification.useful, 0x00F1),
    ItemData("Snowy Tear", ItemClassification.useful, 0x00F2),
    ItemData("Azure Tear", ItemClassification.useful, 0x00F3),
    ItemData("Moon Maiden", ItemClassification.useful, 0x00F4),
    ItemData("Fortune Ring", ItemClassification.useful, 0x0187),
    ItemData("Magick Ring", ItemClassification.useful, 0x0188),
    ItemData("Angel Ring", ItemClassification.useful, 0x0189),
    ItemData("Scarab Charm", ItemClassification.useful, 0x018A),
    ItemData("Ruby Earring", ItemClassification.useful, 0x018B),
    ItemData("Empyreal Armband", ItemClassification.useful, 0x018C),
    ItemData("Orb of Minwu", ItemClassification.useful, 0x018D),
    ItemData("Golden Amulet", ItemClassification.useful, 0x018E),
    ItemData("Gigas Pendant", ItemClassification.useful, 0x018F),
    ItemData("Corsage of Corruption", ItemClassification.useful, 0x0190),
    ItemData("Armlet of Whispers", ItemClassification.useful, 0x0191),
    ItemData("Pin of Order", ItemClassification.useful, 0x0192),
    ItemData("Ewer of Darkness", ItemClassification.useful, 0x0193),
    ItemData("Raging Brooch", ItemClassification.useful, 0x0194),
    ItemData("Tainted Cufflink", ItemClassification.useful, 0x0195),
    ItemData("Earrings of the Dead", ItemClassification.useful, 0x0196),
    ItemData("Ring of the Wheel", ItemClassification.useful, 0x0197),
    ItemData("Condemner's Choker", ItemClassification.useful, 0x0198),
    ItemData("Gift of the Judge-Sal", ItemClassification.useful, 0x0199),
    ItemData("High Seraph's Plume", ItemClassification.useful, 0x019A),
    ItemData("Ring of Precepts", ItemClassification.useful, 0x019B),
]

Consumables: typing.List[ItemData] = [
    ItemData("Potion", ItemClassification.filler, 0x019C),
    ItemData("Hi-Potion", ItemClassification.filler, 0x019D),
    ItemData("X-Potion", ItemClassification.filler, 0x019E),
    ItemData("Ether", ItemClassification.filler, 0x019F),
    ItemData("Elixir", ItemClassification.filler, 0x01A0),
    ItemData("Phoenix Down", ItemClassification.filler, 0x01A1),
    ItemData("Echo Herbs", ItemClassification.filler, 0x01A2),
    ItemData("Maiden's Kiss", ItemClassification.filler, 0x01A3),
    ItemData("Gold Needle", ItemClassification.filler, 0x01A4),
    ItemData("Holy Water", ItemClassification.filler, 0x01A5),
    ItemData("Antidote", ItemClassification.filler, 0x01A6),
    ItemData("Eye Drops", ItemClassification.filler, 0x01A7),
    ItemData("Bandage", ItemClassification.filler, 0x01A8),
    ItemData("Remedy", ItemClassification.filler, 0x01A9),
    ItemData("Handkerchief", ItemClassification.filler, 0x01AA),
    ItemData("Knot of Rust", ItemClassification.filler, 0x01AB),
    ItemData("Eureka Crystal", ItemClassification.filler, 0x01AC),
    ItemData("Grimoire Stone", ItemClassification.filler, 0x01AD),
    ItemData("Dark Matter", ItemClassification.filler, 0x01AE),
]

Loot: typing.List[ItemData] = [
    ItemData("Tarkov Crystal", ItemClassification.useful, 0x01AF),
    ItemData("Mind Ceffyl", ItemClassification.useful, 0x01B0),
    ItemData("Body Ceffyl", ItemClassification.useful, 0x01B1),
    ItemData("Soul Ceffyl", ItemClassification.useful, 0x01B2),
    ItemData("Earthwyrm Crystal", ItemClassification.useful, 0x01B3),
    ItemData("Windgod Crystal", ItemClassification.useful, 0x01B4),
    ItemData("Waterwyrd Crystal", ItemClassification.useful, 0x01B5),
    ItemData("Firebird Crystal", ItemClassification.useful, 0x01B6),
    ItemData("Snowcat Crystal", ItemClassification.useful, 0x01B7),
    ItemData("Stormsoul Crystal", ItemClassification.useful, 0x01B8),
    ItemData("Lightwing Crystal", ItemClassification.useful, 0x01B9),
    ItemData("Darklord Crystal", ItemClassification.useful, 0x01BA),
    ItemData("Earth Stone", ItemClassification.useful, 0x01BB),
    ItemData("Wind Stone", ItemClassification.useful, 0x01BC),
    ItemData("Water Stone", ItemClassification.useful, 0x01BD),
    ItemData("Fire Stone", ItemClassification.useful, 0x01BE),
    ItemData("Ice Stone", ItemClassification.useful, 0x01BF),
    ItemData("Storm Stone", ItemClassification.useful, 0x01C0),
    ItemData("Holy Stone", ItemClassification.useful, 0x01C1),
    ItemData("Dark Stone", ItemClassification.useful, 0x01C2),
    ItemData("Wind Sigil", ItemClassification.useful, 0x01C3),
    ItemData("Earth Sigil", ItemClassification.useful, 0x01C4),
    ItemData("Fire Sigil", ItemClassification.useful, 0x01C5),
    ItemData("Water Sigil", ItemClassification.useful, 0x01C6),
    ItemData("Storm Sigil", ItemClassification.useful, 0x01C7),
    ItemData("Ice Sigil", ItemClassification.useful, 0x01C8),
    ItemData("Low Arcana", ItemClassification.useful, 0x01C9),
    ItemData("High Arcana", ItemClassification.useful, 0x01CA),
    ItemData("Adamantite", ItemClassification.useful, 0x01CB),
    ItemData("Zodiac Ore", ItemClassification.useful, 0x01CC),
    ItemData("Leestone", ItemClassification.useful, 0x01CD),
    ItemData("Mythril", ItemClassification.useful, 0x01CE),
    ItemData("Adamant Alloy", ItemClassification.useful, 0x01CF),
    ItemData("Crusite Alloy", ItemClassification.useful, 0x01D0),
    ItemData("Mysidia Alloy", ItemClassification.useful, 0x01D1),
    ItemData("Scarletite", ItemClassification.useful, 0x01D2),
    ItemData("Damascus", ItemClassification.useful, 0x01D3),
    ItemData("Orichalcum", ItemClassification.useful, 0x01D4),
    ItemData("Einherjarium", ItemClassification.useful, 0x01D5),
    ItemData("Gemsteel", ItemClassification.useful, 0x01D6),
    ItemData("Zinconium", ItemClassification.useful, 0x01D7),
    ItemData("Zincatite", ItemClassification.useful, 0x01D8),
    ItemData("Xergis Tin", ItemClassification.useful, 0x01D9),
    ItemData("Cruzle Brass", ItemClassification.useful, 0x01DA),
    ItemData("Dipraeu Bronze", ItemClassification.useful, 0x01DB),
    ItemData("Platinum", ItemClassification.useful, 0x01DC),
    ItemData("Gikhet Lead", ItemClassification.useful, 0x01DD),
    ItemData("Gun Gear", ItemClassification.useful, 0x01DE),
    ItemData("Clock Gear", ItemClassification.useful, 0x01DF),
    ItemData("Gold Chalice", ItemClassification.useful, 0x01E0),
    ItemData("Trusty Frying Pan", ItemClassification.useful, 0x01E1),
    ItemData("Cursed Coin", ItemClassification.useful, 0x01E2),
    ItemData("Bundle of Needles", ItemClassification.useful, 0x01E3),
    ItemData("Sanative Needle", ItemClassification.useful, 0x01E4),
    ItemData("Moon Ring", ItemClassification.useful, 0x01E5),
    ItemData("Tiger Hide", ItemClassification.useful, 0x01E6),
    ItemData("Chocobo Skin", ItemClassification.useful, 0x01E7),
    ItemData("Rat Pelt", ItemClassification.useful, 0x01E8),
    ItemData("Snake Skin", ItemClassification.useful, 0x01E9),
    ItemData("Tyrant Hide", ItemClassification.useful, 0x01EA),
    ItemData("Quality Hide", ItemClassification.useful, 0x01EB),
    ItemData("Tanned Hide", ItemClassification.useful, 0x01EC),
    ItemData("Giant's Tanned Hide", ItemClassification.useful, 0x01ED),
    ItemData("Tanned Tyrant Hide", ItemClassification.useful, 0x01EE),
    ItemData("Prime Tanned Hide", ItemClassification.useful, 0x01EF),
    ItemData("Wolf Pelt", ItemClassification.useful, 0x01F0),
    ItemData("Coeurl Pelt", ItemClassification.useful, 0x01F1),
    ItemData("Quality Pelt", ItemClassification.useful, 0x01F2),
    ItemData("Prime Pelt", ItemClassification.useful, 0x01F3),
    ItemData("Rabbit Pelt", ItemClassification.useful, 0x01F4),
    ItemData("Rabbit Tail", ItemClassification.useful, 0x01F5),
    ItemData("Rat Tail", ItemClassification.useful, 0x01F6),
    ItemData("Pink Tail", ItemClassification.useful, 0x01F7),
    ItemData("Cockatrice Skin", ItemClassification.useful, 0x01F8),
    ItemData("Bat Tail", ItemClassification.useful, 0x01F9),
    ItemData("Tanned Beast Hide", ItemClassification.useful, 0x01FA),
    ItemData("Animal Bone", ItemClassification.useful, 0x01FB),
    ItemData("Dragon Bone", ItemClassification.useful, 0x01FC),
    ItemData("Sturdy Bone", ItemClassification.useful, 0x01FD),
    ItemData("Blood-darkened Bone", ItemClassification.useful, 0x01FE),
    ItemData("Bomb Shell", ItemClassification.useful, 0x01FF),
    ItemData("Mirror Scale", ItemClassification.useful, 0x0200),
    ItemData("Emperor Scale", ItemClassification.useful, 0x0201),
    ItemData("Cod Scale", ItemClassification.useful, 0x0202),
    ItemData("Lamia Scale", ItemClassification.useful, 0x0203),
    ItemData("Molting", ItemClassification.useful, 0x0204),
    ItemData("Iron Carapace", ItemClassification.useful, 0x0205),
    ItemData("Wyrm Carapace", ItemClassification.useful, 0x0206),
    ItemData("Insect Husk", ItemClassification.useful, 0x0207),
    ItemData("Battlewyrm Carapace", ItemClassification.useful, 0x0208),
    ItemData("Pointed Horn", ItemClassification.useful, 0x0209),
    ItemData("Beastlord Horn", ItemClassification.useful, 0x020A),
    ItemData("Great Serpent's Fang", ItemClassification.useful, 0x020B),
    ItemData("Vampyr Fang", ItemClassification.useful, 0x020C),
    ItemData("Crooked Fang", ItemClassification.useful, 0x020D),
    ItemData("Spiral Incisor", ItemClassification.useful, 0x020E),
    ItemData("Wyvern Fang", ItemClassification.useful, 0x020F),
    ItemData("Gimble Stalk", ItemClassification.useful, 0x0210),
    ItemData("Alraune Drill", ItemClassification.useful, 0x0211),
    ItemData("Zingu Pearl", ItemClassification.useful, 0x0212),
    ItemData("Zingu Pearl Shell", ItemClassification.useful, 0x0213),
    ItemData("Star Fragments", ItemClassification.useful, 0x0214),
    ItemData("Fury Fragments", ItemClassification.useful, 0x0215),
    ItemData("Coral Fragments", ItemClassification.useful, 0x0216),
    ItemData("Turtle Shell", ItemClassification.useful, 0x0217),
    ItemData("Aged Turtle Shell", ItemClassification.useful, 0x0218),
    ItemData("Ancient Turtle Shell", ItemClassification.useful, 0x0219),
    ItemData("Bone Chips", ItemClassification.useful, 0x021A),
    ItemData("Skull", ItemClassification.useful, 0x021B),
    ItemData("Moon Bloom", ItemClassification.useful, 0x021C),
    ItemData("Telaq Flower", ItemClassification.useful, 0x021D),
    ItemData("Silk Bloom", ItemClassification.useful, 0x021E),
    ItemData("Malboro Flower", ItemClassification.useful, 0x021F),
    ItemData("Marriom Heather", ItemClassification.useful, 0x0220),
    ItemData("Prima Petal", ItemClassification.useful, 0x0221),
    ItemData("Leucojum", ItemClassification.useful, 0x0222),
    ItemData("Kalos", ItemClassification.useful, 0x0223),
    ItemData("Hedychium", ItemClassification.useful, 0x0224),
    ItemData("Nepenthis", ItemClassification.useful, 0x0225),
    ItemData("Recall Grass", ItemClassification.useful, 0x0226),
    ItemData("Whisperweed", ItemClassification.useful, 0x0227),
    ItemData("Ladies' Tresses", ItemClassification.useful, 0x0228),
    ItemData("Flutegrass", ItemClassification.useful, 0x0229),
    ItemData("Goldcap", ItemClassification.useful, 0x022A),
    ItemData("Magick Fruit", ItemClassification.useful, 0x022B),
    ItemData("Power Fruit", ItemClassification.useful, 0x022C),
    ItemData("Succulent Fruit", ItemClassification.useful, 0x022D),
    ItemData("Cactus Fruit", ItemClassification.useful, 0x022E),
    ItemData("Suspect Mushroom", ItemClassification.useful, 0x022F),
    ItemData("Tiny Mushrooms", ItemClassification.useful, 0x0230),
    ItemData("Screamroot", ItemClassification.useful, 0x0231),
    ItemData("Onion", ItemClassification.useful, 0x0232),
    ItemData("Hedychium Pollen", ItemClassification.useful, 0x0233),
    ItemData("Aurea Pollen", ItemClassification.useful, 0x0234),
    ItemData("Faren Pollen", ItemClassification.useful, 0x0235),
    ItemData("Malboro Vine", ItemClassification.useful, 0x0236),
    ItemData("Sturdy Vine", ItemClassification.useful, 0x0237),
    ItemData("Spiral Vine", ItemClassification.useful, 0x0238),
    ItemData("Four-leaf Clover", ItemClassification.useful, 0x0239),
    ItemData("Ball Moss", ItemClassification.useful, 0x023A),
    ItemData("Pearl Moss", ItemClassification.useful, 0x023B),
    ItemData("Tomato Stalk", ItemClassification.useful, 0x023C),
    ItemData("Peppergrass", ItemClassification.useful, 0x023D),
    ItemData("Stradivari", ItemClassification.useful, 0x023E),
    ItemData("Strawood", ItemClassification.useful, 0x023F),
    ItemData("Divariwood", ItemClassification.useful, 0x0240),
    ItemData("Moonwood", ItemClassification.useful, 0x0241),
    ItemData("Danbukwood", ItemClassification.useful, 0x0242),
    ItemData("Quality Lumber", ItemClassification.useful, 0x0243),
    ItemData("Cottonflue", ItemClassification.useful, 0x0244),
    ItemData("Waltwood", ItemClassification.useful, 0x0245),
    ItemData("Kempas", ItemClassification.useful, 0x0246),
    ItemData("Agathis", ItemClassification.useful, 0x0247),
    ItemData("Mape Wood", ItemClassification.useful, 0x0248),
    ItemData("Red Geeps", ItemClassification.useful, 0x0249),
    ItemData("Spruce", ItemClassification.useful, 0x024A),
    ItemData("Quince", ItemClassification.useful, 0x024B),
    ItemData("Birch", ItemClassification.useful, 0x024C),
    ItemData("Rose Branch", ItemClassification.useful, 0x024D),
    ItemData("Mahbeny", ItemClassification.useful, 0x024E),
    ItemData("Gurnat", ItemClassification.useful, 0x024F),
    ItemData("Pagoda Wood", ItemClassification.useful, 0x0250),
    ItemData("Kuraisle Boxwood", ItemClassification.useful, 0x0251),
    ItemData("Wyrmtwig", ItemClassification.useful, 0x0252),
    ItemData("Godwood", ItemClassification.useful, 0x0253),
    ItemData("Green Liquid", ItemClassification.useful, 0x0254),
    ItemData("Yellow Liquid", ItemClassification.useful, 0x0255),
    ItemData("Silver Liquid", ItemClassification.useful, 0x0256),
    ItemData("Foul Liquid", ItemClassification.useful, 0x0257),
    ItemData("Putrid Liquid", ItemClassification.useful, 0x0258),
    ItemData("Unpurified Ether", ItemClassification.useful, 0x0259),
    ItemData("Hero Tonic", ItemClassification.useful, 0x025A),
    ItemData("Crusader Tonic", ItemClassification.useful, 0x025B),
    ItemData("Healing Water", ItemClassification.useful, 0x025C),
    ItemData("Strange Liquid", ItemClassification.useful, 0x025D),
    ItemData("Fresh Water", ItemClassification.useful, 0x025E),
    ItemData("Aqua Galac", ItemClassification.useful, 0x025F),
    ItemData("Fiend's Blood", ItemClassification.useful, 0x0260),
    ItemData("Malboro Wine", ItemClassification.useful, 0x0261),
    ItemData("Clear Sap", ItemClassification.useful, 0x0262),
    ItemData("Sweet Sap", ItemClassification.useful, 0x0263),
    ItemData("Bitter Sap", ItemClassification.useful, 0x0264),
    ItemData("Cloudy Sap", ItemClassification.useful, 0x0265),
]

GateItems: typing.List[ItemData] = [
    ItemData("Black Thread", ItemClassification.progression, 0x0266),
    ItemData("White Thread", ItemClassification.progression, 0x0267),
    ItemData("Dirty Wool", ItemClassification.progression, 0x0268),
    ItemData("Wool", ItemClassification.progression, 0x0269),
    ItemData("Fine Wool", ItemClassification.progression, 0x026A),
    ItemData("Spider Silk", ItemClassification.progression, 0x026B),
    ItemData("Aged Linen Thread", ItemClassification.progression, 0x026C),
    ItemData("Silk Thread", ItemClassification.progression, 0x026D),
    ItemData("Superior Silk Thread", ItemClassification.progression, 0x026E),
    ItemData("Soft Cotton", ItemClassification.progression, 0x026F),
    ItemData("Velvet", ItemClassification.progression, 0x0270),
    ItemData("Rainbow Thread", ItemClassification.progression, 0x0271),
    ItemData("Ahriman Wing", ItemClassification.progression, 0x0272),
    ItemData("Faerie Wing", ItemClassification.progression, 0x0273),
    ItemData("Small Feather", ItemClassification.progression, 0x0274),
    ItemData("Large Feather", ItemClassification.progression, 0x0275),
    ItemData("Giant Feather", ItemClassification.progression, 0x0276),
    ItemData("Windslicer Pinion", ItemClassification.progression, 0x0277),
    ItemData("Demon Feather", ItemClassification.progression, 0x0278),
    ItemData("Bat Wing", ItemClassification.progression, 0x0279),
    ItemData("Wyvern Wing", ItemClassification.progression, 0x027A),
]

dummyItems: typing.List[ItemData] = [
    ItemData("-", ItemClassification.useful, 0x00F5),  # Archipelago item for now
    ItemData("-", ItemClassification.useful, 0x00F6),  # Job unlock item for now
    ItemData("-", ItemClassification.useful, 0x00F7),
    ItemData("-", ItemClassification.useful, 0x00F8),
    ItemData("-", ItemClassification.useful, 0x00F9),
    ItemData("-", ItemClassification.useful, 0x00FA),
    ItemData("-", ItemClassification.useful, 0x00FB),
]

jobUnlockOffset = 0x400
jobUnlockItems: typing.List[ItemData] = [
    ItemData("Job Unlock: Soldier", ItemClassification.useful, 0x401),
    ItemData("Job Unlock: Thief", ItemClassification.useful, 0x402),
    ItemData("Job Unlock: White Mage", ItemClassification.useful, 0x403),
    ItemData("Job Unlock: Black Mage", ItemClassification.useful, 0x404),
    ItemData("Job Unlock: Archer", ItemClassification.useful, 0x405),
    ItemData("Job Unlock: Paladin", ItemClassification.useful, 0x406),
    ItemData("Job Unlock: Fighter", ItemClassification.useful, 0x407),
    ItemData("Job Unlock: Parivir", ItemClassification.useful, 0x408),
    ItemData("Job Unlock: Ninja", ItemClassification.useful, 0x409),
    ItemData("Job Unlock: Illusionist", ItemClassification.useful, 0x40a),
    ItemData("Job Unlock: Blue Mage", ItemClassification.useful, 0x40b),
    ItemData("Job Unlock: Hunter", ItemClassification.useful, 0x40c),
    ItemData("Job Unlock: Seer", ItemClassification.useful, 0x40d),
    ItemData("Job Unlock: Warrior", ItemClassification.useful, 0x40e),
    ItemData("Job Unlock: White Monk", ItemClassification.useful, 0x40f),
    ItemData("Job Unlock: Dragoon", ItemClassification.useful, 0x410),
    ItemData("Job Unlock: Defender", ItemClassification.useful, 0x411),
    ItemData("Job Unlock: Gladiator", ItemClassification.useful, 0x412),
    ItemData("Job Unlock: Master Monk", ItemClassification.useful, 0x413),
    ItemData("Job Unlock: Bishop", ItemClassification.useful, 0x414),
    ItemData("Job Unlock: Templar", ItemClassification.useful, 0x415),
    ItemData("Job Unlock: Cannoneer", ItemClassification.useful, 0x416),
    ItemData("Job Unlock: Trickster", ItemClassification.useful, 0x417),
    ItemData("Job Unlock: Beastmaster", ItemClassification.useful, 0x418),
    ItemData("Job Unlock: Time Mage", ItemClassification.useful, 0x419),
    ItemData("Job Unlock: Alchemist", ItemClassification.useful, 0x41a),
    ItemData("Job Unlock: Arcanist", ItemClassification.useful, 0x41b),
    ItemData("Job Unlock: Sage", ItemClassification.useful, 0x41c),
    ItemData("Job Unlock: Scholar", ItemClassification.useful, 0x41d),
    #ItemData("Job Unlock: Keeper", ItemClassification.useful, 0x41e),
    ItemData("Job Unlock: Fencer", ItemClassification.useful, 0x41f),
    ItemData("Job Unlock: Green Mage", ItemClassification.useful, 0x420),
    ItemData("Job Unlock: Elementalist", ItemClassification.useful, 0x421),
    ItemData("Job Unlock: Red Mage", ItemClassification.useful, 0x422),
    ItemData("Job Unlock: Spellblade", ItemClassification.useful, 0x423),
    ItemData("Job Unlock: Summoner", ItemClassification.useful, 0x424),
    ItemData("Job Unlock: Assassin", ItemClassification.useful, 0x425),
    ItemData("Job Unlock: Sniper", ItemClassification.useful, 0x426),
    ItemData("Job Unlock: Animist", ItemClassification.useful, 0x427),
    ItemData("Job Unlock: Moogle Knight", ItemClassification.useful, 0x428),
    ItemData("Job Unlock: Fusilier", ItemClassification.useful, 0x429),
    ItemData("Job Unlock: Juggler", ItemClassification.useful, 0x42a),
    ItemData("Job Unlock: Tinker", ItemClassification.useful, 0x42b),
    ItemData("Job Unlock: Chocobo Knight", ItemClassification.useful, 0x42c),
    ItemData("Job Unlock: Flintlock", ItemClassification.useful, 0x42d),
    ItemData("Job Unlock: Berserker", ItemClassification.useful, 0x42e),
    ItemData("Job Unlock: Ranger", ItemClassification.useful, 0x42f),
    ItemData("Job Unlock: Lanista", ItemClassification.useful, 0x430),
    ItemData("Job Unlock: Viking", ItemClassification.useful, 0x431),
    ItemData("Job Unlock: Raptor", ItemClassification.useful, 0x432),
    ItemData("Job Unlock: Ravager", ItemClassification.useful, 0x433),
    ItemData("Job Unlock: Geomancer", ItemClassification.useful, 0x434),
]


MeleeWeapons: typing.List[ItemData] = EquipKnives + EquipSwords + EquipBlades + EquipSabers + EquipKnightswords + \
                                 EquipRapiers + EquipGreatswords + EquipBroadswords + EquipKatanas + EquipSpears + \
                                 EquipRods + EquipStaves + EquipPoles + EquipKnuckles + EquipInstruments + EquipAxes + \
                                 EquipHammers + EquipMaces + EquipBooks

RangedWeapons: typing.List[ItemData] = EquipBows + EquipGreatbows + EquipGuns + EquipHandcannons + EquipCards

Weapons: typing.List[ItemData] = EquipKnives + EquipSwords + EquipBlades + EquipSabers + EquipKnightswords + \
                                 EquipRapiers + EquipGreatswords + EquipBroadswords + EquipKatanas + EquipSpears + \
                                 EquipRods + EquipStaves + EquipPoles + EquipKnuckles + EquipBows + EquipGreatbows + \
                                 EquipGuns + EquipInstruments + EquipHandcannons + EquipAxes + EquipHammers + \
                                 EquipMaces + EquipCards + EquipBooks

Accessories: typing.List[ItemData] = EquipShoes + EquipGloves + EquipRings

AllItems: typing.List[ItemData] = Weapons + EquipShields + EquipHelmets + EquipeFemaleHats + EquipHats + \
                                  EquipHeavyArmor + EquipLightArmor + EquipRobes + EquipShoes + EquipGloves + \
                                  EquipRings + Consumables + Loot + GateItems + jobUnlockItems

FillerItems: typing.List[ItemData] = [x for x in AllItems if x.progression == ItemClassification.filler]

item_table: typing.Dict[str, ItemData] = {item.itemName: item for item in AllItems}
items_by_id: typing.Dict[int, ItemData] = {item.itemID: item for item in AllItems}


def create_item_label_to_code_map() -> Dict[str, int]:
    """
    Creates a map from item labels to their AP item id (code)
    """
    offset = 0
    label_to_code_map: Dict[str, int] = {}
    for item in AllItems:
        label_to_code_map[item.itemName] = item.itemID + offset

    return label_to_code_map
