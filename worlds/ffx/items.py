from typing import Dict, List
import typing
from BaseClasses import Item, ItemClassification


class ItemData(typing.NamedTuple):
    itemName: str
    progression: ItemClassification
    itemID: int = 0x00
    player: int = 0


class FFXItem(Item):
    itemName: str
    progression: ItemClassification
    itemID: int = 0x00
    player: int = 0
    game: str = "Final Fantasy X"


filler_items: List[ItemData] = [
    ItemData("Potion", ItemClassification.filler, 0x2000),
    ItemData("Hi-Potion", ItemClassification.filler, 0x2001),
    ItemData("X-Potion", ItemClassification.filler, 0x2002),
    ItemData("Mega-Potion", ItemClassification.filler, 0x2003),
    ItemData("Ether", ItemClassification.filler, 0x2004),
    ItemData("Turbo Ether", ItemClassification.filler, 0x2005),
    ItemData("Phoenix Down", ItemClassification.filler, 0x2006),
    ItemData("Mega Phoenix", ItemClassification.filler, 0x2007),
    ItemData("Elixir", ItemClassification.filler, 0x2008),
    ItemData("Megalixir", ItemClassification.filler, 0x2009),
    ItemData("Antidote", ItemClassification.filler, 0x200A),
    ItemData("Soft", ItemClassification.filler, 0x200B),
    ItemData("Eye Drops", ItemClassification.filler, 0x200C),
    ItemData("Echo Screen", ItemClassification.filler, 0x200D),
    ItemData("Holy Water", ItemClassification.filler, 0x200E),
    ItemData("Remedy", ItemClassification.filler, 0x200F),
    ItemData("1000 Gil", ItemClassification.filler, 0x1000),
]

