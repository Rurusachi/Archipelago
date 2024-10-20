from typing import NamedTuple, List, Dict


from .items import (ItemData, EquipKnives, EquipSwords, EquipBlades, EquipSabers, EquipKnightswords,
                    EquipRapiers, EquipGreatswords, EquipBroadswords, EquipKatanas, EquipSpears,
                    EquipRods, EquipStaves, EquipPoles, EquipKnuckles, EquipBows, EquipGreatbows,
                    EquipGuns, EquipInstruments, EquipHandcannons, EquipAxes, EquipHammers,
                    EquipMaces, EquipCards, EquipBooks, EquipHelmets, EquipHats, EquipHeavyArmor,
                    EquipLightArmor, EquipRobes, MeleeWeapons)


class JobEquipment(NamedTuple):
    weapon: List[ItemData]
    head: List[ItemData]
    body: List[ItemData]
    shield: bool


races: List[str] = ["Hume", "Bangaa", "Nu Mou", "Viera", "Moogle", "Seeq", "Gria"]

RaceJobOffsets: Dict[str, int] = {
    "Hume": 0x1,
    "Bangaa": 0xe,
    "Nu Mou": 0x18,
    "Viera": 0x22,
    "Moogle": 0x2c,
    "Seeq": 0x36,
    "Gria": 0x3a,
}

raceToJobs: Dict[str, str] = {
    "Hume": [
        "Soldier", "Thief", "White Mage", "Black Mage", "Archer", "Paladin",
        "Fighter", "Parivir", "Ninja", "Illusionist", "Blue Mage", "Hunter", "Seer",
    ],
    "Bangaa": [
        "Warrior", "White Monk", "Dragoon", "Defender", "Gladiator",
        "Master Monk", "Bishop", "Templar", "Cannoneer", "Trickster",
    ],
    "Nu Mou": [
        "White Mage", "Black Mage", "Beastmaster", "Time Mage", "Illusionist",
        "Alchemist", "Arcanist", "Sage", "Scholar", #"Keeper",
    ],
    "Viera": [
        "Fencer", "White Mage", "Green Mage", "Archer", "Elementalist",
        "Red Mage", "Spellblade", "Summoner", "Assassin", "Sniper",
    ],
    "Moogle": [
        "Animist", "Thief", "Black Mage", "Moogle Knight", "Fusilier",
        "Juggler", "Tinker", "Time Mage", "Chocobo Knight", "Flintlock",
    ],
    "Seeq": [
        "Berserker", "Ranger", "Lanista", "Viking",
    ],
    "Gria": [
        "Hunter", "Raptor", "Ravager", "Geomancer",
    ]
}

# Hume
SoldierEquipment = JobEquipment(EquipSwords + EquipGreatswords,
                                EquipHelmets + EquipHats,
                                EquipHeavyArmor + EquipLightArmor,
                                True,
                                )

ThiefEquipment = JobEquipment(EquipKnives,
                              EquipHats,
                              EquipLightArmor,
                              False)

WhiteMageEquipment = JobEquipment(EquipStaves,
                                  EquipHats,
                                  EquipLightArmor + EquipRobes,
                                  False)

BlackMageEquipment = JobEquipment(EquipRods,
                                  EquipHats,
                                  EquipLightArmor + EquipRobes,
                                  False)

ArcherEquipment = JobEquipment(EquipBows,
                               EquipHats,
                               EquipLightArmor,
                               False)

PaladinEquipment = JobEquipment(EquipGreatswords + EquipKnightswords,
                                EquipHelmets,
                                EquipRobes + EquipHeavyArmor,
                                True)

FighterEquipment = JobEquipment(EquipBlades,
                                EquipHats,
                                EquipLightArmor,
                                False)

ParivirEquipment = JobEquipment(EquipKatanas,
                                EquipHats,
                                EquipLightArmor,
                                False)

NinjaEquipment = JobEquipment(EquipKatanas,
                              EquipHats,
                              EquipLightArmor,
                              False)

IllusionistEquipment = JobEquipment(EquipRods,
                                    EquipHats,
                                    EquipLightArmor + EquipRobes,
                                    False)

BlueMageEquipment = JobEquipment(EquipSabers,
                                 EquipHats,
                                 EquipLightArmor + EquipRobes,
                                 False)

HunterEquipment = JobEquipment(EquipKnives + EquipGreatbows,
                               EquipHats,
                               EquipLightArmor,
                               False)

