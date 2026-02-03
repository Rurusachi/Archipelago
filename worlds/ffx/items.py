from typing import NamedTuple
from itertools import chain
import re

from BaseClasses import Item, ItemClassification


class ItemData(NamedTuple):
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


normalItemOffset      = 0x2000
keyItemOffset         = 0xA000
equipItemOffset       = 0x5000
partyMemberItemOffset = 0xF000
regionItemOffset      = 0xE000
abilityItemOffset     = 0xD000
gilItemOffset         = 0x1000
trapItemOffset        = 0x9000




normal_items: list[ItemData] = [ItemData(f"{x[0]} x {i}", x[1], x[2] | normalItemOffset | (i << 16)) for i in range(10, 100, 10) for x in [
    ("Potion",               ItemClassification.filler, 0x0000),
    ("Hi-Potion",            ItemClassification.filler, 0x0001),
    ("X-Potion",             ItemClassification.filler, 0x0002),
    ("Mega-Potion",          ItemClassification.filler, 0x0003),
    ("Ether",                ItemClassification.filler, 0x0004),
    ("Turbo Ether",          ItemClassification.filler, 0x0005),
    ("Phoenix Down",         ItemClassification.filler, 0x0006),
    ("Mega Phoenix",         ItemClassification.useful, 0x0007),
    ("Elixir",               ItemClassification.filler, 0x0008),
    ("Megalixir",            ItemClassification.filler, 0x0009),
    ("Antidote",             ItemClassification.filler, 0x000A),
    ("Soft",                 ItemClassification.filler, 0x000B),
    ("Eye Drops",            ItemClassification.filler, 0x000C),
    ("Echo Screen",          ItemClassification.filler, 0x000D),
    ("Holy Water",           ItemClassification.filler, 0x000E),
    ("Remedy",               ItemClassification.filler, 0x000F),
    # ("Power Distiller",      ItemClassification.useful, 0x0010),
    # ("Mana Distiller",       ItemClassification.useful, 0x0011),
    # ("Speed Distiller",      ItemClassification.useful, 0x0012),
    # ("Ability Distiller",    ItemClassification.useful, 0x0013),
    ("Al Bhed Potion",       ItemClassification.useful, 0x0014),
    ("Healing Water",        ItemClassification.useful, 0x0015),
    ("Tetra Elemental",      ItemClassification.useful, 0x0016),
    ("Antarctic Wind",       ItemClassification.useful, 0x0017),
    ("Arctic Wind",          ItemClassification.useful, 0x0018),
    ("Ice Gem",              ItemClassification.useful, 0x0019),
    ("Bomb Fragment",        ItemClassification.useful, 0x001A),
    ("Bomb Core",            ItemClassification.useful, 0x001B),
    ("Fire Gem",             ItemClassification.useful, 0x001C),
    ("Electro Marble",       ItemClassification.useful, 0x001D),
    ("Lightning Marble",     ItemClassification.useful, 0x001E),
    ("Lightning Gem",        ItemClassification.useful, 0x001F),
    ("Fish Scale",           ItemClassification.useful, 0x0020),
    ("Dragon Scale",         ItemClassification.useful, 0x0021),
    ("Water Gem",            ItemClassification.useful, 0x0022),
    ("Grenade",              ItemClassification.useful, 0x0023),
    ("Frag Grenade",         ItemClassification.useful, 0x0024),
    ("Sleeping Powder",      ItemClassification.useful, 0x0025),
    ("Dream Powder",         ItemClassification.useful, 0x0026),
    ("Silence Grenade",      ItemClassification.useful, 0x0027),
    ("Smoke Bomb",           ItemClassification.useful, 0x0028),
    ("Shadow Gem",           ItemClassification.useful, 0x0029),
    ("Shining Gem",          ItemClassification.useful, 0x002A),
    ("Blessed Gem",          ItemClassification.useful, 0x002B),
    ("Supreme Gem",          ItemClassification.useful, 0x002C),
    ("Poison Fang",          ItemClassification.useful, 0x002D),
    ("Silver Hourglass",     ItemClassification.useful, 0x002E),
    ("Gold Hourglass",       ItemClassification.useful, 0x002F),
    ("Candle of Life",       ItemClassification.useful, 0x0030),
    ("Petrify Grenade",      ItemClassification.useful, 0x0031),
    ("Farplane Shadow",      ItemClassification.useful, 0x0032),
    ("Farplane Wind",        ItemClassification.useful, 0x0033),
    ("[Designer Wallet]",    ItemClassification.useful, 0x0034),
    ("Dark Matter",          ItemClassification.useful, 0x0035),
    ("Chocobo Feather",      ItemClassification.useful, 0x0036),
    ("Chocobo Wing",         ItemClassification.useful, 0x0037),
    ("Lunar Curtain",        ItemClassification.useful, 0x0038),
    ("Light Curtain",        ItemClassification.useful, 0x0039),
    ("Star Curtain",         ItemClassification.useful, 0x003A),
    ("Healing Spring",       ItemClassification.useful, 0x003B),
    ("Mana Spring",          ItemClassification.useful, 0x003C),
    ("Stamina Spring",       ItemClassification.useful, 0x003D),
    ("Soul Spring",          ItemClassification.useful, 0x003E),
    ("Purifying Salt",       ItemClassification.useful, 0x003F),
    ("Stamina Tablet",       ItemClassification.useful, 0x0040),
    ("Mana Tablet",          ItemClassification.useful, 0x0041),
    ("Twin Stars",           ItemClassification.useful, 0x0042),
    ("Stamina Tonic",        ItemClassification.useful, 0x0043),
    ("Mana Tonic",           ItemClassification.useful, 0x0044),
    ("Three Stars",          ItemClassification.useful, 0x0045),
    #("[Power Sphere]",       ItemClassification.useful, 0x0046), # Infinite supply
    #("[Mana Sphere]",        ItemClassification.useful, 0x0047), # Infinite supply
    #("[Speed Sphere]",       ItemClassification.useful, 0x0048), # Infinite supply
    #("[Ability Sphere]",     ItemClassification.useful, 0x0049), # Infinite supply
    ("[Fortune Sphere]",     ItemClassification.useful, 0x004A),
    ("[Attribute Sphere]",   ItemClassification.useful, 0x004B),
    ("[Special Sphere]",     ItemClassification.useful, 0x004C),
    ("[Skill Sphere]",       ItemClassification.useful, 0x004D),
    ("[Wht Magic Sphere]",   ItemClassification.useful, 0x004E),
    ("[Blk Magic Sphere]",   ItemClassification.useful, 0x004F),
    ("[Master Sphere]",      ItemClassification.useful, 0x0050),
    ("[Lv. 1 Key Sphere]",   ItemClassification.useful, 0x0051),
    ("[Lv. 2 Key Sphere]",   ItemClassification.useful, 0x0052),
    ("[Lv. 3 Key Sphere]",   ItemClassification.useful, 0x0053),
    ("[Lv. 4 Key Sphere]",   ItemClassification.useful, 0x0054),
    ("[HP Sphere]",          ItemClassification.useful, 0x0055),
    ("[MP Sphere]",          ItemClassification.useful, 0x0056),
    ("[Strength Sphere]",    ItemClassification.useful, 0x0057),
    ("[Defense Sphere]",     ItemClassification.useful, 0x0058),
    ("[Magic Sphere]",       ItemClassification.useful, 0x0059),
    ("[Magic Def Sphere]",   ItemClassification.useful, 0x005A),
    ("[Agility Sphere]",     ItemClassification.useful, 0x005B),
    ("[Evasion Sphere]",     ItemClassification.useful, 0x005C),
    ("[Accuracy Sphere]",    ItemClassification.useful, 0x005D),
    ("[Luck Sphere]",        ItemClassification.useful, 0x005E),
    ("[Clear Sphere]",       ItemClassification.useful, 0x005F),
    ("[Return Sphere]",      ItemClassification.useful, 0x0060),
    ("[Friend Sphere]",      ItemClassification.useful, 0x0061),
    ("[Teleport Sphere]",    ItemClassification.useful, 0x0062),
    ("[Warp Sphere]",        ItemClassification.useful, 0x0063),
    ("[Map]",                ItemClassification.useful, 0x0064),
    ("[Rename Card]",        ItemClassification.useful, 0x0065),
    ("[Musk]",               ItemClassification.useful, 0x0066),
    ("[Hypello Potion]",     ItemClassification.useful, 0x0067),
    ("[Shining Thorn]",      ItemClassification.useful, 0x0068),
    ("[Pendulum]",           ItemClassification.useful, 0x0069),
    ("[Amulet]",             ItemClassification.useful, 0x006A),
    ("[Door to Tomorrow]",   ItemClassification.useful, 0x006B),
    ("[Wings to Discovery]", ItemClassification.useful, 0x006C),
    ("[Gambler's Spirit]",   ItemClassification.useful, 0x006D),
    ("[Underdog's Secret]",  ItemClassification.useful, 0x006E),
    ("[Winning Formula]",    ItemClassification.useful, 0x006F),
]]