normal_items: List[ItemData] = [
    ItemData("Power Distiller", ItemClassification.useful, 0x2010),
    ItemData("Mana Distiller", ItemClassification.useful, 0x2011),
    ItemData("Speed Distiller", ItemClassification.useful, 0x2012),
    ItemData("Ability Distiller", ItemClassification.useful, 0x2013),
    ItemData("Al Bhed Potion", ItemClassification.useful, 0x2014),
    ItemData("Healing Water", ItemClassification.useful, 0x2015),
    ItemData("Tetra Elemental", ItemClassification.useful, 0x2016),
    ItemData("Antarctic Wind", ItemClassification.useful, 0x2017),
    ItemData("Arctic Wind", ItemClassification.useful, 0x2018),
    ItemData("Ice Gem", ItemClassification.useful, 0x2019),
    ItemData("Bomb Fragment", ItemClassification.useful, 0x201A),
    ItemData("Bomb Core", ItemClassification.useful, 0x201B),
    ItemData("Fire Gem", ItemClassification.useful, 0x201C),
    ItemData("Electro Marble", ItemClassification.useful, 0x201D),
    ItemData("Lightning Marble", ItemClassification.useful, 0x201E),
    ItemData("Lightning Gem", ItemClassification.useful, 0x201F),
    ItemData("Fish Scale", ItemClassification.useful, 0x2020),
    ItemData("Dragon Scale", ItemClassification.useful, 0x2021),
    ItemData("Water Gem", ItemClassification.useful, 0x2022),
    ItemData("Grenade", ItemClassification.useful, 0x2023),
    ItemData("Frag Grenade", ItemClassification.useful, 0x2024),
    ItemData("Sleeping Powder", ItemClassification.useful, 0x2025),
    ItemData("Dream Powder", ItemClassification.useful, 0x2026),
    ItemData("Silence Grenade", ItemClassification.useful, 0x2027),
    ItemData("Smoke Bomb", ItemClassification.useful, 0x2028),
    ItemData("Shadow Gem", ItemClassification.useful, 0x2029),
    ItemData("Shining Gem", ItemClassification.useful, 0x202A),
    ItemData("Blessed Gem", ItemClassification.useful, 0x202B),
    ItemData("Supreme Gem", ItemClassification.useful, 0x202C),
    ItemData("Poison Fang", ItemClassification.useful, 0x202D),
    ItemData("Silver Hourglass", ItemClassification.useful, 0x202E),
    ItemData("Gold Hourglass", ItemClassification.useful, 0x202F),
    ItemData("Candle of Life", ItemClassification.useful, 0x2030),
    ItemData("Petrify Grenade", ItemClassification.useful, 0x2031),
    ItemData("Farplane Shadow", ItemClassification.useful, 0x2032),
    ItemData("Farplane Wind", ItemClassification.useful, 0x2033),
    ItemData("[Designer Wallet]", ItemClassification.useful, 0x2034),
    ItemData("Dark Matter", ItemClassification.useful, 0x2035),
    ItemData("Chocobo Feather", ItemClassification.useful, 0x2036),
    ItemData("Chocobo Wing", ItemClassification.useful, 0x2037),
    ItemData("Lunar Curtain", ItemClassification.useful, 0x2038),
    ItemData("Light Curtain", ItemClassification.useful, 0x2039),
    ItemData("Star Curtain", ItemClassification.useful, 0x203A),
    ItemData("Healing Spring", ItemClassification.useful, 0x203B),
    ItemData("Mana Spring", ItemClassification.useful, 0x203C),
    ItemData("Stamina Spring", ItemClassification.useful, 0x203D),
    ItemData("Soul Spring", ItemClassification.useful, 0x203E),
    ItemData("Purifying Salt", ItemClassification.useful, 0x203F),
    ItemData("Stamina Tablet", ItemClassification.useful, 0x2040),
    ItemData("Mana Tablet", ItemClassification.useful, 0x2041),
    ItemData("Twin Stars", ItemClassification.useful, 0x2042),
    ItemData("Stamina Tonic", ItemClassification.useful, 0x2043),
    ItemData("Mana Tonic", ItemClassification.useful, 0x2044),
    ItemData("Three Stars", ItemClassification.useful, 0x2045),
    ItemData("[Power Sphere]", ItemClassification.useful, 0x2046),
    ItemData("[Mana Sphere]", ItemClassification.useful, 0x2047),
    ItemData("[Speed Sphere]", ItemClassification.useful, 0x2048),
    ItemData("[Ability Sphere]", ItemClassification.useful, 0x2049),
    ItemData("[Fortune Sphere]", ItemClassification.useful, 0x204A),
    ItemData("[Attribute Sphere]", ItemClassification.useful, 0x204B),
    ItemData("[Special Sphere]", ItemClassification.useful, 0x204C),
    ItemData("[Skill Sphere]", ItemClassification.useful, 0x204D),
    ItemData("[Wht Magic Sphere]", ItemClassification.useful, 0x204E),
    ItemData("[Blk Magic Sphere]", ItemClassification.useful, 0x204F),
    ItemData("[Master Sphere]", ItemClassification.useful, 0x2050),
    ItemData("[Lv. 1 Key Sphere]", ItemClassification.useful, 0x2051),
    ItemData("[Lv. 2 Key Sphere]", ItemClassification.useful, 0x2052),
    ItemData("[Lv. 3 Key Sphere]", ItemClassification.useful, 0x2053),
    ItemData("[Lv. 4 Key Sphere]", ItemClassification.useful, 0x2054),
    ItemData("[HP Sphere]", ItemClassification.useful, 0x2055),
    ItemData("[MP Sphere]", ItemClassification.useful, 0x2056),
    ItemData("[Strength Sphere]", ItemClassification.useful, 0x2057),
    ItemData("[Defense Sphere]", ItemClassification.useful, 0x2058),
    ItemData("[Magic Sphere]", ItemClassification.useful, 0x2059),
    ItemData("[Magic Def Sphere]", ItemClassification.useful, 0x205A),
    ItemData("[Agility Sphere]", ItemClassification.useful, 0x205B),
    ItemData("[Evasion Sphere]", ItemClassification.useful, 0x205C),
    ItemData("[Accuracy Sphere]", ItemClassification.useful, 0x205D),
    ItemData("[Luck Sphere]", ItemClassification.useful, 0x205E),
    ItemData("[Clear Sphere]", ItemClassification.useful, 0x205F),
    ItemData("[Return Sphere]", ItemClassification.useful, 0x2060),
    ItemData("[Friend Sphere]", ItemClassification.useful, 0x2061),
    ItemData("[Teleport Sphere]", ItemClassification.useful, 0x2062),
    ItemData("[Warp Sphere]", ItemClassification.useful, 0x2063),
    ItemData("[Map]", ItemClassification.useful, 0x2064),
    ItemData("[Rename Card]", ItemClassification.useful, 0x2065),
    ItemData("[Musk]", ItemClassification.useful, 0x2066),
    ItemData("[Hypello Potion]", ItemClassification.useful, 0x2067),
    ItemData("[Shining Thorn]", ItemClassification.useful, 0x2068),
    ItemData("[Pendulum]", ItemClassification.useful, 0x2069),
    ItemData("[Amulet]", ItemClassification.useful, 0x206A),
    ItemData("[Door to Tomorrow]", ItemClassification.useful, 0x206B),
    ItemData("[Wings to Discovery]", ItemClassification.useful, 0x206C),
    ItemData("[Gambler's Spirit]", ItemClassification.useful, 0x206D),
    ItemData("[Underdog's Secret]", ItemClassification.useful, 0x206E),
    ItemData("[Winning Formula]", ItemClassification.useful, 0x206F),
]