SeerEquipment = JobEquipment(EquipBooks,
                             EquipHats,
                             EquipLightArmor + EquipRobes,
                             False)

# Moogle
AnimistEquipment = JobEquipment(EquipInstruments,
                                EquipHats,
                                EquipLightArmor,
                                False)

# Thief

# Black Mage

MoogleKnightEquipment = JobEquipment(EquipBlades,
                                     EquipHats + EquipHelmets,
                                     EquipHeavyArmor,
                                     True)

FusilierEquipment = JobEquipment(EquipGuns,
                                 EquipHats,
                                 EquipLightArmor,
                                 False)

JugglerEquipment = JobEquipment(EquipKnives,
                                EquipHats,
                                EquipLightArmor,
                                False)

TinkerEquipment = JobEquipment(EquipKnuckles,
                               EquipHats,
                               EquipLightArmor,
                               False)

TimeMageEquipment = JobEquipment(EquipRods,
                                 EquipHats,
                                 EquipLightArmor + EquipRobes,
                                 False)

ChocoboKnightEquipment = JobEquipment(MeleeWeapons,  # Unsure
                                      EquipHats,
                                      EquipLightArmor,
                                      False)

FlintlockEquipment = JobEquipment(EquipHandcannons,
                                  EquipHats,
                                  EquipLightArmor,
                                  False)

# Nu Mou

# White Mage

# Black Mage

BeastmasterEquipment = JobEquipment(EquipInstruments,
                                    EquipHats,
                                    EquipLightArmor,
                                    False)

# Time Mage

# Illusionist

AlchemistEquipment = JobEquipment(EquipMaces,
                                  EquipHats,
                                  EquipLightArmor,
                                  False)

ArcanistEquipment = JobEquipment(EquipRods,
                                 EquipHats,
                                 EquipLightArmor + EquipRobes,
                                 False)

SageEquipment = JobEquipment(EquipMaces,
                             EquipHats,
                             EquipLightArmor + EquipRobes,
                             True)

ScholarEquipment = JobEquipment(EquipBooks,
                                EquipHats,
                                EquipLightArmor,
                                False)

# Bangaa

WarriorEquipment = JobEquipment(EquipSwords + EquipBroadswords,
                                EquipHats + EquipHelmets,
                                EquipLightArmor + EquipHeavyArmor,
                                True)

WhiteMonkEquipment = JobEquipment(EquipKnuckles,
                                  None,
                                  EquipLightArmor,
                                  False)

DragoonEquipment = JobEquipment(EquipSwords + EquipSpears,
                                EquipHelmets,
                                EquipHeavyArmor,
                                False)

DefenderEquipment = JobEquipment(EquipKnightswords + EquipBroadswords,
                                 EquipHelmets,
                                 EquipHeavyArmor,
                                 True)

GladiatorEquipment = JobEquipment(EquipBlades,
                                  EquipHats,
                                  EquipLightArmor,
                                  False)

MasterMonkEquipment = JobEquipment(EquipPoles,
                                   EquipHats,
                                   EquipLightArmor,
                                   False)

BishopEquipment = JobEquipment(EquipStaves,
                               EquipHats,
                               EquipLightArmor + EquipRobes,
                               False)

TemplarEquipment = JobEquipment(EquipKnightswords + EquipSpears,
                                EquipHelmets,
                                EquipHeavyArmor + EquipRobes,
                                False)

CannoneerEquipment = JobEquipment(EquipHandcannons,
                                  EquipHats,
                                  EquipLightArmor,
                                  False)

TricksterEquipment = JobEquipment(EquipCards,
                                  EquipHats,
                                  EquipLightArmor,
                                  False)

# Viera

FencerEquipment = JobEquipment(EquipRapiers,
                               EquipHats,
                               EquipLightArmor,
                               True)

# White Mage

GreenMageEquipment = JobEquipment(EquipHammers + EquipMaces,
                                  EquipHats,
                                  EquipLightArmor + EquipRobes,
                                  False)

# Archer

ElementalistEquipment = JobEquipment(EquipRapiers,
                                     EquipHats,
                                     EquipLightArmor,
                                     False)

RedMageEquipment = JobEquipment(EquipRapiers,
                                EquipHats,
                                EquipLightArmor + EquipRobes,
                                False)

SpellbladeEquipment = JobEquipment(EquipSwords,
                                   EquipHats,
                                   EquipLightArmor,
                                   False)