key_items: list[ItemData] = [ItemData(x[0], x[1], x[2] | keyItemOffset) for x in [
    ("Withered Bouquet",     ItemClassification.progression, 0x0000),
    ("Flint",                ItemClassification.progression, 0x0001),
    ("Cloudy Mirror",        ItemClassification.progression, 0x0002),
    ("Celestial Mirror",     ItemClassification.progression, 0x0003),
    ("Al Bhed Primer I",     ItemClassification.progression, 0x0004),
    ("Al Bhed Primer II",    ItemClassification.progression, 0x0005),
    ("Al Bhed Primer III",   ItemClassification.progression, 0x0006),
    ("Al Bhed Primer IV",    ItemClassification.progression, 0x0007),
    ("Al Bhed Primer V",     ItemClassification.progression, 0x0008),
    ("Al Bhed Primer VI",    ItemClassification.progression, 0x0009),
    ("Al Bhed Primer VII",   ItemClassification.progression, 0x000A),
    ("Al Bhed Primer VIII",  ItemClassification.progression, 0x000B),
    ("Al Bhed Primer IX",    ItemClassification.progression, 0x000C),
    ("Al Bhed Primer X",     ItemClassification.progression, 0x000D),
    ("Al Bhed Primer XI",    ItemClassification.progression, 0x000E),
    ("Al Bhed Primer XII",   ItemClassification.progression, 0x000F),
    ("Al Bhed Primer XIII",  ItemClassification.progression, 0x0010),
    ("Al Bhed Primer XIV",   ItemClassification.progression, 0x0011),
    ("Al Bhed Primer XV",    ItemClassification.progression, 0x0012),
    ("Al Bhed Primer XVI",   ItemClassification.progression, 0x0013),
    ("Al Bhed Primer XVII",  ItemClassification.progression, 0x0014),
    ("Al Bhed Primer XVIII", ItemClassification.progression, 0x0015),
    ("Al Bhed Primer XIX",   ItemClassification.progression, 0x0016),
    ("Al Bhed Primer XX",    ItemClassification.progression, 0x0017),
    ("Al Bhed Primer XXI",   ItemClassification.progression, 0x0018),
    ("Al Bhed Primer XXII",  ItemClassification.progression, 0x0019),
    ("Al Bhed Primer XXIII", ItemClassification.progression, 0x001A),
    ("Al Bhed Primer XXIV",  ItemClassification.progression, 0x001B),
    ("Al Bhed Primer XXV",   ItemClassification.progression, 0x001C),
    ("Al Bhed Primer XXVI",  ItemClassification.progression, 0x001D),
    ("Summoner's Soul",      ItemClassification.progression, 0x001E),
    ("Aeon's Soul",          ItemClassification.progression, 0x001F),
    ("Jecht's Sphere",       ItemClassification.progression, 0x0020),
    ("Rusty Sword",          ItemClassification.progression, 0x0021),
    # ("",                   ItemClassification.progression, 0x0022),
    ("Sun Crest",            ItemClassification.progression, 0x0023),
    ("Sun Sigil",            ItemClassification.progression, 0x0024),
    ("Moon Crest",           ItemClassification.progression, 0x0025),
    ("Moon Sigil",           ItemClassification.progression, 0x0026),
    ("Mars Crest",           ItemClassification.progression, 0x0027),
    ("Mars Sigil",           ItemClassification.progression, 0x0028),
    ("Mark of Conquest",     ItemClassification.progression, 0x0029),
    ("Saturn Crest",         ItemClassification.progression, 0x002A),
    ("Saturn Sigil",         ItemClassification.progression, 0x002B),
    ("Jupiter Crest",        ItemClassification.progression, 0x002C),
    ("Jupiter Sigil",        ItemClassification.progression, 0x002D),
    ("Venus Crest",          ItemClassification.progression, 0x002E),
    ("Venus Sigil",          ItemClassification.progression, 0x002F),
    ("Mercury Crest",        ItemClassification.progression, 0x0030),
    ("Mercury Sigil",        ItemClassification.progression, 0x0031),
    ("Blossom Crown",        ItemClassification.progression, 0x0032),
    ("Flower Scepter",       ItemClassification.progression, 0x0033),
    # ("",                   ItemClassification.progression, 0x0034),
    # ("",                   ItemClassification.progression, 0x0035),
    # ("",                   ItemClassification.progression, 0x0036),
    # ("",                   ItemClassification.progression, 0x0037),
    # ("",                   ItemClassification.progression, 0x0038),
    # ("",                   ItemClassification.progression, 0x0039),
    # ("",                   ItemClassification.progression, 0x003A),
    # ("",                   ItemClassification.progression, 0x003B),
    # ("",                   ItemClassification.progression, 0x003C),
    # ("",                   ItemClassification.progression, 0x003D),
    # ("",                   ItemClassification.progression, 0x003E),
    # ("",                   ItemClassification.progression, 0x003F),
]]