key_items: List[ItemData] = [
    ItemData("Withered Bouquet", ItemClassification.progression, 0xA000),
    ItemData("Flint", ItemClassification.progression, 0xA001),
    ItemData("Cloudy Mirror", ItemClassification.progression, 0xA002),
    ItemData("Celestial Mirror", ItemClassification.progression, 0xA003),
    ItemData("Al Bhed Primer I", ItemClassification.progression, 0xA004),
    ItemData("Al Bhed Primer II", ItemClassification.progression, 0xA005),
    ItemData("Al Bhed Primer III", ItemClassification.progression, 0xA006),
    ItemData("Al Bhed Primer IV", ItemClassification.progression, 0xA007),
    ItemData("Al Bhed Primer V", ItemClassification.progression, 0xA008),
    ItemData("Al Bhed Primer VI", ItemClassification.progression, 0xA009),
    ItemData("Al Bhed Primer VII", ItemClassification.progression, 0xA00A),
    ItemData("Al Bhed Primer VIII", ItemClassification.progression, 0xA00B),
    ItemData("Al Bhed Primer IX", ItemClassification.progression, 0xA00C),
    ItemData("Al Bhed Primer X", ItemClassification.progression, 0xA00D),
    ItemData("Al Bhed Primer XI", ItemClassification.progression, 0xA00E),
    ItemData("Al Bhed Primer XII", ItemClassification.progression, 0xA00F),
    ItemData("Al Bhed Primer XIII", ItemClassification.progression, 0xA010),
    ItemData("Al Bhed Primer XIV", ItemClassification.progression, 0xA011),
    ItemData("Al Bhed Primer XV", ItemClassification.progression, 0xA012),
    ItemData("Al Bhed Primer XVI", ItemClassification.progression, 0xA013),
    ItemData("Al Bhed Primer XVII", ItemClassification.progression, 0xA014),
    ItemData("Al Bhed Primer XVIII", ItemClassification.progression, 0xA015),
    ItemData("Al Bhed Primer XIX", ItemClassification.progression, 0xA016),
    ItemData("Al Bhed Primer XX", ItemClassification.progression, 0xA017),
    ItemData("Al Bhed Primer XXI", ItemClassification.progression, 0xA018),
    ItemData("Al Bhed Primer XXII", ItemClassification.progression, 0xA019),
    ItemData("Al Bhed Primer XXIII", ItemClassification.progression, 0xA01A),
    ItemData("Al Bhed Primer XXIV", ItemClassification.progression, 0xA01B),
    ItemData("Al Bhed Primer XXV", ItemClassification.progression, 0xA01C),
    ItemData("Al Bhed Primer XXVI", ItemClassification.progression, 0xA01D),
    ItemData("Summoner's Soul", ItemClassification.progression, 0xA01E),
    ItemData("Aeon's Soul", ItemClassification.progression, 0xA01F),
    ItemData("Jecht's Sphere", ItemClassification.progression, 0xA020),
    ItemData("Rusty Sword", ItemClassification.progression, 0xA021),
    # ItemData("", ItemClassification.progression, 0xA022),
    ItemData("Sun Crest", ItemClassification.progression, 0xA023),
    ItemData("Sun Sigil", ItemClassification.progression, 0xA024),
    ItemData("Moon Crest", ItemClassification.progression, 0xA025),
    ItemData("Moon Sigil", ItemClassification.progression, 0xA026),
    ItemData("Mars Crest", ItemClassification.progression, 0xA027),
    ItemData("Mars Sigil", ItemClassification.progression, 0xA028),
    ItemData("Mark of Conquest", ItemClassification.progression, 0xA029),
    ItemData("Saturn Crest", ItemClassification.progression, 0xA02A),
    ItemData("Saturn Sigil", ItemClassification.progression, 0xA02B),
    ItemData("Jupiter Crest", ItemClassification.progression, 0xA02C),
    ItemData("Jupiter Sigil", ItemClassification.progression, 0xA02D),
    ItemData("Venus Crest", ItemClassification.progression, 0xA02E),
    ItemData("Venus Sigil", ItemClassification.progression, 0xA02F),
    ItemData("Mercury Crest", ItemClassification.progression, 0xA030),
    ItemData("Mercury Sigil", ItemClassification.progression, 0xA031),
    ItemData("Blossom Crown", ItemClassification.progression, 0xA032),
    ItemData("Flower Scepter", ItemClassification.progression, 0xA033),
    # ItemData("", ItemClassification.progression, 0xA034),
    # ItemData("", ItemClassification.progression, 0xA035),
    # ItemData("", ItemClassification.progression, 0xA036),
    # ItemData("", ItemClassification.progression, 0xA037),
    # ItemData("", ItemClassification.progression, 0xA038),
    # ItemData("", ItemClassification.progression, 0xA039),
    # ItemData("", ItemClassification.progression, 0xA03A),
    # ItemData("", ItemClassification.progression, 0xA03B),
    # ItemData("", ItemClassification.progression, 0xA03C),
    # ItemData("", ItemClassification.progression, 0xA03D),
    # ItemData("", ItemClassification.progression, 0xA03E),
    # ItemData("", ItemClassification.progression, 0xA03F),
]

