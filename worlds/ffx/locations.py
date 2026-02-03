from typing import Dict, Optional, List, Tuple, NamedTuple
from itertools import chain

from BaseClasses import Location, Region


class FFXLocation(Location):
    game: str = "Final Fantasy X"

    def __init__(self, player: int, name: str = '', address: Optional[int] = None, parent: Optional[Region] = None):
        super().__init__(player, name, address, parent)


class FFXLocationData(NamedTuple):
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
RecruitOffset: int = 0x7000
SphereGridOffset: int = 0x8000
CaptureOffset: int = 0x9000

location_types: Dict[int, str] = {
    TreasureOffset: "Treasure",
    BossOffset: "Boss",
    PartyMemberOffset: "PartyMember",
    OverdriveOffset: "Overdrive",
    OverdriveModeOffset: "OverdriveMode",
    OtherOffset: "Other",
    RecruitOffset: "Recruit",
    SphereGridOffset: "SphereGrid",
    CaptureOffset: "Capture"
}

def get_location_type(location_id: int):
    return location_types[location_id & 0xF000]

encounter_to_id = {
    "Baaj: Defeat Klikk (Boss)"                     : ["bjyt04_01"],
    "Al Bhed Ship: Defeat Tros (Boss)"              : ["cdsp07_00"],
    "Besaid: Defeat Dark Valefor (Superboss)"       : ["bsil07_70"],
    "S.S. Liki: Defeat Sin Fin (Boss)"              : ["slik02_00"],
    "S.S. Liki: Defeat Sinspawn Echuilles (Boss)"   : ["slik02_01"],
    "Kilika: Woods - Defeat Lord Ochu (Boss)"       : ["klyt00_00"],
    "Kilika: Defeat Sinspawn Geneaux (Boss)"        : ["klyt01_00"],
    "Luca: Defeat Oblitzerator (Boss)"              : ["cdsp02_00"],
    "Mi'ihen: Defeat Chocobo Eater (Boss)"          : ["mihn02_00"],
    "MRR: Defeat Sinspawn Gui First Phase (Boss)"   : ["kino02_00"],
    "MRR: Defeat Sinspawn Gui Second Phase (Boss)"  : ["kino03_10"],
    "Moonflow: Defeat Extractor (Boss)"             : ["genk09_00"],
    "Thunder Plains: Defeat Dark Ixion (Superboss)" : ["kami03_71"],
    "Macalania Woods: Defeat Spherimorph (Boss) (1)": ["mcfr03_00"],
    "Lake Macalania: Defeat Crawler (Boss)"         : ["maca02_00"],
    "Lake Macalaina: Defeat Seymour (Boss)"         : ["mcyt06_00"],
    "Lake Macalania: Defeat Wendigo (Boss)"         : ["maca02_01"],
    "Lake Macalania: Defeat Dark Shiva (Superboss)" : ["mcyt00_70"],
    "Bikanel: Defeat Dark Ifrit (Superboss)"        : ["bika03_70"],
    "Airship: Defeat Evrae (Boss)"                  : ["hiku15_00"],
    "Airship: Defeat Sin Left Fin (Boss)"           : ["ssbt00_00"],
    "Airship: Defeat Sin Right Fin (Boss)"          : ["ssbt01_00"],
    "Airship: Defeat Sin Core (Boss)"               : ["ssbt02_00"],
    "Airship: Defeat Overdrive Sin (Boss)"          : ["ssbt03_00"],
    "Airship: Defeat Penance (Superboss)"           : ["hiku15_70"],
    "Bevelle: Defeat Isaaru (Boss)"                 : ["bvyt09_12"], # Probably?
    "Bevelle: Defeat Evrae Altana (Boss)"           : ["stbv00_10"],
    "Bevelle: Defeat Seymour Natus (Boss)"          : ["stbv01_10"],
    "Calm Lands: Defeat Defender X (Boss)"          : ["nagi01_00"],
    "Monster Arena: Defeat Nemesis (Superboss)"     : ["zzzz02_76"],
    "CotSF: Defeat Dark Yojimbo (Superboss)"        : ["nagi05_74"],
    "Gagazet: Defeat Biran and Yenke (Boss)"        : ["mtgz01_10"],
    "Gagazet: Defeat Seymour Flux (Boss)"           : ["mtgz02_00"],
    "Gagazet: Defeat Dark Anima (Superboss)"        : ["mtgz01_70"],
    "Gagazet: Defeat Sanctuary Keeper (Boss)"       : ["mtgz08_00"],
    "Zanarkand: Defeat Spectral Keeper (Boss)"      : ["dome02_00"],
    "Zanarkand: Defeat Yunalesca (Boss)"            : ["dome06_00"],
    "Zanarkand: Defeat Dark Bahamut (Superboss)"    : ["dome06_70"],
    "Sin: Defeat Seymour Omnis (Boss)"              : ["sins03_00"],
    "Sin: Defeat Braska's Final Aeon (Boss)"        : ["sins06_00"],
    "Sin: Defeat Yuna's Aeons (Boss)"               : ["sins07_0x"],
    "Sin: Defeat Yu Yevon (Boss)"                   : ["sins07_10"],
    "Omega Ruins: Defeat Ultima (Boss)"             : ["omeg00_10"],
    "Omega Ruins: Defeat Omega (Superboss)"         : ["omeg01_10"],
    "MRR: Defeat Dark Mindy (Superboss)"            : ["kino00_70", "kino01_70", "kino01_72", "kino05_71"],
    "MRR: Defeat Dark Sandy (Superboss)"            : ["kino00_70", "kino01_70", "kino01_72", "kino05_70"],
    "MRR: Defeat Dark Cindy (Superboss)"            : ["kino00_70", "kino01_70", "kino01_71"],
    "Baaj: Defeat Geosgaeno (Boss)"                 : ["bjyt02_02"],
    "Bikanel: Defeat Zu (Boss)"                     : ["bika00_10"],
}


FFXBossLocations: List[FFXLocationData] = [ FFXLocationData(location[1]+BossOffset, *location) for location in [
    ("Baaj: Defeat Klikk (Boss)",                               0, False),
    ("Al Bhed Ship: Defeat Tros (Boss)",                        1, False),
    ("Besaid: Defeat Dark Valefor (Superboss)",                 2, False),
    ("S.S. Liki: Defeat Sin Fin (Boss)",                        3, False),
    ("S.S. Liki: Defeat Sinspawn Echuilles (Boss)",             4, False),
    ("Kilika: Woods - Defeat Lord Ochu (Boss)",                 5, False),
    ("Kilika: Defeat Sinspawn Geneaux (Boss)",                  6, False),
    ("Luca: Defeat Oblitzerator (Boss)",                        7, False),
    ("Mi'ihen: Defeat Chocobo Eater (Boss)",                    8, False),
    ("MRR: Defeat Sinspawn Gui First Phase (Boss)",             9, False),
    ("MRR: Defeat Sinspawn Gui Second Phase (Boss)",           10, False),
    #("MRR: Defeat Dark Magus Sisters (Superboss)",            11, False),
    ("Moonflow: Defeat Extractor (Boss)",                      12, False),
    ("Thunder Plains: Defeat Dark Ixion (Superboss)",          13, False),
    ("Macalania Woods: Defeat Spherimorph (Boss) (1)",         14, False),
    ("Lake Macalania: Defeat Crawler (Boss)",                  15, False),
    ("Lake Macalaina: Defeat Seymour (Boss)",                  16, False),
    ("Lake Macalania: Defeat Wendigo (Boss)",                  17, False),
    ("Lake Macalania: Defeat Dark Shiva (Superboss)",          18, False),
    ("Bikanel: Defeat Dark Ifrit (Superboss)",                 19, False),
    ("Airship: Defeat Evrae (Boss)",                           20, False),
    ("Airship: Defeat Sin Left Fin (Boss)",                    21, False),
    ("Airship: Defeat Sin Right Fin (Boss)",                   22, False),
    ("Airship: Defeat Sin Core (Boss)",                        23, False),
    ("Airship: Defeat Overdrive Sin (Boss)",                   24, False),
    # ("Airship: Defeat Penance (Superboss)",                    25, False),
    ("Bevelle: Defeat Isaaru (Boss)",                          26, False),
    ("Bevelle: Defeat Evrae Altana (Boss)",                    27, False),
    ("Bevelle: Defeat Seymour Natus (Boss)",                   28, False),
    ("Calm Lands: Defeat Defender X (Boss)",                   29, False),
    ("Monster Arena: Defeat Nemesis (Superboss)",              30, False),
    ("CotSF: Defeat Dark Yojimbo (Superboss)",                 31, False),
    ("Gagazet: Defeat Biran and Yenke (Boss)",                 32, False),
    ("Gagazet: Defeat Seymour Flux (Boss)",                    33, False),
    ("Gagazet: Defeat Dark Anima (Superboss)",                 34, False),
    ("Gagazet: Defeat Sanctuary Keeper (Boss)",                35, False),
    ("Zanarkand: Defeat Spectral Keeper (Boss)",               36, False),
    ("Zanarkand: Defeat Yunalesca (Boss)",                     37, False),
    ("Zanarkand: Defeat Dark Bahamut (Superboss)",             38, False),
    ("Sin: Defeat Seymour Omnis (Boss)",                       39, False),
    #("Sin: Defeat Braska's Final Aeon (Boss)",                40, False),
    #("Sin: Defeat Yuna's Aeons (Boss)",                       41, False),
    #("Sin: Defeat Yu Yevon (Boss)",                           42, False),
    ("Omega Ruins: Defeat Ultima (Boss)",                      43, False),
    ("Omega Ruins: Defeat Omega (Superboss)",                  44, False),
    ("MRR: Defeat Dark Mindy (Superboss)",                     45, False),
    ("MRR: Defeat Dark Sandy (Superboss)",                     46, False),
    ("MRR: Defeat Dark Cindy (Superboss)",                     47, False),
    ("Baaj: Defeat Geosgaeno (Boss)",                          48, False),
    ("Monster Arena: Defeat Stratoavis (Arena Boss)",          49, False),
    ("Monster Arena: Defeat Malboro Menace (Arena Boss)",      50, False),
    ("Monster Arena: Defeat Kottos (Arena Boss)",              51, False),
    ("Monster Arena: Defeat Coeurlregina (Arena Boss)",        52, False),
    ("Monster Arena: Defeat Jormungand (Arena Boss)",          53, False),
    ("Monster Arena: Defeat Cactuar King (Arena Boss)",        54, False),
    ("Monster Arena: Defeat Espada (Arena Boss)",              55, False),
    ("Monster Arena: Defeat Abyss Worm (Arena Boss)",          56, False),
    ("Monster Arena: Defeat Chimerageist (Arena Boss)",        57, False),
    ("Monster Arena: Defeat Don Tonberry (Arena Boss)",        58, False),
    ("Monster Arena: Defeat Catoblepas (Arena Boss)",          59, False),
    ("Monster Arena: Defeat Abaddon (Arena Boss)",             60, False),
    ("Monster Arena: Defeat Vorban (Arena Boss)",              61, False),
    ("Monster Arena: Defeat Fenrir (Arena Boss)",              62, False),
    ("Monster Arena: Defeat Ornitholestes (Arena Boss)",       63, False),
    ("Monster Arena: Defeat Pteryx (Arena Boss)",              64, False),
    ("Monster Arena: Defeat Hornet (Arena Boss)",              65, False),
    ("Monster Arena: Defeat Vidatu (Arena Boss)",              66, False),
    ("Monster Arena: Defeat One-Eye (Arena Boss)",             67, False),
    ("Monster Arena: Defeat Jumbo Flan (Arena Boss)",          68, False),
    ("Monster Arena: Defeat Nega Elemental (Arena Boss)",      69, False),
    ("Monster Arena: Defeat Tanket (Arena Boss)",              70, False),
    ("Monster Arena: Defeat Fafnir (Arena Boss)",              71, False),
    ("Monster Arena: Defeat Sleep Sprout (Arena Boss)",        72, False),
    ("Monster Arena: Defeat Bomb King (Arena Boss)",           73, False),
    ("Monster Arena: Defeat Juggernaut (Arena Boss)",          74, False),
    ("Monster Arena: Defeat Ironclad (Arena Boss)",            75, False),
    ("Monster Arena: Defeat Earth Eater (Superboss)",          76, False),
    ("Monster Arena: Defeat Greater Sphere (Superboss)",       77, False),
    ("Monster Arena: Defeat Catastrophe (Superboss)",          78, False),
    ("Monster Arena: Defeat Th'uban (Superboss)",              79, False),
    ("Monster Arena: Defeat Neslug (Superboss)",               80, False),
    ("Monster Arena: Defeat Ultima Buster (Superboss)",        81, False),
    ("Monster Arena: Defeat Shinryu (Superboss)",              82, False),
    ("Monster Arena: Defeat Nemesis (Superboss)",              83, False),
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
    ("Seed Cannon",    10, False), #Ragora, Grat, Sandragora, Ragora (m039, m040, m221, m234)
    ("Stone Breath",   11, False), #Basilisk, Anacondaur, Demonolith(?), Yenke Ronso, (m185, m186, m095, m135)
    ("Self Destruct",  12, False), #Bomb, Grenade, Puroboros, Biran Ronso (, m134)
    ("Fire Breath",    13, False), #Dual Horn, Valaha, Grendel, Yenke Ronso (m055, m056, m057, m135)
    ("Aqua Breath",    14, False), #Chimera, Chimera Brain, Chimera, Yenke Ronso (m087, m088, m227, m135)
    ("Bad Breath",     15, False), #Malboro, Great Malboro (m064, m065)
    ("Doom",           16, False), #Ghost, Wraith, Biran Ronso (m050, m220, m134)
    ("Thrust Kick",    17, False), #YKT-63, YKT-11, Biran Ronso (m195, m196, m134)
    ("White Wind",     18, False), #Dark Flan, Spirit, Yenke Ronso (m021, m219, m135)
    ("Mighty Guard",   19, False), #Behemoth, Behemoth King, Biran Ronso (m085, m086, m134)
    ("Nova",           20, False), #Omega Weapon, Nemesis (m100, m276)
    ("Besaid: Village, House - Something Mangled and Slobbery from Dog (NPC)",   21, False), #Energy Blast
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

    ("Al Bhed Ship: Deck & Bikanel: Oasis (Primer)",                                1, False), # Al Bhed Primer I
    ("Besaid: Village, Crusader Lodge - On Ground Near Counter (Primer)",           2, False), # Al Bhed Primer II
    ("S.S. Liki: Power Room & Bikanel: Oasis (Primer)",                             3, False), # Al Bhed Primer III
    ("Kilika: Tavern - On Counter (Primer)",                                        4, False), # Al Bhed Primer IV
    ("S.S. Winno: Bridge & Bikanel: Desert, East (Primer)",                         5, False), # Al Bhed Primer V
    ("Luca: Stadium Basement B - Behind Isken (Primer)",                             6, False), # Al Bhed Primer VI
    ("Luca: Theater Reception - Bottom of Stairs, Left Side (Primer)",              7, False), # Al Bhed Primer VII
    ("Mi'ihen: Agency - Exit After Resting (Event) (2)",                            8, False), # Al Bhed Primer VIII
    ("Mi'ihen: Newroad, North - Peak of South Bend Before Shelinda (Primer)",       9, False), # Al Bhed Primer IX
    ("MRR: Precipice - End of Curved Path West of North Elevator (Primer)",         10, False), # Al Bhed Primer X
    ("Djose: Highroad - South End, Behind Left Pillar (Primer)",                    11, False), # Al Bhed Primer XI
    ("Moonflow: North Wharf - Up Slope Right of Hypello (Primer)",                  12, False), # Al Bhed Primer XII
    ("Guadosalam: House - On Floor (Primer)",                                       13, False), # Al Bhed Primer XIII
    ("Thunder Plains: Agency & Bikanel: Desert, East (Primer)",                     14, False), # Al Bhed Primer XIV
    ("Macalania Woods: Lake Road - Near Southeast Exit (Primer)",                   15, False), # Al Bhed Primer XV
    ("Lake Macalania: Agency Front - Left Side (Primer)",                           16, False), # Al Bhed Primer XVI
    ("Bikanel: Desert, Central - Northeast Structure of Northwest Zone (Primer)",   17, False), # Al Bhed Primer XVII
    ("Bikanel: Desert, Central - Near Sign At Northeast Exit (Primer)",             18, False), # Al Bhed Primer XVIII
    ("Home: Left of Entrance (Primer)",                                             19, False), # Al Bhed Primer XIX
    ("Home: Living Quarters, South of Main Corridor - On Bed (Primer)",             20, False), # Al Bhed Primer XX
    ("Home: Main Corridor - Northeast Corner (Primer)",                             21, False), # Al Bhed Primer XXI
    ("Bevelle: Priests' Passage - Corner South of Save Point (Primer)",             22, False), # Al Bhed Primer XXII
    ("Calm Lands: North - Northwest Corner (Primer)",                               23, False), # Al Bhed Primer XXIII
    ("Calm Lands: Remiem Temple - Northwest Corner (Primer)",                       24, False), # Al Bhed Primer XXIV
    ("CotSF: Dead End West of Third Intersection (Primer)",                         25, False), # Al Bhed Primer XXV
    ("Omega Ruins: North Side of Four Chest Intersection (Primer)",                 26, False), # Al Bhed Primer XXVI
 
    #("Macalania Woods: Defeat Spherimorph (Boss) (2)",                        27, False),
    #("Besaid: Village - East of Temple (Jecht Sphere)",                       28, False),
    #("Jecht Sphere - S.S. Liki",                                              29, False),
    #("Luca: Stadium Basement A - East Locker Hall (Jecht Sphere)",            30, False),
    #("Mi'ihen: Oldroad, South - South End (Jecht Sphere)",                    31, False),
    #("MRR: Precipice - South of Large Elevator (Auron's Sphere)",             32, False),
    #("Jecht Sphere - Moonflow",                                               33, False),
    #("Jecht Sphere - Thunder Plains",                                         34, False),
    #("Braska's Sphere - Mt. Gagazet",                                         35, False),
                                       
    #("S.S. Winno: Jecht Shot (Event)",                          36, False),
    ("Guadosalam: Automatic Upon Leaving Farplane (Event)",      37, False), # Brotherhood Upgrade

    ("Macalania Woods: Upgrade Caladbolg Once (Event)",          38, False), # Caladbolg Crest Upgrade
    ("Macalania Woods: Upgrade Caladbolg Twice (Event)",         39, False), # Caladbolg Sigil Upgrade
    ("Macalania Woods: Upgrade Nirvana Once (Event)",            40, False), # Nirvana Crest Upgrade
    ("Macalania Woods: Upgrade Nirvana Twice (Event)",           41, False), # Nirvana Sigil Upgrade
    ("Macalania Woods: Upgrade Masamune Once (Event)",           42, False), # Masamune Crest Upgrade
    ("Macalania Woods: Upgrade Masamune Twice (Event)",          43, False), # Masamune Sigil Upgrade
    ("Macalania Woods: Upgrade Spirit Lance Once (Event)",       44, False), # Spirit Lance Crest Upgrade
    ("Macalania Woods: Upgrade Spirit Lance Twice (Event)",      45, False), # Spirit Lance Sigil Upgrade
    ("Macalania Woods: Upgrade World Champion Once (Event)",     46, False), # World Champion Crest Upgrade
    ("Macalania Woods: Upgrade World Champion Twice (Event)",    47, False), # World Champion Sigil Upgrade
    ("Macalania Woods: Upgrade Onion Knight Once (Event)",       48, False), # Onion Knight Crest Upgrade
    ("Macalania Woods: Upgrade Onion Knight Twice (Event)",      49, False), # Onion Knight Sigil Upgrade
    ("Macalania Woods: Upgrade Godhand Once (Event)",            50, False), # Godhand Crest Upgrade
    ("Macalania Woods: Upgrade Godhand Twice (Event)",           51, False), # Godhand Sigil Upgrade
]] #