equip_items: list[ItemData] = [ItemData(x[0], x[1], x[2] | equipItemOffset) for x in [
    ("Weapon (Tidus): Crystal Sword",       ItemClassification.useful     , 0x0000),  # Offset=0014 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Firestrike [801Eh], Icestrike [8022h], Lightningstrike [8026h], Waterstrike [802Ah]} }
    ("Weapon (Tidus): Brotherhood",         ItemClassification.progression, 0x0001),  # Offset=0024 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Strength +5% [8063h], Strength +10% [8064h], Waterstrike [802Ah], Sensor [8000h]}, Brotherhood }
    ("Weapon (Yuna): Astral Rod",           ItemClassification.useful     , 0x0002),  # Offset=0034 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {One MP Cost [800Dh], Empty, Empty, Empty} }
    ("Weapon (Lulu): Onion Knight",         ItemClassification.progression, 0x0003),  # Offset=0044 Weapon [00h], Formula=Celestial MP-based [12h], Power=16, Crit=3%, Slots=4 {No AP [8014h], Empty, Empty, Empty}, Celestial }
    ("Weapon (Tidus): Flametongue",         ItemClassification.useful     , 0x0004),  # Offset=0054 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Firestrike [801Eh]} }
    ("Weapon (Yuna): Rod of Wisdom",        ItemClassification.useful     , 0x0005),  # Offset=0064 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Magic +5% [8067h], !Magic +3% [8066h], !Sensor [8000h]} }
    ("Armor (Kimahri): Red Armlet",         ItemClassification.useful     , 0x0006),  # Offset=0074 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=3 {Fire Ward [801Fh], Ice Ward [8023h], Lightning Ward [8027h]} }
    ("Armor (Lulu): Serene Bangle",         ItemClassification.useful     , 0x0007),  # Offset=0084 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Berserk Ward [8051h]} }
    ("Weapon (Wakka): Scout I",             ItemClassification.useful     , 0x0008),  # Offset=0094 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Icestrike [8022h], Sensor [8000h]} }
    ("Armor (Tidus): NulBlaze Shield",      ItemClassification.useful     , 0x0009),  # Offset=00A4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {SOS NulBlaze [8061h]} }
    ("Weapon (Kimahri): Tidal Spear",       ItemClassification.useful     , 0x000a),  # Offset=00B4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Piercing [800Bh], Waterstrike [802Ah]} }
    ("Weapon (Tidus): Ice Brand",           ItemClassification.useful     , 0x000b),  # Offset=00C4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Icestrike [8022h]} }
    ("Weapon (Auron): Thunder Blade",       ItemClassification.useful     , 0x000c),  # Offset=00D4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Piercing [800Bh], Lightningstrike [8026h]} }
    ("Weapon (Wakka): Scout II",            ItemClassification.useful     , 0x000d),  # Offset=00E4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Lightningstrike [8026h], Sensor [8000h]} }
    ("Weapon (Kimahri): Heat Lance",        ItemClassification.useful     , 0x000e),  # Offset=00F4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Piercing [800Bh], Firestrike [801Eh]} }
    ("Armor (Auron): Serene Bracer",        ItemClassification.useful     , 0x000f),  # Offset=0104 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {HP +5% [8072h], Berserk Ward [8051h]} }
    ("Armor (Lulu): Bright Bangle",         ItemClassification.useful     , 0x0010),  # Offset=0114 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Dark Ward [8049h], Empty} }
    ("Armor (Yuna): Serum Ring",            ItemClassification.useful     , 0x0011),  # Offset=0124 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Lightning Ward [8027h], Poison Ward [803Dh]} }
    ("Armor (Kimahri): Serene Armlet",      ItemClassification.useful     , 0x0012),  # Offset=0134 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Dark Ward [8049h], Berserk Ward [8051h]} }
    ("Weapon (Wakka): All-Rounder",         ItemClassification.useful     , 0x0013),  # Offset=0144 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Strength +3% [8062h], Strength +5% [8063h]} }
    ("Weapon (Lulu): Sleepy Cait Sith",     ItemClassification.useful     , 0x0014),  # Offset=0154 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Sleeptouch [803Fh]} }
    ("Armor (Yuna): Lucid Ring I",          ItemClassification.useful     , 0x0015),  # Offset=0164 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Silence Ward [8045h], Confuse Ward [804Fh]} }
    ("Weapon (Tidus): Avenger I",           ItemClassification.useful     , 0x0016),  # Offset=0174 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Counterattack [8003h]} }
    ("Weapon (Lulu): Quiet Cait Sith",      ItemClassification.useful     , 0x0017),  # Offset=0184 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Silencetouch [8043h], Magic +5% [8067h]} }
    ("Armor (Rikku): Shell Targe",          ItemClassification.useful     , 0x0018),  # Offset=0194 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {SOS Shell [8059h]} }
    ("Armor (Kimahri): Lucid Armlet",       ItemClassification.useful     , 0x0019),  # Offset=01A4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Poison Ward [803Dh], Confuse Ward [804Fh], Silence Ward [8045h], Empty} }
    ("Weapon (Wakka): World Champion",      ItemClassification.progression, 0x001a),  # Offset=01B4 Weapon [00h], Formula=Celestial HP-based [11h], Power=16, Crit=3%, Slots=4 {No AP [8014h], Empty, Empty, Empty}, Celestial }
    ("Weapon (Wakka): Scout III",           ItemClassification.useful     , 0x001b),  # Offset=01C4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Sensor [8000h]} }
    ("Weapon (Kimahri): Ice Lance",         ItemClassification.useful     , 0x001c),  # Offset=01D4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Piercing [800Bh], Icestrike [8022h]} }
    ("Armor (Yuna): Moon Ring",             ItemClassification.useful     , 0x001d),  # Offset=01E4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {SOS Shell [8059h], SOS Protect [805Ah]} }
    ("Weapon (Auron): Masamune",            ItemClassification.progression, 0x001e),  # Offset=01F4 Weapon [00h], Formula=Celestial Auron [13h], Power=16, Crit=3%, Slots=4 {No AP [8014h], Empty, Empty, Empty}, Celestial }
    ("Weapon (Tidus): Avenger II",          ItemClassification.useful     , 0x001f),  # Offset=0204 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Counterattack [8003h]} }
    ("Weapon (Wakka): Rematch",             ItemClassification.useful     , 0x0020),  # Offset=0214 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Evade & Counter [8004h]} }
    ("Weapon (Kimahri): Knight Lance I",    ItemClassification.useful     , 0x0021),  # Offset=0224 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=3 {Strength +3% [8062h], Strength +5% [8063h], Strength +10% [8064h]} }
    ("Armor (Yuna): Lucid Ring II",         ItemClassification.useful     , 0x0022),  # Offset=0234 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=3 {Silence Ward [8045h], Confuse Ward [804Fh], Poison Ward [803Dh]} }
    ("Weapon (Wakka): Bright Armguard",     ItemClassification.useful     , 0x0023),  # Offset=0244 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Fire Ward [801Fh], Dark Ward [8049h]} }
    ("Weapon (Yuna): Nirvana",              ItemClassification.progression, 0x0024),  # Offset=0254 Weapon [00h], Formula=Celestial MP-based [12h], Power=16, Crit=3%, Slots=4 {No AP [8014h], Empty, Empty, Empty}, Celestial }
    ("Weapon (Tidus): Caladbolg",           ItemClassification.progression, 0x0025),  # Offset=0264 Weapon [00h], Formula=Celestial HP-based [11h], Power=16, Crit=3%, Slots=4 {No AP [8014h], Empty, Empty, Empty}, Celestial }
    ("Armor (Kimahri): Tetra Armlet",       ItemClassification.useful     , 0x0026),  # Offset=0274 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {HP +10% [8073h], Empty, Empty, Empty} }
    ("Weapon (Rikku): Flexible Arm",        ItemClassification.useful     , 0x0027),  # Offset=0284 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Empty, Empty, Empty, Empty} }
    ("Armor (Auron): Defending Bracer I",   ItemClassification.useful     , 0x0028),  # Offset=0294 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Stoneproof [8038h], Poisonproof [803Ch]} }
    ("Weapon (Wakka): Pep Talk",            ItemClassification.useful     , 0x0029),  # Offset=02A4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=3 {SOS NulFrost [805Fh], SOS NulShock [8060h], SOS NulBlaze [8061h]} }
    ("Armor (Yuna): Recovery Ring",         ItemClassification.useful     , 0x002a),  # Offset=02B4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {HP Stroll [801Bh]} }
    ("Armor (Rikku): Spiritual Targe",      ItemClassification.useful     , 0x002b),  # Offset=02C4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {MP Stroll [801Ch]} }
    ("Armor (Auron): Defending Bracer II",  ItemClassification.useful     , 0x002c),  # Offset=02D4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Silenceproof [8044h], Darkproof [8048h]} }
    ("Weapon (Wakka): Turnover",            ItemClassification.useful     , 0x002d),  # Offset=02E4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Magic Counter [8005h], Counterattack [8003h]} }
    ("Armor (Kimahri): Defending Armlet",   ItemClassification.useful     , 0x002e),  # Offset=02F4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Stoneproof [8038h], Poisonproof [803Ch], Empty, Empty} }
    ("Armor (Yuna): Phantom Ring I",        ItemClassification.useful     , 0x002f),  # Offset=0304 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Ice Eater [8025h], Fire Eater [8021h], Lightning Eater [8029h], Empty} }
    ("Weapon (Lulu): Cactuar Wizard",       ItemClassification.useful     , 0x0030),  # Offset=0314 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Half MP Cost [800Ch]} }
    ("Weapon (Rikku): Warmonger",           ItemClassification.useful     , 0x0031),  # Offset=0324 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Double AP [8012h], !Double Overdrive [800Eh]} }
    ("Weapon (Kimahri): Wizard Lance",      ItemClassification.useful     , 0x0032),  # Offset=0334 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Magic +3% [8066h], Magic +5% [8067h], Magic +10% [8068h], Empty} }
    ("Armor (Yuna): Phantom Ring II",       ItemClassification.useful     , 0x0033),  # Offset=0344 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Water Eater [802Dh], Fire Eater [8021h], Lightning Eater [8029h], Empty} }
    ("Weapon (Wakka): Four-on-One",         ItemClassification.useful     , 0x0034),  # Offset=0354 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Waterstrike [802Ah], Firestrike [801Eh], Lightningstrike [8026h], Icestrike [8022h]} }
    ("Armor (Auron): Defending Bracer III", ItemClassification.useful     , 0x0035),  # Offset=0364 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Darkproof [8048h], Deathproof [8030h], Empty, Empty} }
    ("Weapon (Yuna): Laevatein",            ItemClassification.useful     , 0x0036),  # Offset=0374 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {SOS Overdrive [8010h]} }
    ("Weapon (Wakka): Water Ball",          ItemClassification.useful     , 0x0037),  # Offset=0384 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Waterstrike [802Ah], Empty} }
    ("Weapon (Kimahri): Spirit Lance",      ItemClassification.progression, 0x0038),  # Offset=0394 Weapon [00h], Formula=Celestial HP-based [11h], Power=16, Crit=3%, Slots=4 {No AP [8014h], Empty, Empty, Empty}, Celestial }
    ("Armor (Yuna): Soft Ring I",           ItemClassification.useful     , 0x0039),  # Offset=03A4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Stone Ward [8039h], HP +5% [8072h]} }
    ("Weapon (Tidus): Variable Steel I",    ItemClassification.useful     , 0x003a),  # Offset=03B4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Strength +3% [8062h], Strength +5% [8063h]} }
    ("Weapon (Lulu): Magician Mog",         ItemClassification.useful     , 0x003b),  # Offset=03C4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Magic +3% [8066h], Magic +5% [8067h], Magic +20% [8069h], Empty} }
    ("Weapon (Yuna): Magistral Rod",        ItemClassification.useful     , 0x003c),  # Offset=03D4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=3 {Half MP Cost [800Ch], Empty, Empty} }
    ("Weapon (Rikku): Godhand",             ItemClassification.progression, 0x003d),  # Offset=03E4 Weapon [00h], Formula=Celestial HP-based [11h], Power=16, Crit=3%, Slots=4 {No AP [8014h], Empty, Empty, Empty}, Celestial }
    ("Armor (Yuna): Tetra Ring I",          ItemClassification.useful     , 0x003e),  # Offset=03F4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {HP +10% [8073h]} }
    ("Weapon (Tidus): Variable Steel II",   ItemClassification.useful     , 0x003f),  # Offset=0404 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Strength +3% [8062h], Empty, Empty, Empty} }
    ("Armor (Yuna): Soft Ring II",          ItemClassification.useful     , 0x0040),  # Offset=0414 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Stoneproof [8038h], Empty} }
    ("Weapon (Kimahri): Shapeshifter",      ItemClassification.useful     , 0x0041),  # Offset=0424 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Magic +20% [8069h], Empty} }
    ("Weapon (Kimahri): Hunter's Spear",    ItemClassification.useful     , 0x0042),  # Offset=0434 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=3 {Piercing [800Bh], Sensor [8000h], Strength +10% [8064h]} }
    ("Armor (Yuna): Red Ring",              ItemClassification.useful     , 0x0043),  # Offset=0444 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {HP +10% [8073h], Fire Ward [801Fh]} }
    ("Armor (Lulu): Tetra Bangle",          ItemClassification.useful     , 0x0044),  # Offset=0454 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {HP +20% [8074h], Empty} }
    ("Armor (Tidus): Yellow Shield",        ItemClassification.useful     , 0x0045),  # Offset=0464 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Lightningproof [8028h], Empty} }
    ("Weapon (Wakka): Ace Wizard",          ItemClassification.useful     , 0x0046),  # Offset=0474 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Magic +20% [8069h], Magic +10% [8068h], Magic +5% [8067h], Magic +3% [8066h]} }
    ("Armor (Yuna): Tetra Ring II",         ItemClassification.useful     , 0x0047),  # Offset=0484 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {HP +10% [8073h], Empty} }
    ("Armor (Rikku): Victorious",           ItemClassification.useful     , 0x0048),  # Offset=0494 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Lightningproof [8028h], Fireproof [8020h], Iceproof [8024h], Empty} }
    ("Weapon (Auron): Murasame",            ItemClassification.useful     , 0x0049),  # Offset=04A4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Piercing [800Bh], One MP Cost [800Dh], Empty, Empty} }
    ("Armor (Yuna): Echo Ring",             ItemClassification.useful     , 0x004a),  # Offset=04B4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {HP +10% [8073h], Silence Ward [8045h]} }
    ("Weapon (Kimahri): Dragoon Lance",     ItemClassification.useful     , 0x004b),  # Offset=04C4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Magic Counter [8005h], Evade & Counter [8004h], Empty, Empty} }
    ("Weapon (Rikku): Sonar",               ItemClassification.useful     , 0x004c),  # Offset=04D4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=3 {Initiative [8002h], Poisonstrike [803Ah], Empty} }
    ("Armor (Lulu): Phantom Bangle",        ItemClassification.useful     , 0x004d),  # Offset=04E4 Armor [01h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Ice Eater [8025h], Fire Eater [8021h], !Water Eater [802Dh]} }
    ("Weapon (Tidus): Ascalon",             ItemClassification.useful     , 0x004e),  # Offset=04F4 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {Double AP [8012h]} }
    ("Weapon (Wakka): Prism Ball",          ItemClassification.useful     , 0x004f),  # Offset=0504 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {Magic Counter [8005h], Empty} }
    ("Weapon (Auron): Stillblade",          ItemClassification.useful     , 0x0050),  # Offset=0514 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=3 {Silencestrike [8042h], Stonestrike [8036h], Empty} }
    ("Weapon (Yuna): Mage's Staff",         ItemClassification.useful     , 0x0051),  # Offset=0524 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Magic +10% [8068h], Magic +5% [8067h], Magic +3% [8066h], Empty} }
    ("Weapon (Kimahri): Knight Lance II",   ItemClassification.useful     , 0x0052),  # Offset=0534 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Strength +10% [8064h], Strength +5% [8063h], Strength +3% [8062h], Empty} }
    ("Weapon (Rikku): Infinity",            ItemClassification.useful     , 0x0053),  # Offset=0544 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=2 {One MP Cost [800Dh], Sensor [8000h]} }
    ("Weapon (Lulu): Wicked Cait Sith",     ItemClassification.useful     , 0x0054),  # Offset=0554 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=4 {Deathstrike [802Eh], Empty, Empty, Empty} }
    ("Weapon (Tidus): Hrunting",            ItemClassification.useful     , 0x0055),  # Offset=0564 Weapon [00h], Formula=STR vs DEF [01h], Power=16, Crit=3%, Slots=1 {SOS Overdrive [8010h]} }
]]