weapons: List[ItemData] = [
    ItemData("Weapon (Tidus): Crystal Sword", ItemClassification.useful, 0x5000),  # Offset=0014 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Firestrike [801Eh], Icestrike [8022h], Lightningstrike [8026h], Waterstrike [802Ah]} }
    ItemData("Weapon (Tidus): Brotherhood", ItemClassification.useful, 0x5001),  # Offset=0024 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Strength +5% [8063h], Strength +10% [8064h], Waterstrike [802Ah], Sensor [8000h]}, Brotherhood }
    ItemData("Weapon (Yuna): Astral Rod", ItemClassification.useful, 0x5002),  # Offset=0034 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {One MP Cost [800Dh], Empty, Empty, Empty} }
    ItemData("Weapon (Lulu): Onion Knight", ItemClassification.useful, 0x5003),  # Offset=0044 Weapon [00h], Formula=Celestial MP-based [12h], Power=16, Crit=3%, Slots=4 {No AP [8014h], Empty, Empty, Empty}, Celestial }
    ItemData("Weapon (Tidus): FLametongue", ItemClassification.useful, 0x5004),  # Offset=0054 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Firestrike [801Eh]} }
    ItemData("Weapon (Yuna): Rod of Wisdom", ItemClassification.useful, 0x5005),  # Offset=0064 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Magic +5% [8067h], !Magic +3% [8066h], !Sensor [8000h]} }
    ItemData("Weapon (Kimahri): Red Armlet", ItemClassification.useful, 0x5006),  # Offset=0074 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=3 {Fire Ward [801Fh], Ice Ward [8023h], Lightning Ward [8027h]} }
    ItemData("Weapon (Lulu): Serene Bangle", ItemClassification.useful, 0x5007),  # Offset=0084 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Berserk Ward [8051h]} }
    ItemData("Weapon (Wakka): Scout", ItemClassification.useful, 0x5008),  # Offset=0094 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Icestrike [8022h], Sensor [8000h]} }
    ItemData("Weapon (Tidus): NulBlaze Shield", ItemClassification.useful, 0x5009),  # Offset=00A4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {SOS NulBlaze [8061h]} }
    ItemData("Weapon (Kimahri): Tidal Spear", ItemClassification.useful, 0x500a),  # Offset=00B4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Piercing [800Bh], Waterstrike [802Ah]} }
    ItemData("Weapon (Tidus): Ice Brand", ItemClassification.useful, 0x500b),  # Offset=00C4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Icestrike [8022h]} }
    ItemData("Weapon (Auron): Thunder Blade", ItemClassification.useful, 0x500c),  # Offset=00D4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Piercing [800Bh], Lightningstrike [8026h]} }
    ItemData("Weapon (Wakka): Scout", ItemClassification.useful, 0x500d),  # Offset=00E4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Lightningstrike [8026h], Sensor [8000h]} }
    ItemData("Weapon (Kimahri): Heat Lance", ItemClassification.useful, 0x500e),  # Offset=00F4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Piercing [800Bh], Firestrike [801Eh]} }
    ItemData("Weapon (Auron) 15", ItemClassification.useful, 0x500f),  # Offset=0104 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {HP +5% [8072h], Berserk Ward [8051h]} }
    ItemData("Weapon (Lulu) 16", ItemClassification.useful, 0x5010),  # Offset=0114 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Dark Ward [8049h], Empty} }
    ItemData("Weapon (Yuna) 17", ItemClassification.useful, 0x5011),  # Offset=0124 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Lightning Ward [8027h], Poison Ward [803Dh]} }
    ItemData("Weapon (Kimahri) 18", ItemClassification.useful, 0x5012),  # Offset=0134 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Dark Ward [8049h], Berserk Ward [8051h]} }
    ItemData("Weapon (Wakka) 19", ItemClassification.useful, 0x5013),  # Offset=0144 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Strength +3% [8062h], Strength +5% [8063h]} }
    ItemData("Weapon (Lulu) 20", ItemClassification.useful, 0x5014),  # Offset=0154 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Sleeptouch [803Fh]} }
    ItemData("Weapon (Yuna) 21", ItemClassification.useful, 0x5015),  # Offset=0164 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Silence Ward [8045h], Confuse Ward [804Fh]} }
    ItemData("Weapon (Tidus) 22", ItemClassification.useful, 0x5016),  # Offset=0174 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Counterattack [8003h]} }
    ItemData("Weapon (Lulu) 23", ItemClassification.useful, 0x5017),  # Offset=0184 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Silencetouch [8043h], Magic +5% [8067h]} }
    ItemData("Weapon (Rikku) 24", ItemClassification.useful, 0x5018),  # Offset=0194 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {SOS Shell [8059h]} }
    ItemData("Weapon (Kimahri) 25", ItemClassification.useful, 0x5019),  # Offset=01A4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Poison Ward [803Dh], Confuse Ward [804Fh], Silence Ward [8045h], Empty} }
    ItemData("Weapon (Wakka) 26", ItemClassification.useful, 0x501a),  # Offset=01B4 Weapon [00h], Formula=Celestial HP-based [11h], Power=16, Crit=3%, Slots=4 {No AP [8014h], Empty, Empty, Empty}, Celestial }
    ItemData("Weapon (Wakka): Scout", ItemClassification.useful, 0x501b),  # Offset=01C4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Sensor [8000h]} }
    ItemData("Weapon (Kimahri): Ice Lance", ItemClassification.useful, 0x501c),  # Offset=01D4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Piercing [800Bh], Icestrike [8022h]} }
    ItemData("Weapon (Yuna): Moon Ring", ItemClassification.useful, 0x501d),  # Offset=01E4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {SOS Shell [8059h], SOS Protect [805Ah]} }
    ItemData("Weapon (Auron) 30", ItemClassification.useful, 0x501e),  # Offset=01F4 Weapon [00h], Formula=Celestial Auron [13h], Power=16, Crit=3%, Slots=4 {No AP [8014h], Empty, Empty, Empty}, Celestial }
    ItemData("Weapon (Tidus) 31", ItemClassification.useful, 0x501f),  # Offset=0204 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Counterattack [8003h]} }
    ItemData("Weapon (Wakka) 32", ItemClassification.useful, 0x5020),  # Offset=0214 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Evade & Counter [8004h]} }
    ItemData("Weapon (Kimahri) 33", ItemClassification.useful, 0x5021),  # Offset=0224 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=3 {Strength +3% [8062h], Strength +5% [8063h], Strength +10% [8064h]} }
    ItemData("Weapon (Yuna) 34", ItemClassification.useful, 0x5022),  # Offset=0234 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=3 {Silence Ward [8045h], Confuse Ward [804Fh], Poison Ward [803Dh]} }
    ItemData("Weapon (Wakka) 35", ItemClassification.useful, 0x5023),  # Offset=0244 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Fire Ward [801Fh], Dark Ward [8049h]} }
    ItemData("Weapon (Yuna): Nirvana", ItemClassification.useful, 0x5024),  # Offset=0254 Weapon [00h], Formula=Celestial MP-based [12h], Power=16, Crit=3%, Slots=4 {No AP [8014h], Empty, Empty, Empty}, Celestial }
    ItemData("Weapon (Tidus): Caladbolg", ItemClassification.useful, 0x5025),  # Offset=0264 Weapon [00h], Formula=Celestial HP-based [11h], Power=16, Crit=3%, Slots=4 {No AP [8014h], Empty, Empty, Empty}, Celestial }
    ItemData("Weapon (Kimahri) 38", ItemClassification.useful, 0x5026),  # Offset=0274 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {HP +10% [8073h], Empty, Empty, Empty} }
    ItemData("Weapon (Rikku) 39", ItemClassification.useful, 0x5027),  # Offset=0284 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Empty, Empty, Empty, Empty} }
    ItemData("Weapon (Auron) 40", ItemClassification.useful, 0x5028),  # Offset=0294 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Stoneproof [8038h], Poisonproof [803Ch]} }
    ItemData("Weapon (Wakka) 41", ItemClassification.useful, 0x5029),  # Offset=02A4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=3 {SOS NulFrost [805Fh], SOS NulShock [8060h], SOS NulBlaze [8061h]} }
    ItemData("Weapon (Yuna) 42", ItemClassification.useful, 0x502a),  # Offset=02B4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {HP Stroll [801Bh]} }
    ItemData("Weapon (Rikku) 43", ItemClassification.useful, 0x502b),  # Offset=02C4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {MP Stroll [801Ch]} }
    ItemData("Weapon (Auron) 44", ItemClassification.useful, 0x502c),  # Offset=02D4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Silenceproof [8044h], Darkproof [8048h]} }
    ItemData("Weapon (Wakka) 45", ItemClassification.useful, 0x502d),  # Offset=02E4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Magic Counter [8005h], Counterattack [8003h]} }
    ItemData("Weapon (Kimahri) 46", ItemClassification.useful, 0x502e),  # Offset=02F4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Stoneproof [8038h], Poisonproof [803Ch], Empty, Empty} }
    ItemData("Weapon (Yuna) 47", ItemClassification.useful, 0x502f),  # Offset=0304 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Ice Eater [8025h], Fire Eater [8021h], Lightning Eater [8029h], Empty} }
    ItemData("Weapon (Lulu) 48", ItemClassification.useful, 0x5030),  # Offset=0314 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Half MP Cost [800Ch]} }
    ItemData("Weapon (Rikku) 49", ItemClassification.useful, 0x5031),  # Offset=0324 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Double AP [8012h], !Double Overdrive [800Eh]} }
    ItemData("Weapon (Kimahri) 50", ItemClassification.useful, 0x5032),  # Offset=0334 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Magic +3% [8066h], Magic +5% [8067h], Magic +10% [8068h], Empty} }
    ItemData("Weapon (Yuna) 51", ItemClassification.useful, 0x5033),  # Offset=0344 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Water Eater [802Dh], Fire Eater [8021h], Lightning Eater [8029h], Empty} }
    ItemData("Weapon (Wakka) 52", ItemClassification.useful, 0x5034),  # Offset=0354 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Waterstrike [802Ah], Firestrike [801Eh], Lightningstrike [8026h], Icestrike [8022h]} }
    ItemData("Weapon (Auron) 53", ItemClassification.useful, 0x5035),  # Offset=0364 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Darkproof [8048h], Deathproof [8030h], Empty, Empty} }
    ItemData("Weapon (Yuna) 54", ItemClassification.useful, 0x5036),  # Offset=0374 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {SOS Overdrive [8010h]} }
    ItemData("Weapon (Wakka) 55", ItemClassification.useful, 0x5037),  # Offset=0384 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Waterstrike [802Ah], Empty} }
    ItemData("Weapon (Kimahri) 56", ItemClassification.useful, 0x5038),  # Offset=0394 Weapon [00h], Formula=Celestial HP-based [11h], Power=16, Crit=3%, Slots=4 {No AP [8014h], Empty, Empty, Empty}, Celestial }
    ItemData("Weapon (Yuna) 57", ItemClassification.useful, 0x5039),  # Offset=03A4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Stone Ward [8039h], HP +5% [8072h]} }
    ItemData("Weapon (Tidus) 58", ItemClassification.useful, 0x503a),  # Offset=03B4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Strength +3% [8062h], Strength +5% [8063h]} }
    ItemData("Weapon (Lulu) 59", ItemClassification.useful, 0x503b),  # Offset=03C4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Magic +3% [8066h], Magic +5% [8067h], Magic +20% [8069h], Empty} }
    ItemData("Weapon (Yuna) 60", ItemClassification.useful, 0x503c),  # Offset=03D4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=3 {Half MP Cost [800Ch], Empty, Empty} }
    ItemData("Weapon (Rikku) 61", ItemClassification.useful, 0x503d),  # Offset=03E4 Weapon [00h], Formula=Celestial HP-based [11h], Power=16, Crit=3%, Slots=4 {No AP [8014h], Empty, Empty, Empty}, Celestial }
    ItemData("Weapon (Yuna) 62", ItemClassification.useful, 0x503e),  # Offset=03F4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {HP +10% [8073h]} }
    ItemData("Weapon (Tidus) 63", ItemClassification.useful, 0x503f),  # Offset=0404 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Strength +3% [8062h], Empty, Empty, Empty} }
    ItemData("Weapon (Yuna) 64", ItemClassification.useful, 0x5040),  # Offset=0414 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Stoneproof [8038h], Empty} }
    ItemData("Weapon (Kimahri) 65", ItemClassification.useful, 0x5041),  # Offset=0424 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Magic +20% [8069h], Empty} }
    ItemData("Weapon (Kimahri) 66", ItemClassification.useful, 0x5042),  # Offset=0434 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=3 {Piercing [800Bh], Sensor [8000h], Strength +10% [8064h]} }
    ItemData("Weapon (Yuna) 67", ItemClassification.useful, 0x5043),  # Offset=0444 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {HP +10% [8073h], Fire Ward [801Fh]} }
    ItemData("Weapon (Lulu) 68", ItemClassification.useful, 0x5044),  # Offset=0454 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {HP +20% [8074h], Empty} }
    ItemData("Weapon (Tidus) 69", ItemClassification.useful, 0x5045),  # Offset=0464 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Lightningproof [8028h], Empty} }
    ItemData("Weapon (Wakka) 70", ItemClassification.useful, 0x5046),  # Offset=0474 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Magic +20% [8069h], Magic +10% [8068h], Magic +5% [8067h], Magic +3% [8066h]} }
    ItemData("Weapon (Yuna) 71", ItemClassification.useful, 0x5047),  # Offset=0484 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {HP +10% [8073h], Empty} }
    ItemData("Weapon (Rikku) 72", ItemClassification.useful, 0x5048),  # Offset=0494 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Lightningproof [8028h], Fireproof [8020h], Iceproof [8024h], Empty} }
    ItemData("Weapon (Auron) 73", ItemClassification.useful, 0x5049),  # Offset=04A4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Piercing [800Bh], One MP Cost [800Dh], Empty, Empty} }
    ItemData("Weapon (Yuna) 74", ItemClassification.useful, 0x504a),  # Offset=04B4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {HP +10% [8073h], Silence Ward [8045h]} }
    ItemData("Weapon (Kimahri) 75", ItemClassification.useful, 0x504b),  # Offset=04C4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Magic Counter [8005h], Evade & Counter [8004h], Empty, Empty} }
    ItemData("Weapon (Rikku) 76", ItemClassification.useful, 0x504c),  # Offset=04D4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=3 {Initiative [8002h], Poisonstrike [803Ah], Empty} }
    ItemData("Weapon (Lulu) 77", ItemClassification.useful, 0x504d),  # Offset=04E4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Ice Eater [8025h], Fire Eater [8021h], !Water Eater [802Dh]} }
    ItemData("Weapon (Tidus) 78", ItemClassification.useful, 0x504e),  # Offset=04F4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Double AP [8012h]} }
    ItemData("Weapon (Wakka) 79", ItemClassification.useful, 0x504f),  # Offset=0504 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Magic Counter [8005h], Empty} }
    ItemData("Weapon (Auron) 80", ItemClassification.useful, 0x5050),  # Offset=0514 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=3 {Silencestrike [8042h], Stonestrike [8036h], Empty} }
    ItemData("Weapon (Yuna) 81", ItemClassification.useful, 0x5051),  # Offset=0524 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Magic +10% [8068h], Magic +5% [8067h], Magic +3% [8066h], Empty} }
    ItemData("Weapon (Kimahri) 82", ItemClassification.useful, 0x5052),  # Offset=0534 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Strength +10% [8064h], Strength +5% [8063h], Strength +3% [8062h], Empty} }
    ItemData("Weapon (Rikku) 83", ItemClassification.useful, 0x5053),  # Offset=0544 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {One MP Cost [800Dh], Sensor [8000h]} }
    ItemData("Weapon (Lulu) 84", ItemClassification.useful, 0x5054),  # Offset=0554 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Deathstrike [802Eh], Empty, Empty, Empty} }
    ItemData("Weapon (Tidus) 85", ItemClassification.useful, 0x5055),  # Offset=0564 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {SOS Overdrive [8010h]} }
]

