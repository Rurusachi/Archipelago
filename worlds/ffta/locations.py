import typing
from typing import Dict

from BaseClasses import Location


class FFTALocation(Location):
    game: str = "Final Fantasy Tactics Advance"


class FFTALocationData(typing.NamedTuple):
    name: str
    mission_id: int
    rom_address: int


MissionGroups = []
bitflags = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]

FFTALocations: typing.List[FFTALocationData] = [
    # Decide whether to use address or memory offset from data array

    FFTALocationData('Herb Picking Reward 1', 0, 0x55AF40),
    FFTALocationData('Herb Picking Reward 2', 0, 0x55AF42),

    FFTALocationData('Thesis Hunt Reward 1', 1, 0x55AF86),
    FFTALocationData('Thesis Hunt Reward 2', 1, 0x55AF88),

    FFTALocationData('The Cheetahs Reward 1', 2, 0x55AFCC),
    FFTALocationData('The Cheetahs Reward 2', 2, 0x55AFCE),

    FFTALocationData('Desert Peril Reward 1', 3, 0x55b012),
    FFTALocationData('Desert Peril Reward 2', 3, 0x55b014),

    FFTALocationData('Twisted Flow Reward 1', 4, 0x55b058),
    FFTALocationData('Twisted Flow Reward 2', 4, 0x55b05a),

    FFTALocationData('Antilaws Reward 1', 5, 0x55b09e),
    FFTALocationData('Antilaws Reward 2', 5, 0x55b0a0),

    FFTALocationData('Diamond Rain Reward 1', 6, 0x55b0e4),
    FFTALocationData('Diamond Rain Reward 2', 6, 0x55b0e6),

    FFTALocationData('Hot Awakening Reward 1', 7, 0x55b12a),
    FFTALocationData('Hot Awakening Reward 2', 7, 0x55b12c),

    FFTALocationData('Magic Wood Reward 1', 8, 0x55b170),
    FFTALocationData('Magic Wood Reward 2', 8, 0x55b172),

    FFTALocationData('Emerald Keep Reward 1', 9, 0x55b1b6),
    FFTALocationData('Emerald Keep Reward 2', 9, 0x55b1b8),

    FFTALocationData('Pale Company Reward 1', 10,  0x55b1fc),
    FFTALocationData('Pale Company Reward 2', 10,  0x55b1fe),

    FFTALocationData('Jagd Hunt Reward 1', 11, 0x55b242),
    FFTALocationData('Jagd Hunt Reward 2', 11, 0x55b244),

    FFTALocationData('The Bounty Reward 1', 12, 0x55b288),
    FFTALocationData('The Bounty Reward 2', 12, 0x55b28a),

    FFTALocationData('Golden Clock Reward 1', 13, 0x55b2ce),
    FFTALocationData('Golden Clock Reward 2', 13, 0x55b2d0),

    FFTALocationData('Scouring Time Reward 1', 14, 0x55b314),
    FFTALocationData('Scouring Time Reward 2', 14, 0x55b316),

    FFTALocationData('The Big Find Reward 1', 15, 0x55b35a),
    FFTALocationData('The Big Find Reward 2', 15, 0x55b35c),

    FFTALocationData('Desert Patrol Reward 1', 16, 0x55b3a0),
    FFTALocationData('Desert Patrol Reward 2', 16, 0x55b3a2),

    FFTALocationData('Quiet Sands Reward 1', 17, 0x55b3e6),
    FFTALocationData('Quiet Sands Reward 2', 17, 0x55b3e8),

    FFTALocationData('Materite Now! Reward 1', 18, 0x55b42c),
    FFTALocationData('Materite Now! Reward 2', 18, 0x55b42e),

    FFTALocationData('Present Day Reward 1', 19, 0x55b472),
    FFTALocationData('Present Day Reward 2', 19, 0x55b474),

    FFTALocationData('Hidden Vein Reward 1', 20, 0x55b4b8),
    FFTALocationData('Hidden Vein Reward 2', 20, 0x55b4ba),

    FFTALocationData('To Ambervale Reward 1', 21, 0x55b4fe),
    FFTALocationData('To Ambervale Reward 2', 21, 0x55b500),

    FFTALocationData('Over The Hill Reward 1', 22, 0x55b544),
    FFTALocationData('Over The Hill Reward 2', 22, 0x55b546),

    # Non story missions
    FFTALocationData('Wanted! Black Mage Dolce Reward 1', 25, 0x55b616),
    FFTALocationData('Wanted! Black Mage Dolce Reward 2', 25, 0x55b618),

    FFTALocationData('Wanted! Gabbana Brothers Reward 1', 26, 0x55b65c),
    FFTALocationData('Wanted! Gabbana Brothers Reward 2', 26,  0x55b65e),

    FFTALocationData('Wanted! Godeye Reward 1', 27, 0x55b6a2),
    FFTALocationData('Wanted! Godeye Reward 2', 27,  0x55b6a4),

    FFTALocationData('Wanted! Swampking Reward 1', 28, 0x55b6e8),
    FFTALocationData('Wanted! Swampking Reward 2', 28,  0x55b6ea),

    FFTALocationData('Wanted! Killer Rayne Reward 1', 29, 0x55b72e),
    FFTALocationData('Wanted! Killer Rayne Reward 2', 29,  0x55b730),

    FFTALocationData('Wanted! Dark Duke Lodion Reward 1', 30, 0x55b774),
    FFTALocationData('Wanted! Dark Duke Lodion Reward 2', 30,  0x55b776),

    FFTALocationData('Ruby Red Reward 1', 31, 0x55b7ba),
    FFTALocationData('Ruby Red Reward 2', 31,  0x55b7bc),

    FFTALocationData('Tower Ruins Reward 1', 32, 0x55b800),
    FFTALocationData('Tower Ruins Reward 2', 32, 0x55b802),

    FFTALocationData('Battle in Aisen Reward 1', 33, 0x55b846),
    FFTALocationData('Battle in Aisen Reward 2', 33, 0x55b848),

    FFTALocationData('Magewyrm Reward 1', 34, 0x55b88c),
    FFTALocationData('Magewyrm Reward 2', 34, 0x55b88e),

    FFTALocationData('Salika Keep Reward 1', 35, 0x55b8d2),
    FFTALocationData('Salika Keep Reward 2', 35, 0x55b8d4),

    FFTALocationData('Twin Swords Reward 1', 36, 0x55b918),
    FFTALocationData('Twin Swords Reward 2', 36, 0x55b91a),

    FFTALocationData('Village Hunt Reward 1', 37, 0x55b95e),
    FFTALocationData('Village Hunt Reward 2', 37, 0x55b960),

    FFTALocationData('Fire! Fire! Reward 1', 38, 0x55b9a4),
    FFTALocationData('Fire! Fire! Reward 2', 38, 0x55b9a6),

    FFTALocationData('The Wanderer Reward 1', 39, 0x55b9ea),
    FFTALocationData('The Wanderer Reward 2', 39, 0x55b9ec),

    FFTALocationData('Battle Tourney Reward 1', 40, 0x55ba30),
    FFTALocationData('Battle Tourney Reward 2', 40, 0x55ba32),

    FFTALocationData('Mage Tourney Reward 1', 41, 0x55ba76),
    FFTALocationData('Mage Tourney Reward 2', 41, 0x55ba78),

    FFTALocationData('Swimming Meet Reward 1', 42, 0x55babc),
    FFTALocationData('Swimming Meet Reward 2', 42, 0x55babe),

    FFTALocationData('Clan Meet Reward 1', 43, 0x55bb02),
    FFTALocationData('Clan Meet Reward 2', 43, 0x55bb04),

    FFTALocationData('Snow in Lutia Reward 1', 44, 0x55bb48),
    FFTALocationData('Snow in Lutia Reward 2', 44, 0x55bb4a),

    FFTALocationData('Frosty Mage Reward 1', 45, 0x55bb8e),
    FFTALocationData('Frosty Mage Reward 2', 45, 0x55bb90),

    FFTALocationData('Prof in Trouble Reward 1', 46, 0x55bbd4),
    FFTALocationData('Prof in Trouble Reward 2', 46, 0x55bbd6),

    FFTALocationData('Hot Recipe Reward 1', 47, 0x55bc1a),
    FFTALocationData('Hot Recipe Reward 2', 47, 0x55bc1c),

    FFTALocationData('S.O.S. Reward 1', 48, 0x55bc60),
    FFTALocationData('S.O.S. Reward 2', 48, 0x55bc62),

    FFTALocationData('A Lost Ring Reward 1', 49, 0x55bca6),
    FFTALocationData('A Lost Ring Reward 2', 49, 0x55bca8),

    FFTALocationData('Staring Eyes Reward 1', 50, 0x55bcec),
    FFTALocationData('Staring Eyes Reward 2', 50, 0x55bcee),

    FFTALocationData('Desert Rose Reward 1', 51, 0x55bd32),
    FFTALocationData('Desert Rose Reward 2', 51, 0x55bd34),

    FFTALocationData('Friend Trouble Reward 1', 52, 0x55bd78),
    FFTALocationData('Friend Trouble Reward 2', 52, 0x55bd7a),

    FFTALocationData('Flesh & Bones Reward 1', 53, 0x55bdbe),
    FFTALocationData('Flesh & Bones Reward 2', 53, 0x55bdc0),

    FFTALocationData('For a Song Reward 1', 54, 0x55be04),
    FFTALocationData('For a Song Reward 2', 54, 0x55be06),

    FFTALocationData('White Flowers Reward 1', 55, 0x55be4a),
    FFTALocationData('White Flowers Reward 2', 55, 0x55be4c),

    FFTALocationData('New Antilaw Reward 1', 56, 0x55be90),
    FFTALocationData('New Antilaw Reward 2', 56, 0x55be92),

    FFTALocationData('Prison Break Reward 1', 57, 0x55bed6),
    FFTALocationData('Prison Break Reward 2', 57, 0x55bed8),

    FFTALocationData('Royal Ruins Reward 1', 58, 0x55bf1c),
    FFTALocationData('Royal Ruins Reward 2', 58, 0x55bf1e),

    FFTALocationData('Sketchy Thief Reward 1', 59, 0x55bf62),
    FFTALocationData('Sketchy Thief Reward 2', 59, 0x55bf64),

    FFTALocationData('Showdown! Reward 1', 60, 0x55bfa8),
    FFTALocationData('Showdown! Reward 2', 60, 0x55bfaa),

    FFTALocationData('Hit Again Reward 1', 61, 0x55bfee),
    FFTALocationData('Hit Again Reward 2', 61, 0x55bff0),

    FFTALocationData('Oasis Frogs Reward 1', 62, 0x55c034),
    FFTALocationData('Oasis Frogs Reward 2', 62, 0x55c036),

    FFTALocationData('Missing Prof Reward 1', 63, 0x55c07a),
    FFTALocationData('Missing Prof Reward 2', 63, 0x55c07c),

    FFTALocationData('Den of Evil Reward 1', 64, 0x55c0c0),
    FFTALocationData('Den of Evil Reward 2', 64, 0x55c0c2),

    FFTALocationData('Exploration Reward 1', 65, 0x55c106),
    FFTALocationData('Exploration Reward 2', 65, 0x55c108),

    FFTALocationData("A Dragon's Aid Reward 1", 66, 0x55c14c),
    FFTALocationData("A Dragon's Aid Reward 2", 66, 0x55c14e),

    FFTALocationData("Missing Meow Reward 1", 68, 0x55c1d8),
    FFTALocationData("Missing Meow Reward 2", 68, 0x55c1da),

    FFTALocationData("Fowl Thief Reward 1", 69, 0x55c21e),
    FFTALocationData("Fowl Thief Reward 2", 69, 0x55c220),

    FFTALocationData("Free Sprohm! Reward 1", 70, 0x55c264),
    FFTALocationData("Free Sprohm! Reward 2", 70, 0x55c266),

    FFTALocationData("Raven's Oath Reward 1", 71, 0x55c2aa),
    FFTALocationData("Raven's Oath Reward 2", 71, 0x55c2ac),

    FFTALocationData("Nubswood Base Reward 1", 72, 0x55c2f0),
    FFTALocationData("Nubswood Base Reward 2", 72, 0x55c2f2),

    FFTALocationData("Lutia Mop-Up Reward 1", 73, 0x55c336),
    FFTALocationData("Lutia Mop-Up Reward 2", 73, 0x55c338),

    FFTALocationData("Borzoi Falling Reward 1", 74, 0x55c37c),
    FFTALocationData("Borzoi Falling Reward 2", 74, 0x55c37e),

    FFTALocationData("Cadoan Watch Reward 1", 75, 0x55c3c2),
    FFTALocationData("Cadoan Watch Reward 2", 75, 0x55c3c4),

    FFTALocationData("Free Cadoan! Reward 1", 76, 0x55c408),
    FFTALocationData("Free Cadoan! Reward 2", 76, 0x55c40a),

    FFTALocationData("Fire Sigil Reward 1", 77, 0x55c44e),
    FFTALocationData("Fire Sigil Reward 2", 77, 0x55c450),

    FFTALocationData("Free Baguba! Reward 1", 78, 0x55c494),
    FFTALocationData("Free Baguba! Reward 2", 78, 0x55c496),

    FFTALocationData("Water Sigil Reward 1", 79, 0x55c4da),
    FFTALocationData("Water Sigil Reward 2", 79, 0x55c4dc),

    FFTALocationData("Wind Sigil Reward 1", 80, 0x55c520),
    FFTALocationData("Wind Sigil Reward 2", 80, 0x55c522),

    FFTALocationData("Earth Sigil Reward 1", 81, 0x55c566),
    FFTALocationData("Earth Sigil Reward 2", 81, 0x55c568),

    FFTALocationData("The Redwings Reward 1", 82, 0x55c5ac),
    FFTALocationData("The Redwings Reward 2", 82, 0x55c5ae),

    FFTALocationData("Free Muscadet! Reward 1", 83, 0x55c5f2),
    FFTALocationData("Free Muscadet! Reward 2", 83, 0x55c5f4),

    FFTALocationData("Foreign Fiend Reward 1", 84, 0x55c638),
    FFTALocationData("Foreign Fiend Reward 2", 84, 0x55c63a),

    FFTALocationData("Foreign Fiend 2 Reward 1", 85, 0x55c67e),
    FFTALocationData("Foreign Fiend 2 Reward 2", 85, 0x55c680),

    FFTALocationData("Foreign Fiend 3 Reward 1", 86, 0x55c6c4),
    FFTALocationData("Foreign Fiend 3 Reward 2", 86, 0x55c6c6),

    FFTALocationData("Last Stand Reward 1", 87, 0x55c70a),
    FFTALocationData("Last Stand Reward 2", 87, 0x55c70c),

    FFTALocationData("Free Bervenia! Reward 1", 88, 0x55c750),
    FFTALocationData("Free Bervenia! Reward 2", 88, 0x55c752),

    FFTALocationData("The Worldwyrm Reward 1", 89, 0x55c796),
    FFTALocationData("The Worldwyrm Reward 2", 89, 0x55c798),

    FFTALocationData("Moogle Bride Reward 1", 90, 0x55c7dc),
    FFTALocationData("Moogle Bride Reward 2", 90, 0x55c7de),

    FFTALocationData("Clan Law Reward 1", 91, 0x55c822),
    FFTALocationData("Clan Law Reward 2", 91, 0x55c824),

    FFTALocationData("Challengers? Reward 1", 92, 0x55c868),
    FFTALocationData("Challengers? Reward 2", 92, 0x55c86a),

    FFTALocationData("Cursed Bride Reward 1", 93, 0x55c8ae),
    FFTALocationData("Cursed Bride Reward 2", 93, 0x55c8b0),

    FFTALocationData("Flan Breakout Reward 1", 94, 0x55c8f4),
    FFTALocationData("Flan Breakout Reward 2", 94, 0x55c8f6),

    FFTALocationData("Sorry, Friend Reward 1", 95, 0x55c93a),
    FFTALocationData("Sorry, Friend Reward 2", 95, 0x55c93c),

    FFTALocationData("Carrot! Reward 1", 96, 0x55c980),
    FFTALocationData("Carrot! Reward 2", 96, 0x55c982),

    FFTALocationData("Shadow Clan Reward 1", 97, 0x55c9c6),
    FFTALocationData("Shadow Clan Reward 2", 97, 0x55c9c8),

    FFTALocationData("The Dark Blade Reward 1", 98, 0x55ca0c),
    FFTALocationData("The Dark Blade Reward 2", 98, 0x55ca0e),

    FFTALocationData("The Hero Blade Reward 1", 99, 0x55ca52),
    FFTALocationData("The Hero Blade Reward 2", 99, 0x55ca54),

    FFTALocationData("The Fey Blade Reward 1", 100, 0x55ca98),
    FFTALocationData("The Fey Blade Reward 2", 100, 0x55ca9a),

    FFTALocationData("Fiend Run Reward 1", 101, 0x55cade),
    FFTALocationData("Fiend Run Reward 2", 101, 0x55cae0),

    FFTALocationData("Clan Roundup Reward 1", 102, 0x55cb24),
    FFTALocationData("Clan Roundup Reward 2", 102, 0x55cb26),

    FFTALocationData("Wyrms Awaken Reward 1", 103, 0x55cb6a),
    FFTALocationData("Wyrms Awaken Reward 2", 103, 0x55cb6c),

    FFTALocationData("Yellow Powerz Reward 1", 104, 0x55cbb0),
    FFTALocationData("Yellow Powerz Reward 2", 104, 0x55cbb2),

    FFTALocationData("Blue Geniuses Reward 1", 105, 0x55cbf6),
    FFTALocationData("Blue Geniuses Reward 2", 105, 0x55cbf8),

    FFTALocationData("Brown Rabbits Reward 1", 106, 0x55cc3c),
    FFTALocationData("Brown Rabbits Reward 2", 106, 0x55cc3e),

    FFTALocationData("White Kupos Reward 1", 107, 0x55cc82),
    FFTALocationData("White Kupos Reward 2", 107, 0x55cc84),

    FFTALocationData("Mythril Rush Reward 1", 108, 0x55ccc8),
    FFTALocationData("Mythril Rush Reward 2", 108, 0x55ccca),

    FFTALocationData("Stolen Scoop Reward 1", 109, 0x55cd0e),
    FFTALocationData("Stolen Scoop Reward 2", 109, 0x55cd10),

    FFTALocationData("Smuggle Bust Reward 1", 110, 0x55cd54),
    FFTALocationData("Smuggle Bust Reward 2", 110, 0x55cd56),

    FFTALocationData("Resistance Reward 1", 111, 0x55cd9a),
    FFTALocationData("Resistance Reward 2", 111, 0x55cd9c),

    FFTALocationData("Old Friends Reward 1", 113, 0x55ce26),
    FFTALocationData("Old Friends Reward 2", 113, 0x55ce28),

    FFTALocationData("Poachers Reward 1", 114, 0x55ce6c),
    FFTALocationData("Poachers Reward 2", 114, 0x55ce6e),

    FFTALocationData("Snow Fairy Reward 1", 115, 0x55ceb2),
    FFTALocationData("Snow Fairy Reward 2", 115, 0x55ceb4),

    FFTALocationData("Revenge Reward 1", 116, 0x55cef8),
    FFTALocationData("Revenge Reward 2", 116, 0x55cefa),

    FFTALocationData("Retrieve Mail Reward 1", 117, 0x55cf3e),
    FFTALocationData("Retrieve Mail Reward 2", 117, 0x55cf40),

    FFTALocationData("A Challenge Reward 1", 118, 0x55cf84),
    FFTALocationData("A Challenge Reward 2", 118, 0x55cf86),

    # First dispatch mission
    # FFTALocationData("Watching You Reward 1", 125, 0x55d16e),
    # FFTALocationData("Watching You Reward 2", 125, 0x55d170),

    FFTALocationData("Reconciliation Reward 1", 374, 0x561584),
    FFTALocationData("Reconciliation Reward 2", 374, 0x561586),

    FFTALocationData("With Babus Reward 1", 376, 0x561610),
    FFTALocationData("With Babus Reward 2", 376, 0x561612),

    # Ritz might be required to be recruited
    FFTALocationData("Mortal Snow Reward 1", 377, 0x561656),
    FFTALocationData("Mortal Snow Reward 2", 377, 0x561658),

    FFTALocationData("Cleanup Time Reward 1", 379, 0x5616e2),
    FFTALocationData("Cleanup Time Reward 2", 379, 0x5616e4),

    FFTALocationData("No Arms Rule Reward 1", 385, 0x561886),
    FFTALocationData("No Arms Rule Reward 2", 385, 0x561888),

    FFTALocationData("Kissing Rule Reward 1", 386, 0x5618cc),
    FFTALocationData("Kissing Rule Reward 2", 386, 0x5618ce),

    FFTALocationData("Immunity Pass Reward 1", 387, 0x561912),
    FFTALocationData("Immunity Pass Reward 2", 387, 0x561914),

    FFTALocationData("No Full HP Reward 1", 388, 0x561958),
    FFTALocationData("No Full HP Reward 2", 388, 0x56195a),

    FFTALocationData("No Literacy Reward 1", 389, 0x56199e),
    FFTALocationData("No Literacy Reward 2", 389, 0x5619a0),

    FFTALocationData("Favoritism Reward 1", 390, 0x5619e4),
    FFTALocationData("Favoritism Reward 2", 390, 0x5619e6),

    FFTALocationData("No Answers Reward 1", 391, 0x561a2a),
    FFTALocationData("No Answers Reward 2", 391, 0x561a2c),

    FFTALocationData("No Jumping Reward 1", 392, 0x561a70),
    FFTALocationData("No Jumping Reward 2", 392, 0x561a72),
]