party_member_items: list[ItemData] = [ItemData(x[0], x[1], x[2] | partyMemberItemOffset) for x in [
    ("Party Member: Tidus",         ItemClassification.progression, 0x0000),
    ("Party Member: Yuna",          ItemClassification.progression, 0x0001),
    ("Party Member: Auron",         ItemClassification.progression, 0x0002),
    ("Party Member: Kimahri",       ItemClassification.progression, 0x0003),
    ("Party Member: Wakka",         ItemClassification.progression, 0x0004),
    ("Party Member: Lulu",          ItemClassification.progression, 0x0005),
    ("Party Member: Rikku",         ItemClassification.progression, 0x0006),
    ("Party Member: Seymour",       ItemClassification.progression, 0x0007),
    ("Party Member: Valefor",       ItemClassification.progression, 0x0008),
    ("Party Member: Ifrit",         ItemClassification.progression, 0x0009),
    ("Party Member: Ixion",         ItemClassification.progression, 0x000A),
    ("Party Member: Shiva",         ItemClassification.progression, 0x000B),
    ("Party Member: Bahamut",       ItemClassification.progression, 0x000C),
    ("Party Member: Anima",         ItemClassification.progression, 0x000D),
    ("Party Member: Yojimbo",       ItemClassification.progression, 0x000E),
    ("Party Member: Magus Sisters", ItemClassification.progression, 0x000F), # Sisters are 0x0f, 0x10, 0x11
]]

