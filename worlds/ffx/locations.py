import typing
from typing import Dict, Optional, List, Tuple

from BaseClasses import Location, Region


class FFXLocation(Location):
    game: str = "Final Fantasy X"

    def __init__(self, player: int, name: str = '', address: Optional[int] = None, parent: Optional[Region] = None):
        super().__init__(player, name, address, parent)


class FFXLocationData(typing.NamedTuple):
    name: str
    quest_id: int
    rom_address: int
    type: str


FFXTreasureLocations: List[FFXLocationData] = [
    FFXLocationData("Baaj Temple: First time visiting Baaj Temple, off to the right north of the glyph", 0, 0x0014, "treasure"),  # Gil: 200 [02h]
    FFXLocationData("Baaj Temple: West side near Al Bhed primer sphere", 1, 0x0018, "treasure"),  # Item: 2x Potion [2000h]
    FFXLocationData("Baaj Temple: Up the stairs to the right at the end of the hall", 2, 0x001C, "treasure"),  # Key Item: Withered Bouquet [A000h]
    FFXLocationData("Baaj Temple: By the save sphere inside the temple, inside a desk", 3, 0x0020, "treasure"),  # Key Item: Flint [A001h]
    FFXLocationData("Treasure 4", 4, 0x0024, "treasure"),  # Gear: buki_get #2 [02h] { Yuna [01h], Weapon {One MP Cost [800Dh], Empty, Empty, Empty} }
    FFXLocationData("Baaj Temple: After beating GeosGaeno in a treasure chest by the temple entrance", 5, 0x0028, "treasure"),  # Gear: buki_get #3 [03h] { Lulu [05h], Weapon Formula=Celestial MP-based [12h] {No AP [8014h], Empty, Empty, Empty} }
    FFXLocationData("Baaj Temple: In northern door, south towards the camera in a chest", 6, 0x002C, "treasure"),  # Item: 1x Ether [2004h]
    FFXLocationData("Baaj Temple: Past the withered bouquet, follow path to the right, in a chest", 7, 0x0030, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 8", 8, 0x0034, "treasure"),  # Item: 1x Phoenix Down [2006h]
    FFXLocationData("Treasure 9", 9, 0x0038, "treasure"),  # Item: 2x Antidote [200Ah]
    FFXLocationData("Treasure 10", 10, 0x003C, "treasure"),  # Gil: 200 [02h]
    FFXLocationData("Treasure 11", 11, 0x0040, "treasure"),  # Gear: buki_get #4 [04h] { Tidus [00h], Weapon {Firestrike [801Eh]} }
    FFXLocationData("Treasure 12", 12, 0x0044, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 13", 13, 0x0048, "treasure"),  # Item: 1x Phoenix Down [2006h]
    FFXLocationData("Treasure 14", 14, 0x004C, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 15", 15, 0x0050, "treasure"),  # Gear: buki_get #5 [05h] { Yuna [01h], Weapon {Magic +5% [8067h], !Magic +3% [8066h], !Sensor [8000h]} }
    FFXLocationData("Treasure 16", 16, 0x0054, "treasure"),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Treasure 17", 17, 0x0058, "treasure"),  # Item: 3x Potion [2000h]
    FFXLocationData("Treasure 18", 18, 0x005C, "treasure"),  # Item: 1x Ether [2004h]
    FFXLocationData("Treasure 19", 19, 0x0060, "treasure"),  # Gear: buki_get #6 [06h] { Kimahri [03h], Armor {Fire Ward [801Fh], Ice Ward [8023h], Lightning Ward [8027h]} }
    FFXLocationData("Treasure 20", 20, 0x0064, "treasure"),  # Gear: buki_get #7 [07h] { Lulu [05h], Armor {Berserk Ward [8051h]} }
    FFXLocationData("Treasure 21", 21, 0x0068, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 22", 22, 0x006C, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 23", 23, 0x0070, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 24", 24, 0x0074, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 25", 25, 0x0078, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 26", 26, 0x007C, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 27", 27, 0x0080, "treasure"),  # Item: 2x Mana Sphere [2047h]
    FFXLocationData("Treasure 28", 28, 0x0084, "treasure"),  # Gear: buki_get #8 [08h] { Wakka [04h], Weapon {Icestrike [8022h], Sensor [8000h]} }
    FFXLocationData("Treasure 29", 29, 0x0088, "treasure"),  # Item: 1x Luck Sphere [205Eh]
    FFXLocationData("Treasure 30", 30, 0x008C, "treasure"),  # Gear: buki_get #9 [09h] { Tidus [00h], Armor {SOS NulBlaze [8061h]} }
    FFXLocationData("Treasure 31", 31, 0x0090, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 32", 32, 0x0094, "treasure"),  # Item: 2x Phoenix Down [2006h]
    FFXLocationData("Treasure 33", 33, 0x0098, "treasure"),  # Gil: 600 [06h]
    FFXLocationData("Treasure 34", 34, 0x009C, "treasure"),  # Gear: buki_get #10 [0Ah] { Kimahri [03h], Weapon {Piercing [800Bh], Waterstrike [802Ah]} }
    FFXLocationData("Treasure 35", 35, 0x00A0, "treasure"),  # Item: 1x HP Sphere [2055h]
    FFXLocationData("Treasure 36", 36, 0x00A4, "treasure"),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Treasure 37", 37, 0x00A8, "treasure"),  # Gil: 1000 [0Ah]
    FFXLocationData("Treasure 38", 38, 0x00AC, "treasure"),  # Gear: buki_get #11 [0Bh] { Tidus [00h], Weapon {Icestrike [8022h]} }
    FFXLocationData("Treasure 39", 39, 0x00B0, "treasure"),  # Item: 1x Fortune Sphere [204Ah]
    FFXLocationData("Treasure 40", 40, 0x00B4, "treasure"),  # Gear: buki_get #12 [0Ch] { Auron [02h], Weapon {Piercing [800Bh], Lightningstrike [8026h]} }
    FFXLocationData("Treasure 41", 41, 0x00B8, "treasure"),  # Gear: buki_get #13 [0Dh] { Wakka [04h], Weapon {Lightningstrike [8026h], Sensor [8000h]} }
    FFXLocationData("Treasure 42", 42, 0x00BC, "treasure"),  # Gear: buki_get #14 [0Eh] { Kimahri [03h], Weapon {Piercing [800Bh], Firestrike [801Eh]} }
    FFXLocationData("Treasure 43", 43, 0x00C0, "treasure"),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Treasure 44", 44, 0x00C4, "treasure"),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Treasure 45", 45, 0x00C8, "treasure"),  # Gil: 2000 [14h]
    FFXLocationData("Treasure 46", 46, 0x00CC, "treasure"),  # Item: 3x Eye Drops [200Ch]
    FFXLocationData("Treasure 47", 47, 0x00D0, "treasure"),  # Item: 4x Soft [200Bh]
    FFXLocationData("Treasure 48", 48, 0x00D4, "treasure"),  # Gil: 1000 [0Ah]
    FFXLocationData("Treasure 49", 49, 0x00D8, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 50", 50, 0x00DC, "treasure"),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Treasure 51", 51, 0x00E0, "treasure"),  # Gear: buki_get #15 [0Fh] { Auron [02h], Armor {HP +5% [8072h], Berserk Ward [8051h]} }
    FFXLocationData("Treasure 52", 52, 0x00E4, "treasure"),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Treasure 53", 53, 0x00E8, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 54", 54, 0x00EC, "treasure"),  # Item: 2x Phoenix Down [2006h]
    FFXLocationData("Treasure 55", 55, 0x00F0, "treasure"),  # Gear: buki_get #16 [10h] { Lulu [05h], Armor {Dark Ward [8049h], Empty} }
    FFXLocationData("Treasure 56", 56, 0x00F4, "treasure"),  # Gear: buki_get #17 [11h] { Yuna [01h], Armor {Lightning Ward [8027h], Poison Ward [803Dh]} }
    FFXLocationData("Treasure 57", 57, 0x00F8, "treasure"),  # Gear: buki_get #18 [12h] { Kimahri [03h], Armor {Dark Ward [8049h], Berserk Ward [8051h]} }
    FFXLocationData("Treasure 58", 58, 0x00FC, "treasure"),  # Item: 4x Ability Sphere [2049h]
    FFXLocationData("Treasure 59", 59, 0x0100, "treasure"),  # Gil: 4000 [28h]
    FFXLocationData("Treasure 60", 60, 0x0104, "treasure"),  # Gear: buki_get #19 [13h] { Wakka [04h], Weapon {Strength +3% [8062h], Strength +5% [8063h]} }
    FFXLocationData("Treasure 61", 61, 0x0108, "treasure"),  # Item: 1x Ether [2004h]
    FFXLocationData("Treasure 62", 62, 0x010C, "treasure"),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Treasure 63", 63, 0x0110, "treasure"),  # Item: 1x Mega Phoenix [2007h]
    FFXLocationData("Treasure 64", 64, 0x0114, "treasure"),  # Gil: 3000 [1Eh]
    FFXLocationData("Treasure 65", 65, 0x0118, "treasure"),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Treasure 66", 66, 0x011C, "treasure"),  # Item: 1x Elixir [2008h]
    FFXLocationData("Treasure 67", 67, 0x0120, "treasure"),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Treasure 68", 68, 0x0124, "treasure"),  # Gil: 2000 [14h]
    FFXLocationData("Treasure 69", 69, 0x0128, "treasure"),  # Gear: buki_get #20 [14h] { Lulu [05h], Weapon {Sleeptouch [803Fh]} }
    FFXLocationData("Treasure 70", 70, 0x012C, "treasure"),  # Item: 3x Phoenix Down [2006h]
    FFXLocationData("Treasure 71", 71, 0x0130, "treasure"),  # Item: 1x MP Sphere [2056h]
    FFXLocationData("Treasure 72", 72, 0x0134, "treasure"),  # Item: 1x Ether [2004h]
    FFXLocationData("Treasure 73", 73, 0x0138, "treasure"),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Treasure 74", 74, 0x013C, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 75", 75, 0x0140, "treasure"),  # Gear: buki_get #21 [15h] { Yuna [01h], Armor {Silence Ward [8045h], Confuse Ward [804Fh]} }
    FFXLocationData("Treasure 76", 76, 0x0144, "treasure"),  # Gil: 4000 [28h]
    FFXLocationData("Treasure 77", 77, 0x0148, "treasure"),  # Item: 1x Lv. 1 Key Sphere [2051h]
    FFXLocationData("Treasure 78", 78, 0x014C, "treasure"),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Treasure 79", 79, 0x0150, "treasure"),  # Gear: buki_get #22 [16h] { Tidus [00h], Weapon {Counterattack [8003h]} }
    FFXLocationData("Treasure 80", 80, 0x0154, "treasure"),  # Item: 1x Lv. 2 Key Sphere [2052h]
    FFXLocationData("Treasure 81", 81, 0x0158, "treasure"),  # Gear: buki_get #23 [17h] { Lulu [05h], Weapon {Silencetouch [8043h], Magic +5% [8067h]} }
    FFXLocationData("Treasure 82", 82, 0x015C, "treasure"),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Treasure 83", 83, 0x0160, "treasure"),  # Gil: 5000 [32h]
    FFXLocationData("Treasure 84", 84, 0x0164, "treasure"),  # Item: 2x X-Potion [2002h]
    FFXLocationData("Treasure 85", 85, 0x0168, "treasure"),  # Gear: buki_get #24 [18h] { Rikku [06h], Armor {SOS Shell [8059h]} }
    FFXLocationData("Treasure 86", 86, 0x016C, "treasure"),  # Item: 3x Phoenix Down [2006h]
    FFXLocationData("Treasure 87", 87, 0x0170, "treasure"),  # Item: 2x Remedy [200Fh]
    FFXLocationData("Treasure 88", 88, 0x0174, "treasure"),  # Gear: buki_get #25 [19h] { Kimahri [03h], Armor {Poison Ward [803Dh], Confuse Ward [804Fh], Silence Ward [8045h], Empty} }
    FFXLocationData("Treasure 89", 89, 0x0178, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 90", 90, 0x017C, "treasure"),  # Item: 1x Phoenix Down [2006h]
    FFXLocationData("Treasure 91", 91, 0x0180, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 92", 92, 0x0184, "treasure"),  # Item: 2x Antidote [200Ah]
    FFXLocationData("Treasure 93", 93, 0x0188, "treasure"),  # Gear: buki_get #26 [1Ah] { Wakka [04h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    FFXLocationData("Mi'Hen Highroad: Donate 100 gil to \"Operation Mi'ihen\"", 94, 0x018C, "treasure"),  # Gear: buki_get #27 [1Bh] { Wakka [04h], Weapon {Sensor [8000h]} }
    FFXLocationData("Mi'Hen Highroad: Donate 1,000 gil to \"Operation Mi'ihen\"", 95, 0x0190, "treasure"),  # Gear: buki_get #28 [1Ch] { Kimahri [03h], Weapon {Piercing [800Bh], Icestrike [8022h]} }
    FFXLocationData("Mi'Hen Highroad: Donate 10,000 gil to \"Operation Mi'ihen\"", 96, 0x0194, "treasure"),  # Gear: buki_get #29 [1Dh] { Yuna [01h], Armor {SOS Shell [8059h], SOS Protect [805Ah]} }
    FFXLocationData("Treasure 97", 97, 0x0198, "treasure"),  # Item: 2x Mega-Potion [2003h]
    FFXLocationData("Treasure 98", 98, 0x019C, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 99", 99, 0x01A0, "treasure"),  # Gear: buki_get #30 [1Eh] { Auron [02h], Weapon Formula=Celestial Auron [13h] {No AP [8014h], Empty, Empty, Empty} }
    FFXLocationData("Treasure 100", 100, 0x01A4, "treasure"),  # Gear: buki_get #31 [1Fh] { Tidus [00h], Weapon {Counterattack [8003h]} }
    FFXLocationData("Treasure 101", 101, 0x01A8, "treasure"),  # Gear: buki_get #32 [20h] { Wakka [04h], Weapon {Evade & Counter [8004h]} }
    FFXLocationData("Treasure 102", 102, 0x01AC, "treasure"),  # Gear: buki_get #33 [21h] { Kimahri [03h], Weapon {Strength +3% [8062h], Strength +5% [8063h], Strength +10% [8064h]} }
    FFXLocationData("Treasure 103", 103, 0x01B0, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 104", 104, 0x01B4, "treasure"),  # Item: 1x Elixir [2008h]
    FFXLocationData("Treasure 105", 105, 0x01B8, "treasure"),  # Item: 1x Wht Magic Sphere [204Eh]
    FFXLocationData("Treasure 106", 106, 0x01BC, "treasure"),  # Item: 1x Skill Sphere [204Dh]
    FFXLocationData("Treasure 107", 107, 0x01C0, "treasure"),  # Gil: 10000 [64h]
    FFXLocationData("Treasure 108", 108, 0x01C4, "treasure"),  # Gear: buki_get #34 [22h] { Yuna [01h], Armor {Silence Ward [8045h], Confuse Ward [804Fh], Poison Ward [803Dh]} }
    FFXLocationData("Treasure 109", 109, 0x01C8, "treasure"),  # Item: 1x Blk Magic Sphere [204Fh]
    FFXLocationData("Treasure 110", 110, 0x01CC, "treasure"),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Treasure 111", 111, 0x01D0, "treasure"),  # Key Item: Celestial Mirror [A003h]
    FFXLocationData("Treasure 112", 112, 0x01D4, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 113", 113, 0x01D8, "treasure"),  # Gear: buki_get #36 [24h] { Yuna [01h], Weapon Formula=Celestial MP-based [12h] {No AP [8014h], Empty, Empty, Empty} }
    FFXLocationData("Treasure 114", 114, 0x01DC, "treasure"),  # Gear: buki_get #37 [25h] { Tidus [00h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    FFXLocationData("Treasure 115", 115, 0x01E0, "treasure"),  # Gil: 10000 [64h]
    FFXLocationData("Treasure 116", 116, 0x01E4, "treasure"),  # Gil: 5000 [32h]
    FFXLocationData("Treasure 117", 117, 0x01E8, "treasure"),  # Item: 1x Lv. 2 Key Sphere [2052h]
    FFXLocationData("Treasure 118", 118, 0x01EC, "treasure"),  # Key Item: Rusty Sword [A021h]
    FFXLocationData("Treasure 119", 119, 0x01F0, "treasure"),  # Gear: buki_get #38 [26h] { Kimahri [03h], Armor {HP +10% [8073h], Empty, Empty, Empty} }
    FFXLocationData("Treasure 120", 120, 0x01F4, "treasure"),  # Item: 1x Megalixir [2009h]
    FFXLocationData("Treasure 121", 121, 0x01F8, "treasure"),  # Item: 1x Lv. 2 Key Sphere [2052h]
    FFXLocationData("Treasure 122", 122, 0x01FC, "treasure"),  # Item: 1x Fortune Sphere [204Ah]
    FFXLocationData("Treasure 123", 123, 0x0200, "treasure"),  # Item: 2x Mega-Potion [2003h]
    FFXLocationData("Treasure 124", 124, 0x0204, "treasure"),  # Gear: buki_get #39 [27h] { Rikku [06h], Weapon {Empty, Empty, Empty, Empty} }
    FFXLocationData("Treasure 125", 125, 0x0208, "treasure"),  # Item: 1x MP Sphere [2056h]
    FFXLocationData("Treasure 126", 126, 0x020C, "treasure"),  # Item: 2x X-Potion [2002h]
    FFXLocationData("Treasure 127", 127, 0x0210, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 128", 128, 0x0214, "treasure"),  # Gil: 20000 [C8h]
    FFXLocationData("Treasure 129", 129, 0x0218, "treasure"),  # Item: 2x Mega-Potion [2003h]
    FFXLocationData("Treasure 130", 130, 0x021C, "treasure"),  # Gear: buki_get #40 [28h] { Auron [02h], Armor {Stoneproof [8038h], Poisonproof [803Ch]} }
    FFXLocationData("Treasure 131", 131, 0x0220, "treasure"),  # Item: 1x Lv. 4 Key Sphere [2054h]
    FFXLocationData("Treasure 132", 132, 0x0224, "treasure"),  # Item: 1x HP Sphere [2055h]
    FFXLocationData("Treasure 133", 133, 0x0228, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 134", 134, 0x022C, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 135", 135, 0x0230, "treasure"),  # Gear: buki_get #41 [29h] { Wakka [04h], Armor {SOS NulFrost [805Fh], SOS NulShock [8060h], SOS NulBlaze [8061h]} }
    FFXLocationData("Treasure 136", 136, 0x0234, "treasure"),  # Item: 1x Lv. 1 Key Sphere [2051h]
    FFXLocationData("Treasure 137", 137, 0x0238, "treasure"),  # Item: 1x Fortune Sphere [204Ah]
    FFXLocationData("Treasure 138", 138, 0x023C, "treasure"),  # Item: 1x Return Sphere [2060h]
    FFXLocationData("Treasure 139", 139, 0x0240, "treasure"),  # Gear: buki_get #42 [2Ah] { Yuna [01h], Armor {HP Stroll [801Bh]} }
    FFXLocationData("Treasure 140", 140, 0x0244, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 141", 141, 0x0248, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 142", 142, 0x024C, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 143", 143, 0x0250, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 144", 144, 0x0254, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 145", 145, 0x0258, "treasure"),  # Item: 1x Fortune Sphere [204Ah]
    FFXLocationData("Treasure 146", 146, 0x025C, "treasure"),  # Gear: buki_get #43 [2Bh] { Rikku [06h], Armor {MP Stroll [801Ch]} }
    FFXLocationData("Treasure 147", 147, 0x0260, "treasure"),  # Gil: 10000 [64h]
    FFXLocationData("Treasure 148", 148, 0x0264, "treasure"),  # Item: 1x Friend Sphere [2061h]
    FFXLocationData("Treasure 149", 149, 0x0268, "treasure"),  # Item: 1x Lv. 3 Key Sphere [2053h]
    FFXLocationData("Treasure 150", 150, 0x026C, "treasure"),  # Item: 1x Luck Sphere [205Eh]
    FFXLocationData("Treasure 151", 151, 0x0270, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 152", 152, 0x0274, "treasure"),  # Item: 1x Lv. 4 Key Sphere [2054h]
    FFXLocationData("Treasure 153", 153, 0x0278, "treasure"),  # Gear: buki_get #44 [2Ch] { Auron [02h], Armor {Silenceproof [8044h], Darkproof [8048h]} }
    FFXLocationData("Treasure 154", 154, 0x027C, "treasure"),  # Gear: buki_get #45 [2Dh] { Wakka [04h], Weapon {Magic Counter [8005h], Counterattack [8003h]} }
    FFXLocationData("Treasure 155", 155, 0x0280, "treasure"),  # Item: 2x Lv. 3 Key Sphere [2053h]
    FFXLocationData("Treasure 156", 156, 0x0284, "treasure"),  # Gear: buki_get #46 [2Eh] { Kimahri [03h], Armor {Stoneproof [8038h], Poisonproof [803Ch], Empty, Empty} }
    FFXLocationData("Treasure 157", 157, 0x0288, "treasure"),  # Item: 2x Friend Sphere [2061h]
    FFXLocationData("Treasure 158", 158, 0x028C, "treasure"),  # Item: 1x Lv. 4 Key Sphere [2054h]
    FFXLocationData("Treasure 159", 159, 0x0290, "treasure"),  # Gear: buki_get #47 [2Fh] { Yuna [01h], Armor {Ice Eater [8025h], Fire Eater [8021h], Lightning Eater [8029h], Empty} }
    FFXLocationData("Treasure 160", 160, 0x0294, "treasure"),  # Gear: buki_get #48 [30h] { Lulu [05h], Weapon {Half MP Cost [800Ch]} }
    FFXLocationData("Treasure 161", 161, 0x0298, "treasure"),  # Gear: buki_get #49 [31h] { Rikku [06h], Weapon {Double AP [8012h], !Double Overdrive [800Eh]} }
    # FFXLocationData("Hired Yojimbo with certain choices", 162, 0x029C, "treasure"),  # Item: 2x Teleport Sphere [2062h]
    FFXLocationData("Treasure 163", 163, 0x02A0, "treasure"),  # Item: 1x Elixir [2008h]
    FFXLocationData("Treasure 164", 164, 0x02A4, "treasure"),  # Gear: buki_get #50 [32h] { Kimahri [03h], Weapon {Magic +3% [8066h], Magic +5% [8067h], Magic +10% [8068h], Empty} }
    FFXLocationData("Treasure 165", 165, 0x02A8, "treasure"),  # Item: 1x Lv. 3 Key Sphere [2053h]
    FFXLocationData("Treasure 166", 166, 0x02AC, "treasure"),  # Gear: buki_get #51 [33h] { Yuna [01h], Armor {Water Eater [802Dh], Fire Eater [8021h], Lightning Eater [8029h], Empty} }
    FFXLocationData("Treasure 167", 167, 0x02B0, "treasure"),  # Item: 1x Special Sphere [204Ch]
    FFXLocationData("Treasure 168", 168, 0x02B4, "treasure"),  # Item: 1x Lv. 4 Key Sphere [2054h]
    FFXLocationData("Treasure 169", 169, 0x02B8, "treasure"),  # Gear: buki_get #52 [34h] { Wakka [04h], Weapon {Waterstrike [802Ah], Firestrike [801Eh], Lightningstrike [8026h], Icestrike [8022h]} }
    FFXLocationData("Treasure 170", 170, 0x02BC, "treasure"),  # Gear: buki_get #53 [35h] { Auron [02h], Armor {Darkproof [8048h], Deathproof [8030h], Empty, Empty} }
    FFXLocationData("Treasure 171", 171, 0x02C0, "treasure"),  # Gil: 20000 [C8h]
    FFXLocationData("Treasure 172", 172, 0x02C4, "treasure"),  # Item: 1x HP Sphere [2055h]
    FFXLocationData("Treasure 173", 173, 0x02C8, "treasure"),  # Item: 1x Defense Sphere [2058h]
    FFXLocationData("Treasure 174", 174, 0x02CC, "treasure"),  # Item: 1x Megalixir [2009h]
    FFXLocationData("Treasure 175", 175, 0x02D0, "treasure"),  # Gear: buki_get #54 [36h] { Yuna [01h], Weapon {SOS Overdrive [8010h]} }
    FFXLocationData("Treasure 176", 176, 0x02D4, "treasure"),  # Key Item: Cloudy Mirror [A002h]
    FFXLocationData("Jecht Sphere", 177, 0x02D8, "treasure"),  # Key Item: Jecht's Sphere [A020h]
    FFXLocationData("Treasure 178", 178, 0x02DC, "treasure"),  # Item: 2x Phoenix Down [2006h]
    FFXLocationData("Treasure 179", 179, 0x02E0, "treasure"),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Treasure 180", 180, 0x02E4, "treasure"),  # Gil: 5000 [32h]
    FFXLocationData("Treasure 181", 181, 0x02E8, "treasure"),  # Gear: buki_get #55 [37h] { Wakka [04h], Weapon {Waterstrike [802Ah], Empty} }
    FFXLocationData("Treasure 182", 182, 0x02EC, "treasure"),  # Item: 1x X-Potion [2002h]
    FFXLocationData("Treasure 183", 183, 0x02F0, "treasure"),  # Item: 1x Ether [2004h]
    FFXLocationData("Treasure 184", 184, 0x02F4, "treasure"),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Treasure 185", 185, 0x02F8, "treasure"),  # Gil: 2000 [14h]
    FFXLocationData("Mi'Hen Highroad: Beat Belgemine's Aeon Fight", 186, 0x02FC, "treasure"),  # Gear: buki_get #74 [4Ah] { Yuna [01h], Armor {HP +10% [8073h], Silence Ward [8045h]} }
    FFXLocationData("Treasure 187", 187, 0x0300, "treasure"),  # Item: 30x Power Sphere [2046h]
    FFXLocationData("Treasure 188", 188, 0x0304, "treasure"),  # Gear: buki_get #56 [38h] { Kimahri [03h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    FFXLocationData("Thunder Plains: Lightning Minigame - 5 Consecutive Lightning Dodges", 189, 0x0308, "treasure"),  # Item: 2x X-Potion [2002h]
    FFXLocationData("Thunder Plains: Lightning Minigame - 10 Consecutive Lightning Dodges", 190, 0x030C, "treasure"),  # Item: 2x Mega-Potion [2003h]
    FFXLocationData("Thunder Plains: Lightning Minigame - 20 Consecutive Lightning Dodges", 191, 0x0310, "treasure"),  # Item: 2x MP Sphere [2056h]
    FFXLocationData("Thunder Plains: Lightning Minigame - 50 Consecutive Lightning Dodges", 192, 0x0314, "treasure"),  # Item: 3x Strength Sphere [2057h]
    FFXLocationData("Thunder Plains: Lightning Minigame - 100 Consecutive Lightning Dodges", 193, 0x0318, "treasure"),  # Item: 3x HP Sphere [2055h]
    FFXLocationData("Thunder Plains: Lightning Minigame - 150 Consecutive Lightning Dodges", 194, 0x031C, "treasure"),  # Item: 4x Megalixir [2009h]
    FFXLocationData("Thunder Plains: Lightning Minigame - 30 Total Lightning Hits", 195, 0x0320, "treasure"),  # Item: 1x Ether [2004h]
    FFXLocationData("Thunder Plains: Lightning Minigame - 80 Total Lightning Hits", 196, 0x0324, "treasure"),  # Item: 1x Elixir [2008h]
    FFXLocationData("Treasure 197", 197, 0x0328, "treasure"),  # Item: 1x X-Potion [2002h]
    FFXLocationData("Treasure 198", 198, 0x032C, "treasure"),  # Item: 2x Phoenix Down [2006h]
    FFXLocationData("Treasure 199", 199, 0x0330, "treasure"),  # Gil: 5000 [32h]
    FFXLocationData("Treasure 200", 200, 0x0334, "treasure"),  # Item: 1x Ether [2004h]
    FFXLocationData("Treasure 201", 201, 0x0338, "treasure"),  # Item: 4x Antidote [200Ah]
    FFXLocationData("Treasure 202", 202, 0x033C, "treasure"),  # Item: 1x Mega-Potion [2003h]
    # FFXLocationData("Baaj Temple: Grenades from Rikku", 203, 0x0340, "treasure"),  # Item: 2x Grenade [2023h]
    FFXLocationData("Treasure 204", 204, 0x0344, "treasure"),  # Item: 1x Megalixir [2009h]
    FFXLocationData("Treasure 205", 205, 0x0348, "treasure"),  # Item: 4x Mega Phoenix [2007h]
    FFXLocationData("Treasure 206", 206, 0x034C, "treasure"),  # Item: 1x Magic Sphere [2059h]
    FFXLocationData("Treasure 207", 207, 0x0350, "treasure"),  # Gear: buki_get #1 [01h] { Tidus [00h], Weapon {Strength +5% [8063h], Strength +10% [8064h], Waterstrike [802Ah], Sensor [8000h]} }
    FFXLocationData("Treasure 208", 208, 0x0354, "treasure"),  # Gear: buki_get #1 [01h] { Tidus [00h], Weapon {Strength +5% [8063h], Strength +10% [8064h], Waterstrike [802Ah], Sensor [8000h]} }
    FFXLocationData("Treasure 209", 209, 0x0358, "treasure"),  # Gear: buki_get #60 [3Ch] { Yuna [01h], Weapon {Half MP Cost [800Ch], Empty, Empty} }
    FFXLocationData("Treasure 210", 210, 0x035C, "treasure"),  # Item: 8x Al Bhed Potion [2014h]
    FFXLocationData("Treasure 211", 211, 0x0360, "treasure"),  # Item: 8x Al Bhed Potion [2014h]
    FFXLocationData("Treasure 212", 212, 0x0364, "treasure"),  # Item: 8x Al Bhed Potion [2014h]
    FFXLocationData("Baaj Temple: South of the eastern door inside the temple, in a chest", 213, 0x0368, "treasure"),  # Item: 1x X-Potion [2002h]
    FFXLocationData("Treasure 214", 214, 0x036C, "treasure"),  # Gear: buki_get #61 [3Dh] { Rikku [06h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    FFXLocationData("Treasure 215", 215, 0x0370, "treasure"),  # Gil: 400 [04h]
    FFXLocationData("Treasure 216", 216, 0x0374, "treasure"),  # Item: 2x Potion [2000h]
    FFXLocationData("Treasure 217", 217, 0x0378, "treasure"),  # Item: 1x HP Sphere [2055h]
    FFXLocationData("Treasure 218", 218, 0x037C, "treasure"),  # Item: 8x Lightning Marble [201Eh]
    FFXLocationData("Baaj Temple: One screen north of starting location, past the save sphere and to the left", 219, 0x0380, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 220", 220, 0x0384, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 221", 221, 0x0388, "treasure"),  # Item: 1x Dark Matter [2035h]
    FFXLocationData("Treasure 222", 222, 0x038C, "treasure"),  # Item: 1x Teleport Sphere [2062h]
    FFXLocationData("Treasure 223", 223, 0x0390, "treasure"),  # Item: 1x Three Stars [2045h]
    FFXLocationData("Treasure 224", 224, 0x0394, "treasure"),  # Item: 1x Luck Sphere [205Eh]
    FFXLocationData("Treasure 225", 225, 0x0398, "treasure"),  # Item: 1x Underdog's Secret [206Eh]
    FFXLocationData("Treasure 226", 226, 0x039C, "treasure"),  # Item: 1x Megalixir [2009h]
    FFXLocationData("Treasure 227", 227, 0x03A0, "treasure"),  # Item: 1x Return Sphere [2060h]
    FFXLocationData("Treasure 228", 228, 0x03A4, "treasure"),  # Item: 1x Lv. 1 Key Sphere [2051h]
    FFXLocationData("Treasure 229", 229, 0x03A8, "treasure"),  # Item: 1x Mega Phoenix [2007h]
    FFXLocationData("Treasure 230", 230, 0x03AC, "treasure"),  # Item: 1x Elixir [2008h]
    FFXLocationData("Treasure 231", 231, 0x03B0, "treasure"),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Treasure 232", 232, 0x03B4, "treasure"),  # Item: 1x X-Potion [2002h]
    FFXLocationData("Treasure 233", 233, 0x03B8, "treasure"),  # Item: 1x Ether [2004h]
    FFXLocationData("Treasure 234", 234, 0x03BC, "treasure"),  # Item: 2x Remedy [200Fh]
    FFXLocationData("Treasure 235", 235, 0x03C0, "treasure"),  # Item: 2x Phoenix Down [2006h]
    FFXLocationData("Treasure 236", 236, 0x03C4, "treasure"),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Treasure 237", 237, 0x03C8, "treasure"),  # Item: 5x Power Sphere [2046h]
    FFXLocationData("Treasure 238", 238, 0x03CC, "treasure"),  # Item: 5x Mana Sphere [2047h]
    FFXLocationData("Treasure 239", 239, 0x03D0, "treasure"),  # Item: 5x Speed Sphere [2048h]
    FFXLocationData("Treasure 240", 240, 0x03D4, "treasure"),  # Item: 5x Ability Sphere [2049h]
    FFXLocationData("Treasure 241", 241, 0x03D8, "treasure"),  # Item: 1x Echo Screen [200Dh]
    FFXLocationData("Treasure 242", 242, 0x03DC, "treasure"),  # Item: 1x Eye Drops [200Ch]
    FFXLocationData("Treasure 243", 243, 0x03E0, "treasure"),  # Item: 1x Antidote [200Ah]
    FFXLocationData("Treasure 244", 244, 0x03E4, "treasure"),  # Key Item: Jupiter Sigil [A02Dh]
    FFXLocationData("Treasure 245", 245, 0x03E8, "treasure"),  # Item: 1x Elixir [2008h]
    FFXLocationData("Treasure 246", 246, 0x03EC, "treasure"),  # Item: 1x X-Potion [2002h]
    FFXLocationData("Treasure 247", 247, 0x03F0, "treasure"),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Treasure 248", 248, 0x03F4, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 249", 249, 0x03F8, "treasure"),  # Item: 4x Echo Screen [200Dh]
    FFXLocationData("Treasure 250", 250, 0x03FC, "treasure"),  # Item: 4x Eye Drops [200Ch]
    FFXLocationData("Treasure 251", 251, 0x0400, "treasure"),  # Item: 4x Antidote [200Ah]
    FFXLocationData("Treasure 252", 252, 0x0404, "treasure"),  # Item: 4x Soft [200Bh]
    FFXLocationData("Treasure 253", 253, 0x0408, "treasure"),  # Item: 2x Potion [2000h]
    FFXLocationData("Treasure 254", 254, 0x040C, "treasure"),  # Item: 2x Phoenix Down [2006h]
    FFXLocationData("Treasure 255", 255, 0x0410, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 256", 256, 0x0414, "treasure"),  # Item: 1x Phoenix Down [2006h]
    FFXLocationData("Treasure 257", 257, 0x0418, "treasure"),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Treasure 258", 258, 0x041C, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 259", 259, 0x0420, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 260", 260, 0x0424, "treasure"),  # Item: 1x Phoenix Down [2006h]
    FFXLocationData("Treasure 261", 261, 0x0428, "treasure"),  # Item: 1x Return Sphere [2060h]
    FFXLocationData("Treasure 262", 262, 0x042C, "treasure"),  # Item: 1x Rename Card [2065h]
    FFXLocationData("Treasure 263", 263, 0x0430, "treasure"),  # Item: 1x Ether [2004h]
    FFXLocationData("Treasure 264", 264, 0x0434, "treasure"),  # Item: 1x X-Potion [2002h]
    FFXLocationData("Treasure 265", 265, 0x0438, "treasure"),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Treasure 266", 266, 0x043C, "treasure"),  # Item: 2x Remedy [200Fh]
    FFXLocationData("Treasure 267", 267, 0x0440, "treasure"),  # Key Item: Sun Crest [A023h]
    FFXLocationData("Treasure 268", 268, 0x0444, "treasure"),  # Key Item: Moon Crest [A025h]
    FFXLocationData("Treasure 269", 269, 0x0448, "treasure"),  # Key Item: Mars Crest [A027h]
    FFXLocationData("Treasure 270", 270, 0x044C, "treasure"),  # Key Item: Saturn Crest [A02Ah]
    FFXLocationData("Treasure 271", 271, 0x0450, "treasure"),  # Key Item: Jupiter Crest [A02Ch]
    FFXLocationData("Treasure 272", 272, 0x0454, "treasure"),  # Key Item: Venus Crest [A02Eh]
    FFXLocationData("Treasure 273", 273, 0x0458, "treasure"),  # Key Item: Mercury Crest [A030h]
    FFXLocationData("Treasure 274", 274, 0x045C, "treasure"),  # Key Item: Sun Sigil [A024h]
    FFXLocationData("Treasure 275", 275, 0x0460, "treasure"),  # Key Item: Moon Sigil [A026h]
    FFXLocationData("Treasure 276", 276, 0x0464, "treasure"),  # Key Item: Mars Sigil [A028h]
    FFXLocationData("Treasure 277", 277, 0x0468, "treasure"),  # Key Item: Saturn Sigil [A02Bh]
    FFXLocationData("Treasure 278", 278, 0x046C, "treasure"),  # Key Item: Venus Sigil [A02Fh]
    FFXLocationData("Treasure 279", 279, 0x0470, "treasure"),  # Key Item: Mercury Sigil [A031h]
    FFXLocationData("Treasure 280", 280, 0x0474, "treasure"),  # Item: 2x Megalixir [2009h]
    FFXLocationData("Treasure 281", 281, 0x0478, "treasure"),  # Item: 2x Elixir [2008h]
    FFXLocationData("Treasure 282", 282, 0x047C, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 283", 283, 0x0480, "treasure"),  # Item: 3x Potion [2000h]
    FFXLocationData("Treasure 284", 284, 0x0484, "treasure"),  # Item: 2x Potion [2000h]
    FFXLocationData("Treasure 285", 285, 0x0488, "treasure"),  # Gil: 200 [02h]
    FFXLocationData("Treasure 286", 286, 0x048C, "treasure"),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Treasure 287", 287, 0x0490, "treasure"),  # Gear: buki_get #62 [3Eh] { Yuna [01h], Armor {HP +10% [8073h]} }
    FFXLocationData("Treasure 288", 288, 0x0494, "treasure"),  # Item: 3x Phoenix Down [2006h]
    FFXLocationData("Treasure 289", 289, 0x0498, "treasure"),  # Gil: 400 [04h]
    FFXLocationData("Treasure 290", 290, 0x049C, "treasure"),  # Item: 1x Ether [2004h]
    FFXLocationData("Treasure 291", 291, 0x04A0, "treasure"),  # Item: 4x Antidote [200Ah]
    FFXLocationData("Treasure 292", 292, 0x04A4, "treasure"),  # Item: 1x Elixir [2008h]
    FFXLocationData("Treasure 293", 293, 0x04A8, "treasure"),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Treasure 294", 294, 0x04AC, "treasure"),  # Item: 3x Phoenix Down [2006h]
    FFXLocationData("Treasure 295", 295, 0x04B0, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 296", 296, 0x04B4, "treasure"),  # Item: 3x Potion [2000h]
    FFXLocationData("Treasure 297", 297, 0x04B8, "treasure"),  # Gear: buki_get #63 [3Fh] { Tidus [00h], Weapon {Strength +3% [8062h], Empty, Empty, Empty} }
    FFXLocationData("Treasure 298", 298, 0x04BC, "treasure"),  # Gear: buki_get #64 [40h] { Yuna [01h], Armor {Stoneproof [8038h], Empty} }
    FFXLocationData("Treasure 299", 299, 0x04C0, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 300", 300, 0x04C4, "treasure"),  # Item: 1x Ether [2004h]
    FFXLocationData("Treasure 301", 301, 0x04C8, "treasure"),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Treasure 302", 302, 0x04CC, "treasure"),  # Gear: buki_get #65 [41h] { Kimahri [03h], Weapon {Magic +20% [8069h], Empty} }
    FFXLocationData("Treasure 303", 303, 0x04D0, "treasure"),  # Item: 10x Potion [2000h]
    FFXLocationData("Treasure 304", 304, 0x04D4, "treasure"),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Treasure 305", 305, 0x04D8, "treasure"),  # Gil: 400 [04h]
    FFXLocationData("Treasure 306", 306, 0x04DC, "treasure"),  # Item: 1x Elixir [2008h]
    FFXLocationData("Treasure 307", 307, 0x04E0, "treasure"),  # Item: 1x Ether [2004h]
    FFXLocationData("Treasure 308", 308, 0x04E4, "treasure"),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Treasure 309", 309, 0x04E8, "treasure"),  # Gear: buki_get #66 [42h] { Kimahri [03h], Weapon {Piercing [800Bh], Sensor [8000h], Strength +10% [8064h]} }
    FFXLocationData("Treasure 310", 310, 0x04EC, "treasure"),  # Item: 2x Antidote [200Ah]
    FFXLocationData("Treasure 311", 311, 0x04F0, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 312", 312, 0x04F4, "treasure"),  # Item: 3x Soft [200Bh]
    FFXLocationData("Treasure 313", 313, 0x04F8, "treasure"),  # Gear: buki_get #67 [43h] { Yuna [01h], Armor {HP +10% [8073h], Fire Ward [801Fh]} }
    FFXLocationData("Treasure 314", 314, 0x04FC, "treasure"),  # Item: 1x Ether [2004h]
    FFXLocationData("Treasure 315", 315, 0x0500, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 316", 316, 0x0504, "treasure"),  # Gil: 600 [06h]
    FFXLocationData("Treasure 317", 317, 0x0508, "treasure"),  # Item: 1x Lv. 1 Key Sphere [2051h]
    FFXLocationData("Treasure 318", 318, 0x050C, "treasure"),  # Item: 4x Antidote [200Ah]
    FFXLocationData("Treasure 319", 319, 0x0510, "treasure"),  # Gear: buki_get #68 [44h] { Lulu [05h], Armor {HP +20% [8074h], Empty} }
    FFXLocationData("Treasure 320", 320, 0x0514, "treasure"),  # Item: 2x Phoenix Down [2006h]
    FFXLocationData("Treasure 321", 321, 0x0518, "treasure"),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Treasure 322", 322, 0x051C, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 323", 323, 0x0520, "treasure"),  # Item: 1x Ether [2004h]
    FFXLocationData("Treasure 324", 324, 0x0524, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 325", 325, 0x0528, "treasure"),  # Item: 10x Potion [2000h]
    FFXLocationData("Treasure 326", 326, 0x052C, "treasure"),  # Gil: 400 [04h]
    FFXLocationData("Treasure 327", 327, 0x0530, "treasure"),  # Item: 1x X-Potion [2002h]
    FFXLocationData("Treasure 328", 328, 0x0534, "treasure"),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Treasure 329", 329, 0x0538, "treasure"),  # Item: 99x Warp Sphere [2063h]
    FFXLocationData("Treasure 330", 330, 0x053C, "treasure"),  # Item: 1x Teleport Sphere [2062h]
    FFXLocationData("Treasure 331", 331, 0x0540, "treasure"),  # Item: 1x Friend Sphere [2061h]
    FFXLocationData("Treasure 332", 332, 0x0544, "treasure"),  # Item: 1x Magic Sphere [2059h]
    FFXLocationData("Treasure 333", 333, 0x0548, "treasure"),  # Key Item: Blossom Crown [A032h]
    FFXLocationData("Treasure 334", 334, 0x054C, "treasure"),  # Key Item: Flower Scepter [A033h]
    FFXLocationData("Treasure 335", 335, 0x0550, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 336", 336, 0x0554, "treasure"),  # Item: 1x Friend Sphere [2061h]
    FFXLocationData("Treasure 337", 337, 0x0558, "treasure"),  # Item: 1x Elixir [2008h]
    FFXLocationData("Treasure 338", 338, 0x055C, "treasure"),  # Item: 1x Lv. 1 Key Sphere [2051h]
    FFXLocationData("Treasure 339", 339, 0x0560, "treasure"),  # Item: 1x Lv. 2 Key Sphere [2052h]
    FFXLocationData("Treasure 340", 340, 0x0564, "treasure"),  # Item: 1x Lv. 3 Key Sphere [2053h]
    FFXLocationData("Treasure 341", 341, 0x0568, "treasure"),  # Item: 1x X-Potion [2002h]
    FFXLocationData("Treasure 342", 342, 0x056C, "treasure"),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Treasure 343", 343, 0x0570, "treasure"),  # Item: 1x Ether [2004h]
    FFXLocationData("Treasure 344", 344, 0x0574, "treasure"),  # Item: 1x Turbo Ether [2005h]
    FFXLocationData("Treasure 345", 345, 0x0578, "treasure"),  # Gear: buki_get #69 [45h] { Tidus [00h], Armor {Lightningproof [8028h], Empty} }
    FFXLocationData("Treasure 346", 346, 0x057C, "treasure"),  # Item: 4x Remedy [200Fh]
    FFXLocationData("Treasure 347", 347, 0x0580, "treasure"),  # Item: 2x Ether [2004h]
    FFXLocationData("Treasure 348", 348, 0x0584, "treasure"),  # Item: 4x Hi-Potion [2001h]
    FFXLocationData("Treasure 349", 349, 0x0588, "treasure"),  # Item: 2x Mega-Potion [2003h]
    FFXLocationData("Treasure 350", 350, 0x058C, "treasure"),  # Item: 2x X-Potion [2002h]
    FFXLocationData("Treasure 351", 351, 0x0590, "treasure"),  # Item: 4x Hi-Potion [2001h]
    FFXLocationData("Treasure 352", 352, 0x0594, "treasure"),  # Item: 1x Elixir [2008h]
    FFXLocationData("Treasure 353", 353, 0x0598, "treasure"),  # Gil: 10000 [64h]
    FFXLocationData("Treasure 354", 354, 0x059C, "treasure"),  # Item: 1x Lv. 2 Key Sphere [2052h]
    FFXLocationData("Treasure 355", 355, 0x05A0, "treasure"),  # Item: 8x Hi-Potion [2001h]
    FFXLocationData("Treasure 356", 356, 0x05A4, "treasure"),  # Item: 3x Mega-Potion [2003h]
    FFXLocationData("Treasure 357", 357, 0x05A8, "treasure"),  # Item: 2x X-Potion [2002h]
    FFXLocationData("Treasure 358", 358, 0x05AC, "treasure"),  # Item: 3x Megalixir [2009h]
    FFXLocationData("Treasure 359", 359, 0x05B0, "treasure"),  # Item: 2x Teleport Sphere [2062h]
    FFXLocationData("Treasure 360", 360, 0x05B4, "treasure"),  # Item: 6x Al Bhed Potion [2014h]
    FFXLocationData("Treasure 361", 361, 0x05B8, "treasure"),  # Item: 4x Al Bhed Potion [2014h]
    FFXLocationData("Treasure 362", 362, 0x05BC, "treasure"),  # Item: 1x Lv. 2 Key Sphere [2052h]
    FFXLocationData("Treasure 363", 363, 0x05C0, "treasure"),  # Item: 1x Lv. 4 Key Sphere [2054h]
    FFXLocationData("Treasure 364", 364, 0x05C4, "treasure"),  # Gil: 10000 [64h]
    FFXLocationData("Treasure 365", 365, 0x05C8, "treasure"),  # Gear: buki_get #70 [46h] { Wakka [04h], Weapon {Magic +20% [8069h], Magic +10% [8068h], Magic +5% [8067h], Magic +3% [8066h]} }
    FFXLocationData("Mi'Hen Highroad: Lose Belgemine's Aeon Fight", 366, 0x05CC, "treasure"),  # Gear: buki_get #71 [47h] { Yuna [01h], Armor {HP +10% [8073h], Empty} }
    FFXLocationData("Treasure 367", 367, 0x05D0, "treasure"),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Treasure 368", 368, 0x05D4, "treasure"),  # Gear: buki_get #72 [48h] { Rikku [06h], Armor {Lightningproof [8028h], Fireproof [8020h], Iceproof [8024h], Empty} }
    FFXLocationData("Treasure 369", 369, 0x05D8, "treasure"),  # Gear: buki_get #73 [49h] { Auron [02h], Weapon {Piercing [800Bh], One MP Cost [800Dh], Empty, Empty} }
    FFXLocationData("Treasure 370", 370, 0x05DC, "treasure"),  # Item: 30x Speed Sphere [2048h]
    FFXLocationData("Treasure 371", 371, 0x05E0, "treasure"),  # Key Item: Aeon's Soul [A01Fh]
    FFXLocationData("Treasure 372", 372, 0x05E4, "treasure"),  # Item: 2x Dragon Scale [2021h]
    FFXLocationData("Treasure 373", 373, 0x05E8, "treasure"),  # Item: 6x Smoke Bomb [2028h]
    FFXLocationData("Treasure 374", 374, 0x05EC, "treasure"),  # Key Item: Summoner's Soul [A01Eh]
    FFXLocationData("Treasure 375", 375, 0x05F0, "treasure"),  # Item: 4x Al Bhed Potion [2014h]
    FFXLocationData("Treasure 376", 376, 0x05F4, "treasure"),  # Item: 3x Lv. 1 Key Sphere [2051h]
    FFXLocationData("Treasure 377", 377, 0x05F8, "treasure"),  # Item: 3x Lv. 1 Key Sphere [2051h]
    FFXLocationData("Treasure 378", 378, 0x05FC, "treasure"),  # Item: 1x Magic Def Sphere [205Ah]
    FFXLocationData("Treasure 379", 379, 0x0600, "treasure"),  # Item: 4x Lightning Gem [201Fh]
    FFXLocationData("Treasure 380", 380, 0x0604, "treasure"),  # Item: 4x Power Sphere [2046h]
    FFXLocationData("Treasure 381", 381, 0x0608, "treasure"),  # Item: 30x X-Potion [2002h]
    FFXLocationData("Treasure 382", 382, 0x060C, "treasure"),  # Item: 5x Mana Sphere [2047h]
    FFXLocationData("Treasure 383", 383, 0x0610, "treasure"),  # Item: 10x Chocobo Feather [2036h]
    FFXLocationData("Treasure 384", 384, 0x0614, "treasure"),  # Item: 8x Power Sphere [2046h]
    FFXLocationData("Treasure 385", 385, 0x0618, "treasure"),  # Item: 60x Mega-Potion [2003h]
    FFXLocationData("Treasure 386", 386, 0x061C, "treasure"),  # Item: 6x Star Curtain [203Ah]
    FFXLocationData("Treasure 387", 387, 0x0620, "treasure"),  # Item: 8x Mana Sphere [2047h]
    FFXLocationData("Treasure 388", 388, 0x0624, "treasure"),  # Item: 8x Shadow Gem [2029h]
    FFXLocationData("Treasure 389", 389, 0x0628, "treasure"),  # Item: 10x Power Sphere [2046h]
    FFXLocationData("Treasure 390", 390, 0x062C, "treasure"),  # Item: 60x Stamina Spring [203Dh]
    FFXLocationData("Treasure 391", 391, 0x0630, "treasure"),  # Item: 10x Mana Sphere [2047h]
    FFXLocationData("Treasure 392", 392, 0x0634, "treasure"),  # Item: 40x Shining Gem [202Ah]
    FFXLocationData("Treasure 393", 393, 0x0638, "treasure"),  # Item: 12x Power Sphere [2046h]
    FFXLocationData("Treasure 394", 394, 0x063C, "treasure"),  # Item: 1x Teleport Sphere [2062h]
    FFXLocationData("Treasure 395", 395, 0x0640, "treasure"),  # Item: 1x Skill Sphere [204Dh]
    FFXLocationData("Treasure 396", 396, 0x0644, "treasure"),  # Item: 1x Special Sphere [204Ch]
    FFXLocationData("Bikanel Island: Vocabulary Chest", 397, 0x0648, "treasure"),  # Item: 1x Friend Sphere [2061h]
    FFXLocationData("Bikanel Island: Treasure Chest of Dreams (Elixir)", 398, 0x064C, "treasure"),  # Item: 1x Elixir [2008h]
    FFXLocationData("Bikanel Island: Treasure Chest of Dreams (Hi-Potion)", 399, 0x0650, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Bikanel Island: Treasure Chest of Dreams (Mega-Potion)", 400, 0x0654, "treasure"),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Bikanel Island: Treasure Chest of Dreams (Soft)", 401, 0x0658, "treasure"),  # Item: 1x Soft [200Bh]
    FFXLocationData("Bikanel Island: Treasure Chest of Dreams (Potion)", 402, 0x065C, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Bikanel Island: Treasure Chest of Dreams (Remedy)", 403, 0x0660, "treasure"),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Treasure 404", 404, 0x0664, "treasure"),  # Item: 2x Potion [2000h]
    FFXLocationData("Treasure 405", 405, 0x0668, "treasure"),  # Item: 99x Underdog's Secret [206Eh]
    FFXLocationData("Treasure 406", 406, 0x066C, "treasure"),  # Item: 1x Wht Magic Sphere [204Eh]
    FFXLocationData("Treasure 407", 407, 0x0670, "treasure"),  # Item: 1x Elixir [2008h]
    FFXLocationData("Treasure 408", 408, 0x0674, "treasure"),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 409", 409, 0x0678, "treasure"),  # Item: 2x Potion [2000h]
    FFXLocationData("Treasure 410", 410, 0x067C, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 411", 411, 0x0680, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 412", 412, 0x0684, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 413", 413, 0x0688, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 414", 414, 0x068C, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 415", 415, 0x0690, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 416", 416, 0x0694, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 417", 417, 0x0698, "treasure"),  # Item: 1x Elixir [2008h]
    FFXLocationData("Treasure 418", 418, 0x069C, "treasure"),  # Item: 1x Megalixir [2009h]
    FFXLocationData("Treasure 419", 419, 0x06A0, "treasure"),  # Item: 60x Three Stars [2045h]
    FFXLocationData("Treasure 420", 420, 0x06A4, "treasure"),  # Item: 30x Pendulum [2069h]
    FFXLocationData("Treasure 421", 421, 0x06A8, "treasure"),  # Item: 30x Wings to Discovery [206Ch]
    FFXLocationData("Treasure 422", 422, 0x06AC, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 423", 423, 0x06B0, "treasure"),  # Item: 1x Lv. 1 Key Sphere [2051h]
    FFXLocationData("Treasure 424", 424, 0x06B4, "treasure"),  # Item: 99x Stamina Tonic [2043h]
    FFXLocationData("Treasure 425", 425, 0x06B8, "treasure"),  # Item: 99x Poison Fang [202Dh]
    FFXLocationData("Treasure 426", 426, 0x06BC, "treasure"),  # Item: 99x Soul Spring [203Eh]
    FFXLocationData("Treasure 427", 427, 0x06C0, "treasure"),  # Item: 99x Candle of Life [2030h]
    FFXLocationData("Treasure 428", 428, 0x06C4, "treasure"),  # Item: 99x Petrify Grenade [2031h]
    FFXLocationData("Treasure 429", 429, 0x06C8, "treasure"),  # Item: 99x Chocobo Wing [2037h]
    FFXLocationData("Treasure 430", 430, 0x06CC, "treasure"),  # Item: 60x Shining Gem [202Ah]
    FFXLocationData("Treasure 431", 431, 0x06D0, "treasure"),  # Item: 99x Shadow Gem [2029h]
    FFXLocationData("Treasure 432", 432, 0x06D4, "treasure"),  # Item: 60x Farplane Wind [2033h]
    FFXLocationData("Treasure 433", 433, 0x06D8, "treasure"),  # Item: 40x Silver Hourglass [202Eh]
    FFXLocationData("Treasure 434", 434, 0x06DC, "treasure"),  # Key Item: Blossom Crown [A032h]
    FFXLocationData("Treasure 435", 435, 0x06E0, "treasure"),  # Item: 99x Lunar Curtain [2038h]
    FFXLocationData("Treasure 436", 436, 0x06E4, "treasure"),  # Item: 60x Designer Wallet [2034h]
    FFXLocationData("Treasure 437", 437, 0x06E8, "treasure"),  # Item: 99x Chocobo Feather [2036h]
    FFXLocationData("Treasure 438", 438, 0x06EC, "treasure"),  # Item: 99x Stamina Spring [203Dh]
    FFXLocationData("Treasure 439", 439, 0x06F0, "treasure"),  # Item: 99x Mega Phoenix [2007h]
    FFXLocationData("Treasure 440", 440, 0x06F4, "treasure"),  # Item: 60x Mana Tonic [2044h]
    FFXLocationData("Treasure 441", 441, 0x06F8, "treasure"),  # Item: 99x Mana Spring [203Ch]
    FFXLocationData("Treasure 442", 442, 0x06FC, "treasure"),  # Item: 60x Stamina Tablet [2040h]
    FFXLocationData("Treasure 443", 443, 0x0700, "treasure"),  # Item: 60x Twin Stars [2042h]
    FFXLocationData("Treasure 444", 444, 0x0704, "treasure"),  # Item: 99x Star Curtain [203Ah]
    FFXLocationData("Treasure 445", 445, 0x0708, "treasure"),  # Item: 99x Gold Hourglass [202Fh]
    FFXLocationData("Treasure 446", 446, 0x070C, "treasure"),  # Item: 99x Purifying Salt [203Fh]
    FFXLocationData("Treasure 447", 447, 0x0710, "treasure"),  # Item: 99x Healing Spring [203Bh]
    FFXLocationData("Treasure 448", 448, 0x0714, "treasure"),  # Item: 60x Turbo Ether [2005h]
    FFXLocationData("Treasure 449", 449, 0x0718, "treasure"),  # Item: 99x Light Curtain [2039h]
    FFXLocationData("Treasure 450", 450, 0x071C, "treasure"),  # Item: 60x Mana Tablet [2041h]
    FFXLocationData("Treasure 451", 451, 0x0720, "treasure"),  # Item: 60x Three Stars [2045h]
    FFXLocationData("Treasure 452", 452, 0x0724, "treasure"),  # Item: 60x Supreme Gem [202Ch]
    FFXLocationData("Treasure 453", 453, 0x0728, "treasure"),  # Item: 99x Door to Tomorrow [206Bh]
    FFXLocationData("Treasure 454", 454, 0x072C, "treasure"),  # Item: 99x Gambler's Spirit [206Dh]
    FFXLocationData("Treasure 455", 455, 0x0730, "treasure"),  # Item: 99x Winning Formula [206Fh]
    FFXLocationData("Treasure 456", 456, 0x0734, "treasure"),  # Item: 99x Dark Matter [2035h]
    FFXLocationData("Treasure 457", 457, 0x0738, "treasure"),  # Item: 30x Megalixir [2009h]
    FFXLocationData("Treasure 458", 458, 0x073C, "treasure"),  # Item: 10x Master Sphere [2050h]
    FFXLocationData("Treasure 459", 459, 0x0740, "treasure"),  # Item: 1x Map [2064h]
    FFXLocationData("Treasure 460", 460, 0x0744, "treasure"),  # Item: 1x Magic Def Sphere [205Ah]
    FFXLocationData("Treasure 461", 461, 0x0748, "treasure"),  # Item: 1x Accuracy Sphere [205Dh]
    FFXLocationData("Treasure 462", 462, 0x074C, "treasure"),  # Item: 1x Magic Sphere [2059h]
    FFXLocationData("Treasure 463", 463, 0x0750, "treasure"),  # Item: 1x Agility Sphere [205Bh]
    FFXLocationData("Treasure 464", 464, 0x0754, "treasure"),  # Item: 1x Magic Def Sphere [205Ah]
    FFXLocationData("Treasure 465", 465, 0x0758, "treasure"),  # Item: 1x Luck Sphere [205Eh]
    FFXLocationData("Treasure 466", 466, 0x075C, "treasure"),  # Item: 1x Defense Sphere [2058h]
    FFXLocationData("Treasure 467", 467, 0x0760, "treasure"),  # Item: 1x Evasion Sphere [205Ch]
    FFXLocationData("Treasure 468", 468, 0x0764, "treasure"),  # Item: 1x Strength Sphere [2057h]
    FFXLocationData("Treasure 469", 469, 0x0768, "treasure"),  # Item: 2x Shadow Gem [2029h]
    FFXLocationData("Treasure 470", 470, 0x076C, "treasure"),  # Item: 1x Shining Gem [202Ah]
    FFXLocationData("Treasure 471", 471, 0x0770, "treasure"),  # Item: 1x Blessed Gem [202Bh]
    FFXLocationData("Treasure 472", 472, 0x0774, "treasure"),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 473", 473, 0x0778, "treasure"),  # Item: 1x Elixir [2008h]
    FFXLocationData("Treasure 474", 474, 0x077C, "treasure"),  # Item: 1x Megalixir [2009h]
    FFXLocationData("Treasure 475", 475, 0x0780, "treasure"),  # Item: 1x Friend Sphere [2061h]
    FFXLocationData("Treasure 476", 476, 0x0784, "treasure"),  # Item: 1x Agility Sphere [205Bh]
    FFXLocationData("Treasure 477", 477, 0x0788, "treasure"),  # Item: 1x Defense Sphere [2058h]
    FFXLocationData("Treasure 478", 478, 0x078C, "treasure"),  # Item: 1x Luck Sphere [205Eh]
    FFXLocationData("Treasure 479", 479, 0x0790, "treasure"),  # Item: 1x Accuracy Sphere [205Dh]
    FFXLocationData("Treasure 480", 480, 0x0794, "treasure"),  # Gear: buki_get #75 [4Bh] { Kimahri [03h], Weapon {Magic Counter [8005h], Evade & Counter [8004h], Empty, Empty} }
    FFXLocationData("Treasure 481", 481, 0x0798, "treasure"),  # Gear: buki_get #76 [4Ch] { Rikku [06h], Weapon {Initiative [8002h], Poisonstrike [803Ah], Empty} }
    FFXLocationData("Treasure 482", 482, 0x079C, "treasure"),  # Gear: buki_get #77 [4Dh] { Lulu [05h], Armor {Ice Eater [8025h], Fire Eater [8021h], !Water Eater [802Dh]} }
    FFXLocationData("Treasure 483", 483, 0x07A0, "treasure"),  # Gear: buki_get #78 [4Eh] { Tidus [00h], Weapon {Double AP [8012h]} }
    FFXLocationData("Treasure 484", 484, 0x07A4, "treasure"),  # Item: 1x Magic Sphere [2059h]
    FFXLocationData("Treasure 485", 485, 0x07A8, "treasure"),  # Item: 1x Luck Sphere [205Eh]
    FFXLocationData("Treasure 486", 486, 0x07AC, "treasure"),  # Gear: buki_get #79 [4Fh] { Wakka [04h], Weapon {Magic Counter [8005h], Empty} }
    FFXLocationData("Treasure 487", 487, 0x07B0, "treasure"),  # Gear: buki_get #80 [50h] { Auron [02h], Weapon {Silencestrike [8042h], Stonestrike [8036h], Empty} }
    FFXLocationData("Treasure 488", 488, 0x07B4, "treasure"),  # Item: 1x Skill Sphere [204Dh]
    FFXLocationData("Treasure 489", 489, 0x07B8, "treasure"),  # Gear: buki_get #81 [51h] { Yuna [01h], Weapon {Magic +10% [8068h], Magic +5% [8067h], Magic +3% [8066h], Empty} }
    FFXLocationData("Treasure 490", 490, 0x07BC, "treasure"),  # Gear: buki_get #82 [52h] { Kimahri [03h], Weapon {Strength +10% [8064h], Strength +5% [8063h], Strength +3% [8062h], Empty} }
    FFXLocationData("Treasure 491", 491, 0x07C0, "treasure"),  # Item: 1x Wht Magic Sphere [204Eh]
    FFXLocationData("Treasure 492", 492, 0x07C4, "treasure"),  # Gear: buki_get #83 [53h] { Rikku [06h], Weapon {One MP Cost [800Dh], Sensor [8000h]} }
    FFXLocationData("Treasure 493", 493, 0x07C8, "treasure"),  # Gear: buki_get #84 [54h] { Lulu [05h], Weapon {Deathstrike [802Eh], Empty, Empty, Empty} }
    FFXLocationData("Treasure 494", 494, 0x07CC, "treasure"),  # Item: 1x Attribute Sphere [204Bh]
    FFXLocationData("Treasure 495", 495, 0x07D0, "treasure"),  # Gear: buki_get #85 [55h] { Tidus [00h], Weapon {SOS Overdrive [8010h]} }
    FFXLocationData("Treasure 496", 496, 0x07D4, "treasure"),  # Key Item: Mark of Conquest [A029h]
    FFXLocationData("Luca: Win story blitzball match ", 497, 0x07D8, "treasure"),  # Item: 1x Strength Sphere [2057h]
]


def create_location_label_to_id_map() -> Dict[str, int]:
    """
    Creates a map from location labels to their AP location id (address)
    """
    label_to_id_map: Dict[str, int] = {}
    for location in FFXTreasureLocations:
        label_to_id_map[location.name] = location.rom_address

    return label_to_id_map
