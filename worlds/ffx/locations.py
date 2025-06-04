import typing
from typing import Dict, Optional, List, Tuple

from BaseClasses import Location, Region


class FFXLocation(Location):
    game: str = "Final Fantasy X"

    def __init__(self, player: int, name: str = '', address: Optional[int] = None, parent: Optional[Region] = None):
        super().__init__(player, name, address, parent)


class FFXLocationData(typing.NamedTuple):
    rom_address: int
    name: str
    location_id: int
    missable: bool



TreasureOffset: int = 0x1000
BossOffset: int = 0x2000
PartyMemberOffset: int = 0x3000
OverdriveOffset: int = 0x4000
OverdriveModeOffset: int = 0x5000
OtherOffset: int = 0x6000
SphereGridOffset: int = 0x7000

location_types: Dict[int, str] = {TreasureOffset: "Treasure",
BossOffset: "Boss",
PartyMemberOffset: "PartyMember",
OverdriveOffset: "Overdrive",
OverdriveModeOffset: "OverdriveMode",
OtherOffset: "Other",
SphereGridOffset: "SphereGrid",}

def get_location_type(location_id: int):
    return location_types[location_id & 0xF000]


FFXBossLocations: List[FFXLocationData] = [ FFXLocationData(location[1]+BossOffset, *location) for location in [
    ("Baaj Temple : Klikk Defeated",              0, False),
    ("Al Bhed Ship: Tros Defeated",               1, False),
    ("Besaid: Dark Valefor",                      2, False),
    ("S.S. Liki: Sin Fin",                        3, False),
    ("S.S. Liki: Sinspawn Echuilles",             4, False),
    ("Kilika: Lord Ochu",                         5, False),
    ("Kilika: Sinspawn Geneaux",                  6, False),
    ("Luca: Oblitzerator defeated",               7, False),
    ("Mi'Hen Highroad: Chocobo Eater",            8, False),
    ("Mushroom Rock Road: Sinspawn Gui",          9, False),
    ("Mushroom Rock Road: Sinspawn Gui 2",       10, False),
    ("Mushroom Rock Road: Dark Magus Sisters",   11, False),
    ("Moonflow: Extractor",                      12, False),
    ("Thunder Plains: Dark Ixion",               13, False),
    ("Macalania Woods: Spherimorph",             14, False),
    ("Lake Macalania: Crawler",                  15, False),
    ("Lake Macalania: Seymour/Anima",            16, False),
    ("Lake Macalania: Wendigo",                  17, False),
    ("Lake Macalania: Dark Shiva",               18, False),
    ("Bikanel: Dark Ifrit",                      19, False),
    ("Airship: Evrae",                           20, False),
    ("Airship: Sin Left Fin",                    21, False),
    ("Airship: Sin Right Fin",                   22, False),
    ("Airship: Sinspawn Genais",                 23, False),
    ("Airship: Overdrive Sin",                   24, False),
    ("Airship: Penance",                         25, False),
    ("Bevelle: Isaaru",                          26, False),
    ("Bevelle: Evrae Altana",                    27, False),
    ("Bevelle: Seymour Natus",                   28, False),
    ("Calm Lands: Defender X",                   29, False),
    ("Monster Arena: Nemesis",                   30, False),
    ("Cavern of the Stolen Fayth: Dark Yojimbo", 31, False),
    ("Gagazet (Outside): Biran and Yenke",       32, False),
    ("Gagazet (Outside): Seymour Flux",          33, False),
    ("Gagazet (Outside): Dark Anima",            34, False),
    ("Gagazet: Sanctuary Keeper",                35, False),
    ("Zanarkand: Spectral Keeper",               36, False),
    ("Zanarkand: Yunalesca",                     37, False),
    ("Zanarkand: Dark Bahamut",                  38, False),
    ("Sin: Seymour Omnis",                       39, False),
    ("Sin: Braska's Final Aeon",                 40, False),
    ("Sin: Contest of Aeons",                    41, False),
    ("Sin: Yu Yevon",                            42, False),
    ("Omega Ruins: Ultima Weapon",               43, False),
    ("Omega Ruins: Omega Weapon",                44, False),
]]

FFXOverdriveLocations: List[FFXLocationData] = [ FFXLocationData(location[1]+OverdriveOffset, *location) for location in [
    ("Slice and Dice",  1, False),
    ("Energy Rain",     2, False),
    ("Blitz Ace",       3, False),
    ("Shooting Star",   4, False),
    ("Banishing Blade", 5, False),
    ("Tornado",         6, False),
    ("Attack Reels",    7, False),
    ("Status Reels",    8, False),
    ("Auroch Reels",    9, False),
    ("Seed Cannon",    10, False),
    ("Stone Breath",   11, False),
    ("Self Destruct",  12, False),
    ("Fire Breath",    13, False),
    ("Aqua Breath",    14, False),
    ("Bad Breath",     15, False),
    ("Doom",           16, False),
    ("Thrust Kick",    17, False),
    ("White Wind",     18, False),
    ("Mighty Guard",   19, False),
    ("Nova",           20, False),
    ("Energy Blast",   21, False),
]]

FFXOverdriveModeLocations: List[FFXLocationData] = [ FFXLocationData(location[1]+OverdriveModeOffset, *location) for location in [
    ("Stoic",      0, False),
    ("Warrior",    1, False),
    ("Comrade",    2, False),
    ("Healer",     3, False),
    ("Tactician",  4, False),
    ("Victim",     5, False),
    ("Dancer",     6, False),
    ("Avenger",    7, False),
    ("Slayer",     8, False),
    ("Hero",       9, False),
    ("Rook",      10, False),
    ("Victor",    11, False),
    ("Coward",    12, False),
    ("Ally",      13, False),
    ("Sufferer",  14, False),
    ("Daredevil", 15, False),
    ("Loner",     16, False),
]]

# Brotherhood, Al Bhed Primers, Jecht Spheres
FFXOtherLocations: List[FFXLocationData] = [ FFXLocationData(location[1]+OtherOffset, *location) for location in [
    ("Brotherhood",                      0, False),

    ("Al Bhed Primer I",                 1, False),
    ("Al Bhed Primer II",                2, False),
    ("Al Bhed Primer III",               3, False),
    ("Al Bhed Primer IV",                4, False),
    ("Al Bhed Primer V",                 5, False),
    ("Al Bhed Primer VI",                6, False),
    ("Al Bhed Primer VII",               7, False),
    ("Al Bhed Primer VIII",              8, False),
    ("Al Bhed Primer IX",                9, False),
    ("Al Bhed Primer X",                10, False),
    ("Al Bhed Primer XI",               11, False),
    ("Al Bhed Primer XII",              12, False),
    ("Al Bhed Primer XIII",             13, False),
    ("Al Bhed Primer XIV",              14, False),
    ("Al Bhed Primer XV",               15, False),
    ("Al Bhed Primer XVI",              16, False),
    ("Al Bhed Primer XVII",             17, False),
    ("Al Bhed Primer XVIII",            18, False),
    ("Al Bhed Primer XIX",              19, False),
    ("Al Bhed Primer XX",               20, False),
    ("Al Bhed Primer XXI",              21, False),
    ("Al Bhed Primer XXII",             22, False),
    ("Al Bhed Primer XXIII",            23, False),
    ("Al Bhed Primer XXIV",             24, False),
    ("Al Bhed Primer XXV",              25, False),
    ("Al Bhed Primer XXVI",             26, False),

    ("Jecht Sphere - Macalania Woods",  27, False),
    ("Jecht Sphere - Besaid",           28, False),
    ("Jecht Sphere - S.S. Liki",        29, False),
    ("Jecht Sphere - Luca",             30, False),
    ("Jecht Sphere - Mi'ihen Oldroad",  31, False),
    ("Auron's Sphere - Mushroom Rock",  32, False),
    ("Jecht Sphere - Moonflow",         33, False),
    ("Jecht Sphere - Thunder Plains",   34, False),
    ("Braska's Sphere - Mt. Gagazet",   35, False),

    ("S.S. Winno: Jecht Shot",  36, False),
    ("Brotherhood Upgrade",     37, False),
]]

FFXPartyMemberLocations: List[FFXLocationData] = [ FFXLocationData(location[1]+PartyMemberOffset, *location) for location in [
    ("Tidus",           0, False),
    ("Yuna",            1, False),
    ("Auron",           2, False),
    ("Kimahri",         3, False),
    ("Wakka",           4, False),
    ("Lulu",            5, False),
    ("Rikku",           6, False),
    ("Seymour",         7, False),
    ("Valefor",         8, False),
    ("Ifrit",           9, False),
    ("Ixion",          10, False),
    ("Shiva",          11, False),
    ("Bahamut",        12, False),
    ("Anima",          13, False),
    ("Yojimbo",        14, False),
    ("Magus Sisters",  15, False),
]]