region_unlock_items: list[ItemData] = [ItemData(x[0], x[1], x[2] | regionItemOffset) for x in [
    #("Region: None",                      ItemClassification.progression,  0),
    #("Region: Dream Zanarkand",           ItemClassification.progression,  1),
    ("Region: Baaj Temple",                ItemClassification.progression,  2),
    ("Region: Besaid",                     ItemClassification.progression,  3),
    ("Region: Kilika",                     ItemClassification.progression,  4),
    ("Region: Luca",                       ItemClassification.progression,  5),
    ("Region: Mi'ihen Highroad",           ItemClassification.progression,  6),
    ("Region: Mushroom Rock Road",         ItemClassification.progression,  7),
    ("Region: Djose",                      ItemClassification.progression,  8),
    ("Region: Moonflow",                   ItemClassification.progression,  9),
    ("Region: Guadosalam",                 ItemClassification.progression, 10),
    ("Region: Thunder Plains",             ItemClassification.progression, 11),
    ("Region: Macalania",                  ItemClassification.progression, 12),
    ("Region: Bikanel",                    ItemClassification.progression, 13),
    ("Region: Airship",                    ItemClassification.progression, 14),
    ("Region: Bevelle",                    ItemClassification.progression, 15),
    ("Region: Calm Lands",                 ItemClassification.progression, 16),
    ("Region: Cavern of the Stolen Fayth", ItemClassification.progression, 17),
    ("Region: Mt. Gagazet",                ItemClassification.progression, 18),
    ("Region: Zanarkand Ruins",            ItemClassification.progression, 19),
    ("Region: Sin",                        ItemClassification.progression, 20),
    ("Region: Omega Ruins",                ItemClassification.progression, 21),
    ("Region: Monster Arena",              ItemClassification.progression, 22),
]]