party_members: List[ItemData] = [
    ItemData("Party Member: Tidus", ItemClassification.useful, 0xF000),
    ItemData("Party Member: Yuna", ItemClassification.useful, 0xF001),
    ItemData("Party Member: Auron", ItemClassification.useful, 0xF002),
    ItemData("Party Member: Kimahri", ItemClassification.useful, 0xF003),
    ItemData("Party Member: Wakka", ItemClassification.useful, 0xF004),
    ItemData("Party Member: Lulu", ItemClassification.useful, 0xF005),
    ItemData("Party Member: Rikku", ItemClassification.useful, 0xF006),
    # ItemData("Party Member: Seymour", ItemClassification.useful, 0xF007),
    ItemData("Party Member: Valefor", ItemClassification.useful, 0xF008),
    ItemData("Party Member: Ifrit", ItemClassification.useful, 0xF009),
    ItemData("Party Member: Ixion", ItemClassification.useful, 0xF00A),
    ItemData("Party Member: Shiva", ItemClassification.useful, 0xF00B),
    ItemData("Party Member: Bahamut", ItemClassification.useful, 0xF00C),
    ItemData("Party Member: Anima", ItemClassification.useful, 0xF00D),
    ItemData("Party Member: Yojimbo", ItemClassification.useful, 0xF00E),
    ItemData("Party Member: Magus Sisters", ItemClassification.useful, 0xF00F),  # Sisters are 0x0f, 0x10, 0x11
]

AllItems = normal_items + key_items + weapons + filler_items

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