FFXPartyMemberLocations: List[FFXLocationData] = [ FFXLocationData(location[1]+PartyMemberOffset, *location) for location in [
    # ("Party Member: Tidus",                                      0, False), 
    ("Besaid: Waterfall Way - Summon Tutorial (Event)",            1, False), # Party Member: Yuna
    ("Luca: Post-Blitzball Tournament (Event)",                    2, False), # Party Member: Auron
    ("S.S. Liki: Encounter Sin Fin (Event)",                       3, False), # Party Member: Kimahri
    ("Besaid: Enter the Valley (Event)",                           4, False), # Party Member: Wakka
    ("Besaid: Village Slope - Element Tutorial (Event)",           5, False), # Party Member: Lulu
    ("Moonflow: North Bank - Mix Tutorial (Event)",                6, False), # Party Member: Rikku
    ("Party Member: Seymour",                                      7, False), # Party Member: Seymour
    ("Besaid: Name Valefor (Event)",                               8, False), # Party Member: Valefor
    ("Kilika: Name Ifrit (Event)",                                 9, False), # Party Member: Ifrit
    ("Djose: Name Ixion (Event)",                                 10, False), # Party Member: Ixion
    ("Lake Macalaina: Fight Seymour (Boss)",                      11, False), # Party Member Shiva
    ("Bevelle: Name Bahamut (Event)",                             12, False), # Party Member: Bahamut
    ("Baaj: Release Anima (Event)",                               13, False), # Party Member: Anima
    ("CotSF: Hire Yojimbo (Event)",                               14, False), # Party Member: Yojimbo
    ("Calm Lands: Name the Magus Sisters (Event)",                15, False), # Party Member: Magus Sisters
]]

FFXRecruitLocations: List[FFXLocationData] = [ FFXLocationData(location[1]+RecruitOffset, *location) for location in [
    ("Recruit: Biggs",       1, False),
    ("Recruit: Brother",     2, False),
    ("Recruit: Durren",      3, False),
    ("Recruit: Jumal",       4, False),
    ("Recruit: Kiyuri",      5, False),
    ("Recruit: Kyou",        6, False),
    ("Recruit: Linna",       7, False),
    ("Recruit: Mep",         8, False),
    ("Recruit: Mifurey",     9, False),
    ("Recruit: Miyu",       10, False),
    ("Recruit: Naida",      11, False),
    ("Recruit: Nedus",      12, False),
    ("Recruit: Rin",        13, False),
    ("Recruit: Ropp",       14, False),
    ("Recruit: Shaami",     15, False),
    ("Recruit: Shuu",       16, False),
    ("Recruit: Svanda",     17, False),
    ("Recruit: Tatts",      18, False),
    ("Recruit: Vilucha",    19, False),
    ("Recruit: Wakka",      20, False),
    ("Recruit: Wedge",      21, False),
    ("Recruit: Yuma Guado", 22, False),
    ("Recruit: Zalits",     23, False),
    ("Recruit: Zev Ronso",  24, False)
]]