SummonerEquipment = JobEquipment(EquipStaves,
                                 EquipHats,
                                 EquipLightArmor + EquipRobes,
                                 False)

AssassinEquipment = JobEquipment(EquipKatanas + EquipGreatbows,
                                 EquipHats,
                                 EquipLightArmor,
                                 False)

SniperEquipment = JobEquipment(EquipGreatbows,
                               EquipHats,
                               EquipLightArmor,
                               False)


# Seeq
BerserkerEquipment = JobEquipment(EquipKnuckles,
                                  EquipHats,
                                  EquipLightArmor,
                                  False)

RangerEquipment = JobEquipment(EquipKnives + EquipBows,
                               EquipHats,
                               EquipLightArmor,
                               False)

LanistaEquipment = JobEquipment(EquipGreatswords,
                                EquipHats + EquipHelmets,
                                EquipLightArmor + EquipHeavyArmor,
                                False)

VikingEquipment = JobEquipment(EquipAxes + EquipHammers,
                               EquipHats + EquipHelmets,
                               EquipLightArmor + EquipHeavyArmor,
                               True)

# Gria

# Hunter

RaptorEquipment = JobEquipment(EquipBroadswords,
                               EquipHats + EquipHelmets,
                               EquipLightArmor + EquipHeavyArmor,
                               True)

RavagerEquipment = JobEquipment(EquipGreatswords,
                                EquipHats + EquipHelmets,
                                EquipLightArmor + EquipHeavyArmor,
                                False)

GeomancerEquipment = JobEquipment(EquipPoles,
                                  EquipHats,
                                  EquipLightArmor + EquipRobes,
                                  False)


# Special jobs

# Hurdy
BardEquipment = JobEquipment(EquipInstruments,
                             EquipHats,
                             EquipLightArmor,
                             False)

# Adelle
HeritorEquipment = JobEquipment(EquipKnives + EquipSwords + EquipBlades + EquipSabers + EquipGreatswords +
                                EquipBroadswords + EquipKnightswords + EquipKatanas + EquipRods +
                                EquipStaves + EquipPoles,
                                EquipHats,
                                EquipLightArmor,
                                False)

# Penelo
DancerEquipment = JobEquipment(EquipKnives + EquipRods + EquipStaves + EquipPoles,
                               EquipHats,
                               EquipLightArmor,
                               False)
# Vaan
SkyPirateEquipment = JobEquipment(EquipSwords + EquipSabers + EquipBlades,
                                  EquipHats,
                                  EquipLightArmor + EquipRobes,
                                  True)
# Al-Cid
AgentEquipment = JobEquipment(EquipGuns,
                              EquipHats,
                              EquipLightArmor,
                              False)


jobToEquipment: Dict[str, JobEquipment] = {
    "Soldier": SoldierEquipment,
    "Thief": ThiefEquipment,
    "White Mage": WhiteMageEquipment,
    "Black Mage": BlackMageEquipment,
    "Archer": ArcherEquipment,
    "Paladin": PaladinEquipment,
    "Fighter": FighterEquipment,
    "Parivir": ParivirEquipment,
    "Ninja": NinjaEquipment,
    "Illusionist": IllusionistEquipment,
    "Blue Mage": BlueMageEquipment,
    "Hunter": HunterEquipment,
    "Seer": SeerEquipment,
    "Animist": AnimistEquipment,
    "Moogle Knight": MoogleKnightEquipment,
    "Fusilier": FusilierEquipment,
    "Juggler": JugglerEquipment,
    "Tinker": TinkerEquipment,
    "Time Mage": TimeMageEquipment,
    "Chocobo Knight": ChocoboKnightEquipment,
    "Flintlock": FlintlockEquipment,
    "Beastmaster": BeastmasterEquipment,
    "Alchemist": AlchemistEquipment,
    "Arcanist": ArcanistEquipment,
    "Sage": SageEquipment,
    "Scholar": ScholarEquipment,
    "Warrior": WarriorEquipment,
    "White Monk": WhiteMonkEquipment,
    "Dragoon": DragoonEquipment,
    "Defender": DefenderEquipment,
    "Gladiator": GladiatorEquipment,
    "Master Monk": MasterMonkEquipment,
    "Bishop": BishopEquipment,
    "Templar": TemplarEquipment,
    "Cannoneer": CannoneerEquipment,
    "Trickster": TricksterEquipment,
    "Fencer": FencerEquipment,
    "Green Mage": GreenMageEquipment,
    "Elementalist": ElementalistEquipment,
    "Red Mage": RedMageEquipment,
    "Spellblade": SpellbladeEquipment,
    "Summoner": SummonerEquipment,
    "Assassin": AssassinEquipment,
    "Sniper": SniperEquipment,
    "Berserker": BerserkerEquipment,
    "Ranger": RangerEquipment,
    "Lanista": LanistaEquipment,
    "Viking": VikingEquipment,
    "Raptor": RaptorEquipment,
    "Ravager": RavagerEquipment,
    "Geomancer": GeomancerEquipment,
    "Bard": BardEquipment,
    "Heritor": HeritorEquipment,
    "Dancer": DancerEquipment,
    "Sky Pirate": SkyPirateEquipment,
    "Agent": AgentEquipment,
}