gil_items: list[ItemData] = [ItemData(f"{i*1000} Gil", ItemClassification.filler, (i << 16) | gilItemOffset) for i in range(1, 10)]
#gil_items: list[ItemData] = [ItemData(x[0], x[1], x[2] | gilItemOffset) for x in [
#    ("1000 Gil", ItemClassification.filler, 0x0000),
#]]

character_names = [
    "Tidus",
    "Yuna",
    "Auron",
    "Kimahri",
    "Wakka",
    "Lulu",
    "Rikku",
    #"Seymour",
]

aeon_names = [
    "Valefor",
    "Ifrit",
    "Ixion",
    "Shiva",
    "Bahamut",
    "Anima",
    "Yojimbo",
    "Magus Sisters",
]

abilities_per_character: list[ItemData] = [ ItemData(f"{character_names[character]} {ability[0]}", ItemClassification.progression, ability[1] | abilityItemOffset | character << 8) for character in range(7) for ability in [
    # Lvl 3 lock
    # Empty node
    ("Ability: Strength +1", 0x0002),
    ("Ability: Strength +2", 0x0003),
    ("Ability: Strength +3", 0x0004),
    ("Ability: Strength +4", 0x0005),

    ("Ability: Defense +1", 0x0006),
    ("Ability: Defense +2", 0x0007),
    ("Ability: Defense +3", 0x0008),
    ("Ability: Defense +4", 0x0009),

    ("Ability: Magic +1", 0x000A),
    ("Ability: Magic +2", 0x000B),
    ("Ability: Magic +3", 0x000C),
    ("Ability: Magic +4", 0x000D),

    ("Ability: Magic Defense +1", 0x000E),
    ("Ability: Magic Defense +2", 0x000F),
    ("Ability: Magic Defense +3", 0x0010),
    ("Ability: Magic Defense +4", 0x0011),

    ("Ability: Agility +1", 0x0012),
    ("Ability: Agility +2", 0x0013),
    ("Ability: Agility +3", 0x0014),
    ("Ability: Agility +4", 0x0015),

    ("Ability: Luck +1", 0x0016),
    ("Ability: Luck +2", 0x0017),
    ("Ability: Luck +3", 0x0018),
    ("Ability: Luck +4", 0x0019),

    ("Ability: Evasion +1", 0x001A),
    ("Ability: Evasion +2", 0x001B),
    ("Ability: Evasion +3", 0x001C),
    ("Ability: Evasion +4", 0x001D),

    ("Ability: Accuracy +1", 0x001E),
    ("Ability: Accuracy +2", 0x001F),
    ("Ability: Accuracy +3", 0x0020),
    ("Ability: Accuracy +4", 0x0021),

    ("Ability: HP +200", 0x0022),
    ("Ability: HP +300", 0x0023),

    ("Ability: MP +40", 0x0024),
    ("Ability: MP +20", 0x0025),
    ("Ability: MP +10", 0x0026),

    # Lvl 1 lock
    # Lvl 2 lock
    # Lvl 4 lock

    ("Ability: Delay Attack",   0x002A),
    ("Ability: Delay Buster",   0x002B),
    ("Ability: Sleep Attack",   0x002C),
    ("Ability: Silence Attack", 0x002D),
    ("Ability: Dark Attack",    0x002E),
    ("Ability: Zombie Attack",  0x002F),
    ("Ability: Sleep Buster",   0x0030),
    ("Ability: Silence Buster", 0x0031),
    ("Ability: Dark Buster",    0x0032),
    ("Ability: Triple Foul",    0x0033),
    ("Ability: Power Break",    0x0034),
    ("Ability: Magic Break",    0x0035),
    ("Ability: Armor Break",    0x0036),
    ("Ability: Mental Break",   0x0037),
    ("Ability: Mug",            0x0038),
    ("Ability: Quick Hit",      0x0039),

    ("Ability: Steal",        0x003A),
    ("Ability: Use",          0x003B),
    ("Ability: Flee",         0x003C),
    ("Ability: Pray",         0x003D),
    ("Ability: Cheer",        0x003E),
    ("Ability: Focus",        0x003F),
    ("Ability: Reflex",       0x0040),
    ("Ability: Aim",          0x0041),
    ("Ability: Luck",         0x0042),
    ("Ability: Jinx",         0x0043),
    ("Ability: Lancet",       0x0044),
    ("Ability: Guard",        0x0045),
    ("Ability: Sentinel",     0x0046),
    ("Ability: Spare Change", 0x0047),
    ("Ability: Threaten",     0x0048),
    ("Ability: Provoke",      0x0049),
    ("Ability: Entrust",      0x004A),
    ("Ability: Copycat",      0x004B),
    ("Ability: Doublecast",   0x004C),
    ("Ability: Bribe",        0x004D),

    ("Ability: Cure",      0x004E),
    ("Ability: Cura",      0x004F),
    ("Ability: Curaga",    0x0050),
    ("Ability: Nul Frost", 0x0051),
    ("Ability: Nul Blaze", 0x0052),
    ("Ability: Nul Shock", 0x0053),
    ("Ability: Nul Tide",  0x0054),
    ("Ability: Scan",      0x0055),
    ("Ability: Esuna",     0x0056),
    ("Ability: Life",      0x0057),
    ("Ability: Full Life", 0x0058),
    ("Ability: Haste",     0x0059),
    ("Ability: Hastega",   0x005A),
    ("Ability: Slow",      0x005B),
    ("Ability: Slowga",    0x005C),
    ("Ability: Shell",     0x005D),
    ("Ability: Protect",   0x005E),
    ("Ability: Reflect",   0x005F),
    ("Ability: Dispel",    0x0060),
    ("Ability: Regen",     0x0061),
    ("Ability: Holy",      0x0062),
    ("Ability: Auto Life", 0x0063),

    ("Ability: Blizzard", 0x0064),
    ("Ability: Fire",     0x0065),
    ("Ability: Thunder",  0x0066),
    ("Ability: Water",    0x0067),
    ("Ability: Fira",     0x0068),
    ("Ability: Blizzara", 0x0069),
    ("Ability: Thundara", 0x006A),
    ("Ability: Watera",   0x006B),
    ("Ability: Firaga",   0x006C),
    ("Ability: Blizzaga", 0x006D),
    ("Ability: Thundaga", 0x006E),
    ("Ability: Waterga",  0x006F),
    ("Ability: Bio",      0x0070),
    ("Ability: Demi",     0x0071),
    ("Ability: Death",    0x0072),
    ("Ability: Drain",    0x0073),
    ("Ability: Osmose",   0x0074),
    ("Ability: Flare",    0x0075),
    ("Ability: Ultima",   0x0076),

    ("Ability: Pilfer Gil",      0x0077),
    ("Ability: Full Break",      0x0078),
    ("Ability: Extract Power",   0x0079),
    ("Ability: Extract Mana",    0x007A),
    ("Ability: Extract Speed",   0x007B),
    ("Ability: Extract Ability", 0x007C),

    ("Ability: Nab Gil",       0x007D),
    ("Ability: Quick Pockets", 0x007E),
]]

