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
    "BAAJ: Defeat Klikk (Boss)"                      : ["bjyt04_01"],
    "ALBS: Defeat Tros (Boss)"                       : ["cdsp07_00"],
    "BSIL: Defeat Dark Valefor (Superboss)"          : ["bsil07_70"],
    "SSLI: Defeat Sin Fin (Boss)"                    : ["slik02_00"],
    "SSLI: Defeat Sinspawn Echuilles (Boss)"         : ["slik02_01"],
    "KILK: Woods - Defeat Lord Ochu (Boss)"          : ["klyt00_00"],
    "KILK: Defeat Sinspawn Geneaux (Boss)"           : ["klyt01_00"],
    "LUCA: Defeat Oblitzerator (Boss)"               : ["cdsp02_00"],
    "MIHN: Defeat Chocobo Eater (Boss)"              : ["mihn02_00"],
    "MUSH: Defeat Sinspawn Gui First Phase (Boss)"   : ["kino02_00"],
    "MUSH: Defeat Sinspawn Gui Second Phase (Boss)"  : ["kino03_10"],
    "MOON: Defeat Extractor (Boss)"                  : ["genk09_00"],
    "THPL: Defeat Dark Ixion (Superboss)"            : ["kami03_71"],
    "MCWO: Defeat Spherimorph (Boss)"                : ["mcfr03_00"],
    "MCLA: Defeat Crawler (Boss)"                    : ["maca02_00"],
    "MCLA: Defeat Seymour (Boss)"                    : ["mcyt06_00"],
    "MCLA: Defeat Wendigo (Boss)"                    : ["maca02_01"],
    "MCLA: Defeat Dark Shiva (Superboss)"            : ["mcyt00_70"],
    "BIKA: Defeat Dark Ifrit (Superboss)"            : ["bika03_70"],
    "AIRS: Defeat Evrae (Boss)"                      : ["hiku15_00"],
    "AIRS: Defeat Sin Left Fin (Boss)"               : ["ssbt00_00"],
    "AIRS: Defeat Sin Right Fin (Boss)"              : ["ssbt01_00"],
    "AIRS: Defeat Sin Core (Boss)"                   : ["ssbt02_00"],
    "AIRS: Defeat Overdrive Sin (Boss)"              : ["ssbt03_00"],
    "AIRS: Defeat Penance (Superboss)"               : ["hiku15_70"],
    "BEVL: Defeat Isaaru (Boss)"                     : ["bvyt09_12"], # Probably?
    "BEVL: Defeat Evrae Altana (Boss)"               : ["stbv00_10"],
    "BEVL: Defeat Seymour Natus (Boss)"              : ["stbv01_10"],
    "CALM: Defeat Defender X (Boss)"                 : ["nagi01_00"],
    "MOAR: Defeat Nemesis (Superboss)"               : ["zzzz02_76"],
    "COSF: Defeat Dark Yojimbo (Superboss)"          : ["nagi05_74"],
    "MTGZ: Defeat Biran and Yenke (Boss)"            : ["mtgz01_10"],
    "MTGZ: Defeat Seymour Flux (Boss)"               : ["mtgz02_00"],
    "MTGZ: Defeat Dark Anima (Superboss)"            : ["mtgz01_70"],
    "MTGC: Defeat Sanctuary Keeper (Boss)"           : ["mtgz08_00"],
    "ZNKD: Defeat Spectral Keeper (Boss)"            : ["dome02_00"],
    "ZNKD: Defeat Yunalesca (Boss)"                  : ["dome06_00"],
    "ZNKD: Defeat Dark Bahamut (Superboss)"          : ["dome06_70"],
    "SINS: Defeat Seymour Omnis (Boss)"              : ["sins03_00"],
    "SINS: Defeat Braska's Final Aeon (Boss)"        : ["sins06_00"],
    "SINS: Defeat Yuna's Aeons (Boss)"               : ["sins07_0x"],
    "SINS: Defeat Yu Yevon (Boss)"                   : ["sins07_10"],
    "OMGR: Defeat Ultima (Boss)"                     : ["omeg00_10"],
    "OMGR: Defeat Omega (Superboss)"                 : ["omeg01_10"],
    "MUSH: Defeat Dark Mindy (Superboss)"            : ["kino00_70", "kino01_70", "kino01_72", "kino05_71"],
    "MUSH: Defeat Dark Sandy (Superboss)"            : ["kino00_70", "kino01_70", "kino01_72", "kino05_70"],
    "MUSH: Defeat Dark Cindy (Superboss)"            : ["kino00_70", "kino01_70", "kino01_71"],
    "BAAJ: Defeat Geosgaeno (Boss)"                  : ["bjyt02_02"],
    "BIKA: Defeat Zu (Boss)"                         : ["bika00_10"],
}


FFXBossLocations: List[FFXLocationData] = [ FFXLocationData(location[1]+BossOffset, *location) for location in [
    ("BAAJ: Defeat Klikk (Boss)",                      0, False),
    ("ALBS: Defeat Tros (Boss)",                       1, False),
    ("BSIL: Defeat Dark Valefor (Superboss)",          2, False),
    ("SSLI: Defeat Sin Fin (Boss)",                    3, False),
    ("SSLI: Defeat Sinspawn Echuilles (Boss)",         4, False),
    ("KILK: Woods - Defeat Lord Ochu (Boss)",          5, False),
    ("KILK: Defeat Sinspawn Geneaux (Boss)",           6, False),
    ("LUCA: Defeat Oblitzerator (Boss)",               7, False),
    ("MIHN: Defeat Chocobo Eater (Boss)",              8, False),
    ("MUSH: Defeat Sinspawn Gui First Phase (Boss)",   9, False),
    ("MUSH: Defeat Sinspawn Gui Second Phase (Boss)", 10, False),
    #("MUSH: Defeat Dark Magus Sisters (Superboss)",  11, False),
    ("MOON: Defeat Extractor (Boss)",                 12, False),
    ("THPL: Defeat Dark Ixion (Superboss)",           13, False),
    ("MCWO: Defeat Spherimorph (Boss)",               14, False),
    ("MCLA: Defeat Crawler (Boss)",                   15, False),
    ("MCLA: Defeat Seymour (Boss)",                   16, False),
    ("MCLA: Defeat Wendigo (Boss)",                   17, False),
    ("MCLA: Defeat Dark Shiva (Superboss)",           18, False),
    ("BIKA: Defeat Dark Ifrit (Superboss)",           19, False),
    ("AIRS: Defeat Evrae (Boss)",                     20, False),
    ("AIRS: Defeat Sin Left Fin (Boss)",              21, False),
    ("AIRS: Defeat Sin Right Fin (Boss)",             22, False),
    ("AIRS: Defeat Sin Core (Boss)",                  23, False),
    ("AIRS: Defeat Overdrive Sin (Boss)",             24, False),
    # ("AIRS: Defeat Penance (Superboss)",            25, False),
    ("BEVL: Defeat Isaaru (Boss)",                    26, False),
    ("BEVL: Defeat Evrae Altana (Boss)",              27, False),
    ("BEVL: Defeat Seymour Natus (Boss)",             28, False),
    ("CALM: Defeat Defender X (Boss)",                29, False),
    ("MOAR: Defeat Nemesis (Superboss)",              30, False),
    ("COSF: Defeat Dark Yojimbo (Superboss)",         31, False),
    ("MTGZ: Defeat Biran and Yenke (Boss)",           32, False),
    ("MTGZ: Defeat Seymour Flux (Boss)",              33, False),
    ("MTGZ: Defeat Dark Anima (Superboss)",           34, False),
    ("MTGC: Defeat Sanctuary Keeper (Boss)",          35, False),
    ("ZNKD: Defeat Spectral Keeper (Boss)",           36, False),
    ("ZNKD: Defeat Yunalesca (Boss)",                 37, False),
    ("ZNKD: Defeat Dark Bahamut (Superboss)",         38, False),
    ("SINS: Defeat Seymour Omnis (Boss)",             39, False),
    #("SINS: Defeat Braska's Final Aeon (Boss)",      40, False),
    #("SINS: Defeat Yuna's Aeons (Boss)",             41, False),
    #("SINS: Defeat Yu Yevon (Boss)",                 42, False),
    ("OMGR: Defeat Ultima (Boss)",                    43, False),
    ("OMGR: Defeat Omega (Superboss)",                44, False),
    ("MUSH: Defeat Dark Mindy (Superboss)",           45, False),
    ("MUSH: Defeat Dark Sandy (Superboss)",           46, False),
    ("MUSH: Defeat Dark Cindy (Superboss)",           47, False),
    ("BAAJ: Defeat Geosgaeno (Boss)",                 48, False),
    ("MOAR: Defeat Stratoavis (Arena Boss)",          49, False),
    ("MOAR: Defeat Malboro Menace (Arena Boss)",      50, False),
    ("MOAR: Defeat Kottos (Arena Boss)",              51, False),
    ("MOAR: Defeat Coeurlregina (Arena Boss)",        52, False),
    ("MOAR: Defeat Jormungand (Arena Boss)",          53, False),
    ("MOAR: Defeat Cactuar King (Arena Boss)",        54, False),
    ("MOAR: Defeat Espada (Arena Boss)",              55, False),
    ("MOAR: Defeat Abyss Worm (Arena Boss)",          56, False),
    ("MOAR: Defeat Chimerageist (Arena Boss)",        57, False),
    ("MOAR: Defeat Don Tonberry (Arena Boss)",        58, False),
    ("MOAR: Defeat Catoblepas (Arena Boss)",          59, False),
    ("MOAR: Defeat Abaddon (Arena Boss)",             60, False),
    ("MOAR: Defeat Vorban (Arena Boss)",              61, False),
    ("MOAR: Defeat Fenrir (Arena Boss)",              62, False),
    ("MOAR: Defeat Ornitholestes (Arena Boss)",       63, False),
    ("MOAR: Defeat Pteryx (Arena Boss)",              64, False),
    ("MOAR: Defeat Hornet (Arena Boss)",              65, False),
    ("MOAR: Defeat Vidatu (Arena Boss)",              66, False),
    ("MOAR: Defeat One-Eye (Arena Boss)",             67, False),
    ("MOAR: Defeat Jumbo Flan (Arena Boss)",          68, False),
    ("MOAR: Defeat Nega Elemental (Arena Boss)",      69, False),
    ("MOAR: Defeat Tanket (Arena Boss)",              70, False),
    ("MOAR: Defeat Fafnir (Arena Boss)",              71, False),
    ("MOAR: Defeat Sleep Sprout (Arena Boss)",        72, False),
    ("MOAR: Defeat Bomb King (Arena Boss)",           73, False),
    ("MOAR: Defeat Juggernaut (Arena Boss)",          74, False),
    ("MOAR: Defeat Ironclad (Arena Boss)",            75, False),
    ("MOAR: Defeat Earth Eater (Superboss)",          76, False),
    ("MOAR: Defeat Greater Sphere (Superboss)",       77, False),
    ("MOAR: Defeat Catastrophe (Superboss)",          78, False),
    ("MOAR: Defeat Th'uban (Superboss)",              79, False),
    ("MOAR: Defeat Neslug (Superboss)",               80, False),
    ("MOAR: Defeat Ultima Buster (Superboss)",        81, False),
    ("MOAR: Defeat Shinryu (Superboss)",              82, False),
    ("MOAR: Defeat Nemesis (Superboss)",              83, False),
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
    ("BSIL: Village, House - Something Mangled and Slobbery from Dog (NPC)",   21, False), #Energy Blast
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

    ("ALBS: Deck & BIKA: Oasis (Primer)",                                         1, False), # Al Bhed Primer I
    ("BSIL: Village, Crusader Lodge - On Ground Near Counter (Primer)",           2, False), # Al Bhed Primer II
    ("SSLI: Power Room & BIKA: Oasis (Primer)",                                   3, False), # Al Bhed Primer III
    ("KILK: Tavern - On Counter (Primer)",                                        4, False), # Al Bhed Primer IV
    ("SSWI: Bridge & BIKA: Desert, East (Primer)",                                5, False), # Al Bhed Primer V
    ("LUCA: Stadium Basement B - Behind Isken (Primer)",                          6, False), # Al Bhed Primer VI
    ("LUCA: Theater Reception - Bottom of Stairs, Left Side (Primer)",            7, False), # Al Bhed Primer VII
    ("MIHN: Agency - Exit After Resting (Event) (2)",                             8, False), # Al Bhed Primer VIII
    ("MIHN: Newroad, North - Peak of South Bend Before Shelinda (Primer)",        9, False), # Al Bhed Primer IX
    ("MUSH: Precipice - End of Curved Path West of North Elevator (Primer)",     10, False), # Al Bhed Primer X
    ("DJOS: Highroad - South End, Behind Left Pillar (Primer)",                  11, False), # Al Bhed Primer XI
    ("MOON: North Wharf - Up Slope Right of Hypello (Primer)",                   12, False), # Al Bhed Primer XII
    ("GUAD: House - On Floor (Primer)",                                          13, False), # Al Bhed Primer XIII
    ("THPL: Agency & BIKA: Desert, East (Primer)",                               14, False), # Al Bhed Primer XIV
    ("MCWO: Lake Road - Near Southeast Exit (Primer)",                           15, False), # Al Bhed Primer XV
    ("MCLA: Agency Front - Left Side (Primer)",                                  16, False), # Al Bhed Primer XVI
    ("BIKA: Desert, Central - Northeast Structure of Northwest Zone (Primer)",   17, False), # Al Bhed Primer XVII
    ("BIKA: Desert, Central - Near Sign At Northeast Exit (Primer)",             18, False), # Al Bhed Primer XVIII
    ("HOME: Left of Entrance (Primer)",                                          19, False), # Al Bhed Primer XIX
    ("HOME: Living Quarters, South of Main Corridor - On Bed (Primer)",          20, False), # Al Bhed Primer XX
    ("HOME: Main Corridor - Northeast Corner (Primer)",                          21, False), # Al Bhed Primer XXI
    ("BEVL: Priests' Passage - Corner South of Save Point (Primer)",             22, False), # Al Bhed Primer XXII
    ("CALM: North - Northwest Corner (Primer)",                                  23, False), # Al Bhed Primer XXIII
    ("REMI: Northwest Corner (Primer)",                                          24, False), # Al Bhed Primer XXIV
    ("COSF: Dead End West of Third Intersection (Primer)",                       25, False), # Al Bhed Primer XXV
    ("OMGR: North Side of Four Chest Intersection (Primer)",                     26, False), # Al Bhed Primer XXVI
 
    #("MCWO: Spherimorph Jecht Sphere",                                          27, False),
    #("BSIL: Village - East of Temple (Jecht Sphere)",                           28, False),
    #("Jecht Sphere - SSLI",                                                     29, False),
    #("LUCA: Stadium Basement A - East Locker Hall (Jecht Sphere)",              30, False),
    #("MIHN: Oldroad, South - South End (Jecht Sphere)",                         31, False),
    #("MUSH: Precipice - South of Large Elevator (Auron's Sphere)",              32, False),
    #("Jecht Sphere - Moonflow",                                                 33, False),
    #("Jecht Sphere - Thunder Plains",                                           34, False),
    #("Braska's Sphere - Mt. Gagazet",                                           35, False),
                                       
    #("SSWI: Jecht Shot (Event)",                                                36, False),
    ("GUAD: Automatic Upon Leaving Farplane (Event)",                            37, False), # Brotherhood Upgrade

    ("MCWO: Upgrade Caladbolg Once (Event)",                                     38, False), # Caladbolg Crest Upgrade
    ("MCWO: Upgrade Caladbolg Twice (Event)",                                    39, False), # Caladbolg Sigil Upgrade
    ("MCWO: Upgrade Nirvana Once (Event)",                                       40, False), # Nirvana Crest Upgrade
    ("MCWO: Upgrade Nirvana Twice (Event)",                                      41, False), # Nirvana Sigil Upgrade
    ("MCWO: Upgrade Masamune Once (Event)",                                      42, False), # Masamune Crest Upgrade
    ("MCWO: Upgrade Masamune Twice (Event)",                                     43, False), # Masamune Sigil Upgrade
    ("MCWO: Upgrade Spirit Lance Once (Event)",                                  44, False), # Spirit Lance Crest Upgrade
    ("MCWO: Upgrade Spirit Lance Twice (Event)",                                 45, False), # Spirit Lance Sigil Upgrade
    ("MCWO: Upgrade World Champion Once (Event)",                                46, False), # World Champion Crest Upgrade
    ("MCWO: Upgrade World Champion Twice (Event)",                               47, False), # World Champion Sigil Upgrade
    ("MCWO: Upgrade Onion Knight Once (Event)",                                  48, False), # Onion Knight Crest Upgrade
    ("MCWO: Upgrade Onion Knight Twice (Event)",                                 49, False), # Onion Knight Sigil Upgrade
    ("MCWO: Upgrade Godhand Once (Event)",                                       50, False), # Godhand Crest Upgrade
    ("MCWO: Upgrade Godhand Twice (Event)",                                      51, False), # Godhand Sigil Upgrade
]] #