jobStartingEquipment: Dict[str, List[str]] = {
    "Soldier": ["Broadsword", "Linen Cuirass"],
    "Thief": ["Jackknife", "Leather Clothing"],
    "White Mage": ["White Staff", "Hempen Robe"],
    "Black Mage": ["Rod", "Hempen Robe"],
    "Archer": ["Longbow", "Leather Clothing"],
    "Paladin": ["Defender", "Linen Cuirass"],
    "Fighter": ["Sweep Blade", "Leather Clothing"],
    "Parivir": ["Murasame", "Leather Clothing"],
    "Ninja": ["Kunai", "Leather Clothing"],
    "Illusionist": ["Firewheel Rod", "Hempen Robe"],
    "Blue Mage": ["Light Saber", "Leather Clothing"],
    "Hunter": ["Windslash Bow", "Leather Clothing"],
    "Seer": ["Battle Folio", "Hempen Robe"],
    "Warrior": ["Broadsword", "Linen Cuirass"],
    "White Monk": ["Metal Knuckles", "Leather Clothing"],
    "Dragoon": ["Javelin", "Linen Cuirass"],
    "Defender": ["Defender", "Linen Cuirass"],
    "Gladiator": ["Sweep Blade", "Leather Clothing"],
    "Master Monk": ["Tonfa", "Leather Clothing"],
    "Bishop": ["Judicer's Staff", "Hempen Robe"],
    "Templar": ["Apocalypse", "Linen Cuirass"],
    "Cannoneer": ["Hand Cannon", "Leather Clothing"],
    "Trickster": ["Four of Spades", "Leather Clothing"],
    "Beastmaster": ["Lamia Harp", "Leather Clothing"],
    "Time Mage": ["Firewheel Rod", "Hempen Robe"],
    "Alchemist": ["Druid Mace", "Leather Clothing"],
    "Arcanist": ["Sleet Rod", "Hempen Robe"],
    "Sage": ["Battle Mace", "Hempen Robe"],
    "Scholar": ["Battle Folio", "Leather Clothing"],
    "Keeper": ["Snowy Tear", "Leather Clothing"],
    "Fencer": ["Stinger", "Leather Clothing"],
    "Green Mage": ["Battle Mace", "Hempen Robe"],
    "Elementalist": ["Estoc", "Leather Clothing"],
    "Red Mage": ["Stinger", "Leather Clothing"],
    "Spellblade": ["Broadsword", "Leather Clothing"],
    "Summoner": ["Staff of Protection", "Hempen Robe"],
    "Assassin": ["Murasame", "Leather Clothing"],
    "Sniper": ["Windslash Bow", "Leather Clothing"],
    "Animist": ["Glass Bell", "Leather Clothing"],
    "Moogle Knight": ["Shadow Blade", "Linen Cuirass"],
    "Fusilier": ["Aiot Gun", "Leather Clothing"],
    "Juggler": ["Scramasax", "Leather Clothing"],
    "Tinker": ["Metal Knuckles", "Leather Clothing"],
    "Chocobo Knight": ["Dagger", "Leather Clothing", "Battle Boots"],
    "Flintlock": ["Hand Cannon", "Leather Clothing"],
    "Berserker": ["Metal Knuckles"],
    "Ranger": ["Kard", "Leather Clothing"],
    "Lanista": ["Xankbras", "Linen Cuirass"],
    "Viking": ["Broadaxe", "Linen Cuirass"],
    "Raptor": ["Samson Sword", "Linen Cuirass"],
    "Ravager": ["Xankbras", "Linen Cuirass"],
    "Geomancer": ["Zephyr Pole", "Hempen Robe"],
}