abilities: list[ItemData] = [
    # Lvl 3 lock
    # Empty node
    ItemData("Ability: Strength +1", ItemClassification.progression, 0xD002),
    ItemData("Ability: Strength +2", ItemClassification.progression, 0xD003),
    ItemData("Ability: Strength +3", ItemClassification.progression, 0xD004),
    ItemData("Ability: Strength +4", ItemClassification.progression, 0xD005),

    ItemData("Ability: Defense +1", ItemClassification.progression, 0xD006),
    ItemData("Ability: Defense +2", ItemClassification.progression, 0xD007),
    ItemData("Ability: Defense +3", ItemClassification.progression, 0xD008),
    ItemData("Ability: Defense +4", ItemClassification.progression, 0xD009),

    ItemData("Ability: Magic +1", ItemClassification.progression, 0xD00A),
    ItemData("Ability: Magic +2", ItemClassification.progression, 0xD00B),
    ItemData("Ability: Magic +3", ItemClassification.progression, 0xD00C),
    ItemData("Ability: Magic +4", ItemClassification.progression, 0xD00D),

    ItemData("Ability: Magic Defense +1", ItemClassification.progression, 0xD00E),
    ItemData("Ability: Magic Defense +2", ItemClassification.progression, 0xD00F),
    ItemData("Ability: Magic Defense +3", ItemClassification.progression, 0xD010),
    ItemData("Ability: Magic Defense +4", ItemClassification.progression, 0xD011),

    ItemData("Ability: Agility +1", ItemClassification.progression, 0xD012),
    ItemData("Ability: Agility +2", ItemClassification.progression, 0xD013),
    ItemData("Ability: Agility +3", ItemClassification.progression, 0xD014),
    ItemData("Ability: Agility +4", ItemClassification.progression, 0xD015),

    ItemData("Ability: Luck +1", ItemClassification.progression, 0xD016),
    ItemData("Ability: Luck +2", ItemClassification.progression, 0xD017),
    ItemData("Ability: Luck +3", ItemClassification.progression, 0xD018),
    ItemData("Ability: Luck +4", ItemClassification.progression, 0xD019),

    ItemData("Ability: Evasion +1", ItemClassification.progression, 0xD01A),
    ItemData("Ability: Evasion +2", ItemClassification.progression, 0xD01B),
    ItemData("Ability: Evasion +3", ItemClassification.progression, 0xD01C),
    ItemData("Ability: Evasion +4", ItemClassification.progression, 0xD01D),

    ItemData("Ability: Accuracy +1", ItemClassification.progression, 0xD01E),
    ItemData("Ability: Accuracy +2", ItemClassification.progression, 0xD01F),
    ItemData("Ability: Accuracy +3", ItemClassification.progression, 0xD020),
    ItemData("Ability: Accuracy +4", ItemClassification.progression, 0xD021),

    ItemData("Ability: HP +200", ItemClassification.progression, 0xD022),
    ItemData("Ability: HP +300", ItemClassification.progression, 0xD023),

    ItemData("Ability: MP +40", ItemClassification.progression, 0xD024),
    ItemData("Ability: MP +20", ItemClassification.progression, 0xD025),
    ItemData("Ability: MP +10", ItemClassification.progression, 0xD026),

    # Lvl 1 lock
    # Lvl 2 lock
    # Lvl 4 lock

    ItemData("Delay Attack",   ItemClassification.progression, 0xD02A),
    ItemData("Delay Buster",   ItemClassification.progression, 0xD02B),
    ItemData("Sleep Attack",   ItemClassification.progression, 0xD02C),
    ItemData("Silence Attack", ItemClassification.progression, 0xD02D),
    ItemData("Dark Attack",    ItemClassification.progression, 0xD02E),
    ItemData("Zombie Attack",  ItemClassification.progression, 0xD02F),
    ItemData("Sleep Buster",   ItemClassification.progression, 0xD030),
    ItemData("Silence Buster", ItemClassification.progression, 0xD031),
    ItemData("Dark Buster",    ItemClassification.progression, 0xD032),
    ItemData("Triple Foul",    ItemClassification.progression, 0xD033),
    ItemData("Power Break",    ItemClassification.progression, 0xD034),
    ItemData("Magic Break",    ItemClassification.progression, 0xD035),
    ItemData("Armor Break",    ItemClassification.progression, 0xD036),
    ItemData("Mental Break",   ItemClassification.progression, 0xD037),
    ItemData("Mug",            ItemClassification.progression, 0xD038),
    ItemData("Quick Hit",      ItemClassification.progression, 0xD039),

    ItemData("Steal",        ItemClassification.progression, 0xD03A),
    ItemData("Use",          ItemClassification.progression, 0xD03B),
    ItemData("Flee",         ItemClassification.progression, 0xD03C),
    ItemData("Pray",         ItemClassification.progression, 0xD03D),
    ItemData("Cheer",        ItemClassification.progression, 0xD03E),
    ItemData("Focus",        ItemClassification.progression, 0xD03F),
    ItemData("Reflex",       ItemClassification.progression, 0xD040),
    ItemData("Aim",          ItemClassification.progression, 0xD041),
    ItemData("Luck",         ItemClassification.progression, 0xD042),
    ItemData("Jinx",         ItemClassification.progression, 0xD043),
    ItemData("Lancet",       ItemClassification.progression, 0xD044),
    ItemData("Guard",        ItemClassification.progression, 0xD045),
    ItemData("Sentinel",     ItemClassification.progression, 0xD046),
    ItemData("Spare Change", ItemClassification.progression, 0xD047),
    ItemData("Threaten",     ItemClassification.progression, 0xD048),
    ItemData("Provoke",      ItemClassification.progression, 0xD049),
    ItemData("Entrust",      ItemClassification.progression, 0xD04A),
    ItemData("Copycat",      ItemClassification.progression, 0xD04B),
    ItemData("Doublecast",   ItemClassification.progression, 0xD04C),
    ItemData("Bribe",        ItemClassification.progression, 0xD04D),

    ItemData("Cure",      ItemClassification.progression, 0xD04E),
    ItemData("Cura",      ItemClassification.progression, 0xD04F),
    ItemData("Curaga",    ItemClassification.progression, 0xD050),
    ItemData("Nul Frost", ItemClassification.progression, 0xD051),
    ItemData("Nul Blaze", ItemClassification.progression, 0xD052),
    ItemData("Nul Shock", ItemClassification.progression, 0xD053),
    ItemData("Nul Tide",  ItemClassification.progression, 0xD054),
    ItemData("Scan",      ItemClassification.progression, 0xD055),
    ItemData("Esuna",     ItemClassification.progression, 0xD056),
    ItemData("Life",      ItemClassification.progression, 0xD057),
    ItemData("Full Life", ItemClassification.progression, 0xD058),
    ItemData("Haste",     ItemClassification.progression, 0xD059),
    ItemData("Hastega",   ItemClassification.progression, 0xD05A),
    ItemData("Slow",      ItemClassification.progression, 0xD05B),
    ItemData("Slowga",    ItemClassification.progression, 0xD05C),
    ItemData("Shell",     ItemClassification.progression, 0xD05D),
    ItemData("Protect",   ItemClassification.progression, 0xD05E),
    ItemData("Reflect",   ItemClassification.progression, 0xD05F),
    ItemData("Dispel",    ItemClassification.progression, 0xD060),
    ItemData("Regen",     ItemClassification.progression, 0xD061),
    ItemData("Holy",      ItemClassification.progression, 0xD062),
    ItemData("Auto Life", ItemClassification.progression, 0xD063),

    ItemData("Blizzard", ItemClassification.progression, 0xD064),
    ItemData("Fire",     ItemClassification.progression, 0xD065),
    ItemData("Thunder",  ItemClassification.progression, 0xD066),
    ItemData("Water",    ItemClassification.progression, 0xD067),
    ItemData("Fira",     ItemClassification.progression, 0xD068),
    ItemData("Blizzara", ItemClassification.progression, 0xD069),
    ItemData("Thundara", ItemClassification.progression, 0xD06A),
    ItemData("Watera",   ItemClassification.progression, 0xD06B),
    ItemData("Firaga",   ItemClassification.progression, 0xD06C),
    ItemData("Blizzaga", ItemClassification.progression, 0xD06D),
    ItemData("Thundaga", ItemClassification.progression, 0xD06E),
    ItemData("Waterga",  ItemClassification.progression, 0xD06F),
    ItemData("Bio",      ItemClassification.progression, 0xD070),
    ItemData("Demi",     ItemClassification.progression, 0xD071),
    ItemData("Death",    ItemClassification.progression, 0xD072),
    ItemData("Drain",    ItemClassification.progression, 0xD073),
    ItemData("Osmose",   ItemClassification.progression, 0xD074),
    ItemData("Flare",    ItemClassification.progression, 0xD075),
    ItemData("Ultima",   ItemClassification.progression, 0xD076),

    ItemData("Pilfer Gil",      ItemClassification.progression, 0xD077),
    ItemData("Full Break",      ItemClassification.progression, 0xD078),
    ItemData("Extract Power",   ItemClassification.progression, 0xD079),
    ItemData("Extract Mana",    ItemClassification.progression, 0xD07A),
    ItemData("Extract Speed",   ItemClassification.progression, 0xD07B),
    ItemData("Extract Ability", ItemClassification.progression, 0xD07C),

    ItemData("Nab Gil",       ItemClassification.progression, 0xD07D),
    ItemData("Quick Pockets", ItemClassification.progression, 0xD07E),
]