FFXPartyMemberLocations: List[FFXLocationData] = [ FFXLocationData(location[1]+PartyMemberOffset, *location) for location in [
    # ("Party Member: Tidus",                                      0, False), 
    ("BSIL: Waterfall Way - Summon Tutorial (Event)",                             1, False), # Party Member: Yuna
    ("LUCA: Post-Blitzball Tournament (Event)",                                   2, False), # Party Member: Auron
    ("SSLI: Encounter Sin Fin (Event)",                                           3, False), # Party Member: Kimahri
    ("BSIL: Enter the Valley (Event)",                                            4, False), # Party Member: Wakka
    ("BSIL: Village Slope - Element Tutorial (Event)",                            5, False), # Party Member: Lulu
    ("MOON: North Bank - Mix Tutorial (Event)",                                   6, False), # Party Member: Rikku
    ("MUSH: Encounter Sinspawn Gui Second Phase (Boss)",                          7, False), # Party Member: Seymour
    ("BSIL: Name Valefor (Event)",                                                8, False), # Party Member: Valefor
    ("KILK: Name Ifrit (Event)",                                                  9, False), # Party Member: Ifrit
    ("DJOS: Name Ixion (Event)",                                                 10, False), # Party Member: Ixion
    ("MCLA: Fight Seymour (Boss)",                                               11, False), # Party Member: Shiva
    ("BEVL: Name Bahamut (Event)",                                               12, False), # Party Member: Bahamut
    ("BAAJ: Release Anima (Event)",                                              13, False), # Party Member: Anima
    ("COSF: Hire Yojimbo (Event)",                                               14, False), # Party Member: Yojimbo
    ("REMI: Name the Magus Sisters (Event)",                                     15, False), # Party Member: Magus Sisters
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
    ("BAAJ: Submerged Ruins - Northeast Structure (Chest)",                                           0, False),  # Gil: 200 [02h]
    ("BAAJ: Submerged Ruins - Northwest Structure (Chest)",                                           1, False),  # Item: 2x Potion [2000h]
    ("BAAJ: Stairs - Flowers in Sconce on Right Wall, North End (Event)",                             2, False),  # Key Item: Withered Bouquet [A000h]
    ("BAAJ: Small Room - Flint Inside Desk (Event)",                                                  3, False),  # Key Item: Flint [A001h]
    #("Treasure 4 (Potentially Trashed Chest)",                                                       4, False),  # Gear: buki_get #2 [02h] { Yuna [01h], Weapon {One MP Cost [800Dh], Empty, Empty, Empty} }
    ("BAAJ: Underwater Hall - South Side Hidden Under Rocks (Chest)",                                 5, False),  # Gear: buki_get #3 [03h] { Lulu [05h], Weapon Formula=Celestial MP-based [12h] {No AP [8014h], Empty, Empty, Empty} }
    ("BAAJ: Stairs - South End (Chest)",                                                              6, False),  # Item: 1x Ether [2004h]
    ("BAAJ: Hall - North exit from Stairs, East End (Chest)",                                         7, False),  # Item: 1x Hi-Potion [2001h]
    #("Treasure 8 (Potentially Trashed Chest)",                                                       8, False),  # Item: 1x Phoenix Down [2006h]
    ("BSIL: Beach - West Near Huts (Chest)",                                                          9, False),  # Item: 2x Antidote [200Ah]
    #("Treasure 10 (Potentially Trashed Chest)",                                                     10, False),  # Gil: 200 [02h]
    #("Treasure 11 (Potentially Trashed Chest)",                                                     11, False),  # Gear: buki_get #4 [04h] { Tidus [00h], Weapon {Firestrike [801Eh]} }
    #("Treasure 12 (Potentially Trashed Chest)",                                                     12, False),  # Item: 1x Potion [2000h]
    ("BSIL: Village - Front of Shop (Chest)",                                                        13, False),  # Item: 1x Phoenix Down [2006h]
    ("BSIL: Village - Behind Shop, Bottom (Chest)",                                                  14, False),  # Item: 1x Hi-Potion [2001h]
    ("BSIL: Cloister - Destruction Sphere (Chest)",                                                  15, False),  # Gear: buki_get #5 [05h] { Yuna [01h], Weapon {Magic +5% [8067h], !Magic +3% [8066h], !Sensor [8000h]} }
    ("SSLI: Cabin (Chest)",                                                                          16, False),  # Item: 1x Remedy [200Fh]
    ("KILK: House - Right of Collapsing House (Chest)",                                              17, False),  # Item: 3x Potion [2000h]
    ("KILK: Tavern - After Rescuing Kulukan's Sister from Collapsing House (Chest)",                 18, False),  # Item: 1x Ether [2004h]
    ("KILK: Cloister - Destruction Sphere (Chest)",                                                  19, False),  # Gear: buki_get #6 [06h] { Kimahri [03h], Armor {Fire Ward [801Fh], Ice Ward [8023h], Lightning Ward [8027h]} }
    #("Treasure 20 (Potentially Trashed Chest)",                                                     20, False),  # Gear: buki_get #7 [07h] { Lulu [05h], Armor {Berserk Ward [8051h]} }
    #("Treasure 21 (Potentially Trashed Chest)",                                                     21, False),  # Item: 1x Potion [2000h] #Likely 21-26 are Potions from Yuna's Luggage as entries are near by S.S. Liki's treasure ID's
    #("Treasure 22 (Potentially Trashed Chest)",                                                     22, False),  # Item: 1x Potion [2000h]
    #("Treasure 23 (Potentially Trashed Chest)",                                                     23, False),  # Item: 1x Potion [2000h]
    #("Treasure 24 (Potentially Trashed Chest)",                                                     24, False),  # Item: 1x Potion [2000h]
    #("Treasure 25 (Potentially Trashed Chest)",                                                     25, False),  # Item: 1x Potion [2000h]
    #("Treasure 26 (Potentially Trashed Chest)",                                                     26, False),  # Item: 1x Potion [2000h]
    ("KILK: Woods - East of First Intersection (Chest)",                                             27, False),  # Item: 2x Mana Sphere [2047h]
    ("KILK: Woods - West of First Intersection, First North Fork (Chest)",                           28, False),  # Gear: buki_get #8 [08h] { Wakka [04h], Weapon {Icestrike [8022h], Sensor [8000h]} }
    ("KILK: Woods - Path North of Lord Ochu, Curving West (Chest)",                                  29, False),  # Item: 1x Luck Sphere [205Eh]
    #("KILK: NulBlaze Shield (Woman NPC after defeating Lord Ochu)",                                 30, False),  # Gear: buki_get #9 [09h] { Tidus [00h], Armor {SOS NulBlaze [8061h]} } COMMENT OUT??
    ("SSWI: Cabin - Left, Between Aurochs and Goers (Chest)",                                        31, False),  # Item: 1x Hi-Potion [2001h]
    ("LUCA: Dock 2 - Left Side (Chest)",                                                             32, False),  # Item: 2x Phoenix Down [2006h]
    ("LUCA: Dock 1 - Right Side (Chest)",                                                            33, False),  # Gil: 600 [06h]
    ("LUCA: Dock 1 - End (Chest)",                                                                   34, False),  # Gear: buki_get #10 [0Ah] { Kimahri [03h], Weapon {Piercing [800Bh], Waterstrike [802Ah]} }
    ("LUCA: Dock 5 - End, Hidden Behind Boxes, Left (Chest)",                                        35, False),  # Item: 1x HP Sphere [2055h]
    ("LUCA: Stadium Basement B - West Locker Hall (Chest)",                                          36, False),  # Item: 2x Hi-Potion [2001h]
    ("LUCA: City Limits - Staircase Leading to Mi'ihen (Chest)",                                     37, False),  # Gil: 1000 [0Ah]
    ("MIHN: South End - Behind Ruins on Left (Chest)",                                               38, False),  # Gear: buki_get #11 [0Bh] { Tidus [00h], Weapon {Icestrike [8022h]} }
    ("MIHN: Oldroad, South - Chocobo Jump, Alcove on East Side (Chest)",                             39, False),  # Item: 1x Fortune Sphere [204Ah]
    ("MIHN: Oldroad, North - Chocobo Jump, Left Side (Chest) (1)",                                   40, False),  # Gear: buki_get #12 [0Ch] { Auron [02h], Weapon {Piercing [800Bh], Lightningstrike [8026h]} }
    ("MIHN: Oldroad, North - Chocobo Jump, Left Side (Chest) (2)",                                   41, False),  # Gear: buki_get #13 [0Dh] { Wakka [04h], Weapon {Lightningstrike [8026h], Sensor [8000h]} }
    ("MIHN: Newroad, North - Chocobo Jump North Peak of Bend (Chest)",                               42, False),  # Gear: buki_get #14 [0Eh] { Kimahri [03h], Weapon {Piercing [800Bh], Firestrike [801Eh]} }
    ("MIHN: North End - Left by Child Soldiers (Chest)",                                             43, False),  # Item: 2x Hi-Potion [2001h]
    ("MIHN: South - Behind Elma, North Side (Chest)",                                                44, False),  # Item: 1x Remedy [200Fh]
    ("MIHN: Central, East Alcove (Chest)",                                                           45, False),  # Gil: 2000 [14h]
    ("MIHN: Central - North Exit (Chest)",                                                           46, False),  # Item: 3x Eye Drops [200Ch]
    ("MUSH: Aftermath - Left Exit Over Boxes (Chest)",                                               47, False),  # Item: 4x Soft [200Bh]
    ("MUSH: Valley - North Alcove After First Elevator (Chest)",                                     48, False),  # Gil: 1000 [0Ah]
    ("MUSH: Valley - Behind Pillar, Before Second Elevator (Chest)",                                 49, False),  # Item: 1x Hi-Potion [2001h]
    ("MUSH: Valley - Left Side, As Trail Turns East (Chest)",                                        50, False),  # Item: 1x Remedy [200Fh]
    ("MUSH: Ridge, Command Center - Behind Spear Rack (Chest)",                                      51, False),  # Gear: buki_get #15 [0Fh] { Auron [02h], Armor {HP +5% [8072h], Berserk Ward [8051h]} }
    ("MUSH: Ridge, Command Center - Near Lulu (Chest)",                                              52, False),  # Item: 1x Mega-Potion [2003h]
    #("Treasure 53 (Potentially Trashed Treasure)",                                                  53, False),  # Item: 1x Potion [2000h]
    ("DJOS: Highroad - South End, West Side (Chest)",                                                54, False),  # Item: 2x Phoenix Down [2006h]
    ("DJOS: Highroad - Midway, Hidden in Western Alcove (Chest)",                                    55, False),  # Gear: Bright Bangle
    #("Treasure 56 (Potentially Trashed Treasure)",                                                  56, False),  # Gear: buki_get #17 [11h] { Yuna [01h], Armor {Lightning Ward [8027h], Poison Ward [803Dh]} }
    ("MUSH: Precipice - Below West Elevator (Chest)",                                                57, False),  # Gear: buki_get #18 [12h] { Kimahri [03h], Armor {Dark Ward [8049h], Berserk Ward [8051h]} }
    ("DJOS: Temple - Northeast Corner (Chest)",                                                      58, False),  # Item: 4x Ability Sphere [2049h]
    ("DJOS: Temple - West Behind Lucil's Squad (Chest)",                                             59, False),  # Gil: 4000 [28h]
    ("DJOS: Inn - Behind Desk (Chest)",                                                              60, False),  # Gear: buki_get #19 [13h] { Wakka [04h], Weapon {Strength +3% [8062h], Strength +5% [8063h]} }
    ("DJOS: Great Hall - In Front of Nuns' Chamber (Chest)",                                         61, False),  # Item: 1x Ether [2004h]
    ("DJOS: Nuns' Chamber (Chest)",                                                                  62, False),  # Item: 1x Remedy [200Fh]
    ("DJOS: Monks' Chamber (Chest)",                                                                 63, False),  # Item: 1x Mega Phoenix [2007h]
    ("GUAD: House - Back Wall (Chest)",                                                              64, False),  # Gil: 3000 [1Eh]
    ("GUAD: East of Mansion (Chest)",                                                                65, False),  # Item: 1x Mega-Potion [2003h]
    ("GUAD: Upper Level, South Side (Chest)",                                                        66, False),  # Item: 1x Elixir [2008h]
    ("GUAD: Mansion, Entrance - Upper Level (Chest)",                                                67, False),  # Item: 2x Hi-Potion [2001h]
    ("MCWO: South - Near North Exit (Chest)",                                                        68, False),  # Gil: 2000 [14h]
    ("MCWO: South - Hidden Behind Tree in Middle of S-Bend (Chest)",                                 69, False),  # Gear: buki_get #20 [14h] { Lulu [05h], Weapon {Sleeptouch [803Fh]} }
    ("MCWO: Central - Hidden Behind Tree Before Spiral Down (Chest)",                                70, False),  # Item: 3x Phoenix Down [2006h]
    ("MCWO: MP Sphere x1 (Butterfly Minigame Reward before Spherimorph)",                            71, False),  # Item: 1x MP Sphere [2056h]
    ("MCWO: Ether x1 (Butterfly Minigame Reward before Spherimorph)",                                72, False),  # Item: 1x Ether [2004h]
    ("MCWO: North - Hidden Behind Tree on West Side (Chest)",                                        73, False),  # Item: 1x Remedy [200Fh]
    #("Treasure 74 (Trashed)",                                                                       74, False),  # Item: 1x Potion [2000h]
    ("MCWO: Campsite - (Chest)",                                                                     75, False),  # Gear: buki_get #21 [15h] { Yuna [01h], Armor {Silence Ward [8045h], Confuse Ward [804Fh]} }
    ("MCLA: Agency Front - Right Side (Chest)",                                                      76, False),  # Gil: 4000 [28h]
    ("MCLA: Crevasse - South End of Narrow Path (Chest)",                                            77, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("MCLA: Crevasse - Near North Exit (Chest)",                                                     78, False),  # Item: 1x Mega-Potion [2003h]
    ("MCLA: Lake Bottom - Hidden Left of Auron (Chest)",                                             79, False),  # Gear: buki_get #22 [16h] { Tidus [00h], Weapon {Counterattack [8003h]} }
    ("MCLA: Lake Bottom - Hidden Behind Kimahri (Chest)",                                            80, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    #("Treasure 81 (Trashed)",                                                                       81, False),  # Gear: buki_get #23 [17h] { Lulu [05h], Weapon {Silencetouch [8043h], Magic +5% [8067h]} }
    #("Treasure 82 (Trashed)",                                                                       82, False),  # Item: 1x Mega-Potion [2003h]
    ("MCLA: Hall - North Side (Chest)",                                                              83, False),  # Gil: 5000 [32h]
    ("MCLA: Hall - South Side (Chest)",                                                              84, False),  # Item: 2x X-Potion [2002h]
    ("MCLA: Hall - Gift from Tromell upon Entrance (Event)",                                         85, False),  # Gear: buki_get #24 [18h] { Rikku [06h], Armor {SOS Shell [8059h]} }
    ("MCLA: Monks' Chamber (Chest)",                                                                 86, False),  # Item: 3x Phoenix Down [2006h]
    ("MCLA: Nuns' Chamber (Chest)",                                                                  87, False),  # Item: 2x Remedy [200Fh]
    #("Treasure 88 (Trashed)",                                                                       88, False),  # Gear: buki_get #25 [19h] { Kimahri [03h], Armor {Poison Ward [803Dh], Confuse Ward [804Fh], Silence Ward [8045h], Empty} }
    #("Treasure 89 (Trashed)",                                                                       89, False),  # Item: 1x Potion [2000h]
    ("BSIL: Valley - South of Spawn, Right Side (Chest)",                                            90, False),  # Item: 1x Phoenix Down [2006h]
    ("BSIL: Valley - South Side, Hidden Behind Right Wall (Chest)",                                  91, False),  # Item: 1x Hi-Potion [2001h]
    ("BSIL: Valley - East Side, Right of Path (Chest)",                                              92, False),  # Item: 2x Antidote [200Ah]
    ("LUCA: Cafe - Talk to Owner After Placing at Least Third in a Tournament (Chest)",              93, False),  # Gear: buki_get #26 [1Ah] { Wakka [04h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    ("MIHN: North End - Donate 100 (NPC)",                                                           94, False),  # Gear: buki_get #27 [1Bh] { Wakka [04h], Weapon {Sensor [8000h]} }
    ("MIHN: North End - Donate 1000 (NPC)",                                                          95, False),  # Gear: buki_get #28 [1Ch] { Kimahri [03h], Weapon {Piercing [800Bh], Icestrike [8022h]} }
    ("MIHN: North End - Donate 10000 (NPC)",                                                         96, False),  # Gear: buki_get #29 [1Dh] { Yuna [01h], Armor {SOS Shell [8059h], SOS Protect [805Ah]} }
    ("MIHN: Agency - Exit After Resting (Event) (1)",                                                97, False),  # Item: 2x Mega-Potion [2003h]
    ("MUSH: Aftermath - Under Overhang, West Side (Chest)",                                          98, False),  # Item: 1x Hi-Potion [2001h]
    ("MUSH: Up Elevator in West Alcove, North Side (Event)",                                         99, False),  # Gear: buki_get #30 [1Eh] { Auron [02h], Weapon Formula=Celestial Auron [13h] {No AP [8014h], Empty, Empty, Empty} }
    ("BEVL: Underwater After Evrae Altana, Right Side After First Turn (Chest)",                    100, False),  # Gear: buki_get #31 [1Fh] { Tidus [00h], Weapon {Counterattack [8003h]} }
    ("BEVL: Underwater After Evrae Altana, Right Side Before First Turn (Chest)",                   101, False),  # Gear: buki_get #32 [20h] { Wakka [04h], Weapon {Evade & Counter [8004h]} }
    ("BEVL: Cloister - Left of Exit, 2 Bevelle Spheres Required (Chest)",                           102, False),  # Gear: buki_get #33 [21h] { Kimahri [03h], Weapon {Strength +3% [8062h], Strength +5% [8063h], Strength +10% [8064h]} }
    #("Treasure 103 (Trashed)",                                                                     103, False),  # Item: 1x Potion [2000h]
    ("BEVL: Via Purifico - Southwest Room Near Glyph (Chest)",                                      104, False),  # Item: 1x Elixir [2008h]
    ("BEVL: Via Purifico - West Room With Lulu (Chest)",                                            105, False),  # Item: 1x Wht Magic Sphere [204Eh]
    ("BEVL: Via Purifico - Puzzle Room Right (Chest)",                                              106, False),  # Item: 1x Skill Sphere [204Dh]
    ("BEVL: Via Purifico - Puzzle Room, Down Near Gate (Chest)",                                    107, False),  # Gil: 10000 [64h]
    ("BEVL: Via Purifico - Puzzle Room Left (Chest)",                                               108, False),  # Gear: buki_get #34 [22h] { Yuna [01h], Armor {Silence Ward [8045h], Confuse Ward [804Fh], Poison Ward [803Dh]} }
    ("BEVL: Via Purifico - Room Northeast of Central Teleporter (Chest)",                           109, False),  # Item: 1x Blk Magic Sphere [204Fh]
    ("BEVL: Via Purifico - East Room With Kimahri (Chest)",                                         110, False),  # Item: 1x Mega-Potion [2003h]
    ("MCWO: Bring Cloudy Mirror to Celestial Flower (Event)",                                       111, False),  # Key Item: Celestial Mirror [A003h]
    #("Treasure 112 (Trashed)",                                                                     112, False),  # Item: 1x Potion [2000h]
    ("MOAR: Nirvana (Chest)",                                                                       113, False),  # Gear: buki_get #36 [24h] { Yuna [01h], Weapon Formula=Celestial MP-based [12h] {No AP [8014h], Empty, Empty, Empty} }
    ("CALM: North - NW Corner, Blocked Until Winning Catcher Chocobo (Event)",                      114, False),  # Gear: buki_get #37 [25h] { Tidus [00h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    ("CALM: South - Southeast Corner, Left (Chest)",                                                115, False),  # Gil: 10000 [64h]
    ("CALM: South - Southeast Corner, Right (Chest)",                                               116, False),  # Gil: 5000 [32h]
    ("CALM: Central - Behind Agency Tent (Chest)",                                                  117, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    ("CALM: Gorge Bottom - Rusty Sword Between Two Rocks, East End (Event)",                        118, False),  # Key Item: Rusty Sword [A021h]
    #("Treasure 119 (Trashed)",                                                                     119, False),  # Gear: buki_get #38 [26h] { Kimahri [03h], Armor {HP +10% [8073h], Empty, Empty, Empty} }
    ("COSF: First Branch East (Chest)",                                                             120, False),  # Item: 1x Megalixir [2009h]
    ("COSF: Chamber East of First Intersection (Chest)",                                            121, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    ("COSF: Dead End North of Second Intersection (Chest)",                                         122, False),  # Item: 1x Fortune Sphere [204Ah]
    ("COSF: Top of Third Intersection (Chest)",                                                     123, False),  # Item: 2x Mega-Potion [2003h]
    ("COSF: Teleport West from Back of Cavern (Chest)",                                             124, False),  # Gear: buki_get #39 [27h] { Rikku [06h], Weapon {Empty, Empty, Empty, Empty} }
    ("COSF: Teleport East from Back of Cavern, Bottom (Chest)",                                     125, False),  # Item: 1x MP Sphere [2056h]
    ("COSF: Teleport East from Back of Cavern, Top (Chest)",                                        126, False),  # Item: 2x X-Potion [2002h]
    #("Treasure 127 (Trashed)",                                                                     127, False),  # Item: 1x Potion [2000h]
    ("MTGS: Trail - Top of Right Ridge Near South Exit (Chest)",                                    128, False),  # Gil: 20000 [C8h]
    ("MTGS: Trail - Left Alcove Near South Exit (Chest)",                                           129, False),  # Item: 2x Mega-Potion [2003h]
    ("MTGS: Trail - West Branch Before Bridge to Wantz (Chest)",                                    130, False),  # Gear: buki_get #40 [28h] { Auron [02h], Armor {Stoneproof [8038h], Poisonproof [803Ch]} }
    ("MTGS: Trail - Under Bridge After Wantz Right (Chest)",                                        131, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    ("MTGS: Trail - Under Bridge After Wantz Left (Chest)",                                         132, False),  # Item: 1x HP Sphere [2055h]
    #("Treasure 133 (Trashed)",                                                                     133, False),  # Item: 1x Potion [2000h]
    #("Treasure 134 (Trashed)",                                                                     134, False),  # Item: 1x Potion [2000h]
    ("MTGC: Cave - After Both Trials, Left Alcove, Northwest of Save Sphere (Chest)",               135, False), # Gear: buki_get #41 [29h] { Wakka [04h], Armor {SOS NulFrost [805Fh], SOS NulShock [8060h], SOS NulBlaze [8061h]} }
    ("MTGC: Submerged Passage - Reward from First Trial (Chest)",                                   136, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("MTGC: Submerged Passage - Reward From Second Trial (Chest)",                                  137, False),  # Item: 1x Fortune Sphere [204Ah]
    ("MTGC: Submerged Passage - After Both Trials, East Exit From Save Sphere, Left (Chest)",       138, False),  # Item: 1x Return Sphere [2060h]
    ("MTGC: Submerged Passage - After Both Trials, East Exit From Save Sphere, Right (Chest)",      139, False),  # Gear: buki_get #42 [2Ah] { Yuna [01h], Armor {HP Stroll [801Bh]} }
    #("Treasure 140 (Trashed)",                                                                     140, False),  # Item: 1x Potion [2000h]
    #("Treasure 141 (Trashed)",                                                                     141, False),  # Item: 1x Potion [2000h]
    #("Treasure 142 (Trashed)",                                                                     142, False),  # Item: 1x Potion [2000h]
    #("Treasure 143 (Trashed)",                                                                     143, False),  # Item: 1x Potion [2000h]
    #("Treasure 144 (Trashed)",                                                                     144, False),  # Item: 1x Potion [2000h]
    ("ZNKD: Overpass - South Side, West Bend (Chest)",                                              145, False),  # Item: 1x Fortune Sphere [204Ah]
    ("ZNKD: Overpass - North Side, Left Alcove (Chest)",                                            146, False),  # Gear: buki_get #43 [2Bh] { Rikku [06h], Armor {MP Stroll [801Ch]} }
    ("ZNKD: Dome Interior - Road Above Underpass (Chest)",                                          147, False),  # Gil: 10000 [64h]
    ("ZNKD: Dome Interior - West From 4-Way Intersection (Chest)",                                  148, False),  # Item: 1x Friend Sphere [2061h]
    ("ZNKD: Dome Interior - Rubble Path Down Before Circular Doorway (Chest)",                      149, False),  # Item: 1x Lv. 3 Key Sphere [2053h]
    ("ZNKD: Dome Corridor - Right Side (Chest)",                                                    150, False),  # Item: 1x Luck Sphere [205Eh]
    #("Treasure 151 (Trashed)",                                                                     151, False),  # Item: 1x Potion [2000h]
    ("OMGR: 1st Chest Reward for Minigame (Chest)",                                                 152, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    ("OMGR: 2nd Chest Reward for Minigame (Chest)",                                                 153, False),  # Gear: buki_get #44 [2Ch] { Auron [02h], Armor {Silenceproof [8044h], Darkproof [8048h]} }
    ("OMGR: 3rd Chest Reward for Minigame (Chest)",                                                 154, False),  # Gear: buki_get #45 [2Dh] { Wakka [04h], Weapon {Magic Counter [8005h], Counterattack [8003h]} }
    ("OMGR: 4th Chest Reward for Minigame (Chest)",                                                 155, False),  # Item: 2x Lv. 3 Key Sphere [2053h]
    ("OMGR: 5th Chest Reward for Minigame (Chest)",                                                 156, False),  # Gear: buki_get #46 [2Eh] { Kimahri [03h], Armor {Stoneproof [8038h], Poisonproof [803Ch], Empty, Empty} }
    ("OMGR: 6th Chest Reward for Minigame (Chest)",                                                 157, False),  # Item: 2x Friend Sphere [2061h]
    ("OMGR: 7th Chest Reward for Minigame (Chest)",                                                 158, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    ("OMGR: 8th Chest Reward for Minigame (Chest)",                                                 159, False),  # Gear: buki_get #47 [2Fh] { Yuna [01h], Armor {Ice Eater [8025h], Fire Eater [8021h], Lightning Eater [8029h], Empty} }
    ("OMGR: 9th Chest Reward for Minigame (Chest)",                                                 160, False),  # Gear: buki_get #48 [30h] { Lulu [05h], Weapon {Half MP Cost [800Ch]} }
    ("OMGR: 10th Chest Reward for Minigame (Chest)",                                                161, False),  # Gear: buki_get #49 [31h] { Rikku [06h], Weapon {Double AP [8012h], !Double Overdrive [800Eh]} }
    ("Yojimbo 3x Reward/OMGR: Teleport Sphere x2 (Chest)",                                          162, False),  # Item: 2x Teleport Sphere [2062h]
    ("SINS: Sea of Sorrow - Northwestern Alcove (Chest)",                                           163, False),  # Item: 1x Elixir [2008h]
    ("SINS: Sea of Sorrow - Atop Eastern Falls (Chest)",                                            164, False),  # Gear: buki_get #50 [32h] { Kimahri [03h], Weapon {Magic +3% [8066h], Magic +5% [8067h], Magic +10% [8068h], Empty} }
    ("SINS: Sea of Sorrow - Eastern Alcove, Near Final North Branch (Chest)",                       165, False),  # Item: 1x Lv. 3 Key Sphere [2053h]
    ("SINS: Sea of Sorrow - West Alcove (Chest)",                                                   166, False),  # Gear: buki_get #51 [33h] { Yuna [01h], Armor {Water Eater [802Dh], Fire Eater [8021h], Lightning Eater [8029h], Empty} }
    ("SINS: Sea of Sorrow - Atop Western Falls (Chest)",                                            167, False),  # Item: 1x Special Sphere [204Ch]
    ("SINS: City of Dying Dreams - East Glyph Near South Exit, Defeat 10/10/15 Fiends (Chest)",     168, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    ("SINS: City of Dying Dreams - South Side, Lift on Small Bridge (Chest)",                       169, False),  # Gear: buki_get #52 [34h] { Wakka [04h], Weapon {Waterstrike [802Ah], Firestrike [801Eh], Lightningstrike [8026h], Icestrike [8022h]} }
    ("SINS: City of Dying Dreams - South of First Open Area, Push North Wall Down (Chest)",         170, False),  # Gear: buki_get #53 [35h] { Auron [02h], Armor {Darkproof [8048h], Deathproof [8030h], Empty, Empty} }
    ("SINS: City of Dying Dreams - First Open Area, Ramp Down in Center (Chest)",                   171, False),  # Gil: 20000 [C8h]
    ("SINS: City of Dying Dreams - Lift Up in Center of First Open Area (Chest)",                   172, False),  # Item: 1x HP Sphere [2055h]
    ("SINS: City of Dying Dreams - Lift Up in Center of First Area, Just Before Lift Down (Chest)", 173, False),  # Item: 1x Defense Sphere [2058h]
    ("SINS: City of Dying Dreams - First Open Area, Glyph in Northwest Corner (Chest)",             174, False),  # Item: 1x Megalixir [2009h]
    ("SINS: City of Dying Dreams - Secret Slide South of Rising Block Area (Chest)",                175, False),  # Gear: buki_get #54 [36h] { Yuna [01h], Weapon {SOS Overdrive [8010h]} }
    ("REMI: Win Chocobo Race (Event)",                                                              176, False),  # Key Item: Cloudy Mirror [A002h]
    ("BSIL: Village - East of Temple (Jecht's Sphere)",                                             177, False),  # Key Item: Jecht's Sphere [A020h]
    ("THPL: South - West Side, South of Save Sphere (Chest)",                                       178, False),  # Item: 2x Phoenix Down [2006h]
    ("THPL: South - West Side, North of Save Sphere (Chest)",                                       179, False),  # Item: 2x Hi-Potion [2001h]
    ("THPL: South - West Side, Behind First Cactuar Statue (Chest)",                                180, False),  # Gil: 5000 [32h]
    ("THPL: South - East Side, Alcove With Second Cactuar Statue (Chest)",                          181, False),  # Gear: buki_get #55 [37h] { Wakka [04h], Weapon {Waterstrike [802Ah], Empty} }
    ("THPL: North - East Side, Near Southeast Exit (Chest)",                                        182, False),  # Item: 1x X-Potion [2002h]
    ("THPL: North - West Side, Behind Sheltered Lightning Rod (Chest)",                             183, False),  # Item: 1x Ether [2004h]
    ("THPL: North - West Side, Near North Exit (Chest)",                                            184, False),  # Item: 1x Remedy [200Fh]
    ("THPL: North - East of Final Lightning Rod (Chest)",                                           185, False),  # Gil: 2000 [14h]
    ("MIHN: South End - Fight Belgemine (Win) (Event)",                                             186, False),  # Gear: buki_get #74 [4Ah] { Yuna [01h], Armor {HP +10% [8073h], Silence Ward [8045h]} }
    ("REMI: Beat Belgemine (NPC)",                                                                  187, False),  # Item: 30x Power Sphere [2046h]
    ("THPL: Cactuar Statue Minigame (Event)",                                                       188, False),  # Gear: buki_get #56 [38h] { Kimahri [03h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} }
    ("THPL: Lightning Dodger - 5 Consecutive Dodges (Event)",                                       189, False),  # Item: 2x X-Potion [2002h]
    ("THPL: Lightning Dodger - 10 Consecutive Dodges (Event)",                                      190, False),  # Item: 2x Mega-Potion [2003h]
    ("THPL: Lightning Dodger - 20 Consecutive Dodges (Event)",                                      191, False),  # Item: 2x MP Sphere [2056h]
    ("THPL: Lightning Dodger - 50 Consecutive Dodges (Event)",                                      192, False),  # Item: 3x Strength Sphere [2057h]
    ("THPL: Lightning Dodger - 100 Consecutive Dodges (Event)",                                     193, False),  # Item: 3x HP Sphere [2055h]
    ("THPL: Lightning Dodger - 150 Consecutive Dodges (Event)",                                     194, False),  # Item: 4x Megalixir [2009h]
    #("Treasure 195 (Trashed)",                                                                     195, False),  # Item: 1x Ether [2004h]
    #("Treasure 196 (Trashed)",                                                                     196, False),  # Item: 1x Elixir [2008h]
    ("MOON: South Bank Road - West Corner as Path Bends East (Chest)",                              197, False),  # Item: 1x X-Potion [2002h]
    ("MOON: South Wharf - Near O'aka XXIII (Chest)",                                                198, False),  # Item: 2x Phoenix Down [2006h]
    ("MOON: South Wharf - Behind Lulu (Chest)",                                                     199, False),  # Gil: 5000 [32h]
    ("MOON: North Wharf - Near Bench (Chest)",                                                      200, False),  # Item: 1x Ether [2004h]
    ("MOON: North Bank - East Side, Right After the Wooden Bridge (Chest)",                         201, False),  # Item: 4x Antidote [200Ah]
    ("MOON: North Bank Road - West Side, Before Guadosalam (Chest)",                                202, False),  # Item: 1x Mega-Potion [2003h]
    #("BAAJ Temple: Grenades from Rikku",                                                           203, False),  # Item: 2x Grenade [2023h]
    ("BAAJ: Antechamber - Right Side (Chest)",                                                      204, False),  # Item: 1x Megalixir [2009h]
    ("BAAJ: Antechamber - Left Side (Chest)",                                                       205, False),  # Item: 4x Mega Phoenix [2007h]
    ("LUCA: Dock 5 - End, Hidden Behind Boxes, Right (Chest)",                                      206, False),  # Item: 1x Magic Sphere [2059h]
    ("BSIL: Exit the Village (Event) (1)",                                                          207, False),  # Gear: buki_get #1 [01h] { Tidus [00h], Weapon {Strength +5% [8063h], Strength +10% [8064h], Waterstrike [802Ah], Sensor [8000h]} }
    ("Brotherhood?",                                                                                208, False),  # Gear: buki_get #1 [01h] { Tidus [00h], Weapon {Strength +5% [8063h], Strength +10% [8064h], Waterstrike [802Ah], Sensor [8000h]} }
    ("ZNKD: Cloister - Destruction Sphere (Chest)",                                                 209, False),  # Gear: buki_get #60 [3Ch] { Yuna [01h], Weapon {Half MP Cost [800Ch], Empty, Empty} }
    ("BIKA: Oasis - Next to Tent (Chest)",                                                          210, False),  # Item: 8x Al Bhed Potion [2014h]
    ("BIKA: Desert, East - Near First Tent, Left (Chest)",                                          211, False),  # Item: 8x Al Bhed Potion [2014h]
    ("BIKA: Desert, Central - Right of Save Sphere (Chest)",                                        212, False),  # Item: 8x Al Bhed Potion [2014h]
    ("BAAJ: Hall - South Side of East Door (Chest)",                                                213, False),  # Item: 1x X-Potion [2002h]
    #("MUSH: Code GODHAND",                                                                         214, False),  # Gear: buki_get #61 [3Dh] { Rikku [06h], Weapon Formula=Celestial HP-based [11h] {No AP [8014h], Empty, Empty, Empty} } UNCOMMENT WHEN CODES ARE INCORPORATED
    ("BSIL: Village - Behind Shop, Middle (Chest)",                                                 215, False),  # Gil: 400 [04h]
    ("BSIL: Village - Behind Shop, Top (Chest)",                                                    216, False),  # Item: 2x Potion [2000h]
    ("BEVL: Cloister - End (Chest)",                                                                217, False),  # Item: 1x HP Sphere [2055h]
    ("GUAD: Road to Farplane - Left Side Behind Wall (Chest)",                                      218, False),  # Item: 8x Lightning Marble [201Eh]
    ("BAAJ: Underwater Hall - West Branch of Main Path (Chest)",                                    219, False),  # Item: 1x Hi-Potion [2001h]
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
    ("ZNKD: Dome Beyond - Chest After Taking Left/Right in Yunalesca Arena (Chest)",                267, False),  # Key Item: Sun Crest [A023h]
    ("BSIL: Beach - East Alcove (Chest)",                                                           268, False),  # Key Item: Moon Crest [A025h]
    ("MIHN: Oldroad, South - South End (Chest)",                                                    269, False),  # Key Item: Mars Crest [A027h]
    ("MTGZ: Prominence - Hidden Between Left Pillars (Chest)",                                      270, False),  # Key Item: Saturn Crest [A02Ah]
    ("LUCA: Stadium Locker Room - Inside Back Right Locker (Event)",                                271, False),  # Key Item: Jupiter Crest [A02Ch]
    ("GUAD: Farplane - West Side (Chest)",                                                          272, False),  # Key Item: Venus Crest [A02Eh]
    ("BIKA: Desert, West - First Western Alcove, Sinkhole (Chest)",                                 273, False),  # Key Item: Mercury Crest [A030h]
    ("CALM: Catcher chocobo Minigame, Time Under 0.00 (Event)",                                     274, False),  # Key Item: Sun Sigil [A024h]
    ("REMI: Defeat All Aeons and Send Belgemine (Event)",                                           275, False),  # Key Item: Moon Sigil [A026h]
    ("MOAR: Unlock Ten Arena Creations (Event)",                                                    276, False),  # Key Item: Mars Sigil [A028h]
    ("MCWO: Finish Butterfly Minigame (Event)",                                                     277, False),  # Key Item: Saturn Sigil [A02Bh]
    ("THPL: Lightning Dodger - 200 Consecutive Dodges (Event)",                                     278, False),  # Key Item: Venus Sigil [A02Fh]
    ("BIKA: Desert - Complete Cactuar Village Quest (Event)",                                       279, False),  # Key Item: Mercury Sigil [A031h]
    ("MCLA: Megalixir x2 (Butterfly Game after defeating Spherimorph)",                             280, False),  # Item: 2x Megalixir [2009h]
    ("MCLA: Elixir x2 (Butterfly Game after defeating Spherimorph)",                                281, False),  # Item: 2x Elixir [2008h]
    ("BSIL: Beach - Datto (NPC)",                                                                   282, False),  # Item: 1x Hi-Potion [2001h]
    ("BSIL: Beach - Jassu (NPC)",                                                                   283, False),  # Item: 3x Potion [2000h]
    ("BSIL: Beach - Botta (NPC)",                                                                   284, False),  # Item: 2x Potion [2000h]
    ("BSIL: Beach - Keepa (NPC)",                                                                   285, False),  # Gil: 200 [02h]
    ("BSIL: Beach, Dock - Boy (NPC)",                                                               286, False),  # Item: 1x Remedy [200Fh]
    ("BSIL: Beach, Dock - Monk (NPC)",                                                              287, False),  # Gear: buki_get #62 [3Eh] { Yuna [01h], Armor {HP +10% [8073h]} }
    ("BSIL: Beach, Dock - Woman (NPC)",                                                             288, False),  # Item: 3x Phoenix Down [2006h]
    ("BSIL: Beach, Dock - Shirtless Man (NPC)",                                                     289, False),  # Gil: 400 [04h]
    ("BSIL: Beach, Dock - Green Shirt (NPC)",                                                       290, False),  # Item: 1x Ether [2004h]
    ("KILK: Woods - Luzzu Before Beating Lord Ochu (NPC)",                                          291, False),  # Item: 4x Antidote [200Ah]
    ("KILK: Woods - Luzzu After Beating Lord Ochu (NPC)",                                           292, False),  # Item: 1x Elixir [2008h]
    ("KILK: Woods - Crusader Commander West of Lord Ochu (NPC)",                                    293, False),  # Item: 1x Remedy [200Fh]
    #("KILK: Phoenix Down x3 (Guard NPC, fight Ochu from west and run?)",                           294, False),  # Item: 3x Phoenix Down [2006h]
    ("KILK: Woods - Crusader Commander North of Lord Ochu (NPC)",                                   295, False),  # Item: 1x Hi-Potion [2001h]
    ("ALBS: Deck - Yellow Al Bhed, on Left (NPC)",                                                  296, False),  # Item: 3x Potion [2000h]
    ("DJOS: Highroad - South End, Silver/Purple Armor (NPC)",                                       297, False),  # Gear: buki_get #63 [3Fh] { Tidus [00h], Weapon {Strength +3% [8062h], Empty, Empty, Empty} }
    ("DJOS: Highroad - South End, Purple Armor (NPC)",                                              298, False),  # Gear: buki_get #64 [40h] { Yuna [01h], Armor {Stoneproof [8038h], Empty} }
    ("DJOS: Highroad - Monk Pacing Between Crusaders (NPC)",                                        299, False),  # Item: 1x Hi-Potion [2001h]
    ("DJOS: Highroad - Midway, Yellow Armor (NPC)",                                                 300, False),  # Item: 1x Ether [2004h]
    ("DJOS: Highroad - North End, Purple Armor (NPC)",                                              301, False),  # Item: 1x Mega-Potion [2003h]
    ("DJOS: Pilgrimage Road - North End, Purple Armor (NPC)",                                       302, False),  # Gear: buki_get #65 [41h] { Kimahri [03h], Weapon {Magic +20% [8069h], Empty} }
    ("DJOS: Pilgrimage Road - South End, Silver/Purple Armor (NPC)",                                303, False),  # Item: 10x Potion [2000h]
    ("DJOS: Pilgrimage Road - Monk Pacing Along Bridge (NPC)",                                      304, False),  # Item: 2x Hi-Potion [2001h]
    ("MCLA: Road - Linna, at Bottom of Stairs (NPC)",                                               305, False),  # Gil: 400 [04h]
    ("MCLA: Monks' Chamber - Purple Monk (NPC)",                                                    306, False),  # Item: 1x Elixir [2008h]
    ("MCLA: Monks' Chamber - Brown Monk (NPC)",                                                     307, False),  # Item: 1x Ether [2004h]
    ("MCLA: Nuns' Chamber - Yellow Nun (NPC)",                                                      308, False),  # Item: 2x Hi-Potion [2001h]
    ("MIHN: South End - Blue/White Man, Looping North to South (NPC)",                              309, False),  # Gear: buki_get #66 [42h] { Kimahri [03h], Weapon {Piercing [800Bh], Sensor [8000h], Strength +10% [8064h]} }
    ("MIHN: South End - Red Skirt Girl, Pacing Between Maechen and Ruins (NPC)",                    310, False),  # Item: 2x Antidote [200Ah]
    ("MIHN: South End - Yellow Man, Looping South to North (NPC)",                                  311, False),  # Item: 1x Hi-Potion [2001h]
    ("MIHN: South - Boy Before Kicking the Blitzball (NPC)",                                        312, False),  # Item: 3x Soft [200Bh]
    ("MIHN: South - Crusader Running East then West (NPC)",                                         313, False),  # Gear: buki_get #67 [43h] { Yuna [01h], Armor {HP +10% [8073h], Fire Ward [801Fh]} }
    ("MIHN: Central - Purple Crusader Freaking Out, West Side (NPC)",                               314, False),  # Item: 1x Ether [2004h]
    ("MIHN: Central - Woman on North End, West Side (NPC)",                                         315, False),  # Item: 1x Hi-Potion [2001h]
    ("MIHN: Central - Male Yellow Crusader, Looping North to South (NPC)",                          316, False),  # Gil: 600 [06h]
    ("MIHN: Central - Purple Crusader, Looping South to North (NPC)",                               317, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("MIHN: Central - Female Yellow Crusader, Looping North to South (NPC)",                        318, False),  # Item: 4x Antidote [200Ah]
    ("MUSH: First Screen - Right Near Southern Exit (NPC)",                                         319, False),  # Gear: buki_get #68 [44h] { Lulu [05h], Armor {HP +20% [8074h], Empty} }
    ("MUSH: First Screen - Pacing Between Blue Commander and North Exit (NPC)",                     320, False),  # Item: 2x Phoenix Down [2006h]
    ("MUSH: First Screen - Left Near Southern Exit (NPC)",                                          321, False),  # Item: 1x Remedy [200Fh]
    ("MUSH: First Screen - Blue Commander on Left Side (NPC)",                                      322, False),  # Item: 1x Hi-Potion [2001h]
    ("MUSH: First Screen - Pacing Between Blue Commander and South Exit (NPC)",                     323, False),  # Item: 1x Ether [2004h]
    ("MUSH: Valley - Woman Before First Elevator (NPC)",                                            324, False),  # Item: 1x Hi-Potion [2001h]
    ("MUSH: Valley - North Alcove After First Elevator (NPC)",                                      325, False),  # Item: 10x Potion [2000h]
    ("MUSH: Precipice - Pacing Between North Elevator and East Ridge (NPC)",                        326, False),  # Gil: 400 [04h]
    ("MUSH: Precipice - Near South Elevator (NPC)",                                                 327, False),  # Item: 1x X-Potion [2002h]
    ("MUSH: Precipice - Near Large Elevator (NPC)",                                                 328, False),  # Item: 1x Mega-Potion [2003h]
    ("OMGR: 12th Chest Reward for Minigame (Chest)",                                                329, False),  # Item: 99x Warp Sphere [2063h]
    ("OMGR: Press Both Glyphs, Then Take Narrow Central Path (Chest)",                              330, False),  # Item: 1x Teleport Sphere [2062h]
    ("OMGR: Zone After Ultima, West Path (Chest)",                                                  331, False),  # Item: 1x Friend Sphere [2061h]
    ("OMGR: Omega Boss Arena (Chest)",                                                              332, False),  # Item: 1x Magic Sphere [2059h]
    #("Treasure 333 (Old Entry?)",                                                                  333, False),  # Key Item: Blossom Crown [A032h]
    ("REMI: Defeat Bahamut (Boss)",                                                                 334, False),  # Key Item: Flower Scepter [A033h]
    #("Treasure 335 (Trashed)",                                                                     335, False),  # Item: 1x Potion [2000h]
    ("SSLI: Clasko, After Breeder Encouragement in Macalania (Event)",                              336, False),  # Item: 1x Friend Sphere [2061h] # Talk to Clasko before Crawler and make sure to have him become a Chocobo Breeder
    ("CALM: Wobbly Chocobo Minigame (Event)",                                                       337, False),  # Item: 1x Elixir [2008h]
    ("CALM: Dodger Chocobo Minigame (Event)",                                                       338, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("CALM: Hyper Dodger Chocobo Minigame (Event)",                                                 339, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    ("CALM: Catcher Chocobo Minigame (Event)",                                                      340, False),  # Item: 1x Lv. 3 Key Sphere [2053h]
    #("Treasure 341 (Trashed)",                                                                     341, False),  # Item: 1x X-Potion [2002h]
    #("Treasure 342 (Trashed)",                                                                     342, False),  # Item: 1x Mega-Potion [2003h]
    #("Treasure 343 (Trashed)",                                                                     343, False),  # Item: 1x Ether [2004h]
    #("Treasure 344 (Trashed)",                                                                     344, False),  # Item: 1x Turbo Ether [2005h]
    ("THPL: Agency Front (Ground Item)",                                                            345, False),  # Gear: buki_get #69 [45h] { Tidus [00h], Armor {Lightningproof [8028h], Empty} }
    ("BIKA: Oasis - In Southwest Corner of Water (Chest)",                                          346, False),  # Item: 4x Remedy [200Fh]
    ("BIKA: Desert, East - Near First Tent, Right (Chest)",                                         347, False),  # Item: 2x Ether [2004h]
    ("BIKA: Desert, East - Western Alcove, Near Structure (Chest)",                                 348, False),  # Item: 4x Hi-Potion [2001h]
    ("BIKA: Desert, Central - Far West Corner (Chest)",                                             349, False),  # Item: 2x Mega-Potion [2003h]
    ("BIKA: Desert, Central - Rock Ridge Southwest of Save Sphere (Chest)",                         350, False),  # Item: 2x X-Potion [2002h]
    ("BIKA: Desert, Central - Structure Southeast of Save Sphere (Chest)",                          351, False),  # Item: 4x Hi-Potion [2001h]
    ("BIKA: Desert, Central - Southwest Corner of Northwest Zone (Chest)",                          352, False),  # Item: 1x Elixir [2008h]
    ("BIKA: Desert, Central - Central Structure of Northwest Zone, Bottom (Chest)",                 353, False),  # Gil: 10000 [64h]
    ("BIKA: Desert, Central - Central Structure of Northwest Zone, Top (Chest)",                    354, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    ("BIKA: Desert, West - First Western Alcove, Between Rocks (Chest)",                            355, False),  # Item: 8x Hi-Potion [2001h]
    ("BIKA: Desert, West - Second Western Alcove, Hidden Behind Rock (Chest)",                      356, False),  # Item: 3x Mega-Potion [2003h]
    ("BIKA: Desert, West - Second Western Alcove, North Side (Chest)",                              357, False),  # Item: 2x X-Potion [2002h]
    ("BIKA: Desert, West - Left Sinkhole on Main Path (Chest)",                                     358, False),  # Item: 3x Megalixir [2009h]
    ("BIKA: Desert, West - Right Sinkhole on Main Path (Chest)",                                    359, False),  # Item: 2x Teleport Sphere [2062h]
    ("HOME: Main Corridor - North Hall, Left (Chest)",                                              360, False),  # Item: 6x Al Bhed Potion [2014h]
    ("HOME: Main Corridor - Bottom of South Stairs, Hidden Behind Left Smoke (Chest)",              361, False),  # Item: 4x Al Bhed Potion [2014h]
    ("HOME: Outside Summoner's Sanctum - Right (Chest)",                                            362, False),  # Item: 1x Lv. 2 Key Sphere [2052h]
    ("HOME: Outside Summoner's Sanctum - Left (Chest)",                                             363, False),  # Item: 1x Lv. 4 Key Sphere [2054h]
    ("HOME: Environment Controls (Chest)",                                                          364, False),  # Gil: 10000 [64h]
    ("SSWI: Deck - Top Floor, Counting Gulls (NPC)",                                                365, False),  # Gear: buki_get #70 [46h] { Wakka [04h], Weapon {Magic +20% [8069h], Magic +10% [8068h], Magic +5% [8067h], Magic +3% [8066h]} }
    ("MIHN: South End - Fight Belgemine (Lose) (Event)",                                            366, False),  # Gear: buki_get #71 [47h] { Yuna [01h], Armor {HP +10% [8073h], Empty} }
    ("HOME: Keyakku, on Ground (NPC)",                                                              367, False),  # Item: 2x Hi-Potion [2001h]
    #("MUSH: Valley - Code VICTORIOUS",                                                             368, False),  # Gear: buki_get #72 [48h] { Rikku [06h], Armor {Lightningproof [8028h], Fireproof [8020h], Iceproof [8024h], Empty} } UNCOMMENT WHEN CODES ARE INCORPORATED
    #("BSIL: BSIL Ruins - Code MURASAME",                                                           369, False),  # Gear: buki_get #73 [49h] { Auron [02h], Weapon {Piercing [800Bh], One MP Cost [800Dh], Empty, Empty} } UNCOMMENT WHEN CODES ARE INCORPORATED
    ("CALM: Speed Sphere x30 (Lose Aeon Fight)",                                                    370, False),  # Item: 30x Speed Sphere [2048h]
    ("Defeat Belgemine Twice",                                                                      371, False),  # Key Item: Aeon's Soul [A01Fh]
    ("MOON: South Bank Road - Fight Belgemine (Win) (Event) (1)",                                   372, False),  # Item: 2x Dragon Scale [2021h]
    ("MOON: South Bank Road - Fight Belgemine (Lose) (Event) (1)",                                  373, False),  # Item: 6x Smoke Bomb [2028h]
    ("Defeat Belgemine Once",                                                                       374, False),  # Key Item: Summoner's Soul [A01Eh]
    ("AIRS: Cabin - Before Evrae, Yellow Al Bhed on Left (NPC)",                                    375, False),  # Item: 4x Al Bhed Potion [2014h]
    ("MOON: South Bank Road - Right of Shelinda (Chest)",                                           376, False),  # Item: 3x Lv. 1 Key Sphere [2051h]
    ("MOON: South Bank Road - East Alcove as Path Bends North (Chest)",                             377, False),  # Item: 3x Lv. 1 Key Sphere [2051h]
    ("MOON: South Bank Road - West Alcove in Forest Past Belgemine (Chest)",                        378, False),  # Item: 1x Magic Def Sphere [205Ah]
    ("REMI: Defeat Valefor (Boss)",                                                                 379, False),  # Item: 4x Lightning Gem [201Fh]
    ("REMI: Valefor Post First Fight (Boss)",                                                       380, False),  # Item: 4x Power Sphere [2046h]
    ("REMI: Defeat Ifrit (Boss)",                                                                   381, False),  # Item: 30x X-Potion [2002h]
    ("REMI: Ifrit Post First Fight (Boss)",                                                         382, False),  # Item: 5x Mana Sphere [2047h]
    ("REMI: Defeat Ixion (Boss)",                                                                   383, False),  # Item: 10x Chocobo Feather [2036h]
    ("REMI: Ixion Post First Fight (Boss)",                                                         384, False),  # Item: 8x Power Sphere [2046h]
    ("REMI: Defeat Shiva (Boss)",                                                                   385, False),  # Item: 60x Mega-Potion [2003h]
    ("REMI: Shiva Post First Fight (Boss)",                                                         386, False),  # Item: 6x Star Curtain [203Ah]
    ("REMI: Bahamut Post First Fight (Boss)",                                                       387, False),  # Item: 8x Mana Sphere [2047h]
    ("REMI: Defeat Yojimbo (Boss)",                                                                 388, False),  # Item: 8x Shadow Gem [2029h]
    ("REMI: Yojimbo Post First Fight (Boss)",                                                       389, False),  # Item: 10x Power Sphere [2046h]
    ("REMI: Defeat Anima (Boss)",                                                                   390, False),  # Item: 60x Stamina Spring [203Dh]
    ("REMI: Anima Post First Fight (Boss)",                                                         391, False),  # Item: 10x Mana Sphere [2047h]
    ("REMI: Defeat Magus Sisters (Boss)",                                                           392, False),  # Item: 40x Shining Gem [202Ah]
    ("REMI: Magus Sisters Post First Fight (Boss)",                                                 393, False),  # Item: 12x Power Sphere [2046h]
    ("MCLA: Teleport Sphere x1 (Butterfly Game after Airship)",                                     394, False),  # Item: 1x Teleport Sphere [2062h]
    ("HOME: Living Quarters, East of Main Corridor - Quiz (Chest)",                                 395, False),  # Item: 1x Skill Sphere [204Dh]
    ("HOME: Living Quarters, East of Main Corridor - Password (Chest)",                             396, False),  # Item: 1x Special Sphere [204Ch]
    ("HOME: Living Quarters, South of Main Corridor - Vocabulary Test (Chest)",                     397, False),  # Item: 1x Friend Sphere [2061h]
    ("HOME: Living Quarters, South of Main Corridor - What do I contain? (Chest)",                  398, False),  # Item: 1x Elixir [2008h]
    #("Treasure 399 (Trashed)",                                                                     399, False),  # Item: 1x Hi-Potion [2001h] 
    #("Treasure 400 (Trashed)",                                                                     400, False),  # Item: 1x Mega-Potion [2003h] 
    #("Treasure 401 (Trashed)",                                                                     401, False),  # Item: 1x Soft [200Bh] 
    #("Treasure 402 (Trashed)",                                                                     402, False),  # Item: 1x Potion [2000h]
    #("Treasure 403 (Trashed)",                                                                     403, False),  # Item: 1x Remedy [200Fh]
    #("Treasure 404 (Trashed)",                                                                     404, False),  # Item: 2x Potion [2000h]
    ("AIRS: Collect All Primers, Talk to Rin (NPC)",                                                405, False),  # Item: 99x Underdog's Secret [206Eh]
    ("BSIL: Fayth Revisit - Northwest (Chest)",                                                     406, False),  # Item: 1x Wht Magic Sphere [204Eh]
    ("BSIL: Fayth Revisit - Northeast (Chest)",                                                     407, False),  # Item: 1x Elixir [2008h]
    ("BSIL: Fayth Revisit - Southwest (Chest)",                                                     408, False),  # Item: 1x Hi-Potion [2001h]
    ("BSIL: Fayth Revisit - Southeast (Chest)",                                                     409, False),  # Item: 2x Potion [2000h]
    #("S.S Liki: Potion (Yuna's suitcase)",                                                         410, False),  # Item: 1x Potion [2000h] # Definitely Yuna's Suitcase
    #("Treasure 411 (Trashed)",                                                                     411, False),  # Item: 1x Potion [2000h]
    #("Treasure 412 (Trashed)",                                                                     412, False),  # Item: 1x Potion [2000h]
    #("Treasure 413 (Trashed)",                                                                     413, False),  # Item: 1x Potion [2000h]
    #("Treasure 414 (Trashed)",                                                                     414, False),  # Item: 1x Potion [2000h]
    #("Treasure 415 (Trashed)",                                                                     415, False),  # Item: 1x Potion [2000h]
    #("Treasure 416 (Trashed)",                                                                     416, False),  # Item: 1x Potion [2000h]
    ("REMI: 1st Chest in Chocobo Race",                                                             417, False),  # Item: 1x Elixir [2008h]
    ("REMI: 2nd Chest in Chocobo Race",                                                             418, False),  # Item: 1x Megalixir [2009h]
    ("REMI: 3rd Chest in Chocobo Race",                                                             419, False),  # Item: 60x Three Stars [2045h]
    ("REMI: 4th Chest in Chocobo Race",                                                             420, False),  # Item: 30x Pendulum [2069h]
    ("REMI: 5th Chest in Chocobo Race",                                                             421, False),  # Item: 30x Wings to Discovery [206Ch]
    #("Treasure 422",                                                                               422, False),  # Item: 1x Potion [2000h]
    ("MIHN: Agency - Green NPC After Resting (Event)",                                              423, False),  # Item: 1x Lv. 1 Key Sphere [2051h]
    ("MOAR: Area Conquest - Capture 1 of Each Besaid Fiend (NPC)",                                  424, False),  # Item: 99x Stamina Tonic [2043h]
    ("MOAR: Area Conquest - Capture 1 of Each Kilika Fiend (NPC)",                                  425, False),  # Item: 99x Poison Fang [202Dh]
    ("MOAR: Area Conquest - Capture 1 of Each Mi'ihen Highroad Fiend (NPC)",                        426, False),  # Item: 99x Soul Spring [203Eh]
    ("MOAR: Area Conquest - Capture 1 of Each Mushroom Rock Road Fiend (NPC)",                      427, False),  # Item: 99x Candle of Life [2030h]
    ("MOAR: Area Conquest - Capture 1 of Each Djose Road Fiend (NPC)",                              428, False),  # Item: 99x Petrify Grenade [2031h]
    ("MOAR: Area Conquest - Capture 1 of Each Thunder Plains Fiend (NPC)",                          429, False),  # Item: 99x Chocobo Wing [2037h]
    ("MOAR: Area Conquest - Capture 1 of Each Macalania Fiend (NPC)",                               430, False),  # Item: 60x Shining Gem [202Ah]
    ("MOAR: Area Conquest - Capture 1 of Each Bikanel Fiend (NPC)",                                 431, False),  # Item: 99x Shadow Gem [2029h]
    ("MOAR: Area Conquest - Capture 1 of Each Calm Lands Fiend (NPC)",                              432, False),  # Item: 60x Farplane Wind [2033h]
    ("MOAR: Area Conquest - Capture 1 of Each CotSF Fiend (NPC)",                                   433, False),  # Item: 40x Silver Hourglass [202Eh]
    ("MOAR: Area Conquest - Capture 1 of Each Mt. Gagazet Fiend (NPC)",                             434, False),  # Key Item: Blossom Crown [A032h]
    ("MOAR: Area Conquest - Capture 1 of Each Inside Sin Fiend (NPC)",                              435, False),  # Item: 99x Lunar Curtain [2038h]
    ("MOAR: Area Conquest - Capture 1 of Each Omega Ruins Fiend (NPC)",                             436, False),  # Item: 60x Designer Wallet [2034h]
    ("MOAR: Species Conquest - Capture 3 of Each Wolf Fiend (NPC)",                                 437, False),  # Item: 99x Chocobo Feather [2036h]
    ("MOAR: Species Conquest - Capture 3 of Each Reptile Fiend (NPC)",                              438, False),  # Item: 99x Stamina Spring [203Dh]
    ("MOAR: Species Conquest - Capture 5 of Each Bird Fiend (NPC)",                                 439, False),  # Item: 99x Mega Phoenix [2007h]
    ("MOAR: Species Conquest - Capture 4 of Each Wasp Fiend (NPC)",                                 440, False),  # Item: 60x Mana Tonic [2044h]
    ("MOAR: Species Conquest - Capture 4 of Each Imp Fiend (NPC)",                                  441, False),  # Item: 99x Mana Spring [203Ch]
    ("MOAR: Species Conquest - Capture 4 of Each Eye Fiend (NPC)",                                  442, False),  # Item: 60x Stamina Tablet [2040h]
    ("MOAR: Species Conquest - Capture 3 of Each Flan Fiend (NPC)",                                 443, False),  # Item: 60x Twin Stars [2042h]
    ("MOAR: Species Conquest - Capture 3 of Each Elemental Fiend (NPC)",                            444, False),  # Item: 99x Star Curtain [203Ah]
    ("MOAR: Species Conquest - Capture 3 of Each Helm Fiend (NPC)",                                 445, False),  # Item: 99x Gold Hourglass [202Fh]
    ("MOAR: Species Conquest - Capture 4 of Each Drake Fiend (NPC)",                                446, False),  # Item: 99x Purifying Salt [203Fh]
    ("MOAR: Species Conquest - Capture 5 of Each Fungus Fiend (NPC)",                               447, False),  # Item: 99x Healing Spring [203Bh]
    ("MOAR: Species Conquest - Capture 5 of Each Bomb Fiend (NPC)",                                 448, False),  # Item: 60x Turbo Ether [2005h]
    ("MOAR: Species Conquest - Capture 5 of Each Ruminant Fiend (NPC)",                             449, False),  # Item: 99x Light Curtain [2039h]
    ("MOAR: Species Conquest - Capture 10 of Each Iron Giant Fiend (NPC)",                          450, False),  # Item: 60x Mana Tablet [2041h]
    ("MOAR: Original Creation - Complete 2 Area Conquests (NPC)",                                   451, False),  # Item: 60x Three Stars [2045h]
    ("MOAR: Original Creation - Complete 2 Species Conquests (NPC)",                                452, False),  # Item: 60x Supreme Gem [202Ch]
    ("MOAR: Original Creation - Complete 6 Area Conquests (NPC)",                                   453, False),  # Item: 99x Door to Tomorrow [206Bh]
    ("MOAR: Original Creation - Complete 6 Species Conquests (NPC)",                                454, False),  # Item: 99x Gambler's Spirit [206Dh]
    ("MOAR: Original Creation - Capture 1 of Each Fiend (NPC)",                                     455, False),  # Item: 99x Winning Formula [206Fh]
    ("MOAR: Original Creation - Capture 5 of Each Fiend (NPC)",                                     456, False),  # Item: 99x Dark Matter [2035h]
    ("MOAR: Original Creation - Capture 2 of Each Mt. Gagazet Underwater Fiend (NPC)",              457, False),  # Item: 30x Megalixir [2009h]
    ("MOAR: Original Creation - Capture 10 of Each Fiend (NPC)",                                    458, False),  # Item: 10x Master Sphere [2050h]
    ("BSIL: Exit the Village (Event) (2)",                                                          459, False),  # Item: 1x Map [2064h]
    ("MCLA: Fayth Revisit - PLACEHOLDER 1",                                                         460, False),  # Item: 1x Magic Def Sphere [205Ah]
    ("MCLA: Fayth Revisit - PLACEHOLDER 2",                                                         461, False),  # Item: 1x Accuracy Sphere [205Dh]
    ("MCLA: Fayth Revisit - PLACEHOLDER 3",                                                         462, False),  # Item: 1x Magic Sphere [2059h]
    ("DJOS: Fayth Revisit - West (Chest)",                                                          463, False),  # Item: 1x Agility Sphere [205Bh]
    ("DJOS: Fayth Revisit - East (Chest)",                                                          464, False),  # Item: 1x Magic Def Sphere [205Ah]
    ("DJOS: Fayth Revisit (Event)",                                                                 465, False),  # Item: 1x Luck Sphere [205Eh]
    ("REMI: Fayth - Revisit (Event)",                                                               466, False),  # Item: 1x Defense Sphere [2058h]
    ("BSIL: Fayth - Revisit (Event)",                                                               467, False),  # Item: 1x Evasion Sphere [205Ch]
    ("REMI: Fayth - Revisit (Event)",                                                               468, False),  # Item: 1x Strength Sphere [2057h]
    ("BIKA: Shadow Gem x2 (Robeya Minigame Chest)",                                                 469, False),  # Item: 2x Shadow Gem [2029h]
    ("BIKA: Shining Gem x1 (Robeya Minigame Chest)",                                                470, False),  # Item: 1x Shining Gem [202Ah]
    ("BIKA: Blessed Gem x1 (Robeya Minigame Chest)",                                                471, False),  # Item: 1x Blessed Gem [202Bh]
    ("BIKA: Potion x1 (Cactuar Sidequest Prize)",                                                   472, False),  # Item: 1x Potion [2000h]
    ("BIKA: Elixir x1 (Cactuar Sidequest Prize)",                                                   473, False),  # Item: 1x Elixir [2008h]
    ("BIKA: Megalixir x1 (Cactuar Sidequest Prize)",                                                474, False),  # Item: 1x Megalixir [2009h]
    ("BIKA: Friend Sphere x1 (Cactuar Sidequest Prize)",                                            475, False),  # Item: 1x Friend Sphere [2061h]
    ("KILK: Fayth Revisit - Northwest (Chest)",                                                     476, False),  # Item: 1x Agility Sphere [205Bh]
    ("KILK: Fayth Revisit - Northeast (Chest)",                                                     477, False),  # Item: 1x Defense Sphere [2058h]
    ("KILK: Fayth Revisit (Event)",                                                                 478, False),  # Item: 1x Luck Sphere [205Eh]
    ("KILK: Fayth Revisit - Southeast (Chest)",                                                     479, False),  # Item: 1x Accuracy Sphere [205Dh]
    ("BSIL: Besaid Falls - X31 Y75, Dragoon Lance",                                                 480, False),  # Gear: buki_get #75 [4Bh] { Kimahri [03h], Weapon {Magic Counter [8005h], Evade & Counter [8004h], Empty, Empty} }
    ("MIHN: Mi'ihen Ruins - X35 Y57 Sonar",                                                         481, False),  # Gear: buki_get #76 [4Ch] { Rikku [06h], Weapon {Initiative [8002h], Poisonstrike [803Ah], Empty} }
    ("MUSH: Battle Site - X41 Y57 Phantom Bangle",                                                  482, False),  # Gear: buki_get #77 [4Dh] { Lulu [05h], Armor {Ice Eater [8025h], Fire Eater [8021h], !Water Eater [802Dh]} }
    ("BIKA: Sanubia Sands - X15 Y42 Ascalon",                                                       483, False),  # Gear: buki_get #78 [4Eh] { Tidus [00h], Weapon {Double AP [8012h]} }
    ("DJOS: Cloister - Destruction Sphere (Chest)",                                                 484, False),  # Item: 1x Magic Sphere [2059h]
    ("MACA: Cloister - Destruction Sphere (Chest)",                                                 485, False),  # Item: 1x Luck Sphere [205Eh]
    ("SINS: Prism Ball (Point of No Return)",                                                       486, False),  # Gear: buki_get #79 [4Fh] { Wakka [04h], Weapon {Magic Counter [8005h], Empty} }
    ("SINS: Stillblade (Point of No Return)",                                                       487, False),  # Gear: buki_get #80 [50h] { Auron [02h], Weapon {Silencestrike [8042h], Stonestrike [8036h], Empty} }
    ("SINS: Skill Sphere x1 (Point of No Return)",                                                  488, False),  # Item: 1x Skill Sphere [204Dh]
    ("SINS: Mage's Staff (Point of No Return)",                                                     489, False),  # Gear: buki_get #81 [51h] { Yuna [01h], Weapon {Magic +10% [8068h], Magic +5% [8067h], Magic +3% [8066h], Empty} }
    ("SINS: Knight Lance (Point of No Return)",                                                     490, False),  # Gear: buki_get #82 [52h] { Kimahri [03h], Weapon {Strength +10% [8064h], Strength +5% [8063h], Strength +3% [8062h], Empty} }
    ("SINS: Wht Magic Sphere x1 (Point of No Return)",                                              491, False),  # Item: 1x Wht Magic Sphere [204Eh]
    ("SINS: Infinity (Point of No Return)",                                                         492, False),  # Gear: buki_get #83 [53h] { Rikku [06h], Weapon {One MP Cost [800Dh], Sensor [8000h]} }
    ("SINS: Wicked Cait Sith (Point of No Return)",                                                 493, False),  # Gear: buki_get #84 [54h] { Lulu [05h], Weapon {Deathstrike [802Eh], Empty, Empty, Empty} }
    ("SINS: Attribute Sphere x1 (Point of No Return)",                                              494, False),  # Item: 1x Attribute Sphere [204Bh]
    ("SINS: Hrunting (Point of No Return)",                                                         495, False),  # Gear: buki_get #85 [55h] { Tidus [00h], Weapon {SOS Overdrive [8010h]} }
    ("MOAR: Defeat Nemesis",                                                                        496, False),  # Key Item: Mark of Conquest [A029h]
    ("LUCA: Win the Story Blitzball Tournament (Event)",                                            497, False),  # Item: 1x Strength Sphere [2057h]
]]

FFXCaptureLocations: List[FFXLocationData] = [ FFXLocationData(location[1]+CaptureOffset, *location) for location in [
    ("Fiend Capture: Raldo",             0, False),
    ("Fiend Capture: Bunyip",            1, False),
    ("Fiend Capture: Murussu",           2, False),
    ("Fiend Capture: Mafdet",            3, False),
    ("Fiend Capture: Shred",             4, False),
    ("Fiend Capture: Gandarewa",         5, False),
    ("Fiend Capture: Aerouge",           6, False),
    ("Fiend Capture: Imp",               7, False),
    ("Fiend Capture: Dingo",             8, False),
    ("Fiend Capture: Mi'ihen Fang",      9, False),
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
    ("Fiend Capture: Zaurus",          100, False),
    ("Fiend Capture: Halma",           101, False),
    ("Fiend Capture: Floating Death",  102, False),
    ("Fiend Capture: Machea",          103, False),
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
