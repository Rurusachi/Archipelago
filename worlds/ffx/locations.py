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
    missable: bool


# Boss offset: 0x2000
FFXBossLocations: List[FFXLocationData] = [
    FFXLocationData("Baaj Temple : Klikk Defeated", 0, 0x3000, False),
    FFXLocationData("Al Bhed Ship: Tros Defeated", 1, 0x3001, False),
    FFXLocationData("Besaid: Dark Valefor", 2, 0x3002, False),
    FFXLocationData("S.S. Liki: Sin Fin", 3, 0x3003, False),
    FFXLocationData("S.S. Liki: Sinspawn Echuilles", 4, 0x3004, False),
    FFXLocationData("Kilika: Lord Ochu", 5, 0x3005, False),
    FFXLocationData("Kilika: Sinspawn Geneaux", 6, 0x3006, False),
    FFXLocationData("Luca: Oblitzerator defeated", 7, 0x3007, False),
    FFXLocationData("Mi'Hen Highroad: Chocobo Eater", 8, 0x3008, False),
    FFXLocationData("Mushroom Rock Road: Sinspawn Gui", 9, 0x3009, False),
    FFXLocationData("Mushroom Rock Road: Sinspawn Gui 2", 10, 0x300a, False),
    FFXLocationData("Mushroom Rock Road: Dark Magus Sisters", 11, 0x300b, False),
    FFXLocationData("Moonflow: Extractor", 12, 0x300c, False),
    FFXLocationData("Thunder Plains: Dark Ixion", 13, 0x300d, False),
    FFXLocationData("Macalania Woods: Spherimorph", 14, 0x300e, False),
    FFXLocationData("Lake Macalania: Crawler", 15, 0x300f, False),
    FFXLocationData("Lake Macalania: Seymour/Anima", 16, 0x3010, False),
    FFXLocationData("Lake Macalania: Dark Shiva", 17, 0x3011, False),
    FFXLocationData("Bikanel: Dark Ifrit", 18, 0x3012, False),
    FFXLocationData("Airship: Evrae", 19, 0x3013, False),
    FFXLocationData("Airship: Sin Left Fin", 20, 0x3014, False),
    FFXLocationData("Airship: Sin Right Fin", 21, 0x3015, False),
    FFXLocationData("Airship: Sinspawn Genais", 22, 0x3016, False),
    FFXLocationData("Airship: Overdrive Sin", 23, 0x3017, False),
    FFXLocationData("Airship: Penance", 24, 0x3018, False),
    FFXLocationData("Bevelle: Issaru", 25, 0x3019, False),
    FFXLocationData("Bevelle: Evrae Altana", 26, 0x301a, False),
    FFXLocationData("Bevelle: Seymour Natus", 27, 0x301b, False),
    FFXLocationData("Calm Lands: Defender X", 28, 0x301c, False),
    FFXLocationData("Monster Arena: Nemesis", 29, 0x301d, False),
    FFXLocationData("Cavern of the Stolen Fayth: Dark Yojimbo", 30, 0x301e, False),
    FFXLocationData("Gagazet (Outside): Biran and Benke", 31, 0x301f, False),
    FFXLocationData("Gagazet (Outside): Seymour Flux", 32, 0x3020, False),
    FFXLocationData("Gagazet (Outside): Dark Anima", 33, 0x3021, False),
    FFXLocationData("Zanarkand: Sanctuary Keeper", 34, 0x3022, False),
    FFXLocationData("Zanarkand: Spectral Keeper", 35, 0x3023, False),
    FFXLocationData("Zanarkand: Yunalesca", 36, 0x3024, False),
    FFXLocationData("Zanarkand: Dark Bahamut", 37, 0x3025, False),
    FFXLocationData("Sin: Seymour Omnis", 38, 0x3026, False),
    FFXLocationData("Sin: Braska's Final Aeon", 39, 0x3027, False),
    FFXLocationData("Sin: Contest of Aeons", 40, 0x3028, False),
    FFXLocationData("Sin: Yu Yevon", 41, 0x3029, False),
    FFXLocationData("Omega Ruins: Ultima Weapon", 42, 0x302a, False),
    FFXLocationData("Omega Ruins: Omega Weapon", 43, 0x302b, False),
]

FFXPartyMemberLocations: List[FFXLocationData] = [
]