trap_items: list[ItemData] = [ItemData(x[0], x[1], x[2] | trapItemOffset) for x in [
    ("Voice Trap", ItemClassification.trap, 0x0000),
]]

stat_abilities = [ability for ability in abilities_per_character if ability.itemID & 0xFF <= 0x26]

skill_abilities = [ability for ability in abilities_per_character if ability not in stat_abilities]

#item_to_stat_value = {item.itemName: int(re.search(r"\+([0-9])+", item.itemName).group(0)) for item in stat_abilities}
item_to_stat_value: dict[str, tuple[str, int]] = dict()
for item in stat_abilities:
    character = re.match(r"([a-zA-Z]+)", item.itemName).group(0)
    value = int(re.search(r"\+([0-9])+", item.itemName).group(0))
    if "HP" in item.itemName:
        value = value / 10
    elif "MP" in item.itemName:
        value = value / 5

    item_to_stat_value[item.itemName] = (character, value)



AllItems = list(chain(normal_items,
                      key_items,
                      equip_items,
                      party_member_items,
                      region_unlock_items,
                      trap_items))

filler_items: list[ItemData] = [item for item in AllItems if item.progression == ItemClassification.filler]

item_table: dict[str, ItemData] = {item.itemName: item for item in AllItems}
items_by_id: dict[int, ItemData] = {item.itemID: item for item in AllItems}


def create_item_label_to_code_map() -> dict[str, int]:
    """
    Creates a map from item labels to their AP item id (code)
    """
    offset = 0
    label_to_code_map: dict[str, int] = {}
    for item in AllItems:
        label_to_code_map[item.itemName] = item.itemID + offset

    return label_to_code_map