FFXTreasureLocations: List[FFXLocationData] = [ FFXLocationData(location[1]+TreasureOffset, *location) for location in [
    ("Baaj: Submerged Ruins - Northeast Structure (Chest)",                                           0, False),  # Gil: 200 [02h]
    ("Baaj: Submerged Ruins - Northwest Structure (Chest)",                                           1, False),  # Item: 2x Potion [2000h]
    ("Baaj: Stairs - Flowers in Sconce on Right Wall, North End (Event)",                             2, False),  # Key Item: Withered Bouquet [A000h]
    ("Baaj: Small Room - Flint Inside Desk (Event)",                                                  3, False),  # Key Item: Flint [A001h]
    #("Treasure 4 (Potentially Trashed Chest)",                                                        4, False),  # Gear: buki_get #2 [02h] { Yuna [01h], Weapon {One MP Cost [800Dh], Empty, Empty, Empty} }
    ("Baaj: Underwater Hall - South Side Hidden Under Rocks (Chest)",                                 5, False),  # Gear: buki_get #3 [03h] { Lulu [05h], Weapon Formula=Celestial MP-based [12h] {No AP [8014h], Empty, Empty, Empty} }
    ("Baaj: Stairs - South End (Chest)",                                                              6, False),  # Item: 1x Ether [2004h]
    ("Baaj: Hall - North exit from Stairs, East End (Chest)",                                         7, False),  # Item: 1x Hi-Potion [2001h]
    #("Treasure 8 (Potentially Trashed Chest)",                                                        8, False),  # Item: 1x Phoenix Down [2006h]
    ("Besaid: Beach - West Near Huts (Chest)",                                                        9, False),  # Item: 2x Antidote [200Ah]
    #("Treasure 10 (Potentially Trashed Chest)",                                                     10, False),  # Gil: 200 [02h]
    #("Treasure 11 (Potentially Trashed Chest)",                                                     11, False),  # Gear: buki_get #4 [04h] { Tidus [00h], Weapon {Firestrike [801Eh]} }
    #("Treasure 12 (Potentially Trashed Chest)",                                                     12, False),  # Item: 1x Potion [2000h]
    ("Besaid: Village - Front of Shop (Chest)",                                                      13, False),  # Item: 1x Phoenix Down [2006h]
    ("Besaid: Village - Behind Shop, Bottom (Chest)",                                                14, False),  # Item: 1x Hi-Potion [2001h]
    ("Besaid: Cloister - Destruction Sphere (Chest)",                                                15, False),  # Gear: buki_get #5 [05h] { Yuna [01h], Weapon {Magic +5% [8067h], !Magic +3% [8066h], !Sensor [8000h]} }
    ("S.S. Liki: Cabin (Chest)",                                                                     16, False),  # Item: 1x Remedy [200Fh]
    ("Kilika: House - Right of Collapsing House (Chest)",                                            17, False),  # Item: 3x Potion [2000h]
    ("Kilika: Tavern - After Rescuing Kulukan's Sister from Collapsing House (Chest)",               18, False),  # Item: 1x Ether [2004h]
    ("Kilika: Trials - Destruction Sphere (Chest)",                                                  19, False),  # Gear: buki_get #6 [06h] { Kimahri [03h], Armor {Fire Ward [801Fh], Ice Ward [8023h], Lightning Ward [8027h]} }
    #("Treasure 20 (Potentially Trashed Chest)",                                                     20, False),  # Gear: buki_get #7 [07h] { Lulu [05h], Armor {Berserk Ward [8051h]} }
    #("Treasure 21 (Potentially Trashed Chest)",                                                     21, False),  # Item: 1x Potion [2000h] #Likely 21-26 are Potions from Yuna's Luggage as entries are near by S.S. Liki's treasure ID's
    #("Treasure 22 (Potentially Trashed Chest)",                                                     22, False),  # Item: 1x Potion [2000h]
    #("Treasure 23 (Potentially Trashed Chest)",                                                     23, False),  # Item: 1x Potion [2000h]
    #("Treasure 24 (Potentially Trashed Chest)",                                                     24, False),  # Item: 1x Potion [2000h]
    #("Treasure 25 (Potentially Trashed Chest)",                                                     25, False),  # Item: 1x Potion [2000h]
    #("Treasure 26 (Potentially Trashed Chest)",                                                     26, False),  # Item: 1x Potion [2000h]
    ("Kilika: Woods - East of First Intersection (Chest)",                                           27, False),  # Item: 2x Mana Sphere [2047h]
    ("Kilika: Woods - West of First Intersection, First North Fork (Chest)",                         28, False),  # Gear: buki_get #8 [08h] { Wakka [04h], Weapon {Icestrike [8022h], Sensor [8000h]} }
    ("Kilika: Woods - Path North of Lord Ochu, Curving West (Chest)",                                29, False),  # Item: 1x Luck Sphere [205Eh]
    #("Kilika: NulBlaze Shield (Woman NPC after defeating Lord Ochu)",                               30, False),  # Gear: buki_get #9 [09h] { Tidus [00h], Armor {SOS NulBlaze [8061h]} } COMMENT OUT??
    ("S.S. Winno: Cabin - Left, Between Aurochs and Goers (Chest)",                                  31, False),  # Item: 1x Hi-Potion [2001h]
    ("Luca: Dock 2 - Left Side (Chest)",                                                             32, False),  # Item: 2x Phoenix Down [2006h]
    ("Luca: Dock 1 - Right Side (Chest)",                                                            33, False),  # Gil: 600 [06h]
    ("Luca: Dock 1 - End (Chest)",                                                                   34, False),  # Gear: buki_get #10 [0Ah] { Kimahri [03h], Weapon {Piercing [800Bh], Waterstrike [802Ah]} }
    ("Luca: Dock 5 - End, Hidden Behind Boxes, Left (Chest)",                                        35, False),  # Item: 1x HP Sphere [2055h]
    ("Luca: Stadium Basement B - West Locker Hall (Chest)",                                          36, False),  # Item: 2x Hi-Potion [2001h]
    ("Luca: City Limits - Staircase Leading to Mi'ihen (Chest)",                                     37, False),  # Gil: 1000 [0Ah]
    ("Mi'ihen: South End - Behind Ruins on Left (Chest)",                                            38, False),  # Gear: buki_get #11 [0Bh] { Tidus [00h], Weapon {Icestrike [8022h]} }
    ("Mi'ihen: Oldroad, South - Chocobo Jump, Alcove on East Side (Chest)",                          39, False),  # Item: 1x Fortune Sphere [204Ah]
    ("Mi'ihen: Oldroad, North - Chocobo Jump, Left Side (Chest) (1)",                                40, False),  # Gear: buki_get #12 [0Ch] { Auron [02h], Weapon {Piercing [800Bh], Lightningstrike [8026h]} }
    ("Mi'ihen: Oldroad, North - Chocobo Jump, Left Side (Chest) (2)",                                41, False),  # Gear: buki_get #13 [0Dh] { Wakka [04h], Weapon {Lightningstrike [8026h], Sensor [8000h]} }
    ("Mi'ihen: Newroad, North - Chocobo Jump North Peak of Bend (Chest)",                            42, False),  # Gear: buki_get #14 [0Eh] { Kimahri [03h], Weapon {Piercing [800Bh], Firestrike [801Eh]} }
    ("Mi'ihen: North End - Left by Child Soldiers (Chest)",                                          43, False),  # Item: 2x Hi-Potion [2001h]
    ("Mi'ihen: South - Behind Elma, North Side (Chest)",                                             44, False),  # Item: 1x Remedy [200Fh]
    ("Mi'ihen: Central, East Alcove (Chest)",                                                        45, False),  # Gil: 2000 [14h]
    ("Mi'ihen: Central - North Exit (Chest)",                                                        46, False),  # Item: 3x Eye Drops [200Ch]
    ("MRR: Aftermath - Left Exit Over Boxes (Chest)",                                                47, False),  # Item: 4x Soft [200Bh]
    ("MRR: Valley - North Alcove After First Elevator (Chest)",                                      48, False),  # Gil: 1000 [0Ah]
    ("MRR: Valley - Behind Pillar, Before Second Elevator (Chest)",                                  49, False),  # Item: 1x Hi-Potion [2001h]
    ("MRR: Valley - Left Side, As Trail Turns East (Chest)",                                         50, False),  # Item: 1x Remedy [200Fh]
    ("MRR: Ridge, Command Center - Behind Spear Rack (Chest)",                                       51, False),  # Gear: buki_get #15 [0Fh] { Auron [02h], Armor {HP +5% [8072h], Berserk Ward [8051h]} }
    ("MRR: Ridge, Command Center - Near Lulu (Chest)",                                               52, False),  # Item: 1x Mega-Potion [2003h]
    #("Treasure 53 (Potentially Trashed Treasure)",                                                  53, False),  # Item: 1x Potion [2000h]
    ("Djose: Highroad - South End, West Side (Chest)",                                               54, False),  # Item: 2x Phoenix Down [2006h]
    ("Djose: Highroad - Midway, Hidden in Western Alcove (Chest)",                                   55, False),  # Gear: Bright Bangle
    #("Treasure 56 (Potentially Trashed Treasure)",                                                  56, False),  # Gear: buki_get #17 [11h] { Yuna [01h], Armor {Lightning Ward [8027h], Poison Ward [803Dh]} }
    ("MRR: Precipice - Below West Elevator (Chest)",                                                 57, False),  # Gear: buki_get #18 [12h] { Kimahri [03h], Armor {Dark Ward [8049h], Berserk Ward [8051h]} }
    ("Djose: Temple - Northeast Corner (Chest)",                                                     58, False),  # Item: 4x Ability Sphere [2049h]
    ("Djose: Temple - West Behind Lucil's Squad (Chest)",                                            59, False),  # Gil: 4000 [28h]
    ("Djose: Inn - Behind Desk (Chest)",                                                             60, False),  # Gear: buki_get #19 [13h] { Wakka [04h], Weapon {Strength +3% [8062h], Strength +5% [8063h]} }
    ("Djose: Great Hall - In Front of Nuns' Chamber (Chest)",                                        61, False),  # Item: 1x Ether [2004h]
    ("Djose: Nuns' Chamber (Chest)",                                                                 62, False),  # Item: 1x Remedy [200Fh]
    ("Djose: Monks' Chamber (Chest)",                                                                63, False),  # Item: 1x Mega Phoenix [2007h]
    ("Guadosalam: House - Back Wall (Chest)",                                                        64, False),  # Gil: 3000 [1Eh]
    ("Guadosalam: East of Mansion (Chest)",                                                          65, False),  # Item: 1x Mega-Potion [2003h]
    ("Guadosalam: Upper Level, South Side (Chest)",                                                  66, False),  # Item: 1x Elixir [2008h]
    ("Guadosalam: Mansion, Entrance- Upper Level (Chest)",                                           67, False),  # Item: 2x Hi-Potion [2001h]
    ("Macalania Woods: South - Near North Exit (Chest)",                                             68, False),  # Gil: 2000 [14h]
    ("Macalania Woods: South - Hidden Behind Tree in Middle of S-Bend (Chest)",                      69, False),  # Gear: buki_get #20 [14h] { Lulu [05h], Weapon {Sleeptouch [803Fh]} }
    ("Macalania Woods: Central - Hidden Behind Tree Before Spiral Down (Chest)",                     70, False),  # Item: 3x Phoenix Down [2006h]
    ("Macalania Woods: MP Sphere x1 (Butterfly Minigame Reward before Spherimorph)",                 71, False),  # Item: 1x MP Sphere [2056h]
    ("Macalania Woods: Ether x1 (Butterfly Minigame Reward before Spherimorph)",                     72, False),  # Item: 1x Ether [2004h]
    ("Macalania Woods: North - Hidden Behind Tree on West Side (Chest)",                             73, False),  # Item: 1x Remedy [200Fh]
    #("Treasure 74 (Trashed)",                                                                       74, False),  # Item: 1x Potion [2000h]
    ("Macalania Woods: Campsite - (Chest)",                                                          75, False),  # Gear: buki_get #21 [15h] { Yuna [01h], Armor {Silence Ward [8045h], Confuse Ward [804Fh]} }
    ("Lake Macalania: Agency Front - Right Side (Chest)",                                            76, False),  # Gil: 4000 [28h]
    ("Lake Macalania: Crevasse - South End of Narrow Path (Chest)",                                  77, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("Lake Macalania: Crevasse - Near North Exit (Chest)",                                           78, False),  # Item: 1x Mega-Potion [2003h]
    ("Lake Macalania: Lake Bottom - Hidden Left of Auron (Chest)",                                   79, False),  # Gear: buki_get #22 [16h] { Tidus [00h], Weapon {Counterattack [8003h]} }
    ("Lake Macalania: Lake Bottom - Hidden Behind Kimahri (Chest)",                                  80, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    #("Treasure 81 (Trashed)",                                                                       81, False),  # Gear: buki_get #23 [17h] { Lulu [05h], Weapon {Silencetouch [8043h], Magic +5% [8067h]} }
    #("Treasure 82 (Trashed)",                                                                       82, False),  # Item: 1x Mega-Potion [2003h]
    ("Lake Macalania: Hall - North Side (Chest)",                                                    83, False),  # Gil: 5000 [32h]
    ("Lake Macalania: Hall - South Side (Chest)",                                                    84, False),  # Item: 2x X-Potion [2002h]
    ("Lake Macalania: Hall - Gift from Trommel upon Entrance (Event)",                               85, False),  # Gear: buki_get #24 [18h] { Rikku [06h], Armor {SOS Shell [8059h]} }
    ("Lake Macalania: Monks' Chamber (Chest)",                                                       86, False),  # Item: 3x Phoenix Down [2006h]
    ("Lake Macalania: Nuns' Chamber (Chest)",                                                        87, False),  # Item: 2x Remedy [200Fh]
    #("Treasure 88 (Trashed)",                                                                       88, False),  # Gear: buki_get #25 [19h] { Kimahri [03h], Armor {Poison Ward [803Dh], Confuse Ward [804Fh], Silence Ward [8045h], Empty} }
    #("Treasure 89 (Trashed)",                                                                       89, False),  # Item: 1x Potion [2000h]
    ("Besaid: Valley - South of Spawn, Right Side (Chest)",                                          90, False),  # Item: 1x Phoenix Down [2006h]
    ("Besaid: Valley - South Side, Hidden Behind Right Wall (Chest)",                                91, False),  # Item: 1x Hi-Potion [2001h]
    ("Besaid: Valley - East Side, Right of Path (Chest)",                                            92, False),  # Item: 2x Antidote [200Ah]
    ("Luca: Cafe - Talk to Owner After Placing at Least Third in a Tournament (Chest)",              93, False),  # Gear: buki_get #26 [1Ah] { Wakka [04h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    ("Mi'ihen: North End - Donate 100 (NPC)",                                                        94, False),  # Gear: buki_get #27 [1Bh] { Wakka [04h], Weapon {Sensor [8000h]} }
    ("Mi'ihen: North End - Donate 1000 (NPC)",                                                       95, False),  # Gear: buki_get #28 [1Ch] { Kimahri [03h], Weapon {Piercing [800Bh], Icestrike [8022h]} }
    ("Mi'ihen: North End - Donate 10000 (NPC)",                                                      96, False),  # Gear: buki_get #29 [1Dh] { Yuna [01h], Armor {SOS Shell [8059h], SOS Protect [805Ah]} }
    ("Mi'ihen: Agency - Exit After Resting (Event) (1)",                                             97, False),  # Item: 2x Mega-Potion [2003h]
    ("MRR: Aftermath - Under Overhang, West Side (Chest)",                                           98, False),  # Item: 1x Hi-Potion [2001h]
    ("MRR: Up Elevator in West Alcove, North Side (Event)",                                          99, False),  # Gear: buki_get #30 [1Eh] { Auron [02h], Weapon Formula=Celestial Auron [13h] {No AP [8014h], Empty, Empty, Empty} }
    ("Bevelle: Underwater After Evrae Altana, Right Side After First Turn (Chest)",                 100, False),  # Gear: buki_get #31 [1Fh] { Tidus [00h], Weapon {Counterattack [8003h]} }
    ("Bevelle: Underwater After Evrae Altana, Right Side Before First Turn (Chest)",                101, False),  # Gear: buki_get #32 [20h] { Wakka [04h], Weapon {Evade & Counter [8004h]} }
    ("Bevelle: Cloister - Left of Exit, 2 Bevelle Spheres Required (Chest)",                        102, False),  # Gear: buki_get #33 [21h] { Kimahri [03h], Weapon {Strength +3% [8062h], Strength +5% [8063h], Strength +10% [8064h]} }
    #("Treasure 103 (Trashed)",                                                                     103, False),  # Item: 1x Potion [2000h]
    ("Bevelle: Via Purifico - Southwest Room Near Glyph (Chest)",                                   104, False),  # Item: 1x Elixir [2008h]
    ("Bevelle: Via Purifico - West Room With Lulu (Chest)",                                         105, False),  # Item: 1x Wht Magic Sphere [204Eh]
    ("Bevelle: Via Purifico - Puzzle Room Right (Chest)",                                           106, False),  # Item: 1x Skill Sphere [204Dh]
    ("Bevelle: Via Purifico - Puzzle Room, Down Near Gate (Chest)",                                 107, False),  # Gil: 10000 [64h]
    ("Bevelle: Via Purifico - Puzzle Room Left (Chest)",                                            108, False),  # Gear: buki_get #34 [22h] { Yuna [01h], Armor {Silence Ward [8045h], Confuse Ward [804Fh], Poison Ward [803Dh]} }
    ("Bevelle: Via Purifico - Room Northeast of Central Teleporter (Chest)",                        109, False),  # Item: 1x Blk Magic Sphere [204Fh]
    ("Bevelle: Via Purifico - East Room With Kimahri (Chest)",                                      110, False),  # Item: 1x Mega-Potion [2003h]
    ("Macalania Woods: Bring Cloudy Mirror to Celestial Flower (Event)",                            111, False),  # Key Item: Celestial Mirror [A003h]
    #("Treasure 112 (Trashed)",                                                                     112, False),  # Item: 1x Potion [2000h]
    ("Monster Arena: Nirvana (Chest)",                                                              113, False),  # Gear: buki_get #36 [24h] { Yuna [01h], Weapon Formula=Celestial MP-based [12h] {No AP [8014h], Empty, Empty, Empty} }
    ("Calm Lands: North - NW Corner, Blocked Until Winning Catcher Chocobo (Event)",                114, False),  # Gear: buki_get #37 [25h] { Tidus [00h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    ("Calm Lands: South - Southeast Corner, Left (Chest)",                                          115, False),  # Gil: 10000 [64h]
    ("Calm Lands: South - Southeast Corner, Right (Chest)",                                         116, False),  # Gil: 5000 [32h]
    ("Calm Lands: Central - Behind Agency Tent (Chest)",                                            117, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    ("Calm Lands: Gorge Bottom - Rusty Sword Between Two Rocks, East End (Event)",                  118, False),  # Key Item: Rusty Sword [A021h]
    #("Treasure 119 (Trashed)",                                                                     119, False),  # Gear: buki_get #38 [26h] { Kimahri [03h], Armor {HP +10% [8073h], Empty, Empty, Empty} }
    ("CotSF: First Branch East (Chest)",                                                            120, False),  # Item: 1x Megalixir [2009h]
    ("CotSF: Chamber East of First Intersection (Chest)",                                           121, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    ("CotSF: Dead End North of Second Intersection (Chest)",                                        122, False),  # Item: 1x Fortune Sphere [204Ah]
    ("CotSF: Top of Third Intersection (Chest)",                                                    123, False),  # Item: 2x Mega-Potion [2003h]
    ("CotSF: Teleport West from Back of Cavern (Chest)",                                            124, False),  # Gear: buki_get #39 [27h] { Rikku [06h], Weapon {Empty, Empty, Empty, Empty} }
    ("CotSF: Teleport East from Back of Cavern, Bottom (Chest)",                                    125, False),  # Item: 1x MP Sphere [2056h]
    ("CotSF: Teleport East from Back of Cavern, Top (Chest)",                                       126, False),  # Item: 2x X-Potion [2002h]
    #("Treasure 127 (Trashed)",                                                                     127, False),  # Item: 1x Potion [2000h]
    ("Gagazet: Trail - Top of Right Ridge Near South Exit (Chest)",                                 128, False),  # Gil: 20000 [C8h]
    ("Gagazet: Trail - Left Alcove Near South Exit (Chest)",                                        129, False),  # Item: 2x Mega-Potion [2003h]
    ("Gagazet: Trail - West Branch Before Bridge to Wantz (Chest)",                                 130, False),  # Gear: buki_get #40 [28h] { Auron [02h], Armor {Stoneproof [8038h], Poisonproof [803Ch]} }
    ("Gagazet: Trail - Under Bridge After Wantz Right (Chest)",                                     131, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    ("Gagazet: Trail - Under Bridge After Wantz Left (Chest)",                                      132, False),  # Item: 1x HP Sphere [2055h]
    #("Treasure 133 (Trashed)",                                                                     133, False),  # Item: 1x Potion [2000h]
    #("Treasure 134 (Trashed)",                                                                     134, False),  # Item: 1x Potion [2000h]
    ("Gagazet: Cave - After Both Trials, Left Alcove, Northwest of Save Sphere (Chest)",            135, False), # Gear: buki_get #41 [29h] { Wakka [04h], Armor {SOS NulFrost [805Fh], SOS NulShock [8060h], SOS NulBlaze [8061h]} }
    ("Gagazet: Submerged Passage - Reward from First Trial (Chest)",                                136, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("Gagazet: Submerged Passage - Reward From Second Trial (Chest)",                               137, False),  # Item: 1x Fortune Sphere [204Ah]
    ("Gagazet: Submerged Passage - After Both Trials, East Exit From Save Sphere, Left (Chest)",    138, False),  # Item: 1x Return Sphere [2060h]
    ("Gagazet: Submerged Passage - After Both Trials, East Exit From Save Sphere, Right (Chest)",   139, False),  # Gear: buki_get #42 [2Ah] { Yuna [01h], Armor {HP Stroll [801Bh]} }
    #("Treasure 140 (Trashed)",                                                                     140, False),  # Item: 1x Potion [2000h]
    #("Treasure 141 (Trashed)",                                                                     141, False),  # Item: 1x Potion [2000h]
    #("Treasure 142 (Trashed)",                                                                     142, False),  # Item: 1x Potion [2000h]
    #("Treasure 143 (Trashed)",                                                                     143, False),  # Item: 1x Potion [2000h]
    #("Treasure 144 (Trashed)",                                                                     144, False),  # Item: 1x Potion [2000h]
    ("Zanarkand: Overpass - South Side, West Bend (Chest)",                                         145, False),  # Item: 1x Fortune Sphere [204Ah]
    ("Zanarkand: Overpass - North Side, Left Alcove (Chest)",                                       146, False),  # Gear: buki_get #43 [2Bh] { Rikku [06h], Armor {MP Stroll [801Ch]} }
    ("Zanarkand: Dome Interior - Road Above Underpass (Chest)",                                     147, False),  # Gil: 10000 [64h]
    ("Zanarkand: Dome Interior - West From 4-Way Intersection (Chest)",                             148, False),  # Item: 1x Friend Sphere [2061h]
    ("Zanarkand: Dome Interior - Rubble Path Down Before Circular Doorway (Chest)",                 149, False),  # Item: 1x Lv. 3 Key Sphere [2053h]
    ("Zanarkand: Dome Corridor - Right Side (Chest)",                                               150, False),  # Item: 1x Luck Sphere [205Eh]
    #("Treasure 151 (Trashed)",                                                                     151, False),  # Item: 1x Potion [2000h]
    ("Omega Ruins: 1st Chest Reward for Minigame (Chest)",                                          152, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    ("Omega Ruins: 2nd Chest Reward for Minigame (Chest)",                                          153, False),  # Gear: buki_get #44 [2Ch] { Auron [02h], Armor {Silenceproof [8044h], Darkproof [8048h]} }
    ("Omega Ruins: 3rd Chest Reward for Minigame (Chest)",                                          154, False),  # Gear: buki_get #45 [2Dh] { Wakka [04h], Weapon {Magic Counter [8005h], Counterattack [8003h]} }
    ("Omega Ruins: 4th Chest Reward for Minigame (Chest)",                                          155, False),  # Item: 2x Lv. 3 Key Sphere [2053h]
    ("Omega Ruins: 5th Chest Reward for Minigame (Chest)",                                          156, False),  # Gear: buki_get #46 [2Eh] { Kimahri [03h], Armor {Stoneproof [8038h], Poisonproof [803Ch], Empty, Empty} }
    ("Omega Ruins: 6th Chest Reward for Minigame (Chest)",                                          157, False),  # Item: 2x Friend Sphere [2061h]
    ("Omega Ruins: 7th Chest Reward for Minigame (Chest)",                                          158, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    ("Omega Ruins: 8th Chest Reward for Minigame (Chest)",                                          159, False),  # Gear: buki_get #47 [2Fh] { Yuna [01h], Armor {Ice Eater [8025h], Fire Eater [8021h], Lightning Eater [8029h], Empty} }
    ("Omega Ruins: 9th Chest Reward for Minigame (Chest)",                                          160, False),  # Gear: buki_get #48 [30h] { Lulu [05h], Weapon {Half MP Cost [800Ch]} }
    ("Omega Ruins: 10th Chest Reward for Minigame (Chest)",                                         161, False),  # Gear: buki_get #49 [31h] { Rikku [06h], Weapon {Double AP [8012h], !Double Overdrive [800Eh]} }
    ("Yojimbo 3x Reward/Omega Ruins: Teleport Sphere x2 (Chest)",                                   162, False),  # Item: 2x Teleport Sphere [2062h]
    ("Sin: Sea of Sorrow - Northwestern Alcove (Chest)",                                            163, False),  # Item: 1x Elixir [2008h]
    ("Sin: Sea of Sorrow - Atop Eastern Falls (Chest)",                                             164, False),  # Gear: buki_get #50 [32h] { Kimahri [03h], Weapon {Magic +3% [8066h], Magic +5% [8067h], Magic +10% [8068h], Empty} }
    ("Sin: Sea of Sorrow - Eastern Alcove, Near Final North Branch (Chest)",                        165, False),  # Item: 1x Lv. 3 Key Sphere [2053h]
    ("Sin: Sea of Sorrow - West Alcove (Chest)",                                                    166, False),  # Gear: buki_get #51 [33h] { Yuna [01h], Armor {Water Eater [802Dh], Fire Eater [8021h], Lightning Eater [8029h], Empty} }
    ("Sin: Sea of Sorrow - Atop Western Falls (Chest)",                                             167, False),  # Item: 1x Special Sphere [204Ch]
    ("Sin: City of Dying Dreams - East Glyph Near South Exit, Defeat 10/10/15 Fiends (Chest)",      168, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    ("Sin: City of Dying Dreams-South Side, Lift on Small Bridge (Chest)",                          169, False),  # Gear: buki_get #52 [34h] { Wakka [04h], Weapon {Waterstrike [802Ah], Firestrike [801Eh], Lightningstrike [8026h], Icestrike [8022h]} }
    ("Sin: City of Dying Dreams - South of First Open Area, Push North Wall Down (Chest)",          170, False),  # Gear: buki_get #53 [35h] { Auron [02h], Armor {Darkproof [8048h], Deathproof [8030h], Empty, Empty} }
    ("Sin: City of Dying Dreams - First Open Area, Ramp Down in Center (Chest)",                    171, False),  # Gil: 20000 [C8h]
    ("Sin: City of Dying Dreams - Lift Up in Center of First Open Area (Chest)",                    172, False),  # Item: 1x HP Sphere [2055h]
    ("Sin: City of Dying Dreams - Lift Up in Center of First Area, Just Before Lift Down (Chest)",  173, False),  # Item: 1x Defense Sphere [2058h]
    ("Sin: City of Dying Dreams - First Open Area, Glyph in Northwest Corner (Chest)",              174, False),  # Item: 1x Megalixir [2009h]
    ("Sin: City of Dying Dreams - Secret Slide South of Rising Block Area (Chest)",                 175, False),  # Gear: buki_get #54 [36h] { Yuna [01h], Weapon {SOS Overdrive [8010h]} }
    ("Calm Lands: Remiem Temple - Win Chocobo Race (Event)",                                        176, False),  # Key Item: Cloudy Mirror [A002h]
    ("Besaid: Village - East of Temple (Jecht's Sphere)",                                           177, False),  # Key Item: Jecht's Sphere [A020h]
    ("Thunder Plains: South - West Side, South of Save Sphere (Chest)",                             178, False),  # Item: 2x Phoenix Down [2006h]
    ("Thunder Plains: South - West Side, North of Save Sphere (Chest)",                             179, False),  # Item: 2x Hi-Potion [2001h]
    ("Thunder Plains: South - West Side, Behind First Cactuar Statue (Chest)",                      180, False),  # Gil: 5000 [32h]
    ("Thunder Plains: East Side, Alcove With Second Cactuar Statue (Chest)",                        181, False),  # Gear: buki_get #55 [37h] { Wakka [04h], Weapon {Waterstrike [802Ah], Empty} }
    ("Thunder Plains: North - East Side, Near Southeast Exit (Chest)",                              182, False),  # Item: 1x X-Potion [2002h]
    ("Thunder Plains: North - West Side, Behind Sheltered Lightning Rod (Chest)",                   183, False),  # Item: 1x Ether [2004h]
    ("Thunder Plains: North - West Side, Near North Exit (Chest)",                                  184, False),  # Item: 1x Remedy [200Fh]
    ("Thunder Plains: North - East of Final Lightning Rod (Chest)",                                 185, False),  # Gil: 2000 [14h]
    ("Mi'ihen: South End - Fight Belgemine (Win) (Event)",                                          186, False),  # Gear: buki_get #74 [4Ah] { Yuna [01h], Armor {HP +10% [8073h], Silence Ward [8045h]} }
    ("Calm Lands: Beat Belgemine (NPC)",                                                            187, False),  # Item: 30x Power Sphere [2046h]
    ("Cactuar Statue Minigame (Event)",                                                             188, False),  # Gear: buki_get #56 [38h] { Kimahri [03h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    ("Thunder Plains: Lightning Dodger - 5 Consecutive Dodges (Event)",                             189, False),  # Item: 2x X-Potion [2002h]
    ("Thunder Plains: Lightning Dodger - 10 Consecutive Dodges (Event)",                            190, False),  # Item: 2x Mega-Potion [2003h]
    ("Thunder Plains: Lightning Dodger - 20 Consecutive Dodges (Event)",                            191, False),  # Item: 2x MP Sphere [2056h]
    ("Thunder Plains: Lightning Dodger - 50 Consecutive Dodges (Event)",                            192, False),  # Item: 3x Strength Sphere [2057h]
    ("Thunder Plains: Lightning Dodger - 100 Consecutive Dodges (Event)",                           193, False),  # Item: 3x HP Sphere [2055h]
    ("Thunder Plains: Lightning Dodger - 150 Consecutive Dodges (Event)",                           194, False),  # Item: 4x Megalixir [2009h]
    #("Treasure 195 (Trashed)",                                                                     195, False),  # Item: 1x Ether [2004h]
    #("Treasure 196 (Trashed)",                                                                     196, False),  # Item: 1x Elixir [2008h]
    ("Moonflow: South Bank Road - West Corner as Path Bends East (Chest)",                          197, False),  # Item: 1x X-Potion [2002h]
    ("Moonflow: South Wharf - Near O'aka XXIII (Chest)",                                            198, False),  # Item: 2x Phoenix Down [2006h]
    ("Moonflow: South Wharf - Behind Lulu (Chest)",                                                 199, False),  # Gil: 5000 [32h]
    ("Moonflow: North Wharf: Near Bench (Chest)",                                                   200, False),  # Item: 1x Ether [2004h]
    ("Moonflow: North Bank - East Side, Right After the Wooden Bridge (Chest)",                     201, False),  # Item: 4x Antidote [200Ah]
    ("Moonflow: North Bank Road - West Side, Before Guadosalam (Chest)",                            202, False),  # Item: 1x Mega-Potion [2003h]
    #("Baaj Temple: Grenades from Rikku",                                                           203, False),  # Item: 2x Grenade [2023h]
    ("Baaj: Antechamber - Right Side (Chest)",                                                      204, False),  # Item: 1x Megalixir [2009h]
    ("Baaj: Antechamber - Left Side (Chest)",                                                       205, False),  # Item: 4x Mega Phoenix [2007h]
    ("Luca: Dock 5 - End, Hidden Behind Boxes, Right (Chest)",                                      206, False),  # Item: 1x Magic Sphere [2059h]
    ("Besaid: Exit the Village (Event) (1)",                                                        207, False),  # Gear: buki_get #1 [01h] { Tidus [00h], Weapon {Strength +5% [8063h], Strength +10% [8064h], Waterstrike [802Ah], Sensor [8000h]} }
    ("Brotherhood?",                                                                                208, False),  # Gear: buki_get #1 [01h] { Tidus [00h], Weapon {Strength +5% [8063h], Strength +10% [8064h], Waterstrike [802Ah], Sensor [8000h]} }
    ("Zanarkand: Destruction Sphere (Chest)",                                                       209, False),  # Gear: buki_get #60 [3Ch] { Yuna [01h], Weapon {Half MP Cost [800Ch], Empty, Empty} }
    ("Bikanel: Oasis - Next to Tent (Chest)",                                                       210, False),  # Item: 8x Al Bhed Potion [2014h]
    ("Bikanel: Desert, East - Near First Tent, Left (Chest)",                                       211, False),  # Item: 8x Al Bhed Potion [2014h]
    ("Bikanel: Desert, Central - Right of Save Sphere (Chest)",                                     212, False),  # Item: 8x Al Bhed Potion [2014h]
    ("Baaj: Hall - South Side of East Door (Chest)",                                                213, False),  # Item: 1x X-Potion [2002h]
    #("MRR: Code GODHAND",                                                                          214, False),  # Gear: buki_get #61 [3Dh] { Rikku [06h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} } UNCOMMENT WHEN CODES ARE INCORPORATED
    ("Besaid: Village - Behind Shop, Middle (Chest)",                                               215, False),  # Gil: 400 [04h]
    ("Besaid: Village - Behind Shop, Top (Chest)",                                                  216, False),  # Item: 2x Potion [2000h]
    ("Bevelle: Cloister - End (Chest)",                                                             217, False),  # Item: 1x HP Sphere [2055h]
    ("Guadosalam: Road to Farplane - Left Side Behind Wall (Chest)",                                218, False),  # Item: 8x Lightning Marble [201Eh]
    ("Baaj: Underwater Hall - West Branch of Main Path (Chest)",                                    219, False),  # Item: 1x Hi-Potion [2001h]
    ("Blitzball Reward 1",                                                                          220, False),  # Item: 1x Hi-Potion [2001h]
    ("Blitzball Reward 2",                                                                          221, False),  # Item: 1x Dark Matter [2035h]
    ("Blitzball Reward 3",                                                                          222, False),  # Item: 1x Teleport Sphere [2062h]
    ("Blitzball Reward 4",                                                                          223, False),  # Item: 1x Three Stars [2045h]
    ("Blitzball Reward 5",                                                                          224, False),  # Item: 1x Luck Sphere [205Eh]
    ("Blitzball Reward 6",                                                                          225, False),  # Item: 1x Underdog's Secret [206Eh]
    ("Blitzball Reward 7",                                                                          226, False),  # Item: 1x Megalixir [2009h]
    ("Blitzball Reward 8",                                                                          227, False),  # Item: 1x Return Sphere [2060h]
    ("Blitzball Reward 9",                                                                          228, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("Blitzball Reward 10",                                                                         229, False),  # Item: 1x Mega Phoenix [2007h]
    ("Blitzball Reward 11",                                                                         230, False),  # Item: 1x Elixir [2008h]
    ("Blitzball Reward 12",                                                                         231, False),  # Item: 1x Mega-Potion [2003h]
    ("Blitzball Reward 13",                                                                         232, False),  # Item: 1x X-Potion [2002h]
    ("Blitzball Reward 14",                                                                         233, False),  # Item: 1x Ether [2004h]
    ("Blitzball Reward 15",                                                                         234, False),  # Item: 2x Remedy [200Fh]
    ("Blitzball Reward 16",                                                                         235, False),  # Item: 2x Phoenix Down [2006h]
    ("Blitzball Reward 17",                                                                         236, False),  # Item: 2x Hi-Potion [2001h]
    ("Blitzball Reward 18",                                                                         237, False),  # Item: 5x Power Sphere [2046h]
    ("Blitzball Reward 19",                                                                         238, False),  # Item: 5x Mana Sphere [2047h]
    ("Blitzball Reward 20",                                                                         239, False),  # Item: 5x Speed Sphere [2048h]
    ("Blitzball Reward 21",                                                                         240, False),  # Item: 5x Ability Sphere [2049h]
    ("Blitzball Reward 22",                                                                         241, False),  # Item: 1x Echo Screen [200Dh]
    ("Blitzball Reward 23",                                                                         242, False),  # Item: 1x Eye Drops [200Ch]
    ("Blitzball Reward 24",                                                                         243, False),  # Item: 1x Antidote [200Ah]
    ("Blitzball: Obtain The Jupiter Sigil League Prize (Event)",                                    244, False),  # Key Item: Jupiter Sigil [A02Dh]
    ("Blitzball Reward 25",                                                                         245, False),  # Item: 1x Elixir [2008h]
    ("Blitzball Reward 26",                                                                         246, False),  # Item: 1x X-Potion [2002h]
    ("Blitzball Reward 27",                                                                         247, False),  # Item: 1x Remedy [200Fh]
    ("Blitzball Reward 28",                                                                         248, False),  # Item: 1x Hi-Potion [2001h]
    ("Blitzball Reward 29",                                                                         249, False),  # Item: 4x Echo Screen [200Dh]
    ("Blitzball Reward 30",                                                                         250, False),  # Item: 4x Eye Drops [200Ch]
    ("Blitzball Reward 31",                                                                         251, False),  # Item: 4x Antidote [200Ah]
    ("Blitzball Reward 32",                                                                         252, False),  # Item: 4x Soft [200Bh]
    ("Blitzball Reward 33",                                                                         253, False),  # Item: 2x Potion [2000h]
    ("Blitzball Reward 34",                                                                         254, False),  # Item: 2x Phoenix Down [2006h]
    ("Blitzball Reward 35",                                                                         255, False),  # Item: 1x Potion [2000h]
    ("Blitzball Reward 36",                                                                         256, False),  # Item: 1x Phoenix Down [2006h]
    ("Blitzball Reward 37",                                                                         257, False),  # Item: 2x Hi-Potion [2001h]
    ("Blitzball Reward 38",                                                                         258, False),  # Item: 1x Hi-Potion [2001h]
    ("Blitzball Reward 39",                                                                         259, False),  # Item: 1x Potion [2000h]
    ("Blitzball Reward 40",                                                                         260, False),  # Item: 1x Phoenix Down [2006h]
    ("Blitzball Reward 41",                                                                         261, False),  # Item: 1x Return Sphere [2060h]
    ("Blitzball Reward 42",                                                                         262, False),  # Item: 1x Rename Card [2065h]
    ("Blitzball Reward 43",                                                                         263, False),  # Item: 1x Ether [2004h]
    ("Blitzball Reward 44",                                                                         264, False),  # Item: 1x X-Potion [2002h]
    ("Blitzball Reward 45",                                                                         265, False),  # Item: 1x Mega-Potion [2003h]
    ("Blitzball Reward 46",                                                                         266, False),  # Item: 2x Remedy [200Fh]
    ("Zanarkand: Dome Beyond - Chest After Taking Left/Right in Yunalesca Arena (Chest)",           267, False),  # Key Item: Sun Crest [A023h]
    ("Besaid: Beach - East Alcove (Chest)",                                                         268, False),  # Key Item: Moon Crest [A025h]
    ("Mi'ihen: Oldroad, South - South End (Chest)",                                                 269, False),  # Key Item: Mars Crest [A027h]
    ("Gagazet: Prominence - Hidden Between Left Pillars (Chest)",                                   270, False),  # Key Item: Saturn Crest [A02Ah]
    ("Luca: Stadium Locker Room - Inside Back Right Locker (Event)",                                271, False),  # Key Item: Jupiter Crest [A02Ch]
    ("Guadosalam: Farplane - West Side (Chest)",                                                    272, False),  # Key Item: Venus Crest [A02Eh]
    ("Bikanel: Desert, West - First Western Alcove, Sinkhole (Chest)",                              273, False),  # Key Item: Mercury Crest [A030h]
    ("Calm Lands: Catcher chocobo Minigame, Time Under 0.00 (Event)",                               274, False),  # Key Item: Sun Sigil [A024h]
    ("Calm Lands: Remiem Temple - Defeat All Aeons and Send Belgemine (Event)",                     275, False),  # Key Item: Moon Sigil [A026h]
    ("Monster Arena: Unlock Ten Arena Creations (Event)",                                           276, False),  # Key Item: Mars Sigil [A028h]
    ("Macalania Woods: Finish Butterfly Minigame (Event)",                                          277, False),  # Key Item: Saturn Sigil [A02Bh]
    ("Thunder Plains: Lightning Dodger - 200 Consecutive Dodges (Event)",                           278, False),  # Key Item: Venus Sigil [A02Fh]
    ("Bikanel: Desert - Complete Cactuar Village Quest (Event)",                                    279, False),  # Key Item: Mercury Sigil [A031h]
    ("Lake Macalania: Megalixir x2 (Butterfly Game after defeating Spherimorph)",                   280, False),  # Item: 2x Megalixir [2009h]
    ("Lake Macalania: Elixir x2 (Butterfly Game after defeating Spherimorph)",                      281, False),  # Item: 2x Elixir [2008h]
    ("Besaid: Beach - Datto (NPC)",                                                                 282, False),  # Item: 1x Hi-Potion [2001h]
    ("Besaid: Beach - Jassu (NPC)",                                                                 283, False),  # Item: 3x Potion [2000h]
    ("Besaid: Beach - Botta (NPC)",                                                                 284, False),  # Item: 2x Potion [2000h]
    ("Besaid: Beach - Keepa (NPC)",                                                                 285, False),  # Gil: 200 [02h]
    ("Besaid: Beach, Dock - Boy (NPC)",                                                             286, False),  # Item: 1x Remedy [200Fh]
    ("Besaid: Beach, Dock - Monk (NPC)",                                                            287, False),  # Gear: buki_get #62 [3Eh] { Yuna [01h], Armor {HP +10% [8073h]} }
    ("Besaid: Beach, Dock - Woman (NPC)",                                                           288, False),  # Item: 3x Phoenix Down [2006h]
    ("Besaid: Beach, Dock - Shirtless Man (NPC)",                                                   289, False),  # Gil: 400 [04h]
    ("Besaid: Beach, Dock - Green Shirt (NPC)",                                                     290, False),  # Item: 1x Ether [2004h]
    ("Kilika: Woods - Luzzu Before Beating Lord Ochu (NPC)",                                        291, False),  # Item: 4x Antidote [200Ah]
    ("Kilika: Woods - Luzzu After Beating Lord Ochu (NPC)",                                         292, False),  # Item: 1x Elixir [2008h]
    ("Kilika: Woods - Crusader Commander West of Lord Ochu (NPC)",                                  293, False),  # Item: 1x Remedy [200Fh]
    #("Kilika: Phoenix Down x3 (Guard NPC, fight Ochu from west and run?)",                         294, False),  # Item: 3x Phoenix Down [2006h]
    ("Kilika: Woods - Crusader Commander North of Lord Ochu (NPC)",                                 295, False),  # Item: 1x Hi-Potion [2001h]
    ("Al Bhed Ship: Deck - Yellow Al Bhed, on Left (NPC)",                                          296, False),  # Item: 3x Potion [2000h]
    ("Djose: Highroad - South End, Silver/Purple Armor (NPC)",                                      297, False),  # Gear: buki_get #63 [3Fh] { Tidus [00h], Weapon {Strength +3% [8062h], Empty, Empty, Empty} }
    ("Djose: Highroad - South End, Purple Armor (NPC)",                                             298, False),  # Gear: buki_get #64 [40h] { Yuna [01h], Armor {Stoneproof [8038h], Empty} }
    ("Djose: Highroad - Monk Pacing Between Crusaders (NPC)",                                       299, False),  # Item: 1x Hi-Potion [2001h]
    ("Djose: Highroad - Midway, Yellow Armor (NPC)",                                                300, False),  # Item: 1x Ether [2004h]
    ("Djose: Highroad - North End, Purple Armor (NPC)",                                             301, False),  # Item: 1x Mega-Potion [2003h]
    ("Djose: Pilgrimage Road - North End, Purple Armor (NPC)",                                      302, False),  # Gear: buki_get #65 [41h] { Kimahri [03h], Weapon {Magic +20% [8069h], Empty} }
    ("Djose: Pilgrimage Road - South End, Silver/Purple Armor (NPC)",                               303, False),  # Item: 10x Potion [2000h]
    ("Djose: Pilgrimage Road - Monk Pacing Along Bridge (NPC)",                                     304, False),  # Item: 2x Hi-Potion [2001h]
    ("Lake Macalania: Road - Linna, at Bottom of Stairs (NPC)",                                     305, False),  # Gil: 400 [04h]
    ("Lake Macalania: Monks' Chamber - Purple Monk (NPC)",                                          306, False),  # Item: 1x Elixir [2008h]
    ("Lake Macalania: Monks' Chamber - Brown Monk (NPC)",                                           307, False),  # Item: 1x Ether [2004h]
    ("Lake Macalania: Nuns' Chamber - Yellow Nun (NPC)",                                            308, False),  # Item: 2x Hi-Potion [2001h]
    ("Mi'ihen: South End - Blue/White Man, Looping North to South (NPC)",                           309, False),  # Gear: buki_get #66 [42h] { Kimahri [03h], Weapon {Piercing [800Bh], Sensor [8000h], Strength +10% [8064h]} }
    ("Mi'ihen: South End - Red Skirt Girl, Pacing Between Maechen and Ruins (NPC)",                 310, False),  # Item: 2x Antidote [200Ah]
    ("Mi'ihen: South End - Yellow Man, Looping South to North (NPC)",                               311, False),  # Item: 1x Hi-Potion [2001h]
    ("Mi'ihen: South - Boy Before Kicking the Blitzball (NPC)",                                     312, False),  # Item: 3x Soft [200Bh]
    ("Mi'ihen: South - Crusader Running East then West (NPC)",                                      313, False),  # Gear: buki_get #67 [43h] { Yuna [01h], Armor {HP +10% [8073h], Fire Ward [801Fh]} }
    ("Mi'ihen: Central - Purple Crusader Freaking Out, West Side (NPC)",                            314, False),  # Item: 1x Ether [2004h]
    ("Mi'ihen: Central - Woman on North End, West Side (NPC)",                                      315, False),  # Item: 1x Hi-Potion [2001h]
    ("Mi'ihen: Central - Male Yellow Crusader, Looping North to South (NPC)",                       316, False),  # Gil: 600 [06h]
    ("Mi'ihen: Central - Purple Crusader, Looping South to North (NPC)",                            317, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("Mi'ihen: Central - Female Yellow Crusader, Looping North to South (NPC)",                     318, False),  # Item: 4x Antidote [200Ah]
    ("MRR: First Screen - Right Near Southern Exit (NPC)",                                          319, False),  # Gear: buki_get #68 [44h] { Lulu [05h], Armor {HP +20% [8074h], Empty} }
    ("MRR: First Screen - Pacing Between Blue Commander and North Exit (NPC)",                      320, False),  # Item: 2x Phoenix Down [2006h]
    ("MRR: First Screen - Left Near Southern Exit (NPC)",                                           321, False),  # Item: 1x Remedy [200Fh]
    ("MRR: First Screen - Blue Commander on Left Side (NPC)",                                       322, False),  # Item: 1x Hi-Potion [2001h]
    ("MRR: First Screen - Pacing Between Blue Commander and South Exit (NPC)",                      323, False),  # Item: 1x Ether [2004h]
    ("MRR: Valley - Woman Before First Elevator (NPC)",                                             324, False),  # Item: 1x Hi-Potion [2001h]
    ("MRR: Valley - North Alcove After First Elevator (NPC)",                                       325, False),  # Item: 10x Potion [2000h]
    ("MRR: Precipice - Pacing Between North Elevator and East Ridge (NPC)",                         326, False),  # Gil: 400 [04h]
    ("MRR: Precipice - Near South Elevator (NPC)",                                                  327, False),  # Item: 1x X-Potion [2002h]
    ("MRR: Precipice - Near Large Elevator (NPC)",                                                  328, False),  # Item: 1x Mega-Potion [2003h]
    ("Omega Ruins: 12th Chest Reward for Minigame (Chest)",                                         329, False),  # Item: 99x Warp Sphere [2063h]
    ("Omega Ruins: Press Both Glyphs, Then Take Narrow Central Path (Chest)",                       330, False),  # Item: 1x Teleport Sphere [2062h]
    ("Omega Ruins: Zone After Ultima, West Path (Chest)",                                           331, False),  # Item: 1x Friend Sphere [2061h]
    ("Omega Ruins: Omega Boss Arena (Chest)",                                                       332, False),  # Item: 1x Magic Sphere [2059h]
    #("Treasure 333 (Old Entry?)",                                                                  333, False),  # Key Item: Blossom Crown [A032h]
    ("Calm Lands: Remiem Temple - Defeat Bahamut (Boss)",                                           334, False),  # Key Item: Flower Scepter [A033h]
    #("Treasure 335 (Trashed)",                                                                     335, False),  # Item: 1x Potion [2000h]
    ("S.S. Liki: Clasko, After Breeder Encouragement in Macalania (Event)",                         336, False),  # Item: 1x Friend Sphere [2061h] # Talk to Clasko before Crawler and make sure to have him become a Chocobo Breeder
    ("Calm Lands: Wobbly Chocobo Minigame (Event)",                                                 337, False),  # Item: 1x Elixir [2008h]
    ("Calm Lands: Dodger Chocobo Minigame (Event)",                                                 338, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("Calm Lands: Hyper Dodger Chocobo Minigame (Event)",                                           339, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    ("Calm Lands: Catcher Chocobo Minigame (Event)",                                                340, False),  # Item: 1x Lv. 3 Key Sphere [2053h]
    #("Treasure 341 (Trashed)",                                                                     341, False),  # Item: 1x X-Potion [2002h]
    #("Treasure 342 (Trashed)",                                                                     342, False),  # Item: 1x Mega-Potion [2003h]
    #("Treasure 343 (Trashed)",                                                                     343, False),  # Item: 1x Ether [2004h]
    #("Treasure 344 (Trashed)",                                                                     344, False),  # Item: 1x Turbo Ether [2005h]
    ("Thunder Plains: Agency Front (Ground Item)",                                                  345, False),  # Gear: buki_get #69 [45h] { Tidus [00h], Armor {Lightningproof [8028h], Empty} }
    ("Bikanel: Oasis - In Southwest Corner of Water (Chest)",                                       346, False),  # Item: 4x Remedy [200Fh]
    ("Bikanel: Desert, East - Near First Tent, Right (Chest)",                                      347, False),  # Item: 2x Ether [2004h]
    ("Bikanel: Desert, East - Western Alcove, Near Structure (Chest)",                              348, False),  # Item: 4x Hi-Potion [2001h]
    ("Bikanel: Desert, Central - Far West Corner (Chest)",                                          349, False),  # Item: 2x Mega-Potion [2003h]
    ("Bikanel: Desert, Central - Rock Ridge Southwest of Save Sphere (Chest)",                      350, False),  # Item: 2x X-Potion [2002h]
    ("Bikanel: Desert, Central - Structure Southeast of Save Sphere (Chest)",                       351, False),  # Item: 4x Hi-Potion [2001h]
    ("Bikanel: Desert, Central - Southwest Corner of Northwest Zone (Chest)",                       352, False),  # Item: 1x Elixir [2008h]
    ("Bikanel: Desert, Central - Central Structure of Northwest Zone, Bottom (Chest)",              353, False),  # Gil: 10000 [64h]
    ("Bikanel: Desert, Central - Central Structure of Northwest Zone, Top (Chest)",                 354, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    ("Bikanel: Desert, West - First Western Alcove, Between Rocks (Chest)",                         355, False),  # Item: 8x Hi-Potion [2001h]
    ("Bikanel: Desert, West - Second Western Alcove, Hidden Behind Rock (Chest)",                   356, False),  # Item: 3x Mega-Potion [2003h]
    ("Bikanel: Desert, West - Second Western Alcove, North Side (Chest)",                           357, False),  # Item: 2x X-Potion [2002h]
    ("Bikanel: Desert, West - Left Sinkhole on Main Path (Chest)",                                  358, False),  # Item: 3x Megalixir [2009h]
    ("Bikanel: Desert, West - Right Sinkhole on  Main Path (Chest)",                                359, False),  # Item: 2x Teleport Sphere [2062h]
    ("Home: Main Corridor - North Hall, Left (Chest)",                                              360, False),  # Item: 6x Al Bhed Potion [2014h]
    ("Home: Main Corridor - Bottom of South Stairs, Hidden Behind Left Smoke (Chest)",              361, False),  # Item: 4x Al Bhed Potion [2014h]
    ("Home: Outside Summoner's Sanctum - Right (Chest)",                                            362, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    ("Home: Outside Summoner's Sanctum - Left (Chest)",                                             363, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    ("Home: Environment Controls (Chest)",                                                          364, False),  # Gil: 10000 [64h]
    ("S.S. Winno: Deck - Top Floor, Counting Gulls (NPC)",                                          365, False),  # Gear: buki_get #70 [46h] { Wakka [04h], Weapon {Magic +20% [8069h], Magic +10% [8068h], Magic +5% [8067h], Magic +3% [8066h]} }
    ("Mi'ihen: South End - Fight Belgemine (Lose) (Event)",                                         366, False),  # Gear: buki_get #71 [47h] { Yuna [01h], Armor {HP +10% [8073h], Empty} }
    ("Home: Keyakku, on Ground (NPC)",                                                              367, False),  # Item: 2x Hi-Potion [2001h]
    #("MRR: Valley - Code VICTORIOUS",                                                              368, False),  # Gear: buki_get #72 [48h] { Rikku [06h], Armor {Lightningproof [8028h], Fireproof [8020h], Iceproof [8024h], Empty} } UNCOMMENT WHEN CODES ARE INCORPORATED
    #("Besaid: Besaid Ruins - Code MURASAME",                                                       369, False),  # Gear: buki_get #73 [49h] { Auron [02h], Weapon {Piercing [800Bh], One MP Cost [800Dh], Empty, Empty} } UNCOMMENT WHEN CODES ARE INCORPORATED
    ("Calm Lands: Speed Sphere x30 (Lose Aeon Fight)",                                              370, False),  # Item: 30x Speed Sphere [2048h]
    ("Defeat Belgemine Twice",                                                                      371, False),  # Key Item: Aeon's Soul [A01Fh]
    ("Moonflow: South Bank Road - Fight Belgemine (Win) (Event) (1)",                               372, False),  # Item: 2x Dragon Scale [2021h]
    ("Moonflow: South Bank Road - Fight Belgemine (Lose) (Event) (1)",                              373, False),  # Item: 6x Smoke Bomb [2028h]
    ("Defeat Belgemine Once",                                                                       374, False),  # Key Item: Summoner's Soul [A01Eh]
    ("Airship: Cabin - Before Evrae, Yellow Al Bhed on Left (NPC)",                                 375, False),  # Item: 4x Al Bhed Potion [2014h]
    ("Moonflow: South Bank Road - Right of Shelinda (Chest)",                                       376, False),  # Item: 3x Lv. 1 Key Sphere [2051h]
    ("Moonflow: South Bank Road - East Alcove as Path Bends North (Chest)",                         377, False),  # Item: 3x Lv. 1 Key Sphere [2051h]
    ("Moonflow: South Bank Road - West Alcove in Forest Past Belgemine (Chest)",                    378, False),  # Item: 1x Magic Def Sphere [205Ah]
    ("Calm Lands: Remiem Temple - Defeat Valefor (Boss)",                                           379, False),  # Item: 4x Lightning Gem [201Fh]
    ("Calm Lands: Remiem Temple - Valefor Post First Fight (Boss)",                                 380, False),  # Item: 4x Power Sphere [2046h]
    ("Calm Lands: Remiem Temple - Defeat Ifrit (Boss)",                                             381, False),  # Item: 30x X-Potion [2002h]
    ("Calm Lands: Remiem Temple - Ifrit Post First Fight (Boss)",                                   382, False),  # Item: 5x Mana Sphere [2047h]
    ("Calm Lands: Remiem Temple - Defeat Ixion (Boss)",                                             383, False),  # Item: 10x Chocobo Feather [2036h]
    ("Calm Lands: Remiem Temple - Ixion Post First Fight (Boss)",                                   384, False),  # Item: 8x Power Sphere [2046h]
    ("Calm Lands: Remiem Temple - Defeat Shiva (Boss)",                                             385, False),  # Item: 60x Mega-Potion [2003h]
    ("Calm Lands: Remiem Temple - Shiva Post First Fight (Boss)",                                   386, False),  # Item: 6x Star Curtain [203Ah]
    ("Calm Lands: Remiem Temple - Bahamut Post First Fight (Boss)",                                 387, False),  # Item: 8x Mana Sphere [2047h]
    ("Calm Lands: Remiem Temple - Defeat Yojimbo (Boss)",                                           388, False),  # Item: 8x Shadow Gem [2029h]
    ("Calm Lands: Remiem Temple - Yojimbo Post First Fight (Boss)",                                 389, False),  # Item: 10x Power Sphere [2046h]
    ("Calm Lands: Remiem Temple - Defeat Anima (Boss)",                                             390, False),  # Item: 60x Stamina Spring [203Dh]
    ("Calm Lands: Remiem Temple - Anima Post First Fight (Boss)",                                   391, False),  # Item: 10x Mana Sphere [2047h]
    ("Calm Lands: Remiem Temple - Defeat Magus Sisters (Boss)",                                     392, False),  # Item: 40x Shining Gem [202Ah]
    ("Calm Lands: Remiem Temple - Magus Sisters Post First Fight (Boss)",                           393, False),  # Item: 12x Power Sphere [2046h]
    ("Lake Macalania: Teleport Sphere x1 (Butterfly Game after Airship)",                           394, False),  # Item: 1x Teleport Sphere [2062h]
    ("Home: Living Quarters, East of Main Corridor - Quiz (Chest)",                                 395, False),  # Item: 1x Skill Sphere [204Dh]
    ("Home: Living Quarters, East of Main Corridor - Password (Chest)",                             396, False),  # Item: 1x Special Sphere [204Ch]
    ("Home: Living Quarters, South of Main Corridor - Vocabulary Test (Chest)",                     397, False),  # Item: 1x Friend Sphere [2061h]
    ("Home: Living Quarters, South of Main Corridor - What do I contain? (Chest)",                  398, False),  # Item: 1x Elixir [2008h]
    #("Treasure 399 (Trashed)",                                                                     399, False),  # Item: 1x Hi-Potion [2001h] 
    #("Treasure 400 (Trashed)",                                                                     400, False),  # Item: 1x Mega-Potion [2003h] 
    #("Treasure 401 (Trashed)",                                                                     401, False),  # Item: 1x Soft [200Bh] 
    #("Treasure 402 (Trashed)",                                                                     402, False),  # Item: 1x Potion [2000h]
    #("Treasure 403 (Trashed)",                                                                     403, False),  # Item: 1x Remedy [200Fh]
    #("Treasure 404 (Trashed)",                                                                     404, False),  # Item: 2x Potion [2000h]
    ("Airship: Collect All Primers, Talk to Rin (NPC)",                                             405, False),  # Item: 99x Underdog's Secret [206Eh]
    ("Besaid: Fayth Revisit - Northwest (Chest)",                                                   406, False),  # Item: 1x Wht Magic Sphere [204Eh]
    ("Besaid: Fayth Revisit - Northeast (Chest)",                                                   407, False),  # Item: 1x Elixir [2008h]
    ("Besaid: Fayth Revisit - Southwest (Chest)",                                                   408, False),  # Item: 1x Hi-Potion [2001h]
    ("Besaid: Fayth Revisit - Southeast (Chest)",                                                   409, False),  # Item: 2x Potion [2000h]
    #("S.S Liki: Potion (Yuna's suitcase)",                                                         410, False),  # Item: 1x Potion [2000h] # Definitely Yuna's Suitcase
    #("Treasure 411 (Trashed)",                                                                     411, False),  # Item: 1x Potion [2000h]
    #("Treasure 412 (Trashed)",                                                                     412, False),  # Item: 1x Potion [2000h]
    #("Treasure 413 (Trashed)",                                                                     413, False),  # Item: 1x Potion [2000h]
    #("Treasure 414 (Trashed)",                                                                     414, False),  # Item: 1x Potion [2000h]
    #("Treasure 415 (Trashed)",                                                                     415, False),  # Item: 1x Potion [2000h]
    #("Treasure 416 (Trashed)",                                                                     416, False),  # Item: 1x Potion [2000h]
    ("Calm Lands: 1st Chest in Chocobo Race",                                                       417, False),  # Item: 1x Elixir [2008h]
    ("Calm Lands: 2nd Chest in Chocobo Race",                                                       418, False),  # Item: 1x Megalixir [2009h]
    ("Calm Lands: 3rd Chest in Chocobo Race",                                                       419, False),  # Item: 60x Three Stars [2045h]
    ("Calm Lands: 4th Chest in Chocobo Race",                                                       420, False),  # Item: 30x Pendulum [2069h]
    ("Calm Lands: 5th Chest in Chocobo Race",                                                       421, False),  # Item: 30x Wings to Discovery [206Ch]
    #("Treasure 422",                                                                               422, False),  # Item: 1x Potion [2000h]
    ("Mi'ihen: Agency - Green NPC After Resting (Event)",                                           423, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("Monster Arena: Area Conquest - Capture 1 of Each Besaid Fiend (NPC)",                         424, False),  # Item: 99x Stamina Tonic [2043h]
    ("Monster Arena: Area Conquest - Capture 1 of Each Kilika Fiend (NPC)",                         425, False),  # Item: 99x Poison Fang [202Dh]
    ("Monster Arena: Area Conquest - Capture 1 of Each Mi'ihen Highroad Fiend (NPC)",               426, False),  # Item: 99x Soul Spring [203Eh]
    ("Monster Arena: Area Conquest - Capture 1 of Each Mushroom Rock Road Fiend (NPC)",             427, False),  # Item: 99x Candle of Life [2030h]
    ("Monster Arena: Area Conquest - Capture 1 of Each Djose Road Fiend (NPC)",                     428, False),  # Item: 99x Petrify Grenade [2031h]
    ("Monster Arena: Area Conquest - Capture 1 of Each Thunder Plains Fiend (NPC)",                 429, False),  # Item: 99x Chocobo Wing [2037h]
    ("Monster Arena: Area Conquest - Capture 1 of Each Macalania Fiend (NPC)",                      430, False),  # Item: 60x Shining Gem [202Ah]
    ("Monster Arena: Area Conquest - Capture 1 of Each Bikanel Fiend (NPC)",                        431, False),  # Item: 99x Shadow Gem [2029h]
    ("Monster Arena: Area Conquest - Capture 1 of Each Calm Lands Fiend (NPC)",                     432, False),  # Item: 60x Farplane Wind [2033h]
    ("Monster Arena: Area Conquest - Capture 1 of Each CotSF Fiend (NPC)",                          433, False),  # Item: 40x Silver Hourglass [202Eh]
    ("Monster Arena: Area Conquest - Capture 1 of Each Mt. Gagazet Fiend (NPC)",                    434, False),  # Key Item: Blossom Crown [A032h]
    ("Monster Arena: Area Conquest - Capture 1 of Each Inside Sin Fiend (NPC)",                     435, False),  # Item: 99x Lunar Curtain [2038h]
    ("Monster Arena: Area Conquest - Capture 1 of Each Omega Ruins Fiend (NPC)",                    436, False),  # Item: 60x Designer Wallet [2034h]
    ("Monster Arena: Species Conquest - Capture 3 of Each Wolf Fiend (NPC)",                        437, False),  # Item: 99x Chocobo Feather [2036h]
    ("Monster Arena: Species Conquest - Capture 3 of Each Reptile Fiend (NPC)",                     438, False),  # Item: 99x Stamina Spring [203Dh]
    ("Monster Arena: Species Conquest - Capture 5 of Each Bird Fiend (NPC)",                        439, False),  # Item: 99x Mega Phoenix [2007h]
    ("Monster Arena: Species Conquest - Capture 4 of Each Wasp Fiend (NPC)",                        440, False),  # Item: 60x Mana Tonic [2044h]
    ("Monster Arena: Species Conquest - Capture 4 of Each Imp Fiend (NPC)",                         441, False),  # Item: 99x Mana Spring [203Ch]
    ("Monster Arena: Species Conquest - Capture 4 of Each Eye Fiend (NPC)",                         442, False),  # Item: 60x Stamina Tablet [2040h]
    ("Monster Arena: Species Conquest - Capture 3 of Each Flan Fiend (NPC)",                        443, False),  # Item: 60x Twin Stars [2042h]
    ("Monster Arena: Species Conquest - Capture 3 of Each Elemental Fiend (NPC)",                   444, False),  # Item: 99x Star Curtain [203Ah]
    ("Monster Arena: Species Conquest - Capture 3 of Each Helm Fiend (NPC)",                        445, False),  # Item: 99x Gold Hourglass [202Fh]
    ("Monster Arena: Species Conquest - Capture 4 of Each Drake Fiend (NPC)",                       446, False),  # Item: 99x Purifying Salt [203Fh]
    ("Monster Arena: Species Conquest - Capture 5 of Each Fungus Fiend (NPC)",                      447, False),  # Item: 99x Healing Spring [203Bh]
    ("Monster Arena: Species Conquest - Capture 5 of Each Bomb Fiend (NPC)",                        448, False),  # Item: 60x Turbo Ether [2005h]
    ("Monster Arena: Species Conquest - Capture 5 of Each Ruminant Fiend (NPC)",                    449, False),  # Item: 99x Light Curtain [2039h]
    ("Monster Arena: Species Conquest - Capture 10 of Each Iron Giant Fiend (NPC)",                 450, False),  # Item: 60x Mana Tablet [2041h]
    ("Monster Arena: Original Creation - Complete 2 Area Conquests (NPC)",                          451, False),  # Item: 60x Three Stars [2045h]
    ("Monster Arena: Original Creation - Complete 2 Species Conquests (NPC)",                       452, False),  # Item: 60x Supreme Gem [202Ch]
    ("Monster Arena: Original Creation - Complete 6 Area Conquests (NPC)",                          453, False),  # Item: 99x Door to Tomorrow [206Bh]
    ("Monster Arena: Original Creation - Complete 6 Species Conquests (NPC)",                       454, False),  # Item: 99x Gambler's Spirit [206Dh]
    ("Monster Arena: Original Creation - Capture 1 of Each Fiend (NPC)",                            455, False),  # Item: 99x Winning Formula [206Fh]
    ("Monster Arena: Original Creation - Capture 5 of Each Fiend (NPC)",                            456, False),  # Item: 99x Dark Matter [2035h]
    ("Monster Arena: Original Creation - Capture 2 of Each Mt. Gagazet Underwater Fiend (NPC)",     457, False),  # Item: 30x Megalixir [2009h]
    ("Monster Arena: Original Creation - Capture 10 of Each Fiend (NPC)",                           458, False),  # Item: 10x Master Sphere [2050h]
    ("Besaid: Exit the Village (Event) (2)",                                                        459, False),  # Item: 1x Map [2064h]
    ("Lake Macalania: Fayth Revisit - PLACEHOLDER 1",                                               460, False),  # Item: 1x Magic Def Sphere [205Ah]
    ("Lake Macalania: Fayth Revisit - PLACEHOLDER 2",                                               461, False),  # Item: 1x Accuracy Sphere [205Dh]
    ("Lake Macalania: Fayth Revisit - PLACEHOLDER 3",                                               462, False),  # Item: 1x Magic Sphere [2059h]
    ("Djose: Fayth Revisit - West (Chest)",                                                         463, False),  # Item: 1x Agility Sphere [205Bh]
    ("Djose: Fayth Revisit - East (Chest)",                                                         464, False),  # Item: 1x Magic Def Sphere [205Ah]
    ("Djose: Fayth Revisit (Event)",                                                                465, False),  # Item: 1x Luck Sphere [205Eh]
    ("Calm Lands: Fayth - Revisit (Event)",                                                         466, False),  # Item: 1x Defense Sphere [2058h]
    ("Besaid: Fayth - Revisit (Event)",                                                             467, False),  # Item: 1x Evasion Sphere [205Ch]
    ("Calm Lands: Fayth - Revisit (Event)",                                                         468, False),  # Item: 1x Strength Sphere [2057h]
    ("Bikanel: Shadow Gem x2 (Robeya Minigame Chest)",                                              469, False),  # Item: 2x Shadow Gem [2029h]
    ("Bikanel: Shining Gem x1 (Robeya Minigame Chest)",                                             470, False),  # Item: 1x Shining Gem [202Ah]
    ("Bikanel: Blessed Gem x1 (Robeya Minigame Chest)",                                             471, False),  # Item: 1x Blessed Gem [202Bh]
    ("Bikanel: Potion x1 (Cactuar Sidequest Prize)",                                                472, False),  # Item: 1x Potion [2000h]
    ("Bikanel: Elixir x1 (Cactuar Sidequest Prize)",                                                473, False),  # Item: 1x Elixir [2008h]
    ("Bikanel: Megalixir x1 (Cactuar Sidequest Prize)",                                             474, False),  # Item: 1x Megalixir [2009h]
    ("Bikanel: Friend Sphere x1 (Cactuar Sidequest Prize)",                                         475, False),  # Item: 1x Friend Sphere [2061h]
    ("Kilika: Fayth Revisit - Northwest (Chest)",                                                   476, False),  # Item: 1x Agility Sphere [205Bh]
    ("Kilika: Fayth Revisit - Northeast (Chest)",                                                   477, False),  # Item: 1x Defense Sphere [2058h]
    ("Kilika: Fayth Revisit (Event)",                                                               478, False),  # Item: 1x Luck Sphere [205Eh]
    ("Kilika: Fayth Revisit - Southeast (Chest)",                                                   479, False),  # Item: 1x Accuracy Sphere [205Dh]
    ("Besaid: Besaid Falls - X31 Y75, Dragoon Lance",                                               480, False),  # Gear: buki_get #75 [4Bh] { Kimahri [03h], Weapon {Magic Counter [8005h], Evade & Counter [8004h], Empty, Empty} }
    ("Mi'ihen Highroad: Mi'ihen Ruins - X35 Y57 Sonar",                                             481, False),  # Gear: buki_get #76 [4Ch] { Rikku [06h], Weapon {Initiative [8002h], Poisonstrike [803Ah], Empty} }
    ("MRR: Battle Site - X41 Y57 Phantom Bangle",                                                   482, False),  # Gear: buki_get #77 [4Dh] { Lulu [05h], Armor {Ice Eater [8025h], Fire Eater [8021h], !Water Eater [802Dh]} }
    ("Bikanel: Sanubia Sands - X15 Y42 Ascalon",                                                    483, False),  # Gear: buki_get #78 [4Eh] { Tidus [00h], Weapon {Double AP [8012h]} }
    ("Djose: Trial - Destruction Sphere (Chest)",                                                   484, False),  # Item: 1x Magic Sphere [2059h]
    ("Lake Macalania: Cloister - Destruction Sphere (Chest)",                                       485, False),  # Item: 1x Luck Sphere [205Eh]
    ("Inside Sin: Prism Ball (Point of No Return)",                                                 486, False),  # Gear: buki_get #79 [4Fh] { Wakka [04h], Weapon {Magic Counter [8005h], Empty} }
    ("Inside Sin: Stillblade (Point of No Return)",                                                 487, False),  # Gear: buki_get #80 [50h] { Auron [02h], Weapon {Silencestrike [8042h], Stonestrike [8036h], Empty} }
    ("Inside Sin: Skill Sphere x1 (Point of No Return)",                                            488, False),  # Item: 1x Skill Sphere [204Dh]
    ("Inside Sin: Mage's Staff (Point of No Return)",                                               489, False),  # Gear: buki_get #81 [51h] { Yuna [01h], Weapon {Magic +10% [8068h], Magic +5% [8067h], Magic +3% [8066h], Empty} }
    ("Inside Sin: Knight Lance (Point of No Return)",                                               490, False),  # Gear: buki_get #82 [52h] { Kimahri [03h], Weapon {Strength +10% [8064h], Strength +5% [8063h], Strength +3% [8062h], Empty} }
    ("Inside Sin: Wht Magic Sphere x1 (Point of No Return)",                                        491, False),  # Item: 1x Wht Magic Sphere [204Eh]
    ("Inside Sin: Infinity (Point of No Return)",                                                   492, False),  # Gear: buki_get #83 [53h] { Rikku [06h], Weapon {One MP Cost [800Dh], Sensor [8000h]} }
    ("Inside Sin: Wicked Cait Sith (Point of No Return)",                                           493, False),  # Gear: buki_get #84 [54h] { Lulu [05h], Weapon {Deathstrike [802Eh], Empty, Empty, Empty} }
    ("Inside Sin: Attribute Sphere x1 (Point of No Return)",                                        494, False),  # Item: 1x Attribute Sphere [204Bh]
    ("Inside Sin: Hrunting (Point of No Return)",                                                   495, False),  # Gear: buki_get #85 [55h] { Tidus [00h], Weapon {SOS Overdrive [8010h]} }
    ("Monster Arena: Defeat Nemesis",                                                               496, False),  # Key Item: Mark of Conquest [A029h]
    ("Luca: Win the Story Blitzball Tournament (Event)",                                            497, False),  # Item: 1x Strength Sphere [2057h]
]]

FFXCaptureLocations: List[FFXLocationData] = [ FFXLocationData(location[1]+CaptureOffset, *location) for location in [
    ("Fiend Capture: Raldo",            0, False),
    ("Fiend Capture: Bunyip",           1, False),
    ("Fiend Capture: Murussu",          2, False),
    ("Fiend Capture: Mafdet",           3, False),
    ("Fiend Capture: Shred",            4, False),
    ("Fiend Capture: Gandarewa",        5, False),
    ("Fiend Capture: Aerouge",          6, False),
    ("Fiend Capture: Imp",              7, False),
    ("Fiend Capture: Dingo",            8, False),
    ("Fiend Capture: Mi'ihen Fang",     9, False),
    ("Fiend Capture: Garm",             10, False),
    ("Fiend Capture: Snow Wolf",        11, False),
    ("Fiend Capture: Sand Wolf",        12, False),
    ("Fiend Capture: Skoll",            13, False),
    ("Fiend Capture: Bandersnatch",     14, False),
    ("Fiend Capture: Water Flan",       15, False),
    ("Fiend Capture: Thunder Flan",     16, False),
    ("Fiend Capture: Snow Flan",        17, False),
    ("Fiend Capture: Ice Flan",         18, False),
    ("Fiend Capture: Flame Flan",       19, False),
    ("Fiend Capture: Dark Flan",        20, False),
    ("Fiend Capture: Dinonix",          21, False),
    ("Fiend Capture: Ipiria",           22, False),
    ("Fiend Capture: Raptor",           23, False),
    ("Fiend Capture: Melusine",         24, False),
    ("Fiend Capture: Iguion",           25, False),
    ("Fiend Capture: Yowie",            26, False),
    ("Fiend Capture: Condor",           27, False),
    ("Fiend Capture: Simurgh",          28, False),
    ("Fiend Capture: Alcyone",          29, False),
    ("Fiend Capture: Killer Bee",       30, False),
    ("Fiend Capture: Bite Bug",         31, False),
    ("Fiend Capture: Wasp",             32, False),
    ("Fiend Capture: Nebiros",          33, False),
    ("Fiend Capture: Floating Eye",     34, False),
    ("Fiend Capture: Buer",             35, False),
    ("Fiend Capture: Evil Eye",         36, False),
    ("Fiend Capture: Ahriman",          37, False),
    ("Fiend Capture: Ragora",           38, False),
    ("Fiend Capture: Grat",             39, False),
    ("Fiend Capture: Garuda",           40, False),
    ("Fiend Capture: Zu",               41, False),
    ("Fiend Capture: Sand Worm",        42, False),
    # ("Unused Arena Index",            43, False),
    ("Fiend Capture: Ghost",            44, False),
    ("Fiend Capture: Achelous",         45, False),
    ("Fiend Capture: Maelspike",        46, False),
    ("Fiend Capture: Dual Horn",        47, False),
    ("Fiend Capture: Valaha",           48, False),
    ("Fiend Capture: Grendel",          49, False),
    ("Fiend Capture: Vouivre",          50, False),
    ("Fiend Capture: Lamashtu",         51, False),
    ("Fiend Capture: Kusariqqu",        52, False),
    ("Fiend Capture: Mushussu",         53, False),
    ("Fiend Capture: Nidhogg",          54, False),
    ("Fiend Capture: Malboro",          55, False),
    ("Fiend Capture: Great Malboro",    56, False),
    ("Fiend Capture: Ogre",             57, False),
    ("Fiend Capture: Bashura",          58, False),
    # ("Unused Arena Index",            59, False),
    ("Fiend Capture: Splasher",         60, False),
    ("Fiend Capture: Yellow Element",   61, False),
    ("Fiend Capture: White Element",    62, False),
    ("Fiend Capture: Red Element",      63, False),
    ("Fiend Capture: Gold Element",     64, False),
    ("Fiend Capture: Blue Element",     65, False),
    ("Fiend Capture: Dark Element",     66, False),
    ("Fiend Capture: Black Element",    67, False),
    ("Fiend Capture: Epaaj",            68, False),
    ("Fiend Capture: Behemoth",         69, False),
    ("Fiend Capture: Behemoth King",    70, False),
    ("Fiend Capture: Chimera",          71, False),
    ("Fiend Capture: Chimera Brain",    72, False),
    ("Fiend Capture: Coeurl",           73, False),
    ("Fiend Capture: Master Coeurl",    74, False),
    ("Fiend Capture: Demonolith",       75, False),
    ("Fiend Capture: Iron Giant",       76, False),
    ("Fiend Capture: Gemini (Sword)",   77, False),
    ("Fiend Capture: Gemini (Club)",    78, False),
    ("Fiend Capture: Basilisk",         79, False),
    ("Fiend Capture: Anacondaur",       80, False),
    ("Fiend Capture: Adamantoise",      81, False),
    ("Fiend Capture: Varuna",           82, False),
    ("Fiend Capture: Ochu",             83, False),
    ("Fiend Capture: Mandragora",       84, False),
    ("Fiend Capture: Bomb",             85, False),
    ("Fiend Capture: Grenade",          86, False),
    ("Fiend Capture: Qactuar",          87, False),
    ("Fiend Capture: Cactuar",          88, False),
    ("Fiend Capture: Larva",            89, False),
    ("Fiend Capture: Barbatos",         90, False),
    ("Fiend Capture: Funguar",          91, False),
    ("Fiend Capture: Thorn",            92, False),
    ("Fiend Capture: Exoray",           93, False),
    ("Fiend Capture: Xiphos",           94, False),
    ("Fiend Capture: Puroboros",        95, False),
    ("Fiend Capture: Spirit",           96, False),
    ("Fiend Capture: Wraith",           97, False),
    ("Fiend Capture: Tonberry",         98, False),
    ("Fiend Capture: Master Tonberry",  99, False),
    ("Fiend Capture: Zaurus",           100, False),
    ("Fiend Capture: Halma",            101, False),
    ("Fiend Capture: Floating Death",   102, False),
    ("Fiend Capture: Machea",           103, False),
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


allLocations = list(chain(FFXTreasureLocations,
                          FFXBossLocations,
                          FFXPartyMemberLocations,
                          FFXOverdriveLocations,
                          FFXOverdriveModeLocations,
                          FFXOtherLocations,
                          FFXRecruitLocations,
                          FFXCaptureLocations,
                          *FFXSphereGridLocations))

def create_location_label_to_id_map() -> Dict[str, int]:
    """
    Creates a map from location labels to their AP location id (address)
    """
    label_to_id_map: Dict[str, int] = {}
    for location in allLocations:
        label_to_id_map[location.name] = location.rom_address

    return label_to_id_map