print(len(FFTALocations))
bitflag_index = 2
byte_i = 0
# Setting up the mission complete flags
for index in range(0, len(FFTALocations), 2):
    print(index)
    #if byte_i == 2 and bitflag_index == 5:
    #    bitflag_index = 6

    if byte_i == 3 and bitflag_index == 1:
        bitflag_index = 3

    elif byte_i == 8 and bitflag_index == 5:
        bitflag_index = 6

    elif byte_i == 14 and bitflag_index == 2:
        bitflag_index = 3

    elif byte_i == 15 and bitflag_index == 1:
        bitflag_index = 0
        byte_i = 47

    elif byte_i == 47 and bitflag_index == 0:
        bitflag_index = 1

    elif byte_i == 47 and bitflag_index == 1:
        bitflag_index = 2

    elif byte_i == 47 and bitflag_index == 4:
        bitflag_index = 5

    elif byte_i == 47 and bitflag_index == 6:
        bitflag_index = 3
        byte_i = 48

    MissionGroups.append(tuple([FFTALocations[index], FFTALocations[(index + 1)], bitflags[bitflag_index], byte_i]))

    bitflag_index = bitflag_index + 1
    if bitflag_index > 7:
        bitflag_index = 0
        byte_i = byte_i + 1


#for index, mission_group in enumerate(MissionGroups):
#    print("Mission group index: " + str(index) + " mission group [0] consists of: " + mission_group[0].name)
#    print("Mission group index: " + str(index) + " mission group [1] consists of: " + mission_group[1].name)

def create_location_label_to_id_map() -> Dict[str, int]:
    """
    Creates a map from location labels to their AP location id (address)
    """
    label_to_id_map: Dict[str, int] = {}
    for location in FFTALocations:
        label_to_id_map[location.name] = location.rom_address

    return label_to_id_map


location_flags: Dict