# Treasure offset: 0x1000
FFXTreasureLocations: List[FFXLocationData] = [
    FFXLocationData("Baaj Temple: Chest 1", 0, 0x1000, False),  # Gil: 200 [02h]
    FFXLocationData("Baaj Temple: Chest 2", 1, 0x1001, False),  # Item: 2x Potion [2000h]
    FFXLocationData("Withered Bouquet", 2, 0x1002, False),  # Key Item: Withered Bouquet [A000h]
    FFXLocationData("Flint", 3, 0x1003, False),  # Key Item: Flint [A001h]
    FFXLocationData("Treasure 4 (Potentially Trashed Chest)", 4, 0x1004, False),  # Gear: buki_get #2 [02h] { Yuna [01h], Weapon {One MP Cost [800Dh], Empty, Empty, Empty} }
    FFXLocationData("Onion Knight", 5, 0x1005, False),  # Gear: buki_get #3 [03h] { Lulu [05h], Weapon Formula=Celestial MP-based [12h] {No AP [8014h], Empty, Empty, Empty} }
    FFXLocationData("Baaj Temple: Ether (Chest)", 6, 0x1006, False),  # Item: 1x Ether [2004h]
    FFXLocationData("Baaj Temple: Hi-Potion (Chest)", 7, 0x1007, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 8 (Potentially Trashed Chest)", 8, 0x1008, False),  # Item: 1x Phoenix Down [2006h]
    FFXLocationData("Besaid: Antidote x2", 9, 0x1009, False),  # Item: 2x Antidote [200Ah]
    # FFXLocationData("Treasure 10 (Potentially Trashed Chest)", 10, 0x100a, False),  # Gil: 200 [02h]
    # FFXLocationData("Treasure 11 (Potentially Trashed Chest)", 11, 0x100b, False),  # Gear: buki_get #4 [04h] { Tidus [00h], Weapon {Firestrike [801Eh]} }
    # FFXLocationData("Treasure 12 (Potentially Trashed Chest)", 12, 0x100c, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Besaid: Phoenix Down x1 (Chest)", 13, 0x100d, False),  # Item: 1x Phoenix Down [2006h]
    FFXLocationData("Besaid: Hi-Potion x1 (Chest)", 14, 0x100e, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Besaid: Destruction Sphere", 15, 0x100f, False),  # Gear: buki_get #5 [05h] { Yuna [01h], Weapon {Magic +5% [8067h], !Magic +3% [8066h], !Sensor [8000h]} }
    FFXLocationData("S.S. Liki: Remedy x1 (Chest)", 16, 0x1010, False),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Kilika: Potion x3 (Chest)", 17, 0x1011, False),  # Item: 3x Potion [2000h]
    FFXLocationData("Kilika: Ether x1 (Chest)", 18, 0x1012, False),  # Item: 1x Ether [2004h]
    FFXLocationData("Kilika: Destruction Sphere", 19, 0x1013, False),  # Gear: buki_get #6 [06h] { Kimahri [03h], Armor {Fire Ward [801Fh], Ice Ward [8023h], Lightning Ward [8027h]} }
    # FFXLocationData("Treasure 20 (Potentially Trashed Chest)", 20, 0x1014, False),  # Gear: buki_get #7 [07h] { Lulu [05h], Armor {Berserk Ward [8051h]} }
    # FFXLocationData("Treasure 21 (Potentially Trashed Chest)", 21, 0x1015, False),  # Item: 1x Potion [2000h] #Likely 21-26 are Potions from Yuna's Luggage as entries are near by S.S. Liki's treasure ID's
    # FFXLocationData("Treasure 22 (Potentially Trashed Chest)", 22, 0x1016, False),  # Item: 1x Potion [2000h]
    # FFXLocationData("Treasure 23 (Potentially Trashed Chest)", 23, 0x1017, False),  # Item: 1x Potion [2000h]
    # FFXLocationData("Treasure 24 (Potentially Trashed Chest)", 24, 0x1018, False),  # Item: 1x Potion [2000h]
    # FFXLocationData("Treasure 25 (Potentially Trashed Chest)", 25, 0x1019, False),  # Item: 1x Potion [2000h]
    # FFXLocationData("Treasure 26 (Potentially Trashed Chest)", 26, 0x101a, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Kilika: Mana Sphere x2 (Chest)", 27, 0x101b, False),  # Item: 2x Mana Sphere [2047h]
    FFXLocationData("Kilika: Scout (Chest)", 28, 0x101c, False),  # Gear: buki_get #8 [08h] { Wakka [04h], Weapon {Icestrike [8022h], Sensor [8000h]} }
    FFXLocationData("Kilika: Luck Sphere x1 (Chest)", 29, 0x101d, False),  # Item: 1x Luck Sphere [205Eh]
    FFXLocationData("Kilika: NulBlaze Shield (Woman NPC after defeating Lord Ochu)", 30, 0x101e, False),  # Gear: buki_get #9 [09h] { Tidus [00h], Armor {SOS NulBlaze [8061h]} }
    FFXLocationData("S.S. Winno: Hi-Potion x1 (Chest)", 31, 0x101f, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Luca: Phoenix Down x2 (Chest)", 32, 0x1020, False),  # Item: 2x Phoenix Down [2006h]
    FFXLocationData("Luca: 600 Gil (Chest)", 33, 0x1021, False),  # Gil: 600 [06h]
    FFXLocationData("Luca: Tidal Spear (Chest)", 34, 0x1022, False),  # Gear: buki_get #10 [0Ah] { Kimahri [03h], Weapon {Piercing [800Bh], Waterstrike [802Ah]} }
    FFXLocationData("Luca: HP Sphere x1 (Chest)", 35, 0x1023, False),  # Item: 1x HP Sphere [2055h]
    FFXLocationData("Luca: Hi-Potion x2 (Chest)", 36, 0x1024, False),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Luca: 1000 Gil (Chest)", 37, 0x1025, False),  # Gil: 1000 [0Ah]
    FFXLocationData("Mi'ihen Highroad: Ice Brand (Chest)", 38, 0x1026, False),  # Gear: buki_get #11 [0Bh] { Tidus [00h], Weapon {Icestrike [8022h]} }
    FFXLocationData("Mi'ihen Highroad: Fortune Sphere (Chest)", 39, 0x1027, False),  # Item: 1x Fortune Sphere [204Ah]
    FFXLocationData("Mi'ihen Highroad: Thunder Blade (Chest)", 40, 0x1028, False),  # Gear: buki_get #12 [0Ch] { Auron [02h], Weapon {Piercing [800Bh], Lightningstrike [8026h]} }
    FFXLocationData("Mi'ihen Highroad: Scout (Chest)", 41, 0x1029, False),  # Gear: buki_get #13 [0Dh] { Wakka [04h], Weapon {Lightningstrike [8026h], Sensor [8000h]} }
    FFXLocationData("Mi'ihen Highroad: Heat Lance (Chest)", 42, 0x102a, False),  # Gear: buki_get #14 [0Eh] { Kimahri [03h], Weapon {Piercing [800Bh], Firestrike [801Eh]} }
    FFXLocationData("Mi'ihen Highroad: Hi-Potion x2 (Chest)", 43, 0x102b, False),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Mi'ihen Highroad: Remedy x1 (Chest)", 44, 0x102c, False),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Mi'ihen Highroad: 2000 gil (Chest)", 45, 0x102d, False),  # Gil: 2000 [14h]
    FFXLocationData("Mi'ihen Highroad: Eye Drops x3 (Chest)", 46, 0x102e, False),  # Item: 3x Eye Drops [200Ch]
    FFXLocationData("Mushroom Rock Road: Soft x4 (Chest)", 47, 0x102f, False),  # Item: 4x Soft [200Bh]
    FFXLocationData("Mushroom Rock Road: 1000 gil (Chest)", 48, 0x1030, False),  # Gil: 1000 [0Ah]
    FFXLocationData("Mushroom Rock Road: Hi-Potion x1 (Chest)", 49, 0x1031, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Mushroom Rock Road: Remedy x1 (Chest)", 50, 0x1032, False),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Mushroom Rock Road: Serene Bracer (Chest)", 51, 0x1033, False),  # Gear: buki_get #15 [0Fh] { Auron [02h], Armor {HP +5% [8072h], Berserk Ward [8051h]} }
    FFXLocationData("Mushroom Rock Road: Mega-Potion x1 (Chest)", 52, 0x1034, False),  # Item: 1x Mega-Potion [2003h]
    # FFXLocationData("Treasure 53 (Potentially Trashed Treasure)", 53, 0x1035, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Djose: Phoenix Down x2 (Chest)", 54, 0x1036, False),  # Item: 2x Phoenix Down [2006h]
    # FFXLocationData("Treasure 56 (Potentially Trashed Treasure)", 56, 0x1038, False),  # Gear: buki_get #17 [11h] { Yuna [01h], Armor {Lightning Ward [8027h], Poison Ward [803Dh]} }
    FFXLocationData("Mushroom Rock Road: Serene Armlet (Chest)", 57, 0x1039, False),  # Gear: buki_get #18 [12h] { Kimahri [03h], Armor {Dark Ward [8049h], Berserk Ward [8051h]} }
    FFXLocationData("Djose: Ability Sphere x4 (Chest)", 58, 0x103a, False),  # Item: 4x Ability Sphere [2049h]
    FFXLocationData("Djose: 4000 gil (Chest)", 59, 0x103b, False),  # Gil: 4000 [28h]
    FFXLocationData("Djose: Switch Hitter (Chest)", 60, 0x103c, False),  # Gear: buki_get #19 [13h] { Wakka [04h], Weapon {Strength +3% [8062h], Strength +5% [8063h]} }
    FFXLocationData("Djose: Ether x1 (Chest)", 61, 0x103d, False),  # Item: 1x Ether [2004h]
    FFXLocationData("Djose: Remedy x1 (Chest)", 62, 0x103e, False),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Djose: Mega Phoenix x1 (Chest)", 63, 0x103f, False),  # Item: 1x Mega Phoenix [2007h]
    FFXLocationData("Guadosalam: 3000 gil (Chest)", 64, 0x1040, False),  # Gil: 3000 [1Eh]
    FFXLocationData("Guadosalam: Mega-Potion x1 (Chest)", 65, 0x1041, False),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Guadosalam: Elixir x1 gil (Chest)", 66, 0x1042, False),  # Item: 1x Elixir [2008h]
    FFXLocationData("Guadosalam: Hi-Potion x2 (Chest)", 67, 0x1043, False),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Macalania Woods: 2000 gil (Chest)", 68, 0x1044, False),  # Gil: 2000 [14h]
    FFXLocationData("Macalania Woods: Sleepy Cait Sith (Chest)", 69, 0x1045, False),  # Gear: buki_get #20 [14h] { Lulu [05h], Weapon {Sleeptouch [803Fh]} }
    FFXLocationData("Macalania Woods: Phoenix Down x3 (Chest)", 70, 0x1046, False),  # Item: 3x Phoenix Down [2006h]
    FFXLocationData("Macalania Woods: MP Sphere x1 (Butterfly Minigame Reward before Spherimorph)", 71, 0x1047, False),  # Item: 1x MP Sphere [2056h]
    FFXLocationData("Macalania Woods: Ether x1 (Butterfly Minigame Reward before Spherimorph)", 72, 0x1048, False),  # Item: 1x Ether [2004h]
    FFXLocationData("Macalania Woods: Remedy x1 (Chest)", 73, 0x1049, False),  # Item: 1x Remedy [200Fh]
    #  FFXLocationData("Treasure 74 (Trashed)", 74, 0x104a, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Macalania Woods: Lucid Ring (Chest)", 75, 0x104b, False),  # Gear: buki_get #21 [15h] { Yuna [01h], Armor {Silence Ward [8045h], Confuse Ward [804Fh]} }
    FFXLocationData("Lake Macalania: 4000 gil (Chest)", 76, 0x104c, False),  # Gil: 4000 [28h]
    FFXLocationData("Lake Macalania: Lv. 1 Key Sphere x1 (Chest)", 77, 0x104d, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    FFXLocationData("Lake Macalania: Mega-Potion x1 (Chest)", 78, 0x104e, False),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Lake Macalania Bottom: Avenger (Chest)", 79, 0x104f, False),  # Gear: buki_get #22 [16h] { Tidus [00h], Weapon {Counterattack [8003h]} }
    FFXLocationData("Lake Macalania Bottom: Lv. 2 Key Sphere (Chest)", 80, 0x1050, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    # FFXLocationData("Treasure 81 (Trashed)", 81, 0x1051, False),  # Gear: buki_get #23 [17h] { Lulu [05h], Weapon {Silencetouch [8043h], Magic +5% [8067h]} }
    # FFXLocationData("Treasure 82 (Trashed)", 82, 0x1052, False),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Lake Macalania: 5000 gil (Chest)", 83, 0x1053, False),  # Gil: 5000 [32h]
    FFXLocationData("Lake Macalania: X-Potion x2 (Chest)", 84, 0x1054, False),  # Item: 2x X-Potion [2002h]
    FFXLocationData("Lake Macalania: Shell Targe (Tromell)", 85, 0x1055, False),  # Gear: buki_get #24 [18h] { Rikku [06h], Armor {SOS Shell [8059h]} }
    FFXLocationData("Lake Macalania: Phoenix Down x3 (Chest)", 86, 0x1056, False),  # Item: 3x Phoenix Down [2006h]
    FFXLocationData("Lake Macalania: Remedy x2 (Chest)", 87, 0x1057, False),  # Item: 2x Remedy [200Fh]
    # FFXLocationData("Treasure 88 (Trashed)", 88, 0x1058, False),  # Gear: buki_get #25 [19h] { Kimahri [03h], Armor {Poison Ward [803Dh], Confuse Ward [804Fh], Silence Ward [8045h], Empty} }
    # FFXLocationData("Treasure 89 (Trashed)", 89, 0x1059, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Besaid: Phoenix Down x1 (Chest)", 90, 0x105a, False),  # Item: 1x Phoenix Down [2006h]
    FFXLocationData("Besaid: Hi-Potion x1(Chest)", 91, 0x105b, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Besaid: Antidote x2 (Chest)", 92, 0x105c, False),  # Item: 2x Antidote [200Ah]
    FFXLocationData("World Champion", 93, 0x105d, False),  # Gear: buki_get #26 [1Ah] { Wakka [04h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    FFXLocationData("Mi'Hen Highroad: Scout (Donate 100 gil to Operation)", 94, 0x105e, False),  # Gear: buki_get #27 [1Bh] { Wakka [04h], Weapon {Sensor [8000h]} }
    FFXLocationData("Mi'Hen Highroad: Ice Lance (Donate 1000 gil to Operation)", 95, 0x105f, False),  # Gear: buki_get #28 [1Ch] { Kimahri [03h], Weapon {Piercing [800Bh], Icestrike [8022h]} }
    FFXLocationData("Mi'Hen Highroad: Moon Ring (Donate 10000 gil to Operation)", 96, 0x1060, False),  # Gear: buki_get #29 [1Dh] { Yuna [01h], Armor {SOS Shell [8059h], SOS Protect [805Ah]} }
    FFXLocationData("Mi'ihen Highroad: Mega-Potion (NPC)", 97, 0x1061, False),  # Item: 2x Mega-Potion [2003h]
    FFXLocationData("Mushroom Rock Road: Hi-Potion x1 (Chest)", 98, 0x1062, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Masamune", 99, 0x1063, False),  # Gear: buki_get #30 [1Eh] { Auron [02h], Weapon Formula=Celestial Auron [13h] {No AP [8014h], Empty, Empty, Empty} }
    FFXLocationData("Bevelle: Avenger (Chest)", 100, 0x1064, False),  # Gear: buki_get #31 [1Fh] { Tidus [00h], Weapon {Counterattack [8003h]} }
    FFXLocationData("Bevelle: Rematch (Chest)", 101, 0x1065, False),  # Gear: buki_get #32 [20h] { Wakka [04h], Weapon {Evade & Counter [8004h]} }
    FFXLocationData("Bevelle: Knight Lance (Chest)", 102, 0x1066, False),  # Gear: buki_get #33 [21h] { Kimahri [03h], Weapon {Strength +3% [8062h], Strength +5% [8063h], Strength +10% [8064h]} }
    # FFXLocationData("Treasure 103 (Trashed)", 103, 0x1067, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Bevelle: Elixir x1 (Chest)", 104, 0x1068, False),  # Item: 1x Elixir [2008h]
    FFXLocationData("Bevelle: Wht Magic Sphere x1 (Chest)", 105, 0x1069, False),  # Item: 1x Wht Magic Sphere [204Eh]
    FFXLocationData("Bevelle: Skill Sphere x1 (Chest)", 106, 0x106a, False),  # Item: 1x Skill Sphere [204Dh]
    FFXLocationData("Bevelle: 10000 gil (Chest)", 107, 0x106b, False),  # Gil: 10000 [64h]
    FFXLocationData("Bevelle: Lucid Ring (Chest)", 108, 0x106c, False),  # Gear: buki_get #34 [22h] { Yuna [01h], Armor {Silence Ward [8045h], Confuse Ward [804Fh], Poison Ward [803Dh]} }
    FFXLocationData("Bevelle: Blk Magic Sphere (Chest)", 109, 0x106d, False),  # Item: 1x Blk Magic Sphere [204Fh]
    FFXLocationData("Bevelle: Mega-Potion x1 (Chest)", 110, 0x106e, False),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Celestial Mirror", 111, 0x106f, False),  # Key Item: Celestial Mirror [A003h]
    # FFXLocationData("Treasure 112 (Trashed)", 112, 0x1070, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Nirvana", 113, 0x1071, False),  # Gear: buki_get #36 [24h] { Yuna [01h], Weapon Formula=Celestial MP-based [12h] {No AP [8014h], Empty, Empty, Empty} }
    FFXLocationData("Caladblog", 114, 0x1072, False),  # Gear: buki_get #37 [25h] { Tidus [00h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    FFXLocationData("Calm Lands: 10000 gil (Chest)", 115, 0x1073, False),  # Gil: 10000 [64h]
    FFXLocationData("Calm Lands: 5000 gil (Chest)", 116, 0x1074, False),  # Gil: 5000 [32h]
    FFXLocationData("Calm Lands: Lv. 2 Key Sphere x1 (Chest)", 117, 0x1075, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    FFXLocationData("Rusty Sword", 118, 0x1076, False),  # Key Item: Rusty Sword [A021h]
    # FFXLocationData("Treasure 119 (Trashed)", 119, 0x1077, False),  # Gear: buki_get #38 [26h] { Kimahri [03h], Armor {HP +10% [8073h], Empty, Empty, Empty} }
    FFXLocationData("Cavern of the Stolen Fayth: Megalixir x1 (Chest)", 120, 0x1078, False),  # Item: 1x Megalixir [2009h]
    FFXLocationData("Cavern of the Stolen Fayth: Lv. 2 Key Sphere x1 (Chest)", 121, 0x1079, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    FFXLocationData("Cavern of the Stolen Fayth: Fortune Sphere x1 (Chest)", 122, 0x107a, False),  # Item: 1x Fortune Sphere [204Ah]
    FFXLocationData("Cavern of the Stolen Fayth: Mega-Potion x1 (Chest)", 123, 0x107b, False),  # Item: 2x Mega-Potion [2003h]
    FFXLocationData("Cavern of the Stolen Fayth: Flexible Arm (Chest)", 124, 0x107c, False),  # Gear: buki_get #39 [27h] { Rikku [06h], Weapon {Empty, Empty, Empty, Empty} }
    FFXLocationData("Cavern of the Stolen Fayth: MP Sphere x1 (Chest)", 125, 0x107d, False),  # Item: 1x MP Sphere [2056h]
    FFXLocationData("Cavern of the Stolen Fayth: X-Potion x2 (Chest)", 126, 0x107e, False),  # Item: 2x X-Potion [2002h]
    # FFXLocationData("Treasure 127 (Trashed)", 127, 0x107f, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Mt. Gagazet: 20000 gil (Chest)", 128, 0x1080, False),  # Gil: 20000 [C8h]
    FFXLocationData("Mt. Gagazet: Mega-Potion x2 (Chest)", 129, 0x1081, False),  # Item: 2x Mega-Potion [2003h]
    FFXLocationData("Mt. Gagazet: Defending Bracer (Chest)", 130, 0x1082, False),  # Gear: buki_get #40 [28h] { Auron [02h], Armor {Stoneproof [8038h], Poisonproof [803Ch]} }
    FFXLocationData("Mt. Gagazet: Lv. 4 Key Sphere x1 (Chest)", 131, 0x1083, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    FFXLocationData("Mt. Gagazet: HP Sphere x1 (Chest)", 132, 0x1084, False),  # Item: 1x HP Sphere [2055h]
    # FFXLocationData("Treasure 133 (Trashed)", 133, 0x1085, False),  # Item: 1x Potion [2000h]
    # FFXLocationData("Treasure 134 (Trashed)", 134, 0x1086, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Mt. Gagazet (Cave): Pep Talk (Chest)", 135, 0x1087, False),  # Gear: buki_get #41 [29h] { Wakka [04h], Armor {SOS NulFrost [805Fh], SOS NulShock [8060h], SOS NulBlaze [8061h]} }
    FFXLocationData("Mt. Gagazet (Cave): Lv. 1 Key Sphere x1 (Chest)", 136, 0x1088, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    FFXLocationData("Mt. Gagazet (Cave): Fortune Sphere x1 (Chest)", 137, 0x1089, False),  # Item: 1x Fortune Sphere [204Ah]
    FFXLocationData("Mt. Gagazet (Cave): Return Sphere x1 (Chest)", 138, 0x108a, False),  # Item: 1x Return Sphere [2060h]
    FFXLocationData("Mt. Gagazet (Cave): Recovery Ring (Chest)", 139, 0x108b, False),  # Gear: buki_get #42 [2Ah] { Yuna [01h], Armor {HP Stroll [801Bh]} }
    # FFXLocationData("Treasure 140 (Trashed)", 140, 0x108c, False),  # Item: 1x Potion [2000h]
    # FFXLocationData("Treasure 141 (Trashed)", 141, 0x108d, False),  # Item: 1x Potion [2000h]
    # FFXLocationData("Treasure 142 (Trashed)", 142, 0x108e, False),  # Item: 1x Potion [2000h]
    # FFXLocationData("Treasure 143 (Trashed)", 143, 0x108f, False),  # Item: 1x Potion [2000h]
    # FFXLocationData("Treasure 144 (Trashed)", 144, 0x1090, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Zanarkand: Fortune Sphere x1 (Chest)", 145, 0x1091, False),  # Item: 1x Fortune Sphere [204Ah]
    FFXLocationData("Zanarkand: Spiritual Targe (Chest)", 146, 0x1092, False),  # Gear: buki_get #43 [2Bh] { Rikku [06h], Armor {MP Stroll [801Ch]} }
    FFXLocationData("Zanarkand: 10000 gil (Chest)", 147, 0x1093, False),  # Gil: 10000 [64h]
    FFXLocationData("Zanarkand: Friend Sphere x1 (Chest)", 148, 0x1094, False),  # Item: 1x Friend Sphere [2061h]
    FFXLocationData("Zanarkand: Lv. 3 Key Sphere x1 (Chest)", 149, 0x1095, False),  # Item: 1x Lv. 3 Key Sphere [2053h]
    FFXLocationData("Zanarkand: Luck Sphere x1", 150, 0x1096, False),  # Item: 1x Luck Sphere [205Eh]
    # FFXLocationData("Treasure 151 (Trashed)", 151, 0x1097, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Omega Ruins: Fortune Sphere x1 (Chest)", 152, 0x1098, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    FFXLocationData("Omega Ruins: Defending Bracer (Chest)", 153, 0x1099, False),  # Gear: buki_get #44 [2Ch] { Auron [02h], Armor {Silenceproof [8044h], Darkproof [8048h]} }
    FFXLocationData("Omega Ruins: Turnover (Chest)", 154, 0x109a, False),  # Gear: buki_get #45 [2Dh] { Wakka [04h], Weapon {Magic Counter [8005h], Counterattack [8003h]} }
    FFXLocationData("Omega Ruins: Lv. 3 Key Sphere x2 (Chest)", 155, 0x109b, False),  # Item: 2x Lv. 3 Key Sphere [2053h]
    FFXLocationData("Omega Ruins: Defending Armlet (Chest)", 156, 0x109c, False),  # Gear: buki_get #46 [2Eh] { Kimahri [03h], Armor {Stoneproof [8038h], Poisonproof [803Ch], Empty, Empty} }
    FFXLocationData("Omega Ruins: Friend Sphere x2 (Chest)", 157, 0x109d, False),  # Item: 2x Friend Sphere [2061h]
    FFXLocationData("Omega Ruins: Lv. 4 Key Sphere x1 (Chest)", 158, 0x109e, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    FFXLocationData("Omega Ruins: Phantom Ring (Chest)", 159, 0x109f, False),  # Gear: buki_get #47 [2Fh] { Yuna [01h], Armor {Ice Eater [8025h], Fire Eater [8021h], Lightning Eater [8029h], Empty} }
    FFXLocationData("Omega Ruins: Cactuar Wizard (Chest)", 160, 0x10a0, False),  # Gear: buki_get #48 [30h] { Lulu [05h], Weapon {Half MP Cost [800Ch]} }
    FFXLocationData("Omega Ruins: Warmonger (Chest)", 161, 0x10a1, False),  # Gear: buki_get #49 [31h] { Rikku [06h], Weapon {Double AP [8012h], !Double Overdrive [800Eh]} }
    FFXLocationData("Yojimbo 3x Reward/Omega Ruins: Teleport Sphere x2 (Chest)", 162, 0x10a2, False),  # Item: 2x Teleport Sphere [2062h]
    FFXLocationData("Inside Sin: Elixir x1 (Chest)", 163, 0x10a3, False),  # Item: 1x Elixir [2008h]
    FFXLocationData("Inside Sin: Wizard Lance (Chest)", 164, 0x10a4, False),  # Gear: buki_get #50 [32h] { Kimahri [03h], Weapon {Magic +3% [8066h], Magic +5% [8067h], Magic +10% [8068h], Empty} }
    FFXLocationData("Inside Sin: Lv. 3 Key Sphere x1 (Chest)", 165, 0x10a5, False),  # Item: 1x Lv. 3 Key Sphere [2053h]
    FFXLocationData("Inside Sin: Phantom Ring (Chest)", 166, 0x10a6, False),  # Gear: buki_get #51 [33h] { Yuna [01h], Armor {Water Eater [802Dh], Fire Eater [8021h], Lightning Eater [8029h], Empty} }
    FFXLocationData("Inside Sin: Special Sphere x1 (Chest)", 167, 0x10a7, False),  # Item: 1x Special Sphere [204Ch]
    FFXLocationData("Inside Sin: Lv. 4 Key Sphere x1 (Chest)", 168, 0x10a8, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    FFXLocationData("Inside Sin: Four-on-One (Chest)", 169, 0x10a9, False),  # Gear: buki_get #52 [34h] { Wakka [04h], Weapon {Waterstrike [802Ah], Firestrike [801Eh], Lightningstrike [8026h], Icestrike [8022h]} }
    FFXLocationData("Inside Sin: Defending Bracer (Chest)", 170, 0x10aa, False),  # Gear: buki_get #53 [35h] { Auron [02h], Armor {Darkproof [8048h], Deathproof [8030h], Empty, Empty} }
    FFXLocationData("Inside Sin: 20000 gil (Chest)", 171, 0x10ab, False),  # Gil: 20000 [C8h]
    FFXLocationData("Inside Sin: HP Sphere x1 (Chest)", 172, 0x10ac, False),  # Item: 1x HP Sphere [2055h]
    FFXLocationData("Inside Sin: Defense Sphere x1 (Chest)", 173, 0x10ad, False),  # Item: 1x Defense Sphere [2058h]
    FFXLocationData("Inside Sin: Megalixir x1 (Chest)", 174, 0x10ae, False),  # Item: 1x Megalixir [2009h]
    FFXLocationData("Inside Sin: Laevatein (Chest)", 175, 0x10af, False),  # Gear: buki_get #54 [36h] { Yuna [01h], Weapon {SOS Overdrive [8010h]} }
    FFXLocationData("Cloudy Mirror", 176, 0x10b0, False),  # Key Item: Cloudy Mirror [A002h]
    FFXLocationData("Jecht Sphere", 177, 0x10b1, False),  # Key Item: Jecht's Sphere [A020h]
    FFXLocationData("Thunder Plains: Phoenix Down x2 (Chest)", 178, 0x10b2, False),  # Item: 2x Phoenix Down [2006h]
    FFXLocationData("Thunder Plains: Hi-Potion x2 (Chest)", 179, 0x10b3, False),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Thunder Plains: 5000 gil (Chest)", 180, 0x10b4, False),  # Gil: 5000 [32h]
    FFXLocationData("Thunder Plains: Water Ball (Chest)", 181, 0x10b5, False),  # Gear: buki_get #55 [37h] { Wakka [04h], Weapon {Waterstrike [802Ah], Empty} }
    FFXLocationData("Thunder Plains: X-Potion x1 (Chest)", 182, 0x10b6, False),  # Item: 1x X-Potion [2002h]
    FFXLocationData("Thunder Plains: Ether x1 (Chest)", 183, 0x10b7, False),  # Item: 1x Ether [2004h]
    FFXLocationData("Thunder Plains: Remedy x1 (Chest)", 184, 0x10b8, False),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Thunder Plains: 2000 gil (Chest)", 185, 0x10b9, False),  # Gil: 2000 [14h]
    FFXLocationData("Mi'Hen Highroad Echo Ring (Win Aeon Fight)", 186, 0x10ba, False),  # Gear: buki_get #74 [4Ah] { Yuna [01h], Armor {HP +10% [8073h], Silence Ward [8045h]} }
    FFXLocationData("Calm Lands: Power Spheres x30 (NPC)", 187, 0x10bb, False),  # Item: 30x Power Sphere [2046h]
    FFXLocationData("Spirit Lance", 188, 0x10bc, False),  # Gear: buki_get #56 [38h] { Kimahri [03h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    FFXLocationData("Thunder Plains: X-Potion x2 (Dodging Minigame Reward)", 189, 0x10bd, False),  # Item: 2x X-Potion [2002h]
    FFXLocationData("Thunder Plains: Mega-Potion x2 (Dodging Minigame Reward)", 190, 0x10be, False),  # Item: 2x Mega-Potion [2003h]
    FFXLocationData("Thunder Plains: MP Sphere x2 (Dodging Minigame Reward)", 191, 0x10bf, False),  # Item: 2x MP Sphere [2056h]
    FFXLocationData("Thunder Plains: Strength Sphere x3 (Dodging Minigame Reward)", 192, 0x10c0, False),  # Item: 3x Strength Sphere [2057h]
    FFXLocationData("Thunder Plains: HP Sphere x3 (Dodging Minigame Reward)", 193, 0x10c1, False),  # Item: 3x HP Sphere [2055h]
    FFXLocationData("Thunder Plains: Megalixir x4 (Dodging Minigame Reward)", 194, 0x10c2, False),  # Item: 4x Megalixir [2009h]
    # FFXLocationData("Treasure 195 (Trashed)", 195, 0x10c3, False),  # Item: 1x Ether [2004h]
    # FFXLocationData("Treasure 196 (Trashed)", 196, 0x10c4, False),  # Item: 1x Elixir [2008h]
    FFXLocationData("Moonflow: X-Potion x1 (Chest)", 197, 0x10c5, False),  # Item: 1x X-Potion [2002h]
    FFXLocationData("Moonflow: Phoenix Down x2 (Chest)", 198, 0x10c6, False),  # Item: 2x Phoenix Down [2006h]
    FFXLocationData("Moonflow: 5000 gil (Chest)", 199, 0x10c7, False),  # Gil: 5000 [32h]
    FFXLocationData("Moonflow: Ether x1 (Chest)", 200, 0x10c8, False),  # Item: 1x Ether [2004h]
    FFXLocationData("Moonflow: Antidote x4 (Chest)", 201, 0x10c9, False),  # Item: 4x Antidote [200Ah]
    FFXLocationData("Moonflow: Mega-Potion x1 (Chest)", 202, 0x10ca, False),  # Item: 1x Mega-Potion [2003h]
    # FFXLocationData("Baaj Temple: Grenades from Rikku", 203, 0x10cb, False),  # Item: 2x Grenade [2023h]
    FFXLocationData("Baaj Temple: Megalixir (Temple Area Chest)", 204, 0x10cc, False),  # Item: 1x Megalixir [2009h]
    FFXLocationData("Baaj Temple: Mega Phoenix x4 (Temple Area Chest)", 205, 0x10cd, False),  # Item: 4x Mega Phoenix [2007h]
    FFXLocationData("Luca: Magic Sphere x1 (Chest)", 206, 0x10ce, False),  # Item: 1x Magic Sphere [2059h]
    FFXLocationData("Brotherhood", 207, 0x10cf, False),  # Gear: buki_get #1 [01h] { Tidus [00h], Weapon {Strength +5% [8063h], Strength +10% [8064h], Waterstrike [802Ah], Sensor [8000h]} }
    FFXLocationData("Brotherhood?", 208, 0x10d0, False),  # Gear: buki_get #1 [01h] { Tidus [00h], Weapon {Strength +5% [8063h], Strength +10% [8064h], Waterstrike [802Ah], Sensor [8000h]} }
    FFXLocationData("Zanarkand Ruins: Destruction Sphere", 209, 0x10d1, False),  # Gear: buki_get #60 [3Ch] { Yuna [01h], Weapon {Half MP Cost [800Ch], Empty, Empty} }
    FFXLocationData("Bikanel: Al Bhed Potion x8 (Chest)", 210, 0x10d2, False),  # Item: 8x Al Bhed Potion [2014h]
    FFXLocationData("Bikanel: Al Bhed Potion x8 (Chest)", 211, 0x10d3, False),  # Item: 8x Al Bhed Potion [2014h]
    FFXLocationData("Bikanel: Al Bhed Potion x8 (Chest)", 212, 0x10d4, False),  # Item: 8x Al Bhed Potion [2014h]
    FFXLocationData("Baaj Temple: X-Potion x1 (Chest)", 213, 0x10d5, False),  # Item: 1x X-Potion [2002h]
    FFXLocationData("Godhand", 214, 0x10d6, False),  # Gear: buki_get #61 [3Dh] { Rikku [06h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    FFXLocationData("Besaid Village: 400 gil (Chest)", 215, 0x10d7, False),  # Gil: 400 [04h]
    FFXLocationData("Besaid Village: Potion x2 (Chest)", 216, 0x10d8, False),  # Item: 2x Potion [2000h]
    FFXLocationData("Bevelle: HP Sphere x1 (Chest)", 217, 0x10d9, False),  # Item: 1x HP Sphere [2055h]
    FFXLocationData("Guadosalam: Lightning Marble x8 (Chest)", 218, 0x10da, False),  # Item: 8x Lightning Marble [201Eh]
    FFXLocationData("Baaj Temple: Hi Potion x1 (Chest)", 219, 0x10db, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Blitzball Reward", 220, 0x10dc, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Blitzball Reward", 221, 0x10dd, False),  # Item: 1x Dark Matter [2035h]
    FFXLocationData("Blitzball Reward", 222, 0x10de, False),  # Item: 1x Teleport Sphere [2062h]
    FFXLocationData("Blitzball Reward", 223, 0x10df, False),  # Item: 1x Three Stars [2045h]
    FFXLocationData("Blitzball Reward", 224, 0x10e0, False),  # Item: 1x Luck Sphere [205Eh]
    FFXLocationData("Blitzball Reward", 225, 0x10e1, False),  # Item: 1x Underdog's Secret [206Eh]
    FFXLocationData("Blitzball Reward", 226, 0x10e2, False),  # Item: 1x Megalixir [2009h]
    FFXLocationData("Blitzball Reward", 227, 0x10e3, False),  # Item: 1x Return Sphere [2060h]
    FFXLocationData("Blitzball Reward", 228, 0x10e4, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    FFXLocationData("Blitzball Reward", 229, 0x10e5, False),  # Item: 1x Mega Phoenix [2007h]
    FFXLocationData("Blitzball Reward", 230, 0x10e6, False),  # Item: 1x Elixir [2008h]
    FFXLocationData("Blitzball Reward", 231, 0x10e7, False),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Blitzball Reward", 232, 0x10e8, False),  # Item: 1x X-Potion [2002h]
    FFXLocationData("Blitzball Reward", 233, 0x10e9, False),  # Item: 1x Ether [2004h]
    FFXLocationData("Blitzball Reward", 234, 0x10ea, False),  # Item: 2x Remedy [200Fh]
    FFXLocationData("Blitzball Reward", 235, 0x10eb, False),  # Item: 2x Phoenix Down [2006h]
    FFXLocationData("Blitzball Reward", 236, 0x10ec, False),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Blitzball Reward", 237, 0x10ed, False),  # Item: 5x Power Sphere [2046h]
    FFXLocationData("Blitzball Reward", 238, 0x10ee, False),  # Item: 5x Mana Sphere [2047h]
    FFXLocationData("Blitzball Reward", 239, 0x10ef, False),  # Item: 5x Speed Sphere [2048h]
    FFXLocationData("Blitzball Reward", 240, 0x10f0, False),  # Item: 5x Ability Sphere [2049h]
    FFXLocationData("Blitzball Reward", 241, 0x10f1, False),  # Item: 1x Echo Screen [200Dh]
    FFXLocationData("Blitzball Reward", 242, 0x10f2, False),  # Item: 1x Eye Drops [200Ch]
    FFXLocationData("Blitzball Reward", 243, 0x10f3, False),  # Item: 1x Antidote [200Ah]
    FFXLocationData("Jupiter Sigil", 244, 0x10f4, False),  # Key Item: Jupiter Sigil [A02Dh]
    FFXLocationData("Blitzball Reward", 245, 0x10f5, False),  # Item: 1x Elixir [2008h]
    FFXLocationData("Blitzball Reward", 246, 0x10f6, False),  # Item: 1x X-Potion [2002h]
    FFXLocationData("Blitzball Reward", 247, 0x10f7, False),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Blitzball Reward", 248, 0x10f8, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Blitzball Reward", 249, 0x10f9, False),  # Item: 4x Echo Screen [200Dh]
    FFXLocationData("Blitzball Reward", 250, 0x10fa, False),  # Item: 4x Eye Drops [200Ch]
    FFXLocationData("Blitzball Reward", 251, 0x10fb, False),  # Item: 4x Antidote [200Ah]
    FFXLocationData("Blitzball Reward", 252, 0x10fc, False),  # Item: 4x Soft [200Bh]
    FFXLocationData("Blitzball Reward", 253, 0x10fd, False),  # Item: 2x Potion [2000h]
    FFXLocationData("Blitzball Reward", 254, 0x10fe, False),  # Item: 2x Phoenix Down [2006h]
    FFXLocationData("Blitzball Reward", 255, 0x10ff, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Blitzball Reward", 256, 0x1100, False),  # Item: 1x Phoenix Down [2006h]
    FFXLocationData("Blitzball Reward", 257, 0x1101, False),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Blitzball Reward", 258, 0x1102, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Blitzball Reward", 259, 0x1103, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Blitzball Reward", 260, 0x1104, False),  # Item: 1x Phoenix Down [2006h]
    FFXLocationData("Blitzball Reward", 261, 0x1105, False),  # Item: 1x Return Sphere [2060h]
    FFXLocationData("Blitzball Reward", 262, 0x1106, False),  # Item: 1x Rename Card [2065h]
    FFXLocationData("Blitzball Reward", 263, 0x1107, False),  # Item: 1x Ether [2004h]
    FFXLocationData("Blitzball Reward", 264, 0x1108, False),  # Item: 1x X-Potion [2002h]
    FFXLocationData("Blitzball Reward", 265, 0x1109, False),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Blitzball Reward", 266, 0x110a, False),  # Item: 2x Remedy [200Fh]
    FFXLocationData("Sun Crest", 267, 0x110b, False),  # Key Item: Sun Crest [A023h]
    FFXLocationData("Moon Crest", 268, 0x110c, False),  # Key Item: Moon Crest [A025h]
    FFXLocationData("Mars Crest", 269, 0x110d, False),  # Key Item: Mars Crest [A027h]
    FFXLocationData("Saturn Crest", 270, 0x110e, False),  # Key Item: Saturn Crest [A02Ah]
    FFXLocationData("Jupiter Crest", 271, 0x110f, False),  # Key Item: Jupiter Crest [A02Ch]
    FFXLocationData("Venus Crest", 272, 0x1110, False),  # Key Item: Venus Crest [A02Eh]
    FFXLocationData("Mercury Crest", 273, 0x1111, False),  # Key Item: Mercury Crest [A030h]
    FFXLocationData("Sun Sigil", 274, 0x1112, False),  # Key Item: Sun Sigil [A024h]
    FFXLocationData("Moon Sigil", 275, 0x1113, False),  # Key Item: Moon Sigil [A026h]
    FFXLocationData("Mars Sigil", 276, 0x1114, False),  # Key Item: Mars Sigil [A028h]
    FFXLocationData("Saturn Sigil", 277, 0x1115, False),  # Key Item: Saturn Sigil [A02Bh]
    FFXLocationData("Venus Sigil", 278, 0x1116, False),  # Key Item: Venus Sigil [A02Fh]
    FFXLocationData("Mercury Sigil", 279, 0x1117, False),  # Key Item: Mercury Sigil [A031h]
    FFXLocationData("Lake Macalania: Megalixir x2 (Butterfly Game after defeating Spherimorph)", 280, 0x1118, False),  # Item: 2x Megalixir [2009h]
    FFXLocationData("Lake Macalania: Elixir x2 (Butterfly Game after defeating Spherimorph)", 281, 0x1119, False),  # Item: 2x Elixir [2008h]
    FFXLocationData("Besaid: Hi-Potion x1 (Datto NPC)", 282, 0x111a, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Besaid: Potion x3 (Jassu NPC)", 283, 0x111b, False),  # Item: 3x Potion [2000h]
    FFXLocationData("Besaid: Potion x2 (Botta NPC)", 284, 0x111c, False),  # Item: 2x Potion [2000h]
    FFXLocationData("Besaid: 200 gil (Keepa NPC)", 285, 0x111d, False),  # Gil: 200 [02h]
    FFXLocationData("Besaid: Remedy x1 (Kid on Dock Bridge NPC)", 286, 0x111e, False),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Besaid: Seeker's Ring (Priest NPC)", 287, 0x111f, False),  # Gear: buki_get #62 [3Eh] { Yuna [01h], Armor {HP +10% [8073h]} }
    FFXLocationData("Besaid: Phoenix Down x3 (Woman NPC)", 288, 0x1120, False),  # Item: 3x Phoenix Down [2006h]
    FFXLocationData("Besaid: 400 gil (Shirtless Man NPC)", 289, 0x1121, False),  # Gil: 400 [04h]
    FFXLocationData("Besaid: Ether (Green Shirt NPC)", 290, 0x1122, False),  # Item: 1x Ether [2004h]
    # FFXLocationData("Treasure 291 (Trashed)", 291, 0x1123, False),  # Item: 4x Antidote [200Ah]
    FFXLocationData("Kilika: Elixir x1 (Luzzu NPC) ", 292, 0x1124, False),  # Item: 1x Elixir [2008h]
    FFXLocationData("Kilika: Remedy x1 (Leader NPC)", 293, 0x1125, False),  # Item: 1x Remedy [200Fh]
    # FFXLocationData("Treasure 294 (Trashed)", 294, 0x1126, False),  # Item: 3x Phoenix Down [2006h]
    FFXLocationData("Kilika: Remedy x1 (Guard NPC)", 295, 0x1127, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Al Bhed Ship: Potion x 3 (NPC)", 296, 0x1128, False),  # Item: 3x Potion [2000h]
    FFXLocationData("Djose: Variable Steel (NPC)", 297, 0x1129, False),  # Gear: buki_get #63 [3Fh] { Tidus [00h], Weapon {Strength +3% [8062h], Empty, Empty, Empty} }
    FFXLocationData("Djose: Soft Ring (NPC)", 298, 0x112a, False),  # Gear: buki_get #64 [40h] { Yuna [01h], Armor {Stoneproof [8038h], Empty} }
    FFXLocationData("Djose: Hi-Potion x1 (NPC)", 299, 0x112b, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Djose: Ether x1 (NPC)", 300, 0x112c, False),  # Item: 1x Ether [2004h]
    FFXLocationData("Djose: Mega-Potion x1 (NPC)", 301, 0x112d, False),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Djose: Halberd (NPC)", 302, 0x112e, False),  # Gear: buki_get #65 [41h] { Kimahri [03h], Weapon {Magic +20% [8069h], Empty} }
    FFXLocationData("Djose: Potion x10 (NPC)", 303, 0x112f, False),  # Item: 10x Potion [2000h]
    FFXLocationData("Djose: Hi-Potion x2 (NPC)", 304, 0x1130, False),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Lake Macalania: 400 gil (Al Bhed Soldier NPC)", 305, 0x1131, False),  # Gil: 400 [04h]
    FFXLocationData("Lake Macalania: Elixir x1 (Man Sitting NPC)", 306, 0x1132, False),  # Item: 1x Elixir [2008h]
    FFXLocationData("Lake Macalania: Ether x1 (Man Sitting NPC)", 307, 0x1133, False),  # Item: 1x Ether [2004h]
    FFXLocationData("Lake Macalania: Hi-Potion x2 (NPC)", 308, 0x1134, False),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Mi'ihen Highroad: Hunters Spear (Blue Shirt NPC)", 309, 0x1135, False),  # Gear: buki_get #66 [42h] { Kimahri [03h], Weapon {Piercing [800Bh], Sensor [8000h], Strength +10% [8064h]} }
    FFXLocationData("Mi'ihen Highroad: Antidote x2 (Red Skirt NPC)", 310, 0x1136, False),  # Item: 2x Antidote [200Ah]
    FFXLocationData("TMi'ihen Highroad: Hi-Potion (Yellow Shirt NPC)", 311, 0x1137, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Mi'ihen Highroad: Soft x3 (Boy NPC)", 312, 0x1138, False),  # Item: 3x Soft [200Bh]
    FFXLocationData("Mi'ihen Highroad: Red Ring (Crusader NPC)", 313, 0x1139, False),  # Gear: buki_get #67 [43h] { Yuna [01h], Armor {HP +10% [8073h], Fire Ward [801Fh]} }
    FFXLocationData("Mi'ihen Highroad: Ether x1 (NPC)", 314, 0x113a, False),  # Item: 1x Ether [2004h]
    FFXLocationData("Mi'ihen Highroad: Hi-Potion x1 (NPC)", 315, 0x113b, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Mi'ihen Highroad: 600 gil (Yellow Crusader NPC)", 316, 0x113c, False),  # Gil: 600 [06h]
    FFXLocationData("Mi'ihen Highroad: Lv. 1 Key Sphere x1 (Purple Crusader NPC)", 317, 0x113d, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    FFXLocationData("Mi'ihen Highroad: Antidote x4 (Woman in Yellow NPC)", 318, 0x113e, False),  # Item: 4x Antidote [200Ah]
    FFXLocationData("Mushroom Rock Road: Tough Bangle (Gray Helmet NPC)", 319, 0x113f, False),  # Gear: buki_get #68 [44h] { Lulu [05h], Armor {HP +20% [8074h], Empty} }
    FFXLocationData("Mushroom Rock Road: Phoenix Down x2 (Blue Shirt Crusader NPC)", 320, 0x1140, False),  # Item: 2x Phoenix Down [2006h]
    FFXLocationData("Mushroom Rock Road: Remedy x1 (Near Grey Helmet NPC)", 321, 0x1141, False),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Mushroom Rock Road: Hi-Potion x1 (Woman in Blue NPC)", 322, 0x1142, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Mushroom Rock Road: Ether x1 (Purple Helmet NPC)", 323, 0x1143, False),  # Item: 1x Ether [2004h]
    FFXLocationData("Mushroom Rock Road: Hi-Potion x1 (Woman NPC near Save Point)", 324, 0x1144, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Mushroom Rock Road: 1000 gil (NPC near chest)", 325, 0x1145, False),  # Item: 10x Potion [2000h]
    FFXLocationData("Mushroom Rock Road: 400 gil (NPC near elevator)", 326, 0x1146, False),  # Gil: 400 [04h]
    FFXLocationData("Mushroom Rock Road: X-Potion x1 (NPC near lift)", 327, 0x1147, False),  # Item: 1x X-Potion [2002h]
    FFXLocationData("Mushroom Rock Road: Mega-Potion x1 (NPC)", 328, 0x1148, False),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Omega Ruins: Warp Sphere x99 (Chest)", 329, 0x1149, False),  # Item: 99x Warp Sphere [2063h]
    FFXLocationData("Omega Ruins: Teleport Sphere x1 (Chest)", 330, 0x114a, False),  # Item: 1x Teleport Sphere [2062h]
    FFXLocationData("Omega Ruins Friend Sphere x1 (Chest)", 331, 0x114b, False),  # Item: 1x Friend Sphere [2061h]
    FFXLocationData("Omega Ruins: Magic Sphere x1 (Chest)", 332, 0x114c, False),  # Item: 1x Magic Sphere [2059h]
    FFXLocationData("Treasure 333 (Old Entry?)", 333, 0x114d, False),  # Key Item: Blossom Crown [A032h]
    FFXLocationData("Flower Scepter", 334, 0x114e, False),  # Key Item: Flower Scepter [A033h]
    # FFXLocationData("Treasure 335 (Trashed)", 335, 0x114f, False),  # Item: 1x Potion [2000h]
    FFXLocationData("S.S. Liki: Friend Sphere x1 (Clasko NPC)", 336, 0x1150, False),  # Item: 1x Friend Sphere [2061h] # Talk to Clasko before Crawler and make sure to have him become a Chocobo Breeder
    FFXLocationData("Calm Lands: Elixir x1 (Wobbly Chocobo Minigame Reward)", 337, 0x1151, False),  # Item: 1x Elixir [2008h]
    FFXLocationData("Calm Lands: Lv. 1 Key Sphere x1 (Dodger Chocobo Minigame Reward)", 338, 0x1152, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    FFXLocationData("Calm Lands: Lv. 2 Key Sphere x1 x1 (Hyper Dodger Chocobo Minigame Reward)", 339, 0x1153, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    FFXLocationData("Calm Lands: Lv. 3 Key Sphere x1 x1 (Catcher Chocobo Minigame Reward)", 340, 0x1154, False),  # Item: 1x Lv. 3 Key Sphere [2053h]
    # FFXLocationData("Treasure 341 (Trashed)", 341, 0x1155, False),  # Item: 1x X-Potion [2002h]
    # FFXLocationData("Treasure 342 (Trashed)", 342, 0x1156, False),  # Item: 1x Mega-Potion [2003h]
    # FFXLocationData("Treasure 343 (Trashed)", 343, 0x1157, False),  # Item: 1x Ether [2004h]
    # FFXLocationData("Treasure 344 (Trashed)", 344, 0x1158, False),  # Item: 1x Turbo Ether [2005h]
    FFXLocationData("Thunder Plains: Yellow Shield (Ground Item)", 345, 0x1159, False),  # Gear: buki_get #69 [45h] { Tidus [00h], Armor {Lightningproof [8028h], Empty} }
    FFXLocationData("Bikanel: Remedy x4 (Chest)", 346, 0x115a, False),  # Item: 4x Remedy [200Fh]
    FFXLocationData("Bikanel: Ether x2 (Chest)", 347, 0x115b, False),  # Item: 2x Ether [2004h]
    FFXLocationData("Bikanel: Hi-Potion x4 (Chest)", 348, 0x115c, False),  # Item: 4x Hi-Potion [2001h]
    FFXLocationData("Bikanel: Mega-Potion x2 (Chest)", 349, 0x115d, False),  # Item: 2x Mega-Potion [2003h]
    FFXLocationData("Bikanel: X-Potion x2 (Chest)", 350, 0x115e, False),  # Item: 2x X-Potion [2002h]
    FFXLocationData("Bikanel: Hi-Potion x4 (Chest)", 351, 0x115f, False),  # Item: 4x Hi-Potion [2001h]
    FFXLocationData("Bikanel: Elixir x1 (Chest)", 352, 0x1160, False),  # Item: 1x Elixir [2008h]
    FFXLocationData("Bikanel: 10000 gil (Chest)", 353, 0x1161, False),  # Gil: 10000 [64h]
    FFXLocationData("Bikanel: Lv. 2 Key Sphere x1 (Chest)", 354, 0x1162, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    FFXLocationData("Bikanel: Hi-Potion x8 (Chest)", 355, 0x1163, False),  # Item: 8x Hi-Potion [2001h]
    FFXLocationData("Bikanel: Mega-Potion x3 (Chest)", 356, 0x1164, False),  # Item: 3x Mega-Potion [2003h]
    FFXLocationData("Bikanel: X-Potion x2 (Chest)", 357, 0x1165, False),  # Item: 2x X-Potion [2002h]
    FFXLocationData("Bikanel: Megalixir x3 (Chest)", 358, 0x1166, False),  # Item: 3x Megalixir [2009h]
    FFXLocationData("Bikanel: Teleport Sphere x2 (Chest)", 359, 0x1167, False),  # Item: 2x Teleport Sphere [2062h]
    FFXLocationData("Home: Al Bhed Potion x6 (Chest)", 360, 0x1168, False),  # Item: 6x Al Bhed Potion [2014h]
    FFXLocationData("Home: Al Bhed Potion x4 (Chest)", 361, 0x1169, False),  # Item: 4x Al Bhed Potion [2014h]
    FFXLocationData("Home: Lv. 2 Key Sphere x1 (Chest)", 362, 0x116a, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    FFXLocationData("Home: Lv. 4 Key Sphere x4 (Chest)", 363, 0x116b, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    FFXLocationData("Home: 10000 gil (Chest)", 364, 0x116c, False),  # Gil: 10000 [64h]
    FFXLocationData("S.S Liki: Ace Wizard", 365, 0x116d, False),  # Gear: buki_get #70 [46h] { Wakka [04h], Weapon {Magic +20% [8069h], Magic +10% [8068h], Magic +5% [8067h], Magic +3% [8066h]} }
    FFXLocationData("Mi'ihen Highroad: Seeker's Ring (Lose Aeon Fight)", 366, 0x116e, False),  # Gear: buki_get #71 [47h] { Yuna [01h], Armor {HP +10% [8073h], Empty} }
    FFXLocationData("Home: Hi-Potion x2 (NPC on Ground)", 367, 0x116f, False),  # Item: 2x Hi-Potion [2001h]
    FFXLocationData("Mushroom Rock Road: Victorious", 368, 0x1170, False),  # Gear: buki_get #72 [48h] { Rikku [06h], Armor {Lightningproof [8028h], Fireproof [8020h], Iceproof [8024h], Empty} }
    FFXLocationData("Besaid Ruins: Murasame", 369, 0x1171, False),  # Gear: buki_get #73 [49h] { Auron [02h], Weapon {Piercing [800Bh], One MP Cost [800Dh], Empty, Empty} }
    FFXLocationData("Calm Lands: Speed Sphere x30 (Lose Aeon Fight)", 370, 0x1172, False),  # Item: 30x Speed Sphere [2048h]
    FFXLocationData("Aeon's Soul", 371, 0x1173, False),  # Key Item: Aeon's Soul [A01Fh]
    FFXLocationData("Moonflow: Dragon Scale x2 (Win Aeon Fight)", 372, 0x1174, False),  # Item: 2x Dragon Scale [2021h]
    FFXLocationData("Moonflow: Smoke Bomb x6 (Lose Aeon Fight)", 373, 0x1175, False),  # Item: 6x Smoke Bomb [2028h]
    FFXLocationData("Summoner's Soul", 374, 0x1176, False),  # Key Item: Summoner's Soul [A01Eh]
    FFXLocationData("Airship: Al Bhed Potion (NPC)", 375, 0x1177, False),  # Item: 4x Al Bhed Potion [2014h]
    FFXLocationData("Moonflow: Lv. Key Sphere x3 (Shelinda Chest)", 376, 0x1178, False),  # Item: 3x Lv. 1 Key Sphere [2051h]
    FFXLocationData("Moonflow: Lv. Key Sphere x3 (Benke and Biran Chest)", 377, 0x1179, False),  # Item: 3x Lv. 1 Key Sphere [2051h]
    FFXLocationData("Moonflow: Magic Def Sphere x1 (Chest)", 378, 0x117a, False),  # Item: 1x Magic Def Sphere [205Ah]
    FFXLocationData("Calm Lands: Valefor Fight First Reward (Remiem Tower)", 379, 0x117b, False),  # Item: 4x Lightning Gem [201Fh]
    FFXLocationData("Calm Lands: Valefor Post First Fight Reward (Remiem Tower)", 380, 0x117c, False),  # Item: 4x Power Sphere [2046h]
    FFXLocationData("Calm Lands: Ifrit Fight (Remiem Tower)", 381, 0x117d, False),  # Item: 30x X-Potion [2002h]
    FFXLocationData("Calm Lands: Ifrit Post First Fight Reward (Remiem Tower)", 382, 0x117e, False),  # Item: 5x Mana Sphere [2047h]
    FFXLocationData("Calm Lands: Ixion Fight (Remiem Tower)", 383, 0x117f, False),  # Item: 10x Chocobo Feather [2036h]
    FFXLocationData("Calm Lands: Ixion Post First Fight Reward (Remiem Tower)", 384, 0x1180, False),  # Item: 8x Power Sphere [2046h]
    FFXLocationData("Calm Lands: Shiva Fight (Remiem Tower)", 385, 0x1181, False),  # Item: 60x Mega-Potion [2003h]
    FFXLocationData("Calm Lands: Shiva Post First Fight Reward (Remiem Tower)", 386, 0x1182, False),  # Item: 6x Star Curtain [203Ah]
    FFXLocationData("Calm Lands: Bahamut Post First Fight Reward (Remiem Tower)", 387, 0x1183, False),  # Item: 8x Mana Sphere [2047h]
    FFXLocationData("Calm Lands: Yojimbo Fight (Remiem Tower)", 388, 0x1184, False),  # Item: 8x Shadow Gem [2029h]
    FFXLocationData("Calm Lands: Yojimbo Post First Fight Reward (Remiem Tower)", 389, 0x1185, False),  # Item: 10x Power Sphere [2046h]
    FFXLocationData("Calm Lands: Anima Fight (Remiem Tower)", 390, 0x1186, False),  # Item: 60x Stamina Spring [203Dh]
    FFXLocationData("Calm Lands: Anima Post First Fight Reward (Remiem Tower)", 391, 0x1187, False),  # Item: 10x Mana Sphere [2047h]
    FFXLocationData("Calm Lands: Magus Sisters Fight (Remiem Tower)", 392, 0x1188, False),  # Item: 40x Shining Gem [202Ah]
    FFXLocationData("Calm Lands: Magus Sisters Post First Fight Reward (Remiem Tower)", 393, 0x1189, False),  # Item: 12x Power Sphere [2046h]
    FFXLocationData("Treasure 394 (Trashed)", 394, 0x118a, False),  # Item: 1x Teleport Sphere [2062h]
    FFXLocationData("Home: Skill Sphere x1 (Al Bhed Quiz Chest)", 395, 0x118b, False),  # Item: 1x Skill Sphere [204Dh]
    FFXLocationData("Home: Skill Sphere x1 (Al Bhed Password Chest)", 396, 0x118c, False),  # Item: 1x Special Sphere [204Ch]
    FFXLocationData("Home: Skill Sphere x1 (Al Bhed Vocabulary Chest)", 397, 0x118d, False),  # Item: 1x Friend Sphere [2061h]
    FFXLocationData("Home: Elixir x1 (Al Bhed Vocabulary Chest)", 398, 0x118e, False),  # Item: 1x Elixir [2008h]
    FFXLocationData("Treasure 399 (Trashed)", 399, 0x118f, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Treasure 400 (Trashed)", 400, 0x1190, False),  # Item: 1x Mega-Potion [2003h]
    FFXLocationData("Treasure 401 (Trashed)", 401, 0x1191, False),  # Item: 1x Soft [200Bh]
    FFXLocationData("Treasure 402 (Trashed)", 402, 0x1192, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Treasure 403 (Trashed)", 403, 0x1193, False),  # Item: 1x Remedy [200Fh]
    FFXLocationData("Treasure 404 (Trashed)", 404, 0x1194, False),  # Item: 2x Potion [2000h]
    FFXLocationData("Complete Al Bhed Primers", 405, 0x1195, False),  # Item: 99x Underdog's Secret [206Eh]
    FFXLocationData("Besaid: Wht Magic Sphere x1 (Aeon Room)", 406, 0x1196, False),  # Item: 1x Wht Magic Sphere [204Eh]
    FFXLocationData("Besaid: Elixir x1 (Aeon Room)", 407, 0x1197, False),  # Item: 1x Elixir [2008h]
    FFXLocationData("Besaid: Hi-Potion x1 (Aeon Room)", 408, 0x1198, False),  # Item: 1x Hi-Potion [2001h]
    FFXLocationData("Besaid: Potion x2 (Aeon Room)", 409, 0x1199, False),  # Item: 2x Potion [2000h]
    # FFXLocationData("S.S Liki: Potion (Yuna's suitcase)", 410, 0x119a, False),  # Item: 1x Potion [2000h] # Definitely Yuna's Suitcase
    # FFXLocationData("Treasure 411 (Trashed)", 411, 0x119b, False),  # Item: 1x Potion [2000h]
    # FFXLocationData("Treasure 412 (Trashed)", 412, 0x119c, False),  # Item: 1x Potion [2000h]
    # FFXLocationData("Treasure 413 (Trashed)", 413, 0x119d, False),  # Item: 1x Potion [2000h]
    # FFXLocationData("Treasure 414 (Trashed)", 414, 0x119e, False),  # Item: 1x Potion [2000h]
    # FFXLocationData("Treasure 415 (Trashed)", 415, 0x119f, False),  # Item: 1x Potion [2000h]
    # FFXLocationData("Treasure 416 (Trashed)", 416, 0x11a0, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Calm Lands: Elixir x1 (Chocobo Race Reward)", 417, 0x11a1, False),  # Item: 1x Elixir [2008h]
    FFXLocationData("Calm Lands: Megalixir x1 (Chocobo Race Reward)", 418, 0x11a2, False),  # Item: 1x Megalixir [2009h]
    FFXLocationData("Calm Lands: Three Stars x60 (Chocobo Race Reward)", 419, 0x11a3, False),  # Item: 60x Three Stars [2045h]
    FFXLocationData("Calm Lands: Pendulum x30 (Chocobo Race Reward)", 420, 0x11a4, False),  # Item: 30x Pendulum [2069h]
    FFXLocationData("Calm Lands: Wings to Discovery x30 (Chocobo Race Reward)", 421, 0x11a5, False),  # Item: 30x Wings to Discovery [206Ch]
    # FFXLocationData("Treasure 422", 422, 0x11a6, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Mi'ihen Highroad: Lv. 1 Key Sphere x1 (NPC)", 423, 0x11a7, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    FFXLocationData("Monster Arena: Stamina Tonic x99 (NPC)", 424, 0x11a8, False),  # Item: 99x Stamina Tonic [2043h]
    FFXLocationData("Monster Arena: Poison Fang x99 (NPC)", 425, 0x11a9, False),  # Item: 99x Poison Fang [202Dh]
    FFXLocationData("Monster Arena: Soul Spring x99 (NPC)", 426, 0x11aa, False),  # Item: 99x Soul Spring [203Eh]
    FFXLocationData("Monster Arena: Candle of Life x99 (NPC)", 427, 0x11ab, False),  # Item: 99x Candle of Life [2030h]
    FFXLocationData("Monster Arena: Petrify Grenade x99 (NPC)", 428, 0x11ac, False),  # Item: 99x Petrify Grenade [2031h]
    FFXLocationData("Monster Arena: Chocobo Wing x99 (NPC)", 429, 0x11ad, False),  # Item: 99x Chocobo Wing [2037h]
    FFXLocationData("Monster Arena: Shining Gem x60 (NPC)", 430, 0x11ae, False),  # Item: 60x Shining Gem [202Ah]
    FFXLocationData("Monster Arena: Shadow Gem x99 (NPC)", 431, 0x11af, False),  # Item: 99x Shadow Gem [2029h]
    FFXLocationData("Monster Arena: Farplane Wind x60 (NPC)", 432, 0x11b0, False),  # Item: 60x Farplane Wind [2033h]
    FFXLocationData("Monster Arena: Silver Hourglass x40 (NPC)", 433, 0x11b1, False),  # Item: 40x Silver Hourglass [202Eh]
    FFXLocationData("Blossom Crown", 434, 0x11b2, False),  # Key Item: Blossom Crown [A032h]
    FFXLocationData("Monster Arena: Lunar Curtain x99 (NPC)", 435, 0x11b3, False),  # Item: 99x Lunar Curtain [2038h]
    FFXLocationData("Monster Arena: Designer Wallet x60 (NPC)", 436, 0x11b4, False),  # Item: 60x Designer Wallet [2034h]
    FFXLocationData("Monster Arena: Chocobo Feather x99 (NPC)", 437, 0x11b5, False),  # Item: 99x Chocobo Feather [2036h]
    FFXLocationData("Monster Arena: Stamina Spring x99 (NPC)", 438, 0x11b6, False),  # Item: 99x Stamina Spring [203Dh]
    FFXLocationData("Monster Arena: Mega Phoenix x99 (NPC)", 439, 0x11b7, False),  # Item: 99x Mega Phoenix [2007h]
    FFXLocationData("Monster Arena: Mana Tonic x60 (NPC)", 440, 0x11b8, False),  # Item: 60x Mana Tonic [2044h]
    FFXLocationData("Monster Arena: Mana Spring x99 (NPC)", 441, 0x11b9, False),  # Item: 99x Mana Spring [203Ch]
    FFXLocationData("Monster Arena: Stamina Tablet x60 (NPC)", 442, 0x11ba, False),  # Item: 60x Stamina Tablet [2040h]
    FFXLocationData("Monster Arena: Twin Stars x60 (NPC)", 443, 0x11bb, False),  # Item: 60x Twin Stars [2042h]
    FFXLocationData("Monster Arena: Star Curtain x99 (NPC)", 444, 0x11bc, False),  # Item: 99x Star Curtain [203Ah]
    FFXLocationData("Monster Arena: Gold Hourglass x99 (NPC)", 445, 0x11bd, False),  # Item: 99x Gold Hourglass [202Fh]
    FFXLocationData("Monster Arena: Purifying Salt x99 (NPC)", 446, 0x11be, False),  # Item: 99x Purifying Salt [203Fh]
    FFXLocationData("Monster Arena: Healing Spring x99 (NPC)", 447, 0x11bf, False),  # Item: 99x Healing Spring [203Bh]
    FFXLocationData("Monster Arena: Turbo Ether x60 (NPC)", 448, 0x11c0, False),  # Item: 60x Turbo Ether [2005h]
    FFXLocationData("Monster Arena: Light Curtain x99 (NPC)", 449, 0x11c1, False),  # Item: 99x Light Curtain [2039h]
    FFXLocationData("Monster Arena: Mana Tablet x60 (NPC)", 450, 0x11c2, False),  # Item: 60x Mana Tablet [2041h]
    FFXLocationData("Monster Arena: Three Stars x60 (NPC)", 451, 0x11c3, False),  # Item: 60x Three Stars [2045h]
    FFXLocationData("Monster Arena: Supreme Gem x60 (NPC)", 452, 0x11c4, False),  # Item: 60x Supreme Gem [202Ch]
    FFXLocationData("Monster Arena: Door to Tomorrow x99 (NPC)", 453, 0x11c5, False),  # Item: 99x Door to Tomorrow [206Bh]
    FFXLocationData("Monster Arena: Gambler's Spirit x99 (NPC)", 454, 0x11c6, False),  # Item: 99x Gambler's Spirit [206Dh]
    FFXLocationData("Monster Arena: Winning Formula x99 (NPC)", 455, 0x11c7, False),  # Item: 99x Winning Formula [206Fh]
    FFXLocationData("Monster Arena: Dark Matter x99 (NPC)", 456, 0x11c8, False),  # Item: 99x Dark Matter [2035h]
    FFXLocationData("Monster Arena: Megalixir x30 (NPC)", 457, 0x11c9, False),  # Item: 30x Megalixir [2009h]
    FFXLocationData("Monster Arena: Master Sphere x10 (NPC)", 458, 0x11ca, False),  # Item: 10x Master Sphere [2050h]
    # FFXLocationData("Treasure 459", 459, 0x11cb, False),  # Item: 1x Map [2064h] #Not the map in Besaid, it's a silent obtain
    FFXLocationData("Lake Macalania: Magic Def Sphere x1 (Aeon Room)", 460, 0x11cc, False),  # Item: 1x Magic Def Sphere [205Ah]
    FFXLocationData("Lake Macalania: Accuracy Sphere x1 (Aeon Room)", 461, 0x11cd, False),  # Item: 1x Accuracy Sphere [205Dh]
    FFXLocationData("Lake Macalania: Magic Sphere x1 (Aeon Room)", 462, 0x11ce, False),  # Item: 1x Magic Sphere [2059h]
    FFXLocationData("Djose: Agility Sphere x1 (Aeon Room)", 463, 0x11cf, False),  # Item: 1x Agility Sphere [205Bh]
    FFXLocationData("Djose: Magic Def Sphere x1 (Aeon Room)", 464, 0x11d0, False),  # Item: 1x Magic Def Sphere [205Ah]
    FFXLocationData("Djose: Luck Sphere x1 (Aeon Room)", 465, 0x11d1, False),  # Item: 1x Luck Sphere [205Eh]
    FFXLocationData("Calm Lands: Defense Sphere x1 (Remiem Temple Aeon Room)", 466, 0x11d2, False),  # Item: 1x Defense Sphere [2058h]
    FFXLocationData("Besaid: Evasion Sphere x1 (Aeon Room)", 467, 0x11d3, False),  # Item: 1x Evasion Sphere [205Ch]
    FFXLocationData("Calm Lands: Strength Sphere x1 (Yojimbo Aeon Room)", 468, 0x11d4, False),  # Item: 1x Strength Sphere [2057h]
    FFXLocationData("Bikanel: Shadow Gem x2 (Robeya Minigame Chest)", 469, 0x11d5, False),  # Item: 2x Shadow Gem [2029h]
    FFXLocationData("Bikanel: Shining Gem x1 (Robeya Minigame Chest)", 470, 0x11d6, False),  # Item: 1x Shining Gem [202Ah]
    FFXLocationData("Bikanel: Blessed Gem x1 (Robeya Minigame Chest)", 471, 0x11d7, False),  # Item: 1x Blessed Gem [202Bh]
    FFXLocationData("Bikanel: Potion x1 (Cactuar Sidequest Prize)", 472, 0x11d8, False),  # Item: 1x Potion [2000h]
    FFXLocationData("Bikanel: Elixir x1 (Cactuar Sidequest Prize)", 473, 0x11d9, False),  # Item: 1x Elixir [2008h]
    FFXLocationData("Bikanel: Megalixir x1 (Cactuar Sidequest Prize)", 474, 0x11da, False),  # Item: 1x Megalixir [2009h]
    FFXLocationData("Bikanel: Friend Sphere x1 (Cactuar Sidequest Prize)", 475, 0x11db, False),  # Item: 1x Friend Sphere [2061h]
    FFXLocationData("Kilika: Agility Sphere x1 (Aeon Room)", 476, 0x11dc, False),  # Item: 1x Agility Sphere [205Bh]
    FFXLocationData("Kilika: Defense Sphere x1 (Aeon Room)", 477, 0x11dd, False),  # Item: 1x Defense Sphere [2058h]
    FFXLocationData("Kilika: Luck Sphere x1 (Aeon Room)", 478, 0x11de, False),  # Item: 1x Luck Sphere [205Eh]
    FFXLocationData("Kilika: Accuracy Sphere x1 (Aeon Room)", 479, 0x11df, False),  # Item: 1x Accuracy Sphere [205Dh]
    FFXLocationData("Besaid: Dragoon Lance", 480, 0x11e0, False),  # Gear: buki_get #75 [4Bh] { Kimahri [03h], Weapon {Magic Counter [8005h], Evade & Counter [8004h], Empty, Empty} }
    FFXLocationData("Mi'ihen Ruins: Sonar", 481, 0x11e1, False),  # Gear: buki_get #76 [4Ch] { Rikku [06h], Weapon {Initiative [8002h], Poisonstrike [803Ah], Empty} }
    FFXLocationData("Battle Site: Phantom Bangle", 482, 0x11e2, False),  # Gear: buki_get #77 [4Dh] { Lulu [05h], Armor {Ice Eater [8025h], Fire Eater [8021h], !Water Eater [802Dh]} }
    FFXLocationData("Sanubia Sands: Ascalon", 483, 0x11e3, False),  # Gear: buki_get #78 [4Eh] { Tidus [00h], Weapon {Double AP [8012h]} }
    FFXLocationData("Djose: Destruction Sphere", 484, 0x11e4, False),  # Item: 1x Magic Sphere [2059h]
    FFXLocationData("Lake Macalania: Destruction Sphere", 485, 0x11e5, False),  # Item: 1x Luck Sphere [205Eh]
    FFXLocationData("Inside Sin: Prism Ball (Point of No Return)", 486, 0x11e6, False),  # Gear: buki_get #79 [4Fh] { Wakka [04h], Weapon {Magic Counter [8005h], Empty} }
    FFXLocationData("Inside Sin: Stillblade (Point of No Return)", 487, 0x11e7, False),  # Gear: buki_get #80 [50h] { Auron [02h], Weapon {Silencestrike [8042h], Stonestrike [8036h], Empty} }
    FFXLocationData("Inside Sin: Skill Sphere x1 (Point of No Return)", 488, 0x11e8, False),  # Item: 1x Skill Sphere [204Dh]
    FFXLocationData("Inside Sin: Mage's Staff (Point of No Return)", 489, 0x11e9, False),  # Gear: buki_get #81 [51h] { Yuna [01h], Weapon {Magic +10% [8068h], Magic +5% [8067h], Magic +3% [8066h], Empty} }
    FFXLocationData("Inside Sin: Knight Lance (Point of No Return)", 490, 0x11ea, False),  # Gear: buki_get #82 [52h] { Kimahri [03h], Weapon {Strength +10% [8064h], Strength +5% [8063h], Strength +3% [8062h], Empty} }
    FFXLocationData("Inside Sin: Wht Magic Sphere x1 (Point of No Return)", 491, 0x11eb, False),  # Item: 1x Wht Magic Sphere [204Eh]
    FFXLocationData("Inside Sin: Infinity (Point of No Return)", 492, 0x11ec, False),  # Gear: buki_get #83 [53h] { Rikku [06h], Weapon {One MP Cost [800Dh], Sensor [8000h]} }
    FFXLocationData("Inside Sin: Wicked Cait Sith (Point of No Return)", 493, 0x11ed, False),  # Gear: buki_get #84 [54h] { Lulu [05h], Weapon {Deathstrike [802Eh], Empty, Empty, Empty} }
    FFXLocationData("Inside Sin: Attribute Sphere x1 (Point of No Return)", 494, 0x11ee, False),  # Item: 1x Attribute Sphere [204Bh]
    FFXLocationData("Inside Sin: Hrunting (Point of No Return)", 495, 0x11ef, False),  # Gear: buki_get #85 [55h] { Tidus [00h], Weapon {SOS Overdrive [8010h]} }
    FFXLocationData("Mark of Conquest", 496, 0x11f0, False),  # Key Item: Mark of Conquest [A029h]
    FFXLocationData("Story Win vs. Luca Goers Reward", 497, 0x11f1, False),  # Item: 1x Strength Sphere [2057h]
]


def create_location_label_to_id_map() -> Dict[str, int]:
    """
    Creates a map from location labels to their AP location id (address)
    """
    label_to_id_map: Dict[str, int] = {}
    for location in FFXTreasureLocations:
        label_to_id_map[location.name] = location.rom_address

    return label_to_id_map