FFXTreasureLocations: List[FFXLocationData] = [ FFXLocationData(location[1]+TreasureOffset, *location) for location in [
    ("Baaj Temple: Chest 1",                                                           0, False),  # Gil: 200 [02h]
    ("Baaj Temple: Chest 2",                                                           1, False),  # Item: 2x Potion [2000h]
    ("Withered Bouquet",                                                               2, False),  # Key Item: Withered Bouquet [A000h]
    ("Flint",                                                                          3, False),  # Key Item: Flint [A001h]
    ("Treasure 4 (Potentially Trashed Chest)",                                         4, False),  # Gear: buki_get #2 [02h] { Yuna [01h], Weapon {One MP Cost [800Dh], Empty, Empty, Empty} }
    ("Onion Knight",                                                                   5, False),  # Gear: buki_get #3 [03h] { Lulu [05h], Weapon Formula=Celestial MP-based [12h] {No AP [8014h], Empty, Empty, Empty} }
    ("Baaj Temple: Ether (Chest)",                                                     6, False),  # Item: 1x Ether [2004h]
    ("Baaj Temple: Hi-Potion (Chest)",                                                 7, False),  # Item: 1x Hi-Potion [2001h]
    ("Treasure 8 (Potentially Trashed Chest)",                                         8, False),  # Item: 1x Phoenix Down [2006h]
    ("Besaid: Antidote x2",                                                            9, False),  # Item: 2x Antidote [200Ah]
    # ("Treasure 10 (Potentially Trashed Chest)",                                     10, False),  # Gil: 200 [02h]
    # ("Treasure 11 (Potentially Trashed Chest)",                                     11, False),  # Gear: buki_get #4 [04h] { Tidus [00h], Weapon {Firestrike [801Eh]} }
    # ("Treasure 12 (Potentially Trashed Chest)",                                     12, False),  # Item: 1x Potion [2000h]
    ("Besaid: Phoenix Down x1 (Chest, Besaid Village)",                               13, False),  # Item: 1x Phoenix Down [2006h]
    ("Besaid: Hi-Potion x1 (Chest)",                                                  14, False),  # Item: 1x Hi-Potion [2001h]
    ("Besaid: Destruction Sphere",                                                    15, False),  # Gear: buki_get #5 [05h] { Yuna [01h], Weapon {Magic +5% [8067h], !Magic +3% [8066h], !Sensor [8000h]} }
    ("S.S. Liki: Remedy x1 (Chest)",                                                  16, False),  # Item: 1x Remedy [200Fh]
    ("Kilika: Potion x3 (Chest)",                                                     17, False),  # Item: 3x Potion [2000h]
    ("Kilika: Ether x1 (Chest)",                                                      18, False),  # Item: 1x Ether [2004h]
    ("Kilika: Destruction Sphere",                                                    19, False),  # Gear: buki_get #6 [06h] { Kimahri [03h], Armor {Fire Ward [801Fh], Ice Ward [8023h], Lightning Ward [8027h]} }
    # ("Treasure 20 (Potentially Trashed Chest)",                                     20, False),  # Gear: buki_get #7 [07h] { Lulu [05h], Armor {Berserk Ward [8051h]} }
    # ("Treasure 21 (Potentially Trashed Chest)",                                     21, False),  # Item: 1x Potion [2000h] #Likely 21-26 are Potions from Yuna's Luggage as entries are near by S.S. Liki's treasure ID's
    # ("Treasure 22 (Potentially Trashed Chest)",                                     22, False),  # Item: 1x Potion [2000h]
    # ("Treasure 23 (Potentially Trashed Chest)",                                     23, False),  # Item: 1x Potion [2000h]
    # ("Treasure 24 (Potentially Trashed Chest)",                                     24, False),  # Item: 1x Potion [2000h]
    # ("Treasure 25 (Potentially Trashed Chest)",                                     25, False),  # Item: 1x Potion [2000h]
    # ("Treasure 26 (Potentially Trashed Chest)",                                     26, False),  # Item: 1x Potion [2000h]
    ("Kilika: Mana Sphere x2 (Chest)",                                                27, False),  # Item: 2x Mana Sphere [2047h]
    ("Kilika: Scout (Chest)",                                                         28, False),  # Gear: buki_get #8 [08h] { Wakka [04h], Weapon {Icestrike [8022h], Sensor [8000h]} }
    ("Kilika: Luck Sphere x1 (Chest)",                                                29, False),  # Item: 1x Luck Sphere [205Eh]
    ("Kilika: NulBlaze Shield (Woman NPC after defeating Lord Ochu)",                 30, False),  # Gear: buki_get #9 [09h] { Tidus [00h], Armor {SOS NulBlaze [8061h]} }
    ("S.S. Winno: Hi-Potion x1 (Chest)",                                              31, False),  # Item: 1x Hi-Potion [2001h]
    ("Luca: Phoenix Down x2 (Chest)",                                                 32, False),  # Item: 2x Phoenix Down [2006h]
    ("Luca: 600 Gil (Chest)",                                                         33, False),  # Gil: 600 [06h]
    ("Luca: Tidal Spear (Chest)",                                                     34, False),  # Gear: buki_get #10 [0Ah] { Kimahri [03h], Weapon {Piercing [800Bh], Waterstrike [802Ah]} }
    ("Luca: HP Sphere x1 (Chest)",                                                    35, False),  # Item: 1x HP Sphere [2055h]
    ("Luca: Hi-Potion x2 (Chest)",                                                    36, False),  # Item: 2x Hi-Potion [2001h]
    ("Luca: 1000 Gil (Chest)",                                                        37, False),  # Gil: 1000 [0Ah]
    ("Mi'ihen Highroad: Ice Brand (Chest)",                                           38, False),  # Gear: buki_get #11 [0Bh] { Tidus [00h], Weapon {Icestrike [8022h]} }
    ("Mi'ihen Highroad: Fortune Sphere (Chest)",                                      39, False),  # Item: 1x Fortune Sphere [204Ah]
    ("Mi'ihen Highroad: Thunder Blade (Chest)",                                       40, False),  # Gear: buki_get #12 [0Ch] { Auron [02h], Weapon {Piercing [800Bh], Lightningstrike [8026h]} }
    ("Mi'ihen Highroad: Scout (Chest)",                                               41, False),  # Gear: buki_get #13 [0Dh] { Wakka [04h], Weapon {Lightningstrike [8026h], Sensor [8000h]} }
    ("Mi'ihen Highroad: Heat Lance (Chest)",                                          42, False),  # Gear: buki_get #14 [0Eh] { Kimahri [03h], Weapon {Piercing [800Bh], Firestrike [801Eh]} }
    ("Mi'ihen Highroad: Hi-Potion x2 (Chest)",                                        43, False),  # Item: 2x Hi-Potion [2001h]
    ("Mi'ihen Highroad: Remedy x1 (Chest)",                                           44, False),  # Item: 1x Remedy [200Fh]
    ("Mi'ihen Highroad: 2000 gil (Chest)",                                            45, False),  # Gil: 2000 [14h]
    ("Mi'ihen Highroad: Eye Drops x3 (Chest)",                                        46, False),  # Item: 3x Eye Drops [200Ch]
    ("Mushroom Rock Road: Soft x4 (Chest)",                                           47, False),  # Item: 4x Soft [200Bh]
    ("Mushroom Rock Road: 1000 gil (Chest)",                                          48, False),  # Gil: 1000 [0Ah]
    ("Mushroom Rock Road: Hi-Potion x1 (Chest)",                                      49, False),  # Item: 1x Hi-Potion [2001h]
    ("Mushroom Rock Road: Remedy x1 (Chest)",                                         50, False),  # Item: 1x Remedy [200Fh]
    ("Mushroom Rock Road: Serene Bracer (Chest)",                                     51, False),  # Gear: buki_get #15 [0Fh] { Auron [02h], Armor {HP +5% [8072h], Berserk Ward [8051h]} }
    ("Mushroom Rock Road: Mega-Potion x1 (Chest)",                                    52, False),  # Item: 1x Mega-Potion [2003h]
    # ("Treasure 53 (Potentially Trashed Treasure)",                                  53, False),  # Item: 1x Potion [2000h]
    ("Djose: Phoenix Down x2 (Chest)",                                                54, False),  # Item: 2x Phoenix Down [2006h]
    ("Djose: Bright Bangle (Chest)",                                                  55, False),  # Gear: Bright Bangle
    # ("Treasure 56 (Potentially Trashed Treasure)",                                  56, False),  # Gear: buki_get #17 [11h] { Yuna [01h], Armor {Lightning Ward [8027h], Poison Ward [803Dh]} }
    ("Mushroom Rock Road: Serene Armlet (Chest)",                                     57, False),  # Gear: buki_get #18 [12h] { Kimahri [03h], Armor {Dark Ward [8049h], Berserk Ward [8051h]} }
    ("Djose: Ability Sphere x4 (Chest)",                                              58, False),  # Item: 4x Ability Sphere [2049h]
    ("Djose: 4000 gil (Chest)",                                                       59, False),  # Gil: 4000 [28h]
    ("Djose: Switch Hitter (Chest)",                                                  60, False),  # Gear: buki_get #19 [13h] { Wakka [04h], Weapon {Strength +3% [8062h], Strength +5% [8063h]} }
    ("Djose: Ether x1 (Chest)",                                                       61, False),  # Item: 1x Ether [2004h]
    ("Djose: Remedy x1 (Chest)",                                                      62, False),  # Item: 1x Remedy [200Fh]
    ("Djose: Mega Phoenix x1 (Chest)",                                                63, False),  # Item: 1x Mega Phoenix [2007h]
    ("Guadosalam: 3000 gil (Chest)",                                                  64, False),  # Gil: 3000 [1Eh]
    ("Guadosalam: Mega-Potion x1 (Chest)",                                            65, False),  # Item: 1x Mega-Potion [2003h]
    ("Guadosalam: Elixir x1 gil (Chest)",                                             66, False),  # Item: 1x Elixir [2008h]
    ("Guadosalam: Hi-Potion x2 (Chest)",                                              67, False),  # Item: 2x Hi-Potion [2001h]
    ("Macalania Woods: 2000 gil (Chest)",                                             68, False),  # Gil: 2000 [14h]
    ("Macalania Woods: Sleepy Cait Sith (Chest)",                                     69, False),  # Gear: buki_get #20 [14h] { Lulu [05h], Weapon {Sleeptouch [803Fh]} }
    ("Macalania Woods: Phoenix Down x3 (Chest)",                                      70, False),  # Item: 3x Phoenix Down [2006h]
    ("Macalania Woods: MP Sphere x1 (Butterfly Minigame Reward before Spherimorph)",  71, False),  # Item: 1x MP Sphere [2056h]
    ("Macalania Woods: Ether x1 (Butterfly Minigame Reward before Spherimorph)",      72, False),  # Item: 1x Ether [2004h]
    ("Macalania Woods: Remedy x1 (Chest)",                                            73, False),  # Item: 1x Remedy [200Fh]
    #  ("Treasure 74 (Trashed)",                                                      74, False),  # Item: 1x Potion [2000h]
    ("Macalania Woods: Lucid Ring (Chest)",                                           75, False),  # Gear: buki_get #21 [15h] { Yuna [01h], Armor {Silence Ward [8045h], Confuse Ward [804Fh]} }
    ("Lake Macalania: 4000 gil (Chest)",                                              76, False),  # Gil: 4000 [28h]
    ("Lake Macalania: Lv. 1 Key Sphere x1 (Chest)",                                   77, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("Lake Macalania: Mega-Potion x1 (Chest)",                                        78, False),  # Item: 1x Mega-Potion [2003h]
    ("Lake Macalania Bottom: Avenger (Chest)",                                        79, False),  # Gear: buki_get #22 [16h] { Tidus [00h], Weapon {Counterattack [8003h]} }
    ("Lake Macalania Bottom: Lv. 2 Key Sphere (Chest)",                               80, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    # ("Treasure 81 (Trashed)",                                                       81, False),  # Gear: buki_get #23 [17h] { Lulu [05h], Weapon {Silencetouch [8043h], Magic +5% [8067h]} }
    # ("Treasure 82 (Trashed)",                                                       82, False),  # Item: 1x Mega-Potion [2003h]
    ("Lake Macalania: 5000 gil (Chest)",                                              83, False),  # Gil: 5000 [32h]
    ("Lake Macalania: X-Potion x2 (Chest)",                                           84, False),  # Item: 2x X-Potion [2002h]
    ("Lake Macalania: Shell Targe (Tromell)",                                         85, False),  # Gear: buki_get #24 [18h] { Rikku [06h], Armor {SOS Shell [8059h]} }
    ("Lake Macalania: Phoenix Down x3 (Chest)",                                       86, False),  # Item: 3x Phoenix Down [2006h]
    ("Lake Macalania: Remedy x2 (Chest)",                                             87, False),  # Item: 2x Remedy [200Fh]
    # ("Treasure 88 (Trashed)",                                                       88, False),  # Gear: buki_get #25 [19h] { Kimahri [03h], Armor {Poison Ward [803Dh], Confuse Ward [804Fh], Silence Ward [8045h], Empty} }
    # ("Treasure 89 (Trashed)",                                                       89, False),  # Item: 1x Potion [2000h]
    ("Besaid: Phoenix Down x1 (Chest, Besaid Valley)",                                90, False),  # Item: 1x Phoenix Down [2006h]
    ("Besaid: Hi-Potion x1(Chest)",                                                   91, False),  # Item: 1x Hi-Potion [2001h]
    ("Besaid: Antidote x2 (Chest)",                                                   92, False),  # Item: 2x Antidote [200Ah]
    ("World Champion",                                                                93, False),  # Gear: buki_get #26 [1Ah] { Wakka [04h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    ("Mi'Hen Highroad: Scout (Donate 100 gil to Operation)",                          94, False),  # Gear: buki_get #27 [1Bh] { Wakka [04h], Weapon {Sensor [8000h]} }
    ("Mi'Hen Highroad: Ice Lance (Donate 1000 gil to Operation)",                     95, False),  # Gear: buki_get #28 [1Ch] { Kimahri [03h], Weapon {Piercing [800Bh], Icestrike [8022h]} }
    ("Mi'Hen Highroad: Moon Ring (Donate 10000 gil to Operation)",                    96, False),  # Gear: buki_get #29 [1Dh] { Yuna [01h], Armor {SOS Shell [8059h], SOS Protect [805Ah]} }
    ("Mi'ihen Highroad: Mega-Potion (NPC)",                                           97, False),  # Item: 2x Mega-Potion [2003h]
    ("Mushroom Rock Road: Hi-Potion x1 (Chest) (Aftermath)",                          98, False),  # Item: 1x Hi-Potion [2001h]
    ("Masamune",                                                                      99, False),  # Gear: buki_get #30 [1Eh] { Auron [02h], Weapon Formula=Celestial Auron [13h] {No AP [8014h], Empty, Empty, Empty} }
    ("Bevelle: Avenger (Chest)",                                                     100, False),  # Gear: buki_get #31 [1Fh] { Tidus [00h], Weapon {Counterattack [8003h]} }
    ("Bevelle: Rematch (Chest)",                                                     101, False),  # Gear: buki_get #32 [20h] { Wakka [04h], Weapon {Evade & Counter [8004h]} }
    ("Bevelle: Knight Lance (Chest)",                                                102, False),  # Gear: buki_get #33 [21h] { Kimahri [03h], Weapon {Strength +3% [8062h], Strength +5% [8063h], Strength +10% [8064h]} }
    # ("Treasure 103 (Trashed)",                                                     103, False),  # Item: 1x Potion [2000h]
    ("Bevelle: Elixir x1 (Chest)",                                                   104, False),  # Item: 1x Elixir [2008h]
    ("Bevelle: Wht Magic Sphere x1 (Chest)",                                         105, False),  # Item: 1x Wht Magic Sphere [204Eh]
    ("Bevelle: Skill Sphere x1 (Chest)",                                             106, False),  # Item: 1x Skill Sphere [204Dh]
    ("Bevelle: 10000 gil (Chest)",                                                   107, False),  # Gil: 10000 [64h]
    ("Bevelle: Lucid Ring (Chest)",                                                  108, False),  # Gear: buki_get #34 [22h] { Yuna [01h], Armor {Silence Ward [8045h], Confuse Ward [804Fh], Poison Ward [803Dh]} }
    ("Bevelle: Blk Magic Sphere (Chest)",                                            109, False),  # Item: 1x Blk Magic Sphere [204Fh]
    ("Bevelle: Mega-Potion x1 (Chest)",                                              110, False),  # Item: 1x Mega-Potion [2003h]
    ("Celestial Mirror",                                                             111, False),  # Key Item: Celestial Mirror [A003h]
    # ("Treasure 112 (Trashed)",                                                     112, False),  # Item: 1x Potion [2000h]
    ("Nirvana",                                                                      113, False),  # Gear: buki_get #36 [24h] { Yuna [01h], Weapon Formula=Celestial MP-based [12h] {No AP [8014h], Empty, Empty, Empty} }
    ("Caladblog",                                                                    114, False),  # Gear: buki_get #37 [25h] { Tidus [00h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    ("Calm Lands: 10000 gil (Chest)",                                                115, False),  # Gil: 10000 [64h]
    ("Calm Lands: 5000 gil (Chest)",                                                 116, False),  # Gil: 5000 [32h]
    ("Calm Lands: Lv. 2 Key Sphere x1 (Chest)",                                      117, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    ("Rusty Sword",                                                                  118, False),  # Key Item: Rusty Sword [A021h]
    # ("Treasure 119 (Trashed)",                                                     119, False),  # Gear: buki_get #38 [26h] { Kimahri [03h], Armor {HP +10% [8073h], Empty, Empty, Empty} }
    ("Cavern of the Stolen Fayth: Megalixir x1 (Chest)",                             120, False),  # Item: 1x Megalixir [2009h]
    ("Cavern of the Stolen Fayth: Lv. 2 Key Sphere x1 (Chest)",                      121, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    ("Cavern of the Stolen Fayth: Fortune Sphere x1 (Chest)",                        122, False),  # Item: 1x Fortune Sphere [204Ah]
    ("Cavern of the Stolen Fayth: Mega-Potion x1 (Chest)",                           123, False),  # Item: 2x Mega-Potion [2003h]
    ("Cavern of the Stolen Fayth: Flexible Arm (Chest)",                             124, False),  # Gear: buki_get #39 [27h] { Rikku [06h], Weapon {Empty, Empty, Empty, Empty} }
    ("Cavern of the Stolen Fayth: MP Sphere x1 (Chest)",                             125, False),  # Item: 1x MP Sphere [2056h]
    ("Cavern of the Stolen Fayth: X-Potion x2 (Chest)",                              126, False),  # Item: 2x X-Potion [2002h]
    # ("Treasure 127 (Trashed)",                                                     127, False),  # Item: 1x Potion [2000h]
    ("Mt. Gagazet: 20000 gil (Chest)",                                               128, False),  # Gil: 20000 [C8h]
    ("Mt. Gagazet: Mega-Potion x2 (Chest)",                                          129, False),  # Item: 2x Mega-Potion [2003h]
    ("Mt. Gagazet: Defending Bracer (Chest)",                                        130, False),  # Gear: buki_get #40 [28h] { Auron [02h], Armor {Stoneproof [8038h], Poisonproof [803Ch]} }
    ("Mt. Gagazet: Lv. 4 Key Sphere x1 (Chest)",                                     131, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    ("Mt. Gagazet: HP Sphere x1 (Chest)",                                            132, False),  # Item: 1x HP Sphere [2055h]
    # ("Treasure 133 (Trashed)",                                                     133, False),  # Item: 1x Potion [2000h]
    # ("Treasure 134 (Trashed)",                                                     134, False),  # Item: 1x Potion [2000h]
    ("Mt. Gagazet (Cave): Pep Talk (Chest)",                                         135, False),  # Gear: buki_get #41 [29h] { Wakka [04h], Armor {SOS NulFrost [805Fh], SOS NulShock [8060h], SOS NulBlaze [8061h]} }
    ("Mt. Gagazet (Cave): Lv. 1 Key Sphere x1 (Chest)",                              136, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("Mt. Gagazet (Cave): Fortune Sphere x1 (Chest)",                                137, False),  # Item: 1x Fortune Sphere [204Ah]
    ("Mt. Gagazet (Cave): Return Sphere x1 (Chest)",                                 138, False),  # Item: 1x Return Sphere [2060h]
    ("Mt. Gagazet (Cave): Recovery Ring (Chest)",                                    139, False),  # Gear: buki_get #42 [2Ah] { Yuna [01h], Armor {HP Stroll [801Bh]} }
    # ("Treasure 140 (Trashed)",                                                     140, False),  # Item: 1x Potion [2000h]
    # ("Treasure 141 (Trashed)",                                                     141, False),  # Item: 1x Potion [2000h]
    # ("Treasure 142 (Trashed)",                                                     142, False),  # Item: 1x Potion [2000h]
    # ("Treasure 143 (Trashed)",                                                     143, False),  # Item: 1x Potion [2000h]
    # ("Treasure 144 (Trashed)",                                                     144, False),  # Item: 1x Potion [2000h]
    ("Zanarkand: Fortune Sphere x1 (Chest)",                                         145, False),  # Item: 1x Fortune Sphere [204Ah]
    ("Zanarkand: Spiritual Targe (Chest)",                                           146, False),  # Gear: buki_get #43 [2Bh] { Rikku [06h], Armor {MP Stroll [801Ch]} }
    ("Zanarkand: 10000 gil (Chest)",                                                 147, False),  # Gil: 10000 [64h]
    ("Zanarkand: Friend Sphere x1 (Chest)",                                          148, False),  # Item: 1x Friend Sphere [2061h]
    ("Zanarkand: Lv. 3 Key Sphere x1 (Chest)",                                       149, False),  # Item: 1x Lv. 3 Key Sphere [2053h]
    ("Zanarkand: Luck Sphere x1",                                                    150, False),  # Item: 1x Luck Sphere [205Eh]
    # ("Treasure 151 (Trashed)",                                                     151, False),  # Item: 1x Potion [2000h]
    ("Omega Ruins: Fortune Sphere x1 (Chest)",                                       152, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    ("Omega Ruins: Defending Bracer (Chest)",                                        153, False),  # Gear: buki_get #44 [2Ch] { Auron [02h], Armor {Silenceproof [8044h], Darkproof [8048h]} }
    ("Omega Ruins: Turnover (Chest)",                                                154, False),  # Gear: buki_get #45 [2Dh] { Wakka [04h], Weapon {Magic Counter [8005h], Counterattack [8003h]} }
    ("Omega Ruins: Lv. 3 Key Sphere x2 (Chest)",                                     155, False),  # Item: 2x Lv. 3 Key Sphere [2053h]
    ("Omega Ruins: Defending Armlet (Chest)",                                        156, False),  # Gear: buki_get #46 [2Eh] { Kimahri [03h], Armor {Stoneproof [8038h], Poisonproof [803Ch], Empty, Empty} }
    ("Omega Ruins: Friend Sphere x2 (Chest)",                                        157, False),  # Item: 2x Friend Sphere [2061h]
    ("Omega Ruins: Lv. 4 Key Sphere x1 (Chest)",                                     158, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    ("Omega Ruins: Phantom Ring (Chest)",                                            159, False),  # Gear: buki_get #47 [2Fh] { Yuna [01h], Armor {Ice Eater [8025h], Fire Eater [8021h], Lightning Eater [8029h], Empty} }
    ("Omega Ruins: Cactuar Wizard (Chest)",                                          160, False),  # Gear: buki_get #48 [30h] { Lulu [05h], Weapon {Half MP Cost [800Ch]} }
    ("Omega Ruins: Warmonger (Chest)",                                               161, False),  # Gear: buki_get #49 [31h] { Rikku [06h], Weapon {Double AP [8012h], !Double Overdrive [800Eh]} }
    ("Yojimbo 3x Reward/Omega Ruins: Teleport Sphere x2 (Chest)",                    162, False),  # Item: 2x Teleport Sphere [2062h]
    ("Inside Sin: Elixir x1 (Chest)",                                                163, False),  # Item: 1x Elixir [2008h]
    ("Inside Sin: Wizard Lance (Chest)",                                             164, False),  # Gear: buki_get #50 [32h] { Kimahri [03h], Weapon {Magic +3% [8066h], Magic +5% [8067h], Magic +10% [8068h], Empty} }
    ("Inside Sin: Lv. 3 Key Sphere x1 (Chest)",                                      165, False),  # Item: 1x Lv. 3 Key Sphere [2053h]
    ("Inside Sin: Phantom Ring (Chest)",                                             166, False),  # Gear: buki_get #51 [33h] { Yuna [01h], Armor {Water Eater [802Dh], Fire Eater [8021h], Lightning Eater [8029h], Empty} }
    ("Inside Sin: Special Sphere x1 (Chest)",                                        167, False),  # Item: 1x Special Sphere [204Ch]
    ("Inside Sin: Lv. 4 Key Sphere x1 (Chest)",                                      168, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    ("Inside Sin: Four-on-One (Chest)",                                              169, False),  # Gear: buki_get #52 [34h] { Wakka [04h], Weapon {Waterstrike [802Ah], Firestrike [801Eh], Lightningstrike [8026h], Icestrike [8022h]} }
    ("Inside Sin: Defending Bracer (Chest)",                                         170, False),  # Gear: buki_get #53 [35h] { Auron [02h], Armor {Darkproof [8048h], Deathproof [8030h], Empty, Empty} }
    ("Inside Sin: 20000 gil (Chest)",                                                171, False),  # Gil: 20000 [C8h]
    ("Inside Sin: HP Sphere x1 (Chest)",                                             172, False),  # Item: 1x HP Sphere [2055h]
    ("Inside Sin: Defense Sphere x1 (Chest)",                                        173, False),  # Item: 1x Defense Sphere [2058h]
    ("Inside Sin: Megalixir x1 (Chest)",                                             174, False),  # Item: 1x Megalixir [2009h]
    ("Inside Sin: Laevatein (Chest)",                                                175, False),  # Gear: buki_get #54 [36h] { Yuna [01h], Weapon {SOS Overdrive [8010h]} }
    ("Cloudy Mirror",                                                                176, False),  # Key Item: Cloudy Mirror [A002h]
    ("Jecht Sphere",                                                                 177, False),  # Key Item: Jecht's Sphere [A020h]
    ("Thunder Plains: Phoenix Down x2 (Chest)",                                      178, False),  # Item: 2x Phoenix Down [2006h]
    ("Thunder Plains: Hi-Potion x2 (Chest)",                                         179, False),  # Item: 2x Hi-Potion [2001h]
    ("Thunder Plains: 5000 gil (Chest)",                                             180, False),  # Gil: 5000 [32h]
    ("Thunder Plains: Water Ball (Chest)",                                           181, False),  # Gear: buki_get #55 [37h] { Wakka [04h], Weapon {Waterstrike [802Ah], Empty} }
    ("Thunder Plains: X-Potion x1 (Chest)",                                          182, False),  # Item: 1x X-Potion [2002h]
    ("Thunder Plains: Ether x1 (Chest)",                                             183, False),  # Item: 1x Ether [2004h]
    ("Thunder Plains: Remedy x1 (Chest)",                                            184, False),  # Item: 1x Remedy [200Fh]
    ("Thunder Plains: 2000 gil (Chest)",                                             185, False),  # Gil: 2000 [14h]
    ("Mi'Hen Highroad Echo Ring (Win Aeon Fight)",                                   186, False),  # Gear: buki_get #74 [4Ah] { Yuna [01h], Armor {HP +10% [8073h], Silence Ward [8045h]} }
    ("Calm Lands: Power Spheres x30 (NPC)",                                          187, False),  # Item: 30x Power Sphere [2046h]
    ("Spirit Lance",                                                                 188, False),  # Gear: buki_get #56 [38h] { Kimahri [03h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    ("Thunder Plains: X-Potion x2 (Dodging Minigame Reward)",                        189, False),  # Item: 2x X-Potion [2002h]
    ("Thunder Plains: Mega-Potion x2 (Dodging Minigame Reward)",                     190, False),  # Item: 2x Mega-Potion [2003h]
    ("Thunder Plains: MP Sphere x2 (Dodging Minigame Reward)",                       191, False),  # Item: 2x MP Sphere [2056h]
    ("Thunder Plains: Strength Sphere x3 (Dodging Minigame Reward)",                 192, False),  # Item: 3x Strength Sphere [2057h]
    ("Thunder Plains: HP Sphere x3 (Dodging Minigame Reward)",                       193, False),  # Item: 3x HP Sphere [2055h]
    ("Thunder Plains: Megalixir x4 (Dodging Minigame Reward)",                       194, False),  # Item: 4x Megalixir [2009h]
    # ("Treasure 195 (Trashed)",                                                     195, False),  # Item: 1x Ether [2004h]
    # ("Treasure 196 (Trashed)",                                                     196, False),  # Item: 1x Elixir [2008h]
    ("Moonflow: X-Potion x1 (Chest)",                                                197, False),  # Item: 1x X-Potion [2002h]
    ("Moonflow: Phoenix Down x2 (Chest)",                                            198, False),  # Item: 2x Phoenix Down [2006h]
    ("Moonflow: 5000 gil (Chest)",                                                   199, False),  # Gil: 5000 [32h]
    ("Moonflow: Ether x1 (Chest)",                                                   200, False),  # Item: 1x Ether [2004h]
    ("Moonflow: Antidote x4 (Chest)",                                                201, False),  # Item: 4x Antidote [200Ah]
    ("Moonflow: Mega-Potion x1 (Chest)",                                             202, False),  # Item: 1x Mega-Potion [2003h]
    # ("Baaj Temple: Grenades from Rikku",                                           203, False),  # Item: 2x Grenade [2023h]
    ("Baaj Temple: Megalixir (Temple Area Chest)",                                   204, False),  # Item: 1x Megalixir [2009h]
    ("Baaj Temple: Mega Phoenix x4 (Temple Area Chest)",                             205, False),  # Item: 4x Mega Phoenix [2007h]
    ("Luca: Magic Sphere x1 (Chest)",                                                206, False),  # Item: 1x Magic Sphere [2059h]
    ("Brotherhood",                                                                  207, False),  # Gear: buki_get #1 [01h] { Tidus [00h], Weapon {Strength +5% [8063h], Strength +10% [8064h], Waterstrike [802Ah], Sensor [8000h]} }
    ("Brotherhood?",                                                                 208, False),  # Gear: buki_get #1 [01h] { Tidus [00h], Weapon {Strength +5% [8063h], Strength +10% [8064h], Waterstrike [802Ah], Sensor [8000h]} }
    ("Zanarkand Ruins: Destruction Sphere",                                          209, False),  # Gear: buki_get #60 [3Ch] { Yuna [01h], Weapon {Half MP Cost [800Ch], Empty, Empty} }
    ("Bikanel: Al Bhed Potion x8 (Chest, 1)",                                        210, False),  # Item: 8x Al Bhed Potion [2014h]
    ("Bikanel: Al Bhed Potion x8 (Chest, 2)",                                        211, False),  # Item: 8x Al Bhed Potion [2014h]
    ("Bikanel: Al Bhed Potion x8 (Chest, 3)",                                        212, False),  # Item: 8x Al Bhed Potion [2014h]
    ("Baaj Temple: X-Potion x1 (Chest)",                                             213, False),  # Item: 1x X-Potion [2002h]
    ("Godhand",                                                                      214, False),  # Gear: buki_get #61 [3Dh] { Rikku [06h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    ("Besaid Village: 400 gil (Chest)",                                              215, False),  # Gil: 400 [04h]
    ("Besaid Village: Potion x2 (Chest)",                                            216, False),  # Item: 2x Potion [2000h]
    ("Bevelle: HP Sphere x1 (Chest)",                                                217, False),  # Item: 1x HP Sphere [2055h]
    ("Guadosalam: Lightning Marble x8 (Chest)",                                      218, False),  # Item: 8x Lightning Marble [201Eh]
    ("Baaj Temple: Hi Potion x1 (Chest)",                                            219, False),  # Item: 1x Hi-Potion [2001h]
    ("Blitzball Reward",                                                             220, False),  # Item: 1x Hi-Potion [2001h]
    ("Blitzball Reward",                                                             221, False),  # Item: 1x Dark Matter [2035h]
    ("Blitzball Reward",                                                             222, False),  # Item: 1x Teleport Sphere [2062h]
    ("Blitzball Reward",                                                             223, False),  # Item: 1x Three Stars [2045h]
    ("Blitzball Reward",                                                             224, False),  # Item: 1x Luck Sphere [205Eh]
    ("Blitzball Reward",                                                             225, False),  # Item: 1x Underdog's Secret [206Eh]
    ("Blitzball Reward",                                                             226, False),  # Item: 1x Megalixir [2009h]
    ("Blitzball Reward",                                                             227, False),  # Item: 1x Return Sphere [2060h]
    ("Blitzball Reward",                                                             228, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("Blitzball Reward",                                                             229, False),  # Item: 1x Mega Phoenix [2007h]
    ("Blitzball Reward",                                                             230, False),  # Item: 1x Elixir [2008h]
    ("Blitzball Reward",                                                             231, False),  # Item: 1x Mega-Potion [2003h]
    ("Blitzball Reward",                                                             232, False),  # Item: 1x X-Potion [2002h]
    ("Blitzball Reward",                                                             233, False),  # Item: 1x Ether [2004h]
    ("Blitzball Reward",                                                             234, False),  # Item: 2x Remedy [200Fh]
    ("Blitzball Reward",                                                             235, False),  # Item: 2x Phoenix Down [2006h]
    ("Blitzball Reward",                                                             236, False),  # Item: 2x Hi-Potion [2001h]
    ("Blitzball Reward",                                                             237, False),  # Item: 5x Power Sphere [2046h]
    ("Blitzball Reward",                                                             238, False),  # Item: 5x Mana Sphere [2047h]
    ("Blitzball Reward",                                                             239, False),  # Item: 5x Speed Sphere [2048h]
    ("Blitzball Reward",                                                             240, False),  # Item: 5x Ability Sphere [2049h]
    ("Blitzball Reward",                                                             241, False),  # Item: 1x Echo Screen [200Dh]
    ("Blitzball Reward",                                                             242, False),  # Item: 1x Eye Drops [200Ch]
    ("Blitzball Reward",                                                             243, False),  # Item: 1x Antidote [200Ah]
    ("Jupiter Sigil",                                                                244, False),  # Key Item: Jupiter Sigil [A02Dh]
    ("Blitzball Reward",                                                             245, False),  # Item: 1x Elixir [2008h]
    ("Blitzball Reward",                                                             246, False),  # Item: 1x X-Potion [2002h]
    ("Blitzball Reward",                                                             247, False),  # Item: 1x Remedy [200Fh]
    ("Blitzball Reward",                                                             248, False),  # Item: 1x Hi-Potion [2001h]
    ("Blitzball Reward",                                                             249, False),  # Item: 4x Echo Screen [200Dh]
    ("Blitzball Reward",                                                             250, False),  # Item: 4x Eye Drops [200Ch]
    ("Blitzball Reward",                                                             251, False),  # Item: 4x Antidote [200Ah]
    ("Blitzball Reward",                                                             252, False),  # Item: 4x Soft [200Bh]
    ("Blitzball Reward",                                                             253, False),  # Item: 2x Potion [2000h]
    ("Blitzball Reward",                                                             254, False),  # Item: 2x Phoenix Down [2006h]
    ("Blitzball Reward",                                                             255, False),  # Item: 1x Potion [2000h]
    ("Blitzball Reward",                                                             256, False),  # Item: 1x Phoenix Down [2006h]
    ("Blitzball Reward",                                                             257, False),  # Item: 2x Hi-Potion [2001h]
    ("Blitzball Reward",                                                             258, False),  # Item: 1x Hi-Potion [2001h]
    ("Blitzball Reward",                                                             259, False),  # Item: 1x Potion [2000h]
    ("Blitzball Reward",                                                             260, False),  # Item: 1x Phoenix Down [2006h]
    ("Blitzball Reward",                                                             261, False),  # Item: 1x Return Sphere [2060h]
    ("Blitzball Reward",                                                             262, False),  # Item: 1x Rename Card [2065h]
    ("Blitzball Reward",                                                             263, False),  # Item: 1x Ether [2004h]
    ("Blitzball Reward",                                                             264, False),  # Item: 1x X-Potion [2002h]
    ("Blitzball Reward",                                                             265, False),  # Item: 1x Mega-Potion [2003h]
    ("Blitzball Reward",                                                             266, False),  # Item: 2x Remedy [200Fh]
    ("Sun Crest",                                                                    267, False),  # Key Item: Sun Crest [A023h]
    ("Moon Crest",                                                                   268, False),  # Key Item: Moon Crest [A025h]
    ("Mars Crest",                                                                   269, False),  # Key Item: Mars Crest [A027h]
    ("Saturn Crest",                                                                 270, False),  # Key Item: Saturn Crest [A02Ah]
    ("Jupiter Crest",                                                                271, False),  # Key Item: Jupiter Crest [A02Ch]
    ("Venus Crest",                                                                  272, False),  # Key Item: Venus Crest [A02Eh]
    ("Mercury Crest",                                                                273, False),  # Key Item: Mercury Crest [A030h]
    ("Sun Sigil",                                                                    274, False),  # Key Item: Sun Sigil [A024h]
    ("Moon Sigil",                                                                   275, False),  # Key Item: Moon Sigil [A026h]
    ("Mars Sigil",                                                                   276, False),  # Key Item: Mars Sigil [A028h]
    ("Saturn Sigil",                                                                 277, False),  # Key Item: Saturn Sigil [A02Bh]
    ("Venus Sigil",                                                                  278, False),  # Key Item: Venus Sigil [A02Fh]
    ("Mercury Sigil",                                                                279, False),  # Key Item: Mercury Sigil [A031h]
    ("Lake Macalania: Megalixir x2 (Butterfly Game after defeating Spherimorph)",    280, False),  # Item: 2x Megalixir [2009h]
    ("Lake Macalania: Elixir x2 (Butterfly Game after defeating Spherimorph)",       281, False),  # Item: 2x Elixir [2008h]
    ("Besaid: Hi-Potion x1 (Datto NPC)",                                             282, False),  # Item: 1x Hi-Potion [2001h]
    ("Besaid: Potion x3 (Jassu NPC)",                                                283, False),  # Item: 3x Potion [2000h]
    ("Besaid: Potion x2 (Botta NPC)",                                                284, False),  # Item: 2x Potion [2000h]
    ("Besaid: 200 gil (Keepa NPC)",                                                  285, False),  # Gil: 200 [02h]
    ("Besaid: Remedy x1 (Kid on Dock Bridge NPC)",                                   286, False),  # Item: 1x Remedy [200Fh]
    ("Besaid: Seeker's Ring (Priest NPC)",                                           287, False),  # Gear: buki_get #62 [3Eh] { Yuna [01h], Armor {HP +10% [8073h]} }
    ("Besaid: Phoenix Down x3 (Woman NPC)",                                          288, False),  # Item: 3x Phoenix Down [2006h]
    ("Besaid: 400 gil (Shirtless Man NPC)",                                          289, False),  # Gil: 400 [04h]
    ("Besaid: Ether (Green Shirt NPC)",                                              290, False),  # Item: 1x Ether [2004h]
    # ("Treasure 291 (Trashed)",                                                     291, False),  # Item: 4x Antidote [200Ah]
    ("Kilika: Elixir x1 (Luzzu NPC) ",                                               292, False),  # Item: 1x Elixir [2008h]
    ("Kilika: Remedy x1 (Leader NPC)",                                               293, False),  # Item: 1x Remedy [200Fh]
    # ("Treasure 294 (Trashed)",                                                     294, False),  # Item: 3x Phoenix Down [2006h]
    ("Kilika: Remedy x1 (Guard NPC)",                                                295, False),  # Item: 1x Hi-Potion [2001h]
    ("Al Bhed Ship: Potion x 3 (NPC)",                                               296, False),  # Item: 3x Potion [2000h]
    ("Djose: Variable Steel (NPC)",                                                  297, False),  # Gear: buki_get #63 [3Fh] { Tidus [00h], Weapon {Strength +3% [8062h], Empty, Empty, Empty} }
    ("Djose: Soft Ring (NPC)",                                                       298, False),  # Gear: buki_get #64 [40h] { Yuna [01h], Armor {Stoneproof [8038h], Empty} }
    ("Djose: Hi-Potion x1 (NPC)",                                                    299, False),  # Item: 1x Hi-Potion [2001h]
    ("Djose: Ether x1 (NPC)",                                                        300, False),  # Item: 1x Ether [2004h]
    ("Djose: Mega-Potion x1 (NPC)",                                                  301, False),  # Item: 1x Mega-Potion [2003h]
    ("Djose: Halberd (NPC)",                                                         302, False),  # Gear: buki_get #65 [41h] { Kimahri [03h], Weapon {Magic +20% [8069h], Empty} }
    ("Djose: Potion x10 (NPC)",                                                      303, False),  # Item: 10x Potion [2000h]
    ("Djose: Hi-Potion x2 (NPC)",                                                    304, False),  # Item: 2x Hi-Potion [2001h]
    ("Lake Macalania: 400 gil (Al Bhed Soldier NPC)",                                305, False),  # Gil: 400 [04h]
    ("Lake Macalania: Elixir x1 (Man Sitting NPC)",                                  306, False),  # Item: 1x Elixir [2008h]
    ("Lake Macalania: Ether x1 (Man Sitting NPC)",                                   307, False),  # Item: 1x Ether [2004h]
    ("Lake Macalania: Hi-Potion x2 (NPC)",                                           308, False),  # Item: 2x Hi-Potion [2001h]
    ("Mi'ihen Highroad: Hunters Spear (Blue Shirt NPC)",                             309, False),  # Gear: buki_get #66 [42h] { Kimahri [03h], Weapon {Piercing [800Bh], Sensor [8000h], Strength +10% [8064h]} }
    ("Mi'ihen Highroad: Antidote x2 (Red Skirt NPC)",                                310, False),  # Item: 2x Antidote [200Ah]
    ("TMi'ihen Highroad: Hi-Potion (Yellow Shirt NPC)",                              311, False),  # Item: 1x Hi-Potion [2001h]
    ("Mi'ihen Highroad: Soft x3 (Boy NPC)",                                          312, False),  # Item: 3x Soft [200Bh]
    ("Mi'ihen Highroad: Red Ring (Crusader NPC)",                                    313, False),  # Gear: buki_get #67 [43h] { Yuna [01h], Armor {HP +10% [8073h], Fire Ward [801Fh]} }
    ("Mi'ihen Highroad: Ether x1 (NPC)",                                             314, False),  # Item: 1x Ether [2004h]
    ("Mi'ihen Highroad: Hi-Potion x1 (NPC)",                                         315, False),  # Item: 1x Hi-Potion [2001h]
    ("Mi'ihen Highroad: 600 gil (Yellow Crusader NPC)",                              316, False),  # Gil: 600 [06h]
    ("Mi'ihen Highroad: Lv. 1 Key Sphere x1 (Purple Crusader NPC)",                  317, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("Mi'ihen Highroad: Antidote x4 (Woman in Yellow NPC)",                          318, False),  # Item: 4x Antidote [200Ah]
    ("Mushroom Rock Road: Tough Bangle (Gray Helmet NPC)",                           319, False),  # Gear: buki_get #68 [44h] { Lulu [05h], Armor {HP +20% [8074h], Empty} }
    ("Mushroom Rock Road: Phoenix Down x2 (Blue Shirt Crusader NPC)",                320, False),  # Item: 2x Phoenix Down [2006h]
    ("Mushroom Rock Road: Remedy x1 (Near Grey Helmet NPC)",                         321, False),  # Item: 1x Remedy [200Fh]
    ("Mushroom Rock Road: Hi-Potion x1 (Woman in Blue NPC)",                         322, False),  # Item: 1x Hi-Potion [2001h]
    ("Mushroom Rock Road: Ether x1 (Purple Helmet NPC)",                             323, False),  # Item: 1x Ether [2004h]
    ("Mushroom Rock Road: Hi-Potion x1 (Woman NPC near Save Point)",                 324, False),  # Item: 1x Hi-Potion [2001h]
    ("Mushroom Rock Road: 1000 gil (NPC near chest)",                                325, False),  # Item: 10x Potion [2000h]
    ("Mushroom Rock Road: 400 gil (NPC near elevator)",                              326, False),  # Gil: 400 [04h]
    ("Mushroom Rock Road: X-Potion x1 (NPC near lift)",                              327, False),  # Item: 1x X-Potion [2002h]
    ("Mushroom Rock Road: Mega-Potion x1 (NPC)",                                     328, False),  # Item: 1x Mega-Potion [2003h]
    ("Omega Ruins: Warp Sphere x99 (Chest)",                                         329, False),  # Item: 99x Warp Sphere [2063h]
    ("Omega Ruins: Teleport Sphere x1 (Chest)",                                      330, False),  # Item: 1x Teleport Sphere [2062h]
    ("Omega Ruins Friend Sphere x1 (Chest)",                                         331, False),  # Item: 1x Friend Sphere [2061h]
    ("Omega Ruins: Magic Sphere x1 (Chest)",                                         332, False),  # Item: 1x Magic Sphere [2059h]
    ("Treasure 333 (Old Entry?)",                                                    333, False),  # Key Item: Blossom Crown [A032h]
    ("Flower Scepter",                                                               334, False),  # Key Item: Flower Scepter [A033h]
    # ("Treasure 335 (Trashed)",                                                     335, False),  # Item: 1x Potion [2000h]
    ("S.S. Liki: Friend Sphere x1 (Clasko NPC)",                                     336, False),  # Item: 1x Friend Sphere [2061h] # Talk to Clasko before Crawler and make sure to have him become a Chocobo Breeder
    ("Calm Lands: Elixir x1 (Wobbly Chocobo Minigame Reward)",                       337, False),  # Item: 1x Elixir [2008h]
    ("Calm Lands: Lv. 1 Key Sphere x1 (Dodger Chocobo Minigame Reward)",             338, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("Calm Lands: Lv. 2 Key Sphere x1 x1 (Hyper Dodger Chocobo Minigame Reward)",    339, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    ("Calm Lands: Lv. 3 Key Sphere x1 x1 (Catcher Chocobo Minigame Reward)",         340, False),  # Item: 1x Lv. 3 Key Sphere [2053h]
    # ("Treasure 341 (Trashed)",                                                     341, False),  # Item: 1x X-Potion [2002h]
    # ("Treasure 342 (Trashed)",                                                     342, False),  # Item: 1x Mega-Potion [2003h]
    # ("Treasure 343 (Trashed)",                                                     343, False),  # Item: 1x Ether [2004h]
    # ("Treasure 344 (Trashed)",                                                     344, False),  # Item: 1x Turbo Ether [2005h]
    ("Thunder Plains: Yellow Shield (Ground Item)",                                  345, False),  # Gear: buki_get #69 [45h] { Tidus [00h], Armor {Lightningproof [8028h], Empty} }
    ("Bikanel: Remedy x4 (Chest)",                                                   346, False),  # Item: 4x Remedy [200Fh]
    ("Bikanel: Ether x2 (Chest)",                                                    347, False),  # Item: 2x Ether [2004h]
    ("Bikanel: Hi-Potion x4 (Chest, 1)",                                             348, False),  # Item: 4x Hi-Potion [2001h]
    ("Bikanel: Mega-Potion x2 (Chest)",                                              349, False),  # Item: 2x Mega-Potion [2003h]
    ("Bikanel: X-Potion x2 (Chest, 1)",                                              350, False),  # Item: 2x X-Potion [2002h]
    ("Bikanel: Hi-Potion x4 (Chest, 2)",                                             351, False),  # Item: 4x Hi-Potion [2001h]
    ("Bikanel: Elixir x1 (Chest)",                                                   352, False),  # Item: 1x Elixir [2008h]
    ("Bikanel: 10000 gil (Chest)",                                                   353, False),  # Gil: 10000 [64h]
    ("Bikanel: Lv. 2 Key Sphere x1 (Chest)",                                         354, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    ("Bikanel: Hi-Potion x8 (Chest)",                                                355, False),  # Item: 8x Hi-Potion [2001h]
    ("Bikanel: Mega-Potion x3 (Chest)",                                              356, False),  # Item: 3x Mega-Potion [2003h]
    ("Bikanel: X-Potion x2 (Chest, 2)",                                              357, False),  # Item: 2x X-Potion [2002h]
    ("Bikanel: Megalixir x3 (Chest)",                                                358, False),  # Item: 3x Megalixir [2009h]
    ("Bikanel: Teleport Sphere x2 (Chest)",                                          359, False),  # Item: 2x Teleport Sphere [2062h]
    ("Home: Al Bhed Potion x6 (Chest)",                                              360, False),  # Item: 6x Al Bhed Potion [2014h]
    ("Home: Al Bhed Potion x4 (Chest)",                                              361, False),  # Item: 4x Al Bhed Potion [2014h]
    ("Home: Lv. 2 Key Sphere x1 (Chest)",                                            362, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    ("Home: Lv. 4 Key Sphere x4 (Chest)",                                            363, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    ("Home: 10000 gil (Chest)",                                                      364, False),  # Gil: 10000 [64h]
    ("S.S Liki: Ace Wizard",                                                         365, False),  # Gear: buki_get #70 [46h] { Wakka [04h], Weapon {Magic +20% [8069h], Magic +10% [8068h], Magic +5% [8067h], Magic +3% [8066h]} }
    ("Mi'ihen Highroad: Seeker's Ring (Lose Aeon Fight)",                            366, False),  # Gear: buki_get #71 [47h] { Yuna [01h], Armor {HP +10% [8073h], Empty} }
    ("Home: Hi-Potion x2 (NPC on Ground)",                                           367, False),  # Item: 2x Hi-Potion [2001h]
    ("Mushroom Rock Road: Victorious",                                               368, False),  # Gear: buki_get #72 [48h] { Rikku [06h], Armor {Lightningproof [8028h], Fireproof [8020h], Iceproof [8024h], Empty} }
    ("Besaid Ruins: Murasame",                                                       369, False),  # Gear: buki_get #73 [49h] { Auron [02h], Weapon {Piercing [800Bh], One MP Cost [800Dh], Empty, Empty} }
    ("Calm Lands: Speed Sphere x30 (Lose Aeon Fight)",                               370, False),  # Item: 30x Speed Sphere [2048h]
    ("Aeon's Soul",                                                                  371, False),  # Key Item: Aeon's Soul [A01Fh]
    ("Moonflow: Dragon Scale x2 (Win Aeon Fight)",                                   372, False),  # Item: 2x Dragon Scale [2021h]
    ("Moonflow: Smoke Bomb x6 (Lose Aeon Fight)",                                    373, False),  # Item: 6x Smoke Bomb [2028h]
    ("Summoner's Soul",                                                              374, False),  # Key Item: Summoner's Soul [A01Eh]
    ("Airship: Al Bhed Potion (NPC)",                                                375, False),  # Item: 4x Al Bhed Potion [2014h]
    ("Moonflow: Lv. Key Sphere x3 (Shelinda Chest)",                                 376, False),  # Item: 3x Lv. 1 Key Sphere [2051h]
    ("Moonflow: Lv. Key Sphere x3 (Benke and Biran Chest)",                          377, False),  # Item: 3x Lv. 1 Key Sphere [2051h]
    ("Moonflow: Magic Def Sphere x1 (Chest)",                                        378, False),  # Item: 1x Magic Def Sphere [205Ah]
    ("Calm Lands: Valefor Fight First Reward (Remiem Tower)",                        379, False),  # Item: 4x Lightning Gem [201Fh]
    ("Calm Lands: Valefor Post First Fight Reward (Remiem Tower)",                   380, False),  # Item: 4x Power Sphere [2046h]
    ("Calm Lands: Ifrit Fight (Remiem Tower)",                                       381, False),  # Item: 30x X-Potion [2002h]
    ("Calm Lands: Ifrit Post First Fight Reward (Remiem Tower)",                     382, False),  # Item: 5x Mana Sphere [2047h]
    ("Calm Lands: Ixion Fight (Remiem Tower)",                                       383, False),  # Item: 10x Chocobo Feather [2036h]
    ("Calm Lands: Ixion Post First Fight Reward (Remiem Tower)",                     384, False),  # Item: 8x Power Sphere [2046h]
    ("Calm Lands: Shiva Fight (Remiem Tower)",                                       385, False),  # Item: 60x Mega-Potion [2003h]
    ("Calm Lands: Shiva Post First Fight Reward (Remiem Tower)",                     386, False),  # Item: 6x Star Curtain [203Ah]
    ("Calm Lands: Bahamut Post First Fight Reward (Remiem Tower)",                   387, False),  # Item: 8x Mana Sphere [2047h]
    ("Calm Lands: Yojimbo Fight (Remiem Tower)",                                     388, False),  # Item: 8x Shadow Gem [2029h]
    ("Calm Lands: Yojimbo Post First Fight Reward (Remiem Tower)",                   389, False),  # Item: 10x Power Sphere [2046h]
    ("Calm Lands: Anima Fight (Remiem Tower)",                                       390, False),  # Item: 60x Stamina Spring [203Dh]
    ("Calm Lands: Anima Post First Fight Reward (Remiem Tower)",                     391, False),  # Item: 10x Mana Sphere [2047h]
    ("Calm Lands: Magus Sisters Fight (Remiem Tower)",                               392, False),  # Item: 40x Shining Gem [202Ah]
    ("Calm Lands: Magus Sisters Post First Fight Reward (Remiem Tower)",             393, False),  # Item: 12x Power Sphere [2046h]
    ("Treasure 394 (Trashed)",                                                       394, False),  # Item: 1x Teleport Sphere [2062h]
    ("Home: Skill Sphere x1 (Al Bhed Quiz Chest)",                                   395, False),  # Item: 1x Skill Sphere [204Dh]
    ("Home: Skill Sphere x1 (Al Bhed Password Chest)",                               396, False),  # Item: 1x Special Sphere [204Ch]
    ("Home: Skill Sphere x1 (Al Bhed Vocabulary Chest)",                             397, False),  # Item: 1x Friend Sphere [2061h]
    ("Home: Elixir x1 (Al Bhed Vocabulary Chest)",                                   398, False),  # Item: 1x Elixir [2008h]
    ("Treasure 399 (Trashed)",                                                       399, False),  # Item: 1x Hi-Potion [2001h]
    ("Treasure 400 (Trashed)",                                                       400, False),  # Item: 1x Mega-Potion [2003h]
    ("Treasure 401 (Trashed)",                                                       401, False),  # Item: 1x Soft [200Bh]
    ("Treasure 402 (Trashed)",                                                       402, False),  # Item: 1x Potion [2000h]
    ("Treasure 403 (Trashed)",                                                       403, False),  # Item: 1x Remedy [200Fh]
    ("Treasure 404 (Trashed)",                                                       404, False),  # Item: 2x Potion [2000h]
    ("Complete Al Bhed Primers",                                                     405, False),  # Item: 99x Underdog's Secret [206Eh]
    ("Besaid: Wht Magic Sphere x1 (Aeon Room)",                                      406, False),  # Item: 1x Wht Magic Sphere [204Eh]
    ("Besaid: Elixir x1 (Aeon Room)",                                                407, False),  # Item: 1x Elixir [2008h]
    ("Besaid: Hi-Potion x1 (Aeon Room)",                                             408, False),  # Item: 1x Hi-Potion [2001h]
    ("Besaid: Potion x2 (Aeon Room)",                                                409, False),  # Item: 2x Potion [2000h]
    # ("S.S Liki: Potion (Yuna's suitcase)",                                         410, False),  # Item: 1x Potion [2000h] # Definitely Yuna's Suitcase
    # ("Treasure 411 (Trashed)",                                                     411, False),  # Item: 1x Potion [2000h]
    # ("Treasure 412 (Trashed)",                                                     412, False),  # Item: 1x Potion [2000h]
    # ("Treasure 413 (Trashed)",                                                     413, False),  # Item: 1x Potion [2000h]
    # ("Treasure 414 (Trashed)",                                                     414, False),  # Item: 1x Potion [2000h]
    # ("Treasure 415 (Trashed)",                                                     415, False),  # Item: 1x Potion [2000h]
    # ("Treasure 416 (Trashed)",                                                     416, False),  # Item: 1x Potion [2000h]
    ("Calm Lands: Elixir x1 (Chocobo Race Reward)",                                  417, False),  # Item: 1x Elixir [2008h]
    ("Calm Lands: Megalixir x1 (Chocobo Race Reward)",                               418, False),  # Item: 1x Megalixir [2009h]
    ("Calm Lands: Three Stars x60 (Chocobo Race Reward)",                            419, False),  # Item: 60x Three Stars [2045h]
    ("Calm Lands: Pendulum x30 (Chocobo Race Reward)",                               420, False),  # Item: 30x Pendulum [2069h]
    ("Calm Lands: Wings to Discovery x30 (Chocobo Race Reward)",                     421, False),  # Item: 30x Wings to Discovery [206Ch]
    # ("Treasure 422",                                                               422, False),  # Item: 1x Potion [2000h]
    ("Mi'ihen Highroad: Lv. 1 Key Sphere x1 (NPC)",                                  423, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("Monster Arena: Stamina Tonic x99 (NPC)",                                       424, False),  # Item: 99x Stamina Tonic [2043h]
    ("Monster Arena: Poison Fang x99 (NPC)",                                         425, False),  # Item: 99x Poison Fang [202Dh]
    ("Monster Arena: Soul Spring x99 (NPC)",                                         426, False),  # Item: 99x Soul Spring [203Eh]
    ("Monster Arena: Candle of Life x99 (NPC)",                                      427, False),  # Item: 99x Candle of Life [2030h]
    ("Monster Arena: Petrify Grenade x99 (NPC)",                                     428, False),  # Item: 99x Petrify Grenade [2031h]
    ("Monster Arena: Chocobo Wing x99 (NPC)",                                        429, False),  # Item: 99x Chocobo Wing [2037h]
    ("Monster Arena: Shining Gem x60 (NPC)",                                         430, False),  # Item: 60x Shining Gem [202Ah]
    ("Monster Arena: Shadow Gem x99 (NPC)",                                          431, False),  # Item: 99x Shadow Gem [2029h]
    ("Monster Arena: Farplane Wind x60 (NPC)",                                       432, False),  # Item: 60x Farplane Wind [2033h]
    ("Monster Arena: Silver Hourglass x40 (NPC)",                                    433, False),  # Item: 40x Silver Hourglass [202Eh]
    ("Blossom Crown",                                                                434, False),  # Key Item: Blossom Crown [A032h]
    ("Monster Arena: Lunar Curtain x99 (NPC)",                                       435, False),  # Item: 99x Lunar Curtain [2038h]
    ("Monster Arena: Designer Wallet x60 (NPC)",                                     436, False),  # Item: 60x Designer Wallet [2034h]
    ("Monster Arena: Chocobo Feather x99 (NPC)",                                     437, False),  # Item: 99x Chocobo Feather [2036h]
    ("Monster Arena: Stamina Spring x99 (NPC)",                                      438, False),  # Item: 99x Stamina Spring [203Dh]
    ("Monster Arena: Mega Phoenix x99 (NPC)",                                        439, False),  # Item: 99x Mega Phoenix [2007h]
    ("Monster Arena: Mana Tonic x60 (NPC)",                                          440, False),  # Item: 60x Mana Tonic [2044h]
    ("Monster Arena: Mana Spring x99 (NPC)",                                         441, False),  # Item: 99x Mana Spring [203Ch]
    ("Monster Arena: Stamina Tablet x60 (NPC)",                                      442, False),  # Item: 60x Stamina Tablet [2040h]
    ("Monster Arena: Twin Stars x60 (NPC)",                                          443, False),  # Item: 60x Twin Stars [2042h]
    ("Monster Arena: Star Curtain x99 (NPC)",                                        444, False),  # Item: 99x Star Curtain [203Ah]
    ("Monster Arena: Gold Hourglass x99 (NPC)",                                      445, False),  # Item: 99x Gold Hourglass [202Fh]
    ("Monster Arena: Purifying Salt x99 (NPC)",                                      446, False),  # Item: 99x Purifying Salt [203Fh]
    ("Monster Arena: Healing Spring x99 (NPC)",                                      447, False),  # Item: 99x Healing Spring [203Bh]
    ("Monster Arena: Turbo Ether x60 (NPC)",                                         448, False),  # Item: 60x Turbo Ether [2005h]
    ("Monster Arena: Light Curtain x99 (NPC)",                                       449, False),  # Item: 99x Light Curtain [2039h]
    ("Monster Arena: Mana Tablet x60 (NPC)",                                         450, False),  # Item: 60x Mana Tablet [2041h]
    ("Monster Arena: Three Stars x60 (NPC)",                                         451, False),  # Item: 60x Three Stars [2045h]
    ("Monster Arena: Supreme Gem x60 (NPC)",                                         452, False),  # Item: 60x Supreme Gem [202Ch]
    ("Monster Arena: Door to Tomorrow x99 (NPC)",                                    453, False),  # Item: 99x Door to Tomorrow [206Bh]
    ("Monster Arena: Gambler's Spirit x99 (NPC)",                                    454, False),  # Item: 99x Gambler's Spirit [206Dh]
    ("Monster Arena: Winning Formula x99 (NPC)",                                     455, False),  # Item: 99x Winning Formula [206Fh]
    ("Monster Arena: Dark Matter x99 (NPC)",                                         456, False),  # Item: 99x Dark Matter [2035h]
    ("Monster Arena: Megalixir x30 (NPC)",                                           457, False),  # Item: 30x Megalixir [2009h]
    ("Monster Arena: Master Sphere x10 (NPC)",                                       458, False),  # Item: 10x Master Sphere [2050h]
    ("Besaid: Map",                                                                  459, False),  # Item: 1x Map [2064h]
    ("Lake Macalania: Magic Def Sphere x1 (Aeon Room)",                              460, False),  # Item: 1x Magic Def Sphere [205Ah]
    ("Lake Macalania: Accuracy Sphere x1 (Aeon Room)",                               461, False),  # Item: 1x Accuracy Sphere [205Dh]
    ("Lake Macalania: Magic Sphere x1 (Aeon Room)",                                  462, False),  # Item: 1x Magic Sphere [2059h]
    ("Djose: Agility Sphere x1 (Aeon Room)",                                         463, False),  # Item: 1x Agility Sphere [205Bh]
    ("Djose: Magic Def Sphere x1 (Aeon Room)",                                       464, False),  # Item: 1x Magic Def Sphere [205Ah]
    ("Djose: Luck Sphere x1 (Aeon Room)",                                            465, False),  # Item: 1x Luck Sphere [205Eh]
    ("Calm Lands: Defense Sphere x1 (Remiem Temple Aeon Room)",                      466, False),  # Item: 1x Defense Sphere [2058h]
    ("Besaid: Evasion Sphere x1 (Aeon Room)",                                        467, False),  # Item: 1x Evasion Sphere [205Ch]
    ("Calm Lands: Strength Sphere x1 (Yojimbo Aeon Room)",                           468, False),  # Item: 1x Strength Sphere [2057h]
    ("Bikanel: Shadow Gem x2 (Robeya Minigame Chest)",                               469, False),  # Item: 2x Shadow Gem [2029h]
    ("Bikanel: Shining Gem x1 (Robeya Minigame Chest)",                              470, False),  # Item: 1x Shining Gem [202Ah]
    ("Bikanel: Blessed Gem x1 (Robeya Minigame Chest)",                              471, False),  # Item: 1x Blessed Gem [202Bh]
    ("Bikanel: Potion x1 (Cactuar Sidequest Prize)",                                 472, False),  # Item: 1x Potion [2000h]
    ("Bikanel: Elixir x1 (Cactuar Sidequest Prize)",                                 473, False),  # Item: 1x Elixir [2008h]
    ("Bikanel: Megalixir x1 (Cactuar Sidequest Prize)",                              474, False),  # Item: 1x Megalixir [2009h]
    ("Bikanel: Friend Sphere x1 (Cactuar Sidequest Prize)",                          475, False),  # Item: 1x Friend Sphere [2061h]
    ("Kilika: Agility Sphere x1 (Aeon Room)",                                        476, False),  # Item: 1x Agility Sphere [205Bh]
    ("Kilika: Defense Sphere x1 (Aeon Room)",                                        477, False),  # Item: 1x Defense Sphere [2058h]
    ("Kilika: Luck Sphere x1 (Aeon Room)",                                           478, False),  # Item: 1x Luck Sphere [205Eh]
    ("Kilika: Accuracy Sphere x1 (Aeon Room)",                                       479, False),  # Item: 1x Accuracy Sphere [205Dh]
    ("Besaid: Dragoon Lance",                                                        480, False),  # Gear: buki_get #75 [4Bh] { Kimahri [03h], Weapon {Magic Counter [8005h], Evade & Counter [8004h], Empty, Empty} }
    ("Mi'ihen Ruins: Sonar",                                                         481, False),  # Gear: buki_get #76 [4Ch] { Rikku [06h], Weapon {Initiative [8002h], Poisonstrike [803Ah], Empty} }
    ("Battle Site: Phantom Bangle",                                                  482, False),  # Gear: buki_get #77 [4Dh] { Lulu [05h], Armor {Ice Eater [8025h], Fire Eater [8021h], !Water Eater [802Dh]} }
    ("Sanubia Sands: Ascalon",                                                       483, False),  # Gear: buki_get #78 [4Eh] { Tidus [00h], Weapon {Double AP [8012h]} }
    ("Djose: Destruction Sphere",                                                    484, False),  # Item: 1x Magic Sphere [2059h]
    ("Lake Macalania: Destruction Sphere",                                           485, False),  # Item: 1x Luck Sphere [205Eh]
    ("Inside Sin: Prism Ball (Point of No Return)",                                  486, False),  # Gear: buki_get #79 [4Fh] { Wakka [04h], Weapon {Magic Counter [8005h], Empty} }
    ("Inside Sin: Stillblade (Point of No Return)",                                  487, False),  # Gear: buki_get #80 [50h] { Auron [02h], Weapon {Silencestrike [8042h], Stonestrike [8036h], Empty} }
    ("Inside Sin: Skill Sphere x1 (Point of No Return)",                             488, False),  # Item: 1x Skill Sphere [204Dh]
    ("Inside Sin: Mage's Staff (Point of No Return)",                                489, False),  # Gear: buki_get #81 [51h] { Yuna [01h], Weapon {Magic +10% [8068h], Magic +5% [8067h], Magic +3% [8066h], Empty} }
    ("Inside Sin: Knight Lance (Point of No Return)",                                490, False),  # Gear: buki_get #82 [52h] { Kimahri [03h], Weapon {Strength +10% [8064h], Strength +5% [8063h], Strength +3% [8062h], Empty} }
    ("Inside Sin: Wht Magic Sphere x1 (Point of No Return)",                         491, False),  # Item: 1x Wht Magic Sphere [204Eh]
    ("Inside Sin: Infinity (Point of No Return)",                                    492, False),  # Gear: buki_get #83 [53h] { Rikku [06h], Weapon {One MP Cost [800Dh], Sensor [8000h]} }
    ("Inside Sin: Wicked Cait Sith (Point of No Return)",                            493, False),  # Gear: buki_get #84 [54h] { Lulu [05h], Weapon {Deathstrike [802Eh], Empty, Empty, Empty} }
    ("Inside Sin: Attribute Sphere x1 (Point of No Return)",                         494, False),  # Item: 1x Attribute Sphere [204Bh]
    ("Inside Sin: Hrunting (Point of No Return)",                                    495, False),  # Gear: buki_get #85 [55h] { Tidus [00h], Weapon {SOS Overdrive [8010h]} }
    ("Mark of Conquest",                                                             496, False),  # Key Item: Mark of Conquest [A029h]
    ("Story Win vs. Luca Goers Reward",                                              497, False),  # Item: 1x Strength Sphere [2057h]
]]

character_names = [
    "Tidus",
    "Yuna",
    "Auron",
    "Kimahri",
    "Wakka",
    "Lulu",
    "Rikku"
]

FFXSphereGridLocations: List[List[FFXLocationData]] = [
    [FFXLocationData(location[1]+SphereGridOffset, *location) for location in [(f"{name}: Sphere Grid Node {i}", i + character*100, False) for i in range(100)]]
    for character, name in enumerate(character_names)
]


def create_location_label_to_id_map() -> Dict[str, int]:
    """
    Creates a map from location labels to their AP location id (address)
    """
    label_to_id_map: Dict[str, int] = {}
    for location in FFXTreasureLocations:
        label_to_id_map[location.name] = location.rom_address

    return label_to_id_map
