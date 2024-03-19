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
DispatchMissionGroups = []
bitflags = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]

FFTALocations: typing.List[FFTALocationData] = [
    # Decide whether to use address or memory offset from data array

    FFTALocationData("Herb Picking Reward 1", 0, 0x55AF40),
    FFTALocationData("Herb Picking Reward 2", 0, 0x55AF42),
    FFTALocationData("Herb Picking Reward 3", 0, 0x55AF44),
    FFTALocationData("Herb Picking Reward 4", 0, 0x55AF46),

    FFTALocationData("Thesis Hunt Reward 1", 1, 0x55AF86),
    FFTALocationData("Thesis Hunt Reward 2", 1, 0x55AF88),
    FFTALocationData("Thesis Hunt Reward 3", 1, 0x55AF8A),
    FFTALocationData("Thesis Hunt Reward 4", 1, 0x55AF8C),

    FFTALocationData("The Cheetahs Reward 1", 2, 0x55AFCC),
    FFTALocationData("The Cheetahs Reward 2", 2, 0x55AFCE),
    FFTALocationData("The Cheetahs Reward 3", 2, 0x55AFD0),
    FFTALocationData("The Cheetahs Reward 4", 2, 0x55AFD2),

    FFTALocationData("Desert Peril Reward 1", 3, 0x55b012),
    FFTALocationData("Desert Peril Reward 2", 3, 0x55b014),
    FFTALocationData("Desert Peril Reward 3", 3, 0x55B016),
    FFTALocationData("Desert Peril Reward 4", 3, 0x55B018),

    FFTALocationData("Twisted Flow Reward 1", 4, 0x55b058),
    FFTALocationData("Twisted Flow Reward 2", 4, 0x55b05a),
    FFTALocationData("Twisted Flow Reward 3", 4, 0x55B05C),
    FFTALocationData("Twisted Flow Reward 4", 4, 0x55B05E),

    FFTALocationData("Antilaws Reward 1", 5, 0x55b09e),
    FFTALocationData("Antilaws Reward 2", 5, 0x55b0a0),
    FFTALocationData("Antilaws Reward 3", 5, 0x55B0A2),
    FFTALocationData("Antilaws Reward 4", 5, 0x55B0A4),

    FFTALocationData("Diamond Rain Reward 1", 6, 0x55b0e4),
    FFTALocationData("Diamond Rain Reward 2", 6, 0x55b0e6),
    FFTALocationData("Diamond Rain Reward 3", 6, 0x55B0E8),
    FFTALocationData("Diamond Rain Reward 4", 6, 0x55B0EA),

    FFTALocationData("Hot Awakening Reward 1", 7, 0x55b12a),
    FFTALocationData("Hot Awakening Reward 2", 7, 0x55b12c),
    FFTALocationData("Hot Awakening Reward 3", 7, 0x55B12E),
    FFTALocationData("Hot Awakening Reward 4", 7, 0x55B130),

    FFTALocationData("Magic Wood Reward 1", 8, 0x55b170),
    FFTALocationData("Magic Wood Reward 2", 8, 0x55b172),
    FFTALocationData("Magic Wood Reward 3", 8, 0x55B174),
    FFTALocationData("Magic Wood Reward 4", 8, 0x55B176),

    FFTALocationData("Emerald Keep Reward 1", 9, 0x55b1b6),
    FFTALocationData("Emerald Keep Reward 2", 9, 0x55b1b8),
    FFTALocationData("Emerald Keep Reward 3", 9, 0x55B1BA),
    FFTALocationData("Emerald Keep Reward 4", 9, 0x55B1BC),

    FFTALocationData("Pale Company Reward 1", 10,  0x55b1fc),
    FFTALocationData("Pale Company Reward 2", 10,  0x55b1fe),
    FFTALocationData("Pale Company Reward 3", 10, 0x55B200),
    FFTALocationData("Pale Company Reward 4", 10, 0x55B202),

    FFTALocationData("Jagd Hunt Reward 1", 11, 0x55b242),
    FFTALocationData("Jagd Hunt Reward 2", 11, 0x55b244),
    FFTALocationData("Jagd Hunt Reward 3", 11, 0x55B246),
    FFTALocationData("Jagd Hunt Reward 4", 11, 0x55B248),

    FFTALocationData("The Bounty Reward 1", 12, 0x55b288),
    FFTALocationData("The Bounty Reward 2", 12, 0x55b28a),
    FFTALocationData("The Bounty Reward 3", 12, 0x55B28C),
    FFTALocationData("The Bounty Reward 4", 12, 0x55B28E),

    FFTALocationData("Golden Clock Reward 1", 13, 0x55b2ce),
    FFTALocationData("Golden Clock Reward 2", 13, 0x55b2d0),
    FFTALocationData("Golden Clock Reward 3", 13, 0x55B2D2),
    FFTALocationData("Golden Clock Reward 4", 13, 0x55B2D4),

    FFTALocationData("Scouring Time Reward 1", 14, 0x55b314),
    FFTALocationData("Scouring Time Reward 2", 14, 0x55b316),
    FFTALocationData("Scouring Time Reward 3", 14, 0x55B318),
    FFTALocationData("Scouring Time Reward 4", 14, 0x55B31A),

    FFTALocationData("The Big Find Reward 1", 15, 0x55b35a),
    FFTALocationData("The Big Find Reward 2", 15, 0x55b35c),
    FFTALocationData("The Big Find Reward 3", 15, 0x55B35E),
    FFTALocationData("The Big Find Reward 4", 15, 0x55B360),

    FFTALocationData("Desert Patrol Reward 1", 16, 0x55b3a0),
    FFTALocationData("Desert Patrol Reward 2", 16, 0x55b3a2),
    FFTALocationData("Desert Patrol Reward 3", 16, 0x55B3A4),
    FFTALocationData("Desert Patrol Reward 4", 16, 0x55B3A6),

    FFTALocationData("Quiet Sands Reward 1", 17, 0x55b3e6),
    FFTALocationData("Quiet Sands Reward 2", 17, 0x55b3e8),
    FFTALocationData("Quiet Sands Reward 3", 17, 0x55B3EA),
    FFTALocationData("Quiet Sands Reward 4", 17, 0x55B3EC),

    FFTALocationData("Materite Now! Reward 1", 18, 0x55b42c),
    FFTALocationData("Materite Now! Reward 2", 18, 0x55b42e),
    FFTALocationData("Materite Now! Reward 3", 18, 0x55B430),
    FFTALocationData("Materite Now! Reward 4", 18, 0x55B432),

    FFTALocationData("Present Day Reward 1", 19, 0x55b472),
    FFTALocationData("Present Day Reward 2", 19, 0x55b474),
    FFTALocationData("Present Day Reward 3", 19, 0x55B476),
    FFTALocationData("Present Day Reward 4", 19, 0x55B478),

    FFTALocationData("Hidden Vein Reward 1", 20, 0x55b4b8),
    FFTALocationData("Hidden Vein Reward 2", 20, 0x55b4ba),
    FFTALocationData("Hidden Vein Reward 3", 20, 0x55B4BC),
    FFTALocationData("Hidden Vein Reward 4", 20, 0x55B4BE),

    FFTALocationData("To Ambervale Reward 1", 21, 0x55b4fe),
    FFTALocationData("To Ambervale Reward 2", 21, 0x55b500),
    FFTALocationData("To Ambervale Reward 3", 21, 0x55B502),
    FFTALocationData("To Ambervale Reward 4", 21, 0x55B504),

    FFTALocationData("Over The Hill Reward 1", 22, 0x55b544),
    FFTALocationData("Over The Hill Reward 2", 22, 0x55b546),
    FFTALocationData("Over The Hill Reward 3", 22, 0x55B548),
    FFTALocationData("Over The Hill Reward 4", 22, 0x55B54A),

    # Non story missions
    FFTALocationData("Wanted! Black Mage Dolce Reward 1", 25, 0x55b616),
    FFTALocationData("Wanted! Black Mage Dolce Reward 2", 25, 0x55b618),
    FFTALocationData("Wanted! Black Mage Dolce Reward 3", 25, 0x55B61A),
    FFTALocationData("Wanted! Black Mage Dolce Reward 4", 25, 0x55B61C),

    FFTALocationData("Wanted! Gabbana Brothers Reward 1", 26, 0x55b65c),
    FFTALocationData("Wanted! Gabbana Brothers Reward 2", 26,  0x55b65e),
    FFTALocationData("Wanted! Gabbana Brothers Reward 3", 26, 0x55B660),
    FFTALocationData("Wanted! Gabbana Brothers Reward 4", 26, 0x55B662),

    FFTALocationData("Wanted! Godeye Reward 1", 27, 0x55b6a2),
    FFTALocationData("Wanted! Godeye Reward 2", 27,  0x55b6a4),
    FFTALocationData("Wanted! Godeye Reward 3", 27, 0x55B6A6),
    FFTALocationData("Wanted! Godeye Reward 4", 27, 0x55B6A8),

    FFTALocationData("Wanted! Swampking Reward 1", 28, 0x55b6e8),
    FFTALocationData("Wanted! Swampking Reward 2", 28,  0x55b6ea),
    FFTALocationData("Wanted! Swampking Reward 3", 28, 0x55B6EC),
    FFTALocationData("Wanted! Swampking Reward 4", 28, 0x55B6EE),

    FFTALocationData("Wanted! Killer Rayne Reward 1", 29, 0x55b72e),
    FFTALocationData("Wanted! Killer Rayne Reward 2", 29,  0x55b730),
    FFTALocationData("Wanted! Killer Rayne Reward 3", 29, 0x55B732),
    FFTALocationData("Wanted! Killer Rayne Reward 4", 29, 0x55B734),

    FFTALocationData("Wanted! Dark Duke Lodion Reward 1", 30, 0x55b774),
    FFTALocationData("Wanted! Dark Duke Lodion Reward 2", 30,  0x55b776),
    FFTALocationData("Wanted! Dark Duke Lodion Reward 3", 30, 0x55B778),
    FFTALocationData("Wanted! Dark Duke Lodion Reward 4", 30, 0x55B77A),

    FFTALocationData("Ruby Red Reward 1", 31, 0x55b7ba),
    FFTALocationData("Ruby Red Reward 2", 31,  0x55b7bc),
    FFTALocationData("Ruby Red Reward 3", 31, 0x55B7BE),
    FFTALocationData("Ruby Red Reward 4", 31, 0x55B7C0),

    FFTALocationData("Tower Ruins Reward 1", 32, 0x55b800),
    FFTALocationData("Tower Ruins Reward 2", 32, 0x55b802),
    FFTALocationData("Tower Ruins Reward 3", 32, 0x55B804),
    FFTALocationData("Tower Ruins Reward 4", 32, 0x55B806),

    FFTALocationData("Battle in Aisen Reward 1", 33, 0x55b846),
    FFTALocationData("Battle in Aisen Reward 2", 33, 0x55b848),
    FFTALocationData("Battle in Aisen Reward 3", 33, 0x55B84A),
    FFTALocationData("Battle in Aisen Reward 4", 33, 0x55B84C),

    FFTALocationData("Magewyrm Reward 1", 34, 0x55b88c),
    FFTALocationData("Magewyrm Reward 2", 34, 0x55b88e),
    FFTALocationData("Magewyrm Reward 3", 34, 0x55B890),
    FFTALocationData("Magewyrm Reward 4", 34, 0x55B892),

    FFTALocationData("Salika Keep Reward 1", 35, 0x55b8d2),
    FFTALocationData("Salika Keep Reward 2", 35, 0x55b8d4),
    FFTALocationData("Salika Keep Reward 3", 35, 0x55B8D6),
    FFTALocationData("Salika Keep Reward 4", 35, 0x55B8D8),

    FFTALocationData("Twin Swords Reward 1", 36, 0x55b918),
    FFTALocationData("Twin Swords Reward 2", 36, 0x55b91a),
    FFTALocationData("Twin Swords Reward 3", 36, 0x55B91C),
    FFTALocationData("Twin Swords Reward 4", 36, 0x55B91E),

    FFTALocationData("Village Hunt Reward 1", 37, 0x55b95e),
    FFTALocationData("Village Hunt Reward 2", 37, 0x55b960),
    FFTALocationData("Village Hunt Reward 3", 37, 0x55B962),
    FFTALocationData("Village Hunt Reward 4", 37, 0x55B964),

    FFTALocationData("Fire! Fire! Reward 1", 38, 0x55b9a4),
    FFTALocationData("Fire! Fire! Reward 2", 38, 0x55b9a6),
    FFTALocationData("Fire! Fire! Reward 3", 38, 0x55B9A8),
    FFTALocationData("Fire! Fire! Reward 4", 38, 0x55B9AA),

    FFTALocationData("The Wanderer Reward 1", 39, 0x55b9ea),
    FFTALocationData("The Wanderer Reward 2", 39, 0x55b9ec),
    FFTALocationData("The Wanderer Reward 3", 39, 0x55B9EE),
    FFTALocationData("The Wanderer Reward 4", 39, 0x55B9F0),

    FFTALocationData("Battle Tourney Reward 1", 40, 0x55ba30),
    FFTALocationData("Battle Tourney Reward 2", 40, 0x55ba32),
    FFTALocationData("Battle Tourney Reward 3", 40, 0x55BA34),
    FFTALocationData("Battle Tourney Reward 4", 40, 0x55BA36),

    FFTALocationData("Mage Tourney Reward 1", 41, 0x55ba76),
    FFTALocationData("Mage Tourney Reward 2", 41, 0x55ba78),
    FFTALocationData("Mage Tourney Reward 3", 41, 0x55BA7A),
    FFTALocationData("Mage Tourney Reward 4", 41, 0x55BA7C),

    FFTALocationData("Swimming Meet Reward 1", 42, 0x55babc),
    FFTALocationData("Swimming Meet Reward 2", 42, 0x55babe),
    FFTALocationData("Swimming Meet Reward 3", 42, 0x55BAC0),
    FFTALocationData("Swimming Meet Reward 4", 42, 0x55BAC2),

    FFTALocationData("Clan League Reward 1", 43, 0x55bb02),
    FFTALocationData("Clan League Reward 2", 43, 0x55bb04),
    FFTALocationData("Clan League Reward 3", 43, 0x55BB06),
    FFTALocationData("Clan League Reward 4", 43, 0x55BB08),

    FFTALocationData("Snow in Lutia Reward 1", 44, 0x55bb48),
    FFTALocationData("Snow in Lutia Reward 2", 44, 0x55bb4a),
    FFTALocationData("Snow in Lutia Reward 3", 44, 0x55BB4C),
    FFTALocationData("Snow in Lutia Reward 4", 44, 0x55BB4E),

    FFTALocationData("Frosty Mage Reward 1", 45, 0x55bb8e),
    FFTALocationData("Frosty Mage Reward 2", 45, 0x55bb90),
    FFTALocationData("Frosty Mage Reward 3", 45, 0x55BB92),
    FFTALocationData("Frosty Mage Reward 4", 45, 0x55BB94),

    FFTALocationData("Prof in Trouble Reward 1", 46, 0x55bbd4),
    FFTALocationData("Prof in Trouble Reward 2", 46, 0x55bbd6),
    FFTALocationData("Prof in Trouble Reward 3", 46, 0x55BBD8),
    FFTALocationData("Prof in Trouble Reward 4", 46, 0x55BBDA),

    FFTALocationData("Hot Recipe Reward 1", 47, 0x55bc1a),
    FFTALocationData("Hot Recipe Reward 2", 47, 0x55bc1c),
    FFTALocationData("Hot Recipe Reward 3", 47, 0x55BC1E),
    FFTALocationData("Hot Recipe Reward 4", 47, 0x55BC20),

    FFTALocationData("S.O.S. Reward 1", 48, 0x55bc60),
    FFTALocationData("S.O.S. Reward 2", 48, 0x55bc62),
    FFTALocationData("S.O.S. Reward 3", 48, 0x55BC64),
    FFTALocationData("S.O.S. Reward 4", 48, 0x55BC66),

    FFTALocationData("A Lost Ring Reward 1", 49, 0x55bca6),
    FFTALocationData("A Lost Ring Reward 2", 49, 0x55bca8),
    FFTALocationData("A Lost Ring Reward 3", 49, 0x55BCAA),
    FFTALocationData("A Lost Ring Reward 4", 49, 0x55BCAC),

    FFTALocationData("Staring Eyes Reward 1", 50, 0x55bcec),
    FFTALocationData("Staring Eyes Reward 2", 50, 0x55bcee),
    FFTALocationData("Staring Eyes Reward 3", 50, 0x55BCF0),
    FFTALocationData("Staring Eyes Reward 4", 50, 0x55BCF2),

    FFTALocationData("Desert Rose Reward 1", 51, 0x55bd32),
    FFTALocationData("Desert Rose Reward 2", 51, 0x55bd34),
    FFTALocationData("Desert Rose Reward 3", 51, 0x55BD36),
    FFTALocationData("Desert Rose Reward 4", 51, 0x55BD38),

    FFTALocationData("Friend Trouble Reward 1", 52, 0x55bd78),
    FFTALocationData("Friend Trouble Reward 2", 52, 0x55bd7a),
    FFTALocationData("Friend Trouble Reward 3", 52, 0x55BD7C),
    FFTALocationData("Friend Trouble Reward 4", 52, 0x55BD7E),

    FFTALocationData("Flesh & Bones Reward 1", 53, 0x55bdbe),
    FFTALocationData("Flesh & Bones Reward 2", 53, 0x55bdc0),
    FFTALocationData("Flesh & Bones Reward 3", 53, 0x55BDC2),
    FFTALocationData("Flesh & Bones Reward 4", 53, 0x55BDC4),

    FFTALocationData("For a Song Reward 1", 54, 0x55be04),
    FFTALocationData("For a Song Reward 2", 54, 0x55be06),
    FFTALocationData("For a Song Reward 3", 54, 0x55BE08),
    FFTALocationData("For a Song Reward 4", 54, 0x55BE0A),

    FFTALocationData("White Flowers Reward 1", 55, 0x55be4a),
    FFTALocationData("White Flowers Reward 2", 55, 0x55be4c),
    FFTALocationData("White Flowers Reward 3", 55, 0x55BE4E),
    FFTALocationData("White Flowers Reward 4", 55, 0x55BE50),

    FFTALocationData("New Antilaw Reward 1", 56, 0x55be90),
    FFTALocationData("New Antilaw Reward 2", 56, 0x55be92),
    FFTALocationData("New Antilaw Reward 3", 56, 0x55BE94),
    FFTALocationData("New Antilaw Reward 4", 56, 0x55BE96),

    FFTALocationData("Prison Break Reward 1", 57, 0x55bed6),
    FFTALocationData("Prison Break Reward 2", 57, 0x55bed8),
    FFTALocationData("Prison Break Reward 3", 57, 0x55BEDA),
    FFTALocationData("Prison Break Reward 4", 57, 0x55BEDC),

    FFTALocationData("Royal Ruins Reward 1", 58, 0x55bf1c),
    FFTALocationData("Royal Ruins Reward 2", 58, 0x55bf1e),
    FFTALocationData("Royal Ruins Reward 3", 58, 0x55BF20),
    FFTALocationData("Royal Ruins Reward 4", 58, 0x55BF22),

    FFTALocationData("Sketchy Thief Reward 1", 59, 0x55bf62),
    FFTALocationData("Sketchy Thief Reward 2", 59, 0x55bf64),
    FFTALocationData("Sketchy Thief Reward 3", 59, 0x55BF66),
    FFTALocationData("Sketchy Thief Reward 4", 59, 0x55BF68),

    FFTALocationData("Showdown! Reward 1", 60, 0x55bfa8),
    FFTALocationData("Showdown! Reward 2", 60, 0x55bfaa),
    FFTALocationData("Showdown! Reward 3", 60, 0x55BFAC),
    FFTALocationData("Showdown! Reward 4", 60, 0x55BFAE),

    FFTALocationData("Hit Again Reward 1", 61, 0x55bfee),
    FFTALocationData("Hit Again Reward 2", 61, 0x55bff0),
    FFTALocationData("Hit Again Reward 3", 61, 0x55BFF2),
    FFTALocationData("Hit Again Reward 4", 61, 0x55BFF4),

    FFTALocationData("Oasis Frogs Reward 1", 62, 0x55c034),
    FFTALocationData("Oasis Frogs Reward 2", 62, 0x55c036),
    FFTALocationData("Oasis Frogs Reward 3", 62, 0x55C038),
    FFTALocationData("Oasis Frogs Reward 4", 62, 0x55C03A),

    FFTALocationData("Missing Prof Reward 1", 63, 0x55c07a),
    FFTALocationData("Missing Prof Reward 2", 63, 0x55c07c),
    FFTALocationData("Missing Prof Reward 3", 63, 0x55C07E),
    FFTALocationData("Missing Prof Reward 4", 63, 0x55C080),

    FFTALocationData("Den of Evil Reward 1", 64, 0x55c0c0),
    FFTALocationData("Den of Evil Reward 2", 64, 0x55c0c2),
    FFTALocationData("Den of Evil Reward 3", 64, 0x55C0C4),
    FFTALocationData("Den of Evil Reward 4", 64, 0x55C0C6),

    FFTALocationData("Exploration Reward 1", 65, 0x55c106),
    FFTALocationData("Exploration Reward 2", 65, 0x55c108),
    FFTALocationData("Exploration Reward 3", 65, 0x55C10A),
    FFTALocationData("Exploration Reward 4", 65, 0x55C10C),

    FFTALocationData("A Dragon's Aid Reward 1", 66, 0x55c14c),
    FFTALocationData("A Dragon's Aid Reward 2", 66, 0x55c14e),
    FFTALocationData("A Dragon's Aid Reward 3", 66, 0x55C150),
    FFTALocationData("A Dragon's Aid Reward 4", 66, 0x55C152),

    FFTALocationData("Missing Meow Reward 1", 68, 0x55c1d8),
    FFTALocationData("Missing Meow Reward 2", 68, 0x55c1da),
    FFTALocationData("Missing Meow Reward 3", 68, 0x55C1DC),
    FFTALocationData("Missing Meow Reward 4", 68, 0x55C1DE),

    FFTALocationData("Fowl Thief Reward 1", 69, 0x55c21e),
    FFTALocationData("Fowl Thief Reward 2", 69, 0x55c220),
    FFTALocationData("Fowl Thief Reward 3", 69, 0x55C222),
    FFTALocationData("Fowl Thief Reward 4", 69, 0x55C224),

    FFTALocationData("Free Sprohm! Reward 1", 70, 0x55c264),
    FFTALocationData("Free Sprohm! Reward 2", 70, 0x55c266),
    FFTALocationData("Free Sprohm! Reward 3", 70, 0x55C268),
    FFTALocationData("Free Sprohm! Reward 4", 70, 0x55C26A),

    FFTALocationData("Raven's Oath Reward 1", 71, 0x55c2aa),
    FFTALocationData("Raven's Oath Reward 2", 71, 0x55c2ac),
    FFTALocationData("Raven's Oath Reward 3", 71, 0x55C2AE),
    FFTALocationData("Raven's Oath Reward 4", 71, 0x55C2B0),

    FFTALocationData("Nubswood Base Reward 1", 72, 0x55c2f0),
    FFTALocationData("Nubswood Base Reward 2", 72, 0x55c2f2),
    FFTALocationData("Nubswood Base Reward 3", 72, 0x55C2F4),
    FFTALocationData("Nubswood Base Reward 4", 72, 0x55C2F6),

    FFTALocationData("Lutia Mop-Up Reward 1", 73, 0x55c336),
    FFTALocationData("Lutia Mop-Up Reward 2", 73, 0x55c338),
    FFTALocationData("Lutia Mop-Up Reward 3", 73, 0x55C33A),
    FFTALocationData("Lutia Mop-Up Reward 4", 73, 0x55C33C),

    FFTALocationData("Borzoi Falling Reward 1", 74, 0x55c37c),
    FFTALocationData("Borzoi Falling Reward 2", 74, 0x55c37e),
    FFTALocationData("Borzoi Falling Reward 3", 74, 0x55C380),
    FFTALocationData("Borzoi Falling Reward 4", 74, 0x55C382),

    FFTALocationData("Cadoan Watch Reward 1", 75, 0x55c3c2),
    FFTALocationData("Cadoan Watch Reward 2", 75, 0x55c3c4),
    FFTALocationData("Cadoan Watch Reward 3", 75, 0x55C3C6),
    FFTALocationData("Cadoan Watch Reward 4", 75, 0x55C3C8),

    FFTALocationData("Free Cadoan! Reward 1", 76, 0x55c408),
    FFTALocationData("Free Cadoan! Reward 2", 76, 0x55c40a),
    FFTALocationData("Free Cadoan! Reward 3", 76, 0x55C40C),
    FFTALocationData("Free Cadoan! Reward 4", 76, 0x55C40E),

    FFTALocationData("Fire Sigil Reward 1", 77, 0x55c44e),
    FFTALocationData("Fire Sigil Reward 2", 77, 0x55c450),
    FFTALocationData("Fire Sigil Reward 3", 77, 0x55C452),
    FFTALocationData("Fire Sigil Reward 4", 77, 0x55C454),

    FFTALocationData("Free Baguba! Reward 1", 78, 0x55c494),
    FFTALocationData("Free Baguba! Reward 2", 78, 0x55c496),
    FFTALocationData("Free Baguba! Reward 3", 78, 0x55C498),
    FFTALocationData("Free Baguba! Reward 4", 78, 0x55C49A),

    FFTALocationData("Water Sigil Reward 1", 79, 0x55c4da),
    FFTALocationData("Water Sigil Reward 2", 79, 0x55c4dc),
    FFTALocationData("Water Sigil Reward 3", 79, 0x55C4DE),
    FFTALocationData("Water Sigil Reward 4", 79, 0x55C4E0),

    FFTALocationData("Wind Sigil Reward 1", 80, 0x55c520),
    FFTALocationData("Wind Sigil Reward 2", 80, 0x55c522),
    FFTALocationData("Wind Sigil Reward 3", 80, 0x55C524),
    FFTALocationData("Wind Sigil Reward 4", 80, 0x55C526),

    FFTALocationData("Earth Sigil Reward 1", 81, 0x55c566),
    FFTALocationData("Earth Sigil Reward 2", 81, 0x55c568),
    FFTALocationData("Earth Sigil Reward 3", 81, 0x55C56A),
    FFTALocationData("Earth Sigil Reward 4", 81, 0x55C56C),

    FFTALocationData("The Redwings Reward 1", 82, 0x55c5ac),
    FFTALocationData("The Redwings Reward 2", 82, 0x55c5ae),
    FFTALocationData("The Redwings Reward 3", 82, 0x55C5B0),
    FFTALocationData("The Redwings Reward 4", 82, 0x55C5B2),

    FFTALocationData("Free Muscadet! Reward 1", 83, 0x55c5f2),
    FFTALocationData("Free Muscadet! Reward 2", 83, 0x55c5f4),
    FFTALocationData("Free Muscadet! Reward 3", 83, 0x55C5F6),
    FFTALocationData("Free Muscadet! Reward 4", 83, 0x55C5F8),

    FFTALocationData("Foreign Fiend Reward 1", 84, 0x55c638),
    FFTALocationData("Foreign Fiend Reward 2", 84, 0x55c63a),
    FFTALocationData("Foreign Fiend Reward 3", 84, 0x55C63C),
    FFTALocationData("Foreign Fiend Reward 4", 84, 0x55C63E),

    FFTALocationData("Foreign Fiend 2 Reward 1", 85, 0x55c67e),
    FFTALocationData("Foreign Fiend 2 Reward 2", 85, 0x55c680),
    FFTALocationData("Foreign Fiend 3 Reward 3", 85, 0x55C682),
    FFTALocationData("Foreign Fiend 4 Reward 4", 85, 0x55C684),

    FFTALocationData("Foreign Fiend 3 Reward 1", 86, 0x55c6c4),
    FFTALocationData("Foreign Fiend 3 Reward 2", 86, 0x55c6c6),
    FFTALocationData("Foreign Fiend 3 Reward 3", 86, 0x55C6C8),
    FFTALocationData("Foreign Fiend 3 Reward 4", 86, 0x55C6CA),

    FFTALocationData("Last Stand Reward 1", 87, 0x55c70a),
    FFTALocationData("Last Stand Reward 2", 87, 0x55c70c),
    FFTALocationData("Last Stand Reward 3", 87, 0x55C70E),
    FFTALocationData("Last Stand Reward 4", 87, 0x55C710),

    FFTALocationData("Free Bervenia! Reward 1", 88, 0x55c750),
    FFTALocationData("Free Bervenia! Reward 2", 88, 0x55c752),
    FFTALocationData("Free Bervenia! Reward 3", 88, 0x55C754),
    FFTALocationData("Free Bervenia! Reward 4", 88, 0x55C756),

    FFTALocationData("The Worldwyrm Reward 1", 89, 0x55c796),
    FFTALocationData("The Worldwyrm Reward 2", 89, 0x55c798),
    FFTALocationData("The Worldwyrm Reward 3", 89, 0x55C79A),
    FFTALocationData("The Worldwyrm Reward 4", 89, 0x55C79C),

    FFTALocationData("Moogle Bride Reward 1", 90, 0x55c7dc),
    FFTALocationData("Moogle Bride Reward 2", 90, 0x55c7de),
    FFTALocationData("Moogle Bride Reward 3", 90, 0x55C7E0),
    FFTALocationData("Moogle Bride Reward 4", 90, 0x55C7E2),

    FFTALocationData("Clan Law Reward 1", 91, 0x55c822),
    FFTALocationData("Clan Law Reward 2", 91, 0x55c824),
    FFTALocationData("Clan Law Reward 3", 91, 0x55C826),
    FFTALocationData("Clan Law Reward 4", 91, 0x55C828),

    FFTALocationData("Challengers? Reward 1", 92, 0x55c868),
    FFTALocationData("Challengers? Reward 2", 92, 0x55c86a),
    FFTALocationData("Challengers? Reward 3", 92, 0x55C86C),
    FFTALocationData("Challengers? Reward 4", 92, 0x55C86E),

    FFTALocationData("Cursed Bride Reward 1", 93, 0x55c8ae),
    FFTALocationData("Cursed Bride Reward 2", 93, 0x55c8b0),
    FFTALocationData("Cursed Bride Reward 3", 93, 0x55C8B2),
    FFTALocationData("Cursed Bride Reward 4", 93, 0x55C8B4),

    FFTALocationData("Flan Breakout Reward 1", 94, 0x55c8f4),
    FFTALocationData("Flan Breakout Reward 2", 94, 0x55c8f6),
    FFTALocationData("Flan Breakout Reward 3", 94, 0x55C8F8),
    FFTALocationData("Flan Breakout Reward 4", 94, 0x55C8FA),

    FFTALocationData("Sorry, Friend Reward 1", 95, 0x55c93a),
    FFTALocationData("Sorry, Friend Reward 2", 95, 0x55c93c),
    FFTALocationData("Sorry, Friend Reward 3", 95, 0x55C93E),
    FFTALocationData("Sorry, Friend Reward 4", 95, 0x55C940),

    FFTALocationData("Carrot! Reward 1", 96, 0x55c980),
    FFTALocationData("Carrot! Reward 2", 96, 0x55c982),
    FFTALocationData("Carrot! Reward 3", 96, 0x55C984),
    FFTALocationData("Carrot! Reward 4", 96, 0x55C986),

    FFTALocationData("Shadow Clan Reward 1", 97, 0x55c9c6),
    FFTALocationData("Shadow Clan Reward 2", 97, 0x55c9c8),
    FFTALocationData("Shadow Clan Reward 3", 97, 0x55C9CA),
    FFTALocationData("Shadow Clan Reward 4", 97, 0x55C9CC),

    FFTALocationData("The Dark Blade Reward 1", 98, 0x55ca0c),
    FFTALocationData("The Dark Blade Reward 2", 98, 0x55ca0e),
    FFTALocationData("The Dark Blade Reward 3", 98, 0x55CA10),
    FFTALocationData("The Dark Blade Reward 4", 98, 0x55CA12),

    FFTALocationData("The Hero Blade Reward 1", 99, 0x55ca52),
    FFTALocationData("The Hero Blade Reward 2", 99, 0x55ca54),
    FFTALocationData("The Hero Blade Reward 3", 99, 0x55CA56),
    FFTALocationData("The Hero Blade Reward 4", 99, 0x55CA58),

    FFTALocationData("The Fey Blade Reward 1", 100, 0x55ca98),
    FFTALocationData("The Fey Blade Reward 2", 100, 0x55ca9a),
    FFTALocationData("The Fey Blade Reward 3", 100, 0x55CA9C),
    FFTALocationData("The Fey Blade Reward 4", 100, 0x55CA9E),

    FFTALocationData("Fiend Run Reward 1", 101, 0x55cade),
    FFTALocationData("Fiend Run Reward 2", 101, 0x55cae0),
    FFTALocationData("Fiend Run Reward 3", 101, 0x55CAE2),
    FFTALocationData("Fiend Run Reward 4", 101, 0x55CAE4),

    FFTALocationData("Clan Roundup Reward 1", 102, 0x55cb24),
    FFTALocationData("Clan Roundup Reward 2", 102, 0x55cb26),
    FFTALocationData("Clan Roundup Reward 3", 102, 0x55CB28),
    FFTALocationData("Clan Roundup Reward 4", 102, 0x55CB2A),

    FFTALocationData("Wyrms Awaken Reward 1", 103, 0x55cb6a),
    FFTALocationData("Wyrms Awaken Reward 2", 103, 0x55cb6c),
    FFTALocationData("Wyrms Awaken Reward 3", 103, 0x55CB6E),
    FFTALocationData("Wyrms Awaken Reward 4", 103, 0x55CB70),

    # League missions currently not working
    #FFTALocationData("Yellow Powerz Reward 1", 104, 0x55cbb0),
    #FFTALocationData("Yellow Powerz Reward 2", 104, 0x55cbb2),
    #FFTALocationData("Yellow Powerz Reward 3", 104, 0x55CBB4),
    #FFTALocationData("Yellow Powerz Reward 4", 104, 0x55CBB6),

    #FFTALocationData("Blue Geniuses Reward 1", 105, 0x55cbf6),
    #FFTALocationData("Blue Geniuses Reward 2", 105, 0x55cbf8),
    #FFTALocationData("Blue Geniuses Reward 3", 105, 0x55CBFA),
    #FFTALocationData("Blue Geniuses Reward 4", 105, 0x55CBFC),

    #FFTALocationData("Brown Rabbits Reward 1", 106, 0x55cc3c),
    #FFTALocationData("Brown Rabbits Reward 2", 106, 0x55cc3e),
    #FFTALocationData("Brown Rabbits Reward 3", 106, 0x55CC40),
    #FFTALocationData("Brown Rabbits Reward 4", 106, 0x55CC42),

    #FFTALocationData("White Kupos Reward 1", 107, 0x55cc82),
    #FFTALocationData("White Kupos Reward 2", 107, 0x55cc84),
    #FFTALocationData("White Kupos Reward 3", 107, 0x55CC86),
    #FFTALocationData("White Kupos Reward 4", 107, 0x55CC88),

    FFTALocationData("Mythril Rush Reward 1", 108, 0x55ccc8),
    FFTALocationData("Mythril Rush Reward 2", 108, 0x55ccca),
    FFTALocationData("Mythril Rush Reward 3", 108, 0x55CCCC),
    FFTALocationData("Mythril Rush Reward 4", 108, 0x55CCCE),

    FFTALocationData("Stolen Scoop Reward 1", 109, 0x55cd0e),
    FFTALocationData("Stolen Scoop Reward 2", 109, 0x55cd10),
    FFTALocationData("Stolen Scoop Reward 3", 109, 0x55CD12),
    FFTALocationData("Stolen Scoop Reward 4", 109, 0x55CD14),

    FFTALocationData("Smuggle Bust Reward 1", 110, 0x55cd54),
    FFTALocationData("Smuggle Bust Reward 2", 110, 0x55cd56),
    FFTALocationData("Smuggle Bust Reward 3", 110, 0x55CD58),
    FFTALocationData("Smuggle Bust Reward 4", 110, 0x55CD5A),

    FFTALocationData("Resistance Reward 1", 111, 0x55cd9a),
    FFTALocationData("Resistance Reward 2", 111, 0x55cd9c),
    FFTALocationData("Resistance Reward 3", 111, 0x55CD9E),
    FFTALocationData("Resistance Reward 4", 111, 0x55CDA0),

    FFTALocationData("Old Friends Reward 1", 113, 0x55ce26),
    FFTALocationData("Old Friends Reward 2", 113, 0x55ce28),
    FFTALocationData("Old Friends Reward 3", 113, 0x55CE2A),
    FFTALocationData("Old Friends Reward 4", 113, 0x55CE2C),

    FFTALocationData("Poachers Reward 1", 114, 0x55ce6c),
    FFTALocationData("Poachers Reward 2", 114, 0x55ce6e),
    FFTALocationData("Poachers Reward 3", 114, 0x55CE70),
    FFTALocationData("Poachers Reward 4", 114, 0x55CE72),

    FFTALocationData("Snow Fairy Reward 1", 115, 0x55ceb2),
    FFTALocationData("Snow Fairy Reward 2", 115, 0x55ceb4),
    FFTALocationData("Snow Fairy Reward 3", 115, 0x55CEB6),
    FFTALocationData("Snow Fairy Reward 4", 115, 0x55CEB8),

    FFTALocationData("Revenge Reward 1", 116, 0x55cef8),
    FFTALocationData("Revenge Reward 2", 116, 0x55cefa),
    FFTALocationData("Revenge Reward 3", 116, 0x55CEFC),
    FFTALocationData("Revenge Reward 4", 116, 0x55CEFE),

    FFTALocationData("Retrieve Mail Reward 1", 117, 0x55cf3e),
    FFTALocationData("Retrieve Mail Reward 2", 117, 0x55cf40),
    FFTALocationData("Retrieve Mail Reward 3", 117, 0x55CF42),
    FFTALocationData("Retrieve Mail Reward 4", 117, 0x55CF44),

    FFTALocationData("A Challenge Reward 1", 118, 0x55cf84),
    FFTALocationData("A Challenge Reward 2", 118, 0x55cf86),
    FFTALocationData("A Challenge Reward 3", 118, 0x55CF88),
    FFTALocationData("A Challenge Reward 4", 118, 0x55CF8A),

    # First dispatch mission
    FFTALocationData("Watching You Reward 1", 125, 0x55d16e),
    FFTALocationData("Watching You Reward 2", 125, 0x55d170),
    FFTALocationData("Watching You Reward 3", 125, 0x55D172),
    FFTALocationData("Watching You Reward 4", 125, 0x55D174),

    FFTALocationData("Golden Gil Reward 1", 126, 0x55d1b4),
    FFTALocationData("Golden Gil Reward 2", 126, 0x55d1b6),
    FFTALocationData("Golden Gil Reward 3", 126, 0x55D1B8),
    FFTALocationData("Golden Gil Reward 4", 126, 0x55D1BA),

    FFTALocationData("Dueling Sub Reward 1", 127, 0x55d1fa),
    FFTALocationData("Dueling Sub Reward 2", 127, 0x55d1fc),
    FFTALocationData("Dueling Sub Reward 3", 127, 0x55D1FE),
    FFTALocationData("Dueling Sub Reward 4", 127, 0x55D200),

    FFTALocationData("Gulag Ghost Reward 1", 128, 0x55d240),
    FFTALocationData("Gulag Ghost Reward 2", 128, 0x55d242),
    FFTALocationData("Gulag Ghost Reward 3", 128, 0x55D244),
    FFTALocationData("Gulag Ghost Reward 4", 128, 0x55D246),

    FFTALocationData("Water City Reward 1", 129, 0x55d286),
    FFTALocationData("Water City Reward 2", 129, 0x55d288),
    FFTALocationData("Water City Reward 3", 129, 0x55D28A),
    FFTALocationData("Water City Reward 4", 129, 0x55D28C),

    FFTALocationData("Mirage Tower Reward 1", 130, 0x55d2cc),
    FFTALocationData("Mirage Tower Reward 2", 130, 0x55d2ce),
    FFTALocationData("Mirage Tower Reward 3", 130, 0x55D2D0),
    FFTALocationData("Mirage Tower Reward 4", 130, 0x55D2D2),

    FFTALocationData("A Barren Land Reward 1", 131, 0x55d312),
    FFTALocationData("A Barren Land Reward 2", 131, 0x55d314),
    FFTALocationData("A Barren Land Reward 3", 131, 0x55D316),
    FFTALocationData("A Barren Land Reward 4", 131, 0x55D318),

    FFTALocationData("Cadoan Meet Reward 1", 132, 0x55d358),
    FFTALocationData("Cadoan Meet Reward 2", 132, 0x55d35a),
    FFTALocationData("Cadoan Meet Reward 3", 132, 0x55D35C),
    FFTALocationData("Cadoan Meet Reward 4", 132, 0x55D35E),

    FFTALocationData("Sprohm Meet Reward 1", 133, 0x55d39e),
    FFTALocationData("Sprohm Meet Reward 2", 133, 0x55d3a0),
    FFTALocationData("Sprohm Meet Reward 3", 133, 0x55D3A2),
    FFTALocationData("Sprohm Meet Reward 4", 133, 0x55D3A4),

    FFTALocationData("Run for Fun Reward 1", 134, 0x55d3e4),
    FFTALocationData("Run for Fun Reward 2", 134, 0x55d3e6),
    FFTALocationData("Run for Fun Reward 3", 134, 0x55D3E8),
    FFTALocationData("Run for Fun Reward 4", 134, 0x55D3EA),

    FFTALocationData("Hungry Ghost Reward 1", 135, 0x55d42a),
    FFTALocationData("Hungry Ghost Reward 2", 135, 0x55d42c),
    FFTALocationData("Hungry Ghost Reward 3", 135, 0x55D42E),
    FFTALocationData("Hungry Ghost Reward 4", 135, 0x55D430),

    FFTALocationData("Pirates Ahoy Reward 1", 136, 0x55d470),
    FFTALocationData("Pirates Ahoy Reward 2", 136, 0x55d472),
    FFTALocationData("Pirates Ahoy Reward 3", 136, 0x55D474),
    FFTALocationData("Pirates Ahoy Reward 4", 136, 0x55D476),

    FFTALocationData("Castle Sit-In Reward 1", 137, 0x55d4b6),
    FFTALocationData("Castle Sit-In Reward 2", 137, 0x55d4b8),
    FFTALocationData("Castle Sit-In Reward 3", 137, 0x55D4BA),
    FFTALocationData("Castle Sit-In Reward 4", 137, 0x55D4BC),

    FFTALocationData("Wine Delivery Reward 1", 138, 0x55d4fc),
    FFTALocationData("Wine Delivery Reward 2", 138, 0x55d4fe),
    FFTALocationData("Wine Delivery Reward 3", 138, 0x55D500),
    FFTALocationData("Wine Delivery Reward 4", 138, 0x55D502),

    FFTALocationData("Broken Tunes Reward 1", 139, 0x55d542),
    FFTALocationData("Broken Tunes Reward 2", 139, 0x55d544),
    FFTALocationData("Broken Tunes Reward 3", 139, 0x55D546),
    FFTALocationData("Broken Tunes Reward 4", 139, 0x55D548),

    FFTALocationData("Falcon Flown Reward 1", 140, 0x55d588),
    FFTALocationData("Falcon Flown Reward 2", 140, 0x55d58a),
    FFTALocationData("Falcon Flown Reward 3", 140, 0x55D58C),
    FFTALocationData("Falcon Flown Reward 4", 140, 0x55D58E),

    FFTALocationData("Danger Pass Reward 1", 141, 0x55d5ce),
    FFTALocationData("Danger Pass Reward 2", 141, 0x55d5d0),
    FFTALocationData("Danger Pass Reward 3", 141, 0x55D5D2),
    FFTALocationData("Danger Pass Reward 4", 141, 0x55D5D4),

    FFTALocationData("Mist Stars Reward 1", 142, 0x55d614),
    FFTALocationData("Mist Stars Reward 2", 142, 0x55d616),
    FFTALocationData("Mist Stars Reward 3", 142, 0x55D618),
    FFTALocationData("Mist Stars Reward 4", 142, 0x55D61A),

    FFTALocationData("Adaman Alloy Reward 1", 143, 0x55d65a),
    FFTALocationData("Adaman Alloy Reward 2", 143, 0x55d65c),
    FFTALocationData("Adaman Alloy Reward 3", 143, 0x55D65E),
    FFTALocationData("Adaman Alloy Reward 4", 143, 0x55D660),

    FFTALocationData("Mysidia Alloy Reward 1", 144, 0x55d6a0),
    FFTALocationData("Mysidia Alloy Reward 2", 144, 0x55d6a2),
    FFTALocationData("Mysidia Alloy Reward 3", 144, 0x55D6A4),
    FFTALocationData("Mysidia Alloy Reward 4", 144, 0x55D6A6),

    FFTALocationData("Crusite Alloy Reward 1", 145, 0x55d6e6),
    FFTALocationData("Crusite Alloy Reward 2", 145, 0x55d6e8),
    FFTALocationData("Crusite Alloy Reward 3", 145, 0x55D6EA),
    FFTALocationData("Crusite Alloy Reward 4", 145, 0x55D6EC),

    FFTALocationData("Faceless Dolls Reward 1", 146, 0x55d72c),
    FFTALocationData("Faceless Dolls Reward 2", 146, 0x55d72e),
    FFTALocationData("Faceless Dolls Reward 3", 146, 0x55D730),
    FFTALocationData("Faceless Dolls Reward 4", 146, 0x55D732),

    FFTALocationData("Faithful Fairy Reward 1", 147, 0x55d772),
    FFTALocationData("Faithful Fairy Reward 2", 147, 0x55d774),
    FFTALocationData("Faithful Fairy Reward 3", 147, 0x55D776),
    FFTALocationData("Faithful Fairy Reward 4", 147, 0x55D778),

    FFTALocationData("For the Lady Reward 1", 148, 0x55d7b8),
    FFTALocationData("For the Lady Reward 2", 148, 0x55d7ba),
    FFTALocationData("For the Lady Reward 3", 148, 0x55D7BC),
    FFTALocationData("For the Lady Reward 4", 148, 0x55D7BE),

    FFTALocationData("Seven Nights Reward 1", 149, 0x55d7fe),
    FFTALocationData("Seven Nights Reward 2", 149, 0x55d800),
    FFTALocationData("Seven Nights Reward 3", 149, 0x55D802),
    FFTALocationData("Seven Nights Reward 4", 149, 0x55D804),

    FFTALocationData("Shady Deals Reward 1", 150, 0x55d844),
    FFTALocationData("Shady Deals Reward 2", 150, 0x55d846),
    FFTALocationData("Shady Deals Reward 3", 150, 0x55D848),
    FFTALocationData("Shady Deals Reward 4", 150, 0x55D84A),

    FFTALocationData("Earthy Colors Reward 1", 151, 0x55d88a),
    FFTALocationData("Earthy Colors Reward 2", 151, 0x55d88c),
    FFTALocationData("Earthy Colors Reward 3", 151, 0x55D88E),
    FFTALocationData("Earthy Colors Reward 4", 151, 0x55D890),

    FFTALocationData("Lost Heirloom Reward 1", 152, 0x55d8d0),
    FFTALocationData("Lost Heirloom Reward 2", 152, 0x55d8d2),
    FFTALocationData("Lost Heirloom Reward 3", 152, 0x55D8D4),
    FFTALocationData("Lost Heirloom Reward 4", 152, 0x55D8D6),

    FFTALocationData("Young Love Reward 1", 153, 0x55d916),
    FFTALocationData("Young Love Reward 2", 153, 0x55d918),
    FFTALocationData("Young Love Reward 3", 153, 0x55D91A),
    FFTALocationData("Young Love Reward 4", 153, 0x55D91C),

    FFTALocationData("Ghosts of War Reward 1", 154, 0x55d95c),
    FFTALocationData("Ghosts of War Reward 2", 154, 0x55d95e),
    FFTALocationData("Ghosts of War Reward 3", 154, 0x55D960),
    FFTALocationData("Ghosts of War Reward 4", 154, 0x55D962),

    FFTALocationData("The Last Day Reward 1", 155, 0x55d9a2),
    FFTALocationData("The Last Day Reward 2", 155, 0x55d9a4),
    FFTALocationData("The Last Day Reward 3", 155, 0x55D9A6),
    FFTALocationData("The Last Day Reward 4", 155, 0x55D9A8),

    FFTALocationData("The Bell Tolls Reward 1", 156, 0x55d9e8),
    FFTALocationData("The Bell Tolls Reward 2", 156, 0x55d9ea),
    FFTALocationData("The Bell Tolls Reward 3", 156, 0x55D9EC),
    FFTALocationData("The Bell Tolls Reward 4", 156, 0x55D9EE),

    FFTALocationData("Goblin Town Reward 1", 157, 0x55da2e),
    FFTALocationData("Goblin Town Reward 2", 157, 0x55da30),
    FFTALocationData("Goblin Town Reward 3", 157, 0x55DA32),
    FFTALocationData("Goblin Town Reward 4", 157, 0x55DA34),

    FFTALocationData("Secret Books Reward 1", 158, 0x55da74),
    FFTALocationData("Secret Books Reward 2", 158, 0x55da76),
    FFTALocationData("Secret Books Reward 3", 158, 0x55DA78),
    FFTALocationData("Secret Books Reward 4", 158, 0x55DA7A),

    FFTALocationData("Words of Love Reward 1", 159, 0x55daba),
    FFTALocationData("Words of Love Reward 2", 159, 0x55dabc),
    FFTALocationData("Words of Love Reward 3", 159, 0x55DABE),
    FFTALocationData("Words of Love Reward 4", 159, 0x55DAC0),

    FFTALocationData("You, Immortal Reward 1", 160, 0x55db00),
    FFTALocationData("You, Immortal Reward 2", 160, 0x55db02),
    FFTALocationData("You, Immortal Reward 3", 160, 0x55DB04),
    FFTALocationData("You, Immortal Reward 4", 160, 0x55DB06),

    FFTALocationData("Clocktower Reward 1", 161, 0x55db46),
    FFTALocationData("Clocktower Reward 2", 161, 0x55db48),
    FFTALocationData("Clocktower Reward 3", 161, 0x55DB4A),
    FFTALocationData("Clocktower Reward 4", 161, 0x55DB4C),

    FFTALocationData("An Education Reward 1", 162, 0x55db8c),
    FFTALocationData("An Education Reward 2", 162, 0x55db8e),
    FFTALocationData("An Education Reward 3", 162, 0x55DB90),
    FFTALocationData("An Education Reward 4", 162, 0x55DB92),

    FFTALocationData("Morning Woes Reward 1", 163, 0x55dbd2),
    FFTALocationData("Morning Woes Reward 2", 163, 0x55dbd4),
    FFTALocationData("Morning Woes Reward 3", 163, 0x55DBD6),
    FFTALocationData("Morning Woes Reward 4", 163, 0x55DBD8),

    FFTALocationData("Down to Earth Reward 1", 164, 0x55dc18),
    FFTALocationData("Down to Earth Reward 2", 164, 0x55dc1a),
    FFTALocationData("Down to Earth Reward 3", 164, 0x55DC1C),
    FFTALocationData("Down to Earth Reward 4", 164, 0x55DC1E),

    FFTALocationData("To Meden Reward 1", 165, 0x55dc5e),
    FFTALocationData("To Meden Reward 2", 165, 0x55dc60),
    FFTALocationData("To Meden Reward 3", 165, 0x55DC62),
    FFTALocationData("To Meden Reward 4", 165, 0x55DC64),

    FFTALocationData("Neighbor! Reward 1", 166, 0x55dca4),
    FFTALocationData("Neighbor! Reward 2", 166, 0x55dca6),
    FFTALocationData("Neighbor! Reward 3", 166, 0x55DCA8),
    FFTALocationData("Neighbor! Reward 4", 166, 0x55DCAA),

    FFTALocationData("Honor Lost Reward 1", 167, 0x55dcea),
    FFTALocationData("Honor Lost Reward 2", 167, 0x55dcec),
    FFTALocationData("Honor Lost Reward 3", 167, 0x55DCEE),
    FFTALocationData("Honor Lost Reward 4", 167, 0x55DCF0),

    FFTALocationData("Inspiration Reward 1", 168, 0x55dd30),
    FFTALocationData("Inspiration Reward 2", 168, 0x55dd32),
    FFTALocationData("Inspiration Reward 3", 168, 0x55DD34),
    FFTALocationData("Inspiration Reward 4", 168, 0x55DD36),

    FFTALocationData("Coo's Break Reward 1", 169, 0x55dd76),
    FFTALocationData("Coo's Break Reward 2", 169, 0x55dd78),
    FFTALocationData("Coo's Break Reward 3", 169, 0x55DD7A),
    FFTALocationData("Coo's Break Reward 4", 169, 0x55DD7C),

    FFTALocationData("The Match Reward 1", 170, 0x55ddbc),
    FFTALocationData("The Match Reward 2", 170, 0x55ddbe),
    FFTALocationData("The Match Reward 3", 170, 0x55DDC0),
    FFTALocationData("The Match Reward 4", 170, 0x55DDC2),

    FFTALocationData("The Deep Sea Reward 1", 171, 0x55de02),
    FFTALocationData("The Deep Sea Reward 2", 171, 0x55de04),
    FFTALocationData("The Deep Sea Reward 3", 171, 0x55DE06),
    FFTALocationData("The Deep Sea Reward 4", 171, 0x55DE08),

    FFTALocationData("A Worthy Eye Reward 1", 172, 0x55de48),
    FFTALocationData("A Worthy Eye Reward 2", 172, 0x55de4a),
    FFTALocationData("A Worthy Eye Reward 3", 172, 0x55DE4C),
    FFTALocationData("A Worthy Eye Reward 4", 172, 0x55DE4E),

    FFTALocationData("Lost in Mist Reward 1", 173, 0x55de8e),
    FFTALocationData("Lost in Mist Reward 2", 173, 0x55de90),
    FFTALocationData("Lost in Mist Reward 3", 173, 0x55DE92),
    FFTALocationData("Lost in Mist Reward 4", 173, 0x55DE94),

    FFTALocationData("Darn Kids Reward 1", 174, 0x55ded4),
    FFTALocationData("Darn Kids Reward 2", 174, 0x55ded6),
    FFTALocationData("Darn Kids Reward 3", 174, 0x55DED8),
    FFTALocationData("Darn Kids Reward 4", 174, 0x55DEDA),

    FFTALocationData("Stage Fright Reward 1", 175, 0x55df1a),
    FFTALocationData("Stage Fright Reward 2", 175, 0x55df1c),
    FFTALocationData("Stage Fright Reward 3", 175, 0x55DF1E),
    FFTALocationData("Stage Fright Reward 4", 175, 0x55DF20),

    FFTALocationData("Diary Dilemma Reward 1", 176, 0x55df60),
    FFTALocationData("Diary Dilemma Reward 2", 176, 0x55df62),
    FFTALocationData("Diary Dilemma Reward 3", 176, 0x55DF64),
    FFTALocationData("Diary Dilemma Reward 4", 176, 0x55DF66),

    FFTALocationData("Hundred-Eye Reward 1", 177, 0x55dfa6),
    FFTALocationData("Hundred-Eye Reward 2", 177, 0x55dfa8),
    FFTALocationData("Hundred-Eye Reward 3", 177, 0x55DFAA),
    FFTALocationData("Hundred-Eye Reward 4", 177, 0x55DFAC),

    FFTALocationData("Runaway Boy Reward 1", 178, 0x55dfec),
    FFTALocationData("Runaway Boy Reward 2", 178, 0x55dfee),
    FFTALocationData("Runaway Boy Reward 3", 178, 0x55DFF0),
    FFTALocationData("Runaway Boy Reward 4", 178, 0x55DFF2),

    FFTALocationData("Mad Alchemist Reward 1", 179, 0x55e032),
    FFTALocationData("Mad Alchemist Reward 2", 179, 0x55e034),
    FFTALocationData("Mad Alchemist Reward 3", 179, 0x55E036),
    FFTALocationData("Mad Alchemist Reward 4", 179, 0x55E038),

    FFTALocationData("Caravan Guard Reward 1", 180, 0x55e078),
    FFTALocationData("Caravan Guard Reward 2", 180, 0x55e07a),
    FFTALocationData("Caravan Guard Reward 3", 180, 0x55E07C),
    FFTALocationData("Caravan Guard Reward 4", 180, 0x55E07E),

    FFTALocationData("Lifework Reward 1", 181, 0x55e0be),
    FFTALocationData("Lifework Reward 2", 181, 0x55e0c0),
    FFTALocationData("Lifework Reward 3", 181, 0x55E0C2),
    FFTALocationData("Lifework Reward 4", 181, 0x55E0C4),

    FFTALocationData("Cheap Laughs Reward 1", 182, 0x55e104),
    FFTALocationData("Cheap Laughs Reward 2", 182, 0x55e106),
    FFTALocationData("Cheap Laughs Reward 3", 182, 0x55E108),
    FFTALocationData("Cheap Laughs Reward 4", 182, 0x55E10A),

    FFTALocationData("T.L.C. Reward 1", 183, 0x55e14a),
    FFTALocationData("T.L.C. Reward 2", 183, 0x55e14c),
    FFTALocationData("T.L.C. Reward 3", 183, 0x55E14E),
    FFTALocationData("T.L.C. Reward 4", 183, 0x55E150),

    FFTALocationData("Frozen Spring Reward 1", 184, 0x55e190),
    FFTALocationData("Frozen Spring Reward 2", 184, 0x55e192),
    FFTALocationData("Frozen Spring Reward 3", 184, 0x55E194),
    FFTALocationData("Frozen Spring Reward 4", 184, 0x55E196),

    FFTALocationData("No Scents Reward 1", 185, 0x55e1d6),
    FFTALocationData("No Scents Reward 2", 185, 0x55e1d8),
    FFTALocationData("No Scents Reward 3", 185, 0x55E1DA),
    FFTALocationData("No Scents Reward 4", 185, 0x55E1DC),

    FFTALocationData("On The Waves Reward 1", 186, 0x55e21c),
    FFTALocationData("On The Waves Reward 2", 186, 0x55e21e),
    FFTALocationData("On The Waves Reward 3", 186, 0x55E220),
    FFTALocationData("On The Waves Reward 4", 186, 0x55E222),

    FFTALocationData("Spirited Boy Reward 1", 187, 0x55e262),
    FFTALocationData("Spirited Boy Reward 2", 187, 0x55e264),
    FFTALocationData("Spirited Boy Reward 3", 187, 0x55E266),
    FFTALocationData("Spirited Boy Reward 4", 187, 0x55E268),

    FFTALocationData("Powder Worries Reward 1", 188, 0x55e2a8),
    FFTALocationData("Powder Worries Reward 2", 188, 0x55e2aa),
    FFTALocationData("Powder Worries Reward 3", 188, 0x55E2AC),
    FFTALocationData("Powder Worries Reward 4", 188, 0x55E2AE),

    FFTALocationData("The Blue Bolt Reward 1", 189, 0x55e2ee),
    FFTALocationData("The Blue Bolt Reward 2", 189, 0x55e2f0),
    FFTALocationData("The Blue Bolt Reward 3", 189, 0x55E2F2),
    FFTALocationData("The Blue Bolt Reward 4", 189, 0x55E2F4),

    FFTALocationData("Sweet Talk Reward 1", 190, 0x55e334),
    FFTALocationData("Sweet Talk Reward 2", 190, 0x55e336),
    FFTALocationData("Sweet Talk Reward 3", 190, 0x55E338),
    FFTALocationData("Sweet Talk Reward 4", 190, 0x55E33A),

    FFTALocationData("Scarface Reward 1", 191, 0x55e37a),
    FFTALocationData("Scarface Reward 2", 191, 0x55e37c),
    FFTALocationData("Scarface Reward 3", 191, 0x55E37E),
    FFTALocationData("Scarface Reward 4", 191, 0x55E380),

    FFTALocationData("Mirage Town Reward 1", 192, 0x55e3c0),
    FFTALocationData("Mirage Town Reward 2", 192, 0x55e3c2),
    FFTALocationData("Mirage Town Reward 3", 192, 0x55E3C4),
    FFTALocationData("Mirage Town Reward 4", 192, 0x55E3C6),

    FFTALocationData("Soldier's Wish Reward 1", 193, 0x55e406),
    FFTALocationData("Soldier's Wish Reward 2", 193, 0x55e408),
    FFTALocationData("Soldier's Wish Reward 3", 193, 0x55E40A),
    FFTALocationData("Soldier's Wish Reward 4", 193, 0x55E40C),

    FFTALocationData("Dry Spell Reward 1", 194, 0x55e44c),
    FFTALocationData("Dry Spell Reward 2", 194, 0x55e44e),
    FFTALocationData("Dry Spell Reward 3", 194, 0x55E450),
    FFTALocationData("Dry Spell Reward 4", 194, 0x55E452),

    FFTALocationData("Swap Meet Reward 1", 195, 0x55e492),
    FFTALocationData("Swap Meet Reward 2", 195, 0x55e494),
    FFTALocationData("Swap Meet Reward 3", 195, 0x55E496),
    FFTALocationData("Swap Meet Reward 4", 195, 0x55E498),

    FFTALocationData("Adaman Order Reward 1", 196, 0x55e4d8),
    FFTALocationData("Adaman Order Reward 2", 196, 0x55e4da),
    FFTALocationData("Adaman Order Reward 3", 196, 0x55E4DC),
    FFTALocationData("Adaman Order Reward 4", 196, 0x55E4DE),

    FFTALocationData("Magic Mysidia Reward 1", 197, 0x55e51e),
    FFTALocationData("Magic Mysidia Reward 2", 197, 0x55e520),
    FFTALocationData("Magic Mysidia Reward 3", 197, 0x55E522),
    FFTALocationData("Magic Mysidia Reward 4", 197, 0x55E524),

    FFTALocationData("Conundrum Reward 1", 198, 0x55e564),
    FFTALocationData("Conundrum Reward 2", 198, 0x55e566),
    FFTALocationData("Conundrum Reward 3", 198, 0x55E568),
    FFTALocationData("Conundrum Reward 4", 198, 0x55E56A),

    FFTALocationData("Lucky Night Reward 1", 199, 0x55e5aa),
    FFTALocationData("Lucky Night Reward 2", 199, 0x55e5ac),
    FFTALocationData("Lucky Night Reward 3", 199, 0x55E5AE),
    FFTALocationData("Lucky Night Reward 4", 199, 0x55E5B0),

    FFTALocationData("Tutor Search Reward 1", 200, 0x55e5f0),
    FFTALocationData("Tutor Search Reward 2", 200, 0x55e5f2),
    FFTALocationData("Tutor Search Reward 3", 200, 0x55E5F4),
    FFTALocationData("Tutor Search Reward 4", 200, 0x55E5F6),

    FFTALocationData("Why Am I Wet? Reward 1", 201, 0x55e636),
    FFTALocationData("Why Am I Wet? Reward 2", 201, 0x55e638),
    FFTALocationData("Why Am I Wet? Reward 3", 201, 0x55E63A),
    FFTALocationData("Why Am I Wet? Reward 4", 201, 0x55E63C),

    FFTALocationData("Run With Us Reward 1", 202, 0x55e67c),
    FFTALocationData("Run With Us Reward 2", 202, 0x55e67e),
    FFTALocationData("Run With Us Reward 3", 202, 0x55E680),
    FFTALocationData("Run With Us Reward 4", 202, 0x55E682),

    FFTALocationData("Lucky Charm Reward 1", 203, 0x55e6c2),
    FFTALocationData("Lucky Charm Reward 2", 203, 0x55e6c4),
    FFTALocationData("Lucky Charm Reward 3", 203, 0x55E6C6),
    FFTALocationData("Lucky Charm Reward 4", 203, 0x55E6C8),

    FFTALocationData("Alchemist Boy Reward 1", 204, 0x55e708),
    FFTALocationData("Alchemist Boy Reward 2", 204, 0x55e70a),
    FFTALocationData("Alchemist Boy Reward 3", 204, 0x55E70C),
    FFTALocationData("Alchemist Boy Reward 4", 204, 0x55E70E),

    FFTALocationData("Thorny Dreams Reward 1", 205, 0x55e74e),
    FFTALocationData("Thorny Dreams Reward 2", 205, 0x55e750),
    FFTALocationData("Thorny Dreams Reward 3", 205, 0x55E752),
    FFTALocationData("Thorny Dreams Reward 4", 205, 0x55E754),

    FFTALocationData("Free Cyril! Reward 1", 206, 0x55e794),
    FFTALocationData("Free Cyril! Reward 2", 206, 0x55e796),
    FFTALocationData("Free Cyril! Reward 3", 206, 0x55E798),
    FFTALocationData("Free Cyril! Reward 4", 206, 0x55E79A),

    FFTALocationData("Ship Needed Reward 1", 207, 0x55e7da),
    FFTALocationData("Ship Needed Reward 2", 207, 0x55e7dc),
    FFTALocationData("Ship Needed Reward 3", 207, 0x55E7DE),
    FFTALocationData("Ship Needed Reward 4", 207, 0x55E7E0),

    FFTALocationData("Mind Ceffyl Reward 1", 208, 0x55e820),
    FFTALocationData("Mind Ceffyl Reward 2", 208, 0x55e822),
    FFTALocationData("Mind Ceffyl Reward 3", 208, 0x55E824),
    FFTALocationData("Mind Ceffyl Reward 4", 208, 0x55E826),

    FFTALocationData("Body Ceffyl Reward 1", 209, 0x55e866),
    FFTALocationData("Body Ceffyl Reward 2", 209, 0x55e868),
    FFTALocationData("Body Ceffyl Reward 3", 209, 0x55E86A),
    FFTALocationData("Body Ceffyl Reward 4", 209, 0x55E86C),

    FFTALocationData("The Spiritstone Reward 1", 210, 0x55e8ac),
    FFTALocationData("The Spiritstone Reward 2", 210, 0x55e8ae),
    FFTALocationData("The Spiritstone Reward 3", 210, 0x55E8B0),
    FFTALocationData("The Spiritstone Reward 4", 210, 0x55E8B2),

    FFTALocationData("Girl In Love Reward 1", 211, 0x55e8f2),
    FFTALocationData("Girl In Love Reward 2", 211, 0x55e8f4),
    FFTALocationData("Girl In Love Reward 3", 211, 0x55E8F6),
    FFTALocationData("Girl In Love Reward 4", 211, 0x55E8F8),

    FFTALocationData("Chocobo Help! Reward 1", 212, 0x55e938),
    FFTALocationData("Chocobo Help! Reward 2", 212, 0x55e93a),
    FFTALocationData("Chocobo Help! Reward 3", 212, 0x55E93C),
    FFTALocationData("Chocobo Help! Reward 4", 212, 0x55E93E),

    FFTALocationData("The Skypole Reward 1", 213, 0x55e97e),
    FFTALocationData("The Skypole Reward 2", 213, 0x55e980),
    FFTALocationData("The Skypole Reward 3", 213, 0x55E982),
    FFTALocationData("The Skypole Reward 4", 213, 0x55E984),

    FFTALocationData("Ruins Survey Reward 1", 214, 0x55e9c4),
    FFTALocationData("Ruins Survey Reward 2", 214, 0x55e9c6),
    FFTALocationData("Ruins Survey Reward 3", 214, 0x55E9C8),
    FFTALocationData("Ruins Survey Reward 4", 214, 0x55E9CA),

    FFTALocationData("Dig Dig Dig Reward 1", 215, 0x55ea0a),
    FFTALocationData("Dig Dig Dig Reward 2", 215, 0x55ea0c),
    FFTALocationData("Dig Dig Dig Reward 3", 215, 0x55EA0E),
    FFTALocationData("Dig Dig Dig Reward 4", 215, 0x55EA10),

    FFTALocationData("Seeking Silver Reward 1", 216, 0x55ea50),
    FFTALocationData("Seeking Silver Reward 2", 216, 0x55ea52),
    FFTALocationData("Seeking Silver Reward 3", 216, 0x55EA54),
    FFTALocationData("Seeking Silver Reward 4", 216, 0x55EA56),

    FFTALocationData("Materite Reward 1", 217, 0x55ea96),
    FFTALocationData("Materite Reward 2", 217, 0x55ea98),
    FFTALocationData("Materite Reward 3", 217, 0x55EA9A),
    FFTALocationData("Materite Reward 4", 217, 0x55EA9C),

    FFTALocationData("The Wormhole Reward 1", 218, 0x55eadc),
    FFTALocationData("The Wormhole Reward 2", 218, 0x55eade),
    FFTALocationData("The Wormhole Reward 3", 218, 0x55EAE0),
    FFTALocationData("The Wormhole Reward 4", 218, 0x55EAE2),

    FFTALocationData("Metal Hunt Reward 1", 219, 0x55eb22),
    FFTALocationData("Metal Hunt Reward 2", 219, 0x55eb24),
    FFTALocationData("Metal Hunt Reward 3", 219, 0x55EB26),
    FFTALocationData("Metal Hunt Reward 4", 219, 0x55EB28),

    FFTALocationData("Math Is Hard Reward 1", 220, 0x55eb68),
    FFTALocationData("Math Is Hard Reward 2", 220, 0x55eb6a),
    FFTALocationData("Math Is Hard Reward 3", 220, 0x55EB6C),
    FFTALocationData("Math Is Hard Reward 4", 220, 0x55EB6E),

    FFTALocationData("The Witness Reward 1", 221, 0x55ebae),
    FFTALocationData("The Witness Reward 2", 221, 0x55ebb0),
    FFTALocationData("The Witness Reward 3", 221, 0x55EBB2),
    FFTALocationData("The Witness Reward 4", 221, 0x55EBB4),

    FFTALocationData("Life Or Death Reward 1", 222, 0x55ebf4),
    FFTALocationData("Life Or Death Reward 2", 222, 0x55ebf6),
    FFTALocationData("Life Or Death Reward 3", 222, 0x55EBF8),
    FFTALocationData("Life Or Death Reward 4", 222, 0x55EBFA),

    FFTALocationData("Karlos's Day Reward 1", 223, 0x55ec3a),
    FFTALocationData("Karlos's Day Reward 2", 223, 0x55ec3c),
    FFTALocationData("Karlos's Day Reward 3", 223, 0x55EC3E),
    FFTALocationData("Karlos's Day Reward 4", 223, 0x55EC40),

    FFTALocationData("To Father Reward 1", 224, 0x55ec80),
    FFTALocationData("To Father Reward 2", 224, 0x55ec82),
    FFTALocationData("To Father Reward 3", 224, 0x55EC84),
    FFTALocationData("To Father Reward 4", 224, 0x55EC86),

    FFTALocationData("Oh Milese Reward 1", 225, 0x55ecc6),
    FFTALocationData("Oh Milese Reward 2", 225, 0x55ecc8),
    FFTALocationData("Oh Milese Reward 3", 225, 0x55ECCA),
    FFTALocationData("Oh Milese Reward 4", 225, 0x55ECCC),

    FFTALocationData("Skinning Time Reward 1", 226, 0x55ed0c),
    FFTALocationData("Skinning Time Reward 2", 226, 0x55ed0e),
    FFTALocationData("Skinning Time Reward 3", 226, 0x55ED10),
    FFTALocationData("Skinning Time Reward 4", 226, 0x55ED12),

    FFTALocationData("Wild River Reward 1", 227, 0x55ed52),
    FFTALocationData("Wild River Reward 2", 227, 0x55ed54),
    FFTALocationData("Wild River Reward 3", 227, 0x55ED56),
    FFTALocationData("Wild River Reward 4", 227, 0x55ED58),

    FFTALocationData("Magic Cloth Reward 1", 228, 0x55ed98),
    FFTALocationData("Magic Cloth Reward 2", 228, 0x55ed9a),
    FFTALocationData("Magic Cloth Reward 3", 228, 0x55ED9C),
    FFTALocationData("Magic Cloth Reward 4", 228, 0x55ED9E),

    FFTALocationData("Cotton Guard Reward 1", 229, 0x55edde),
    FFTALocationData("Cotton Guard Reward 2", 229, 0x55ede0),
    FFTALocationData("Cotton Guard Reward 3", 229, 0x55EDE2),
    FFTALocationData("Cotton Guard Reward 4", 229, 0x55EDE4),

    FFTALocationData("Help Dad Reward 1", 230, 0x55ee24),
    FFTALocationData("Help Dad Reward 2", 230, 0x55ee26),
    FFTALocationData("Help Dad Reward 3", 230, 0x55EE28),
    FFTALocationData("Help Dad Reward 4", 230, 0x55EE2A),

    FFTALocationData("Rubber or Real Reward 1", 231, 0x55ee6a),
    FFTALocationData("Rubber or Real Reward 2", 231, 0x55ee6c),
    FFTALocationData("Rubber or Real Reward 3", 231, 0x55EE6E),
    FFTALocationData("Rubber or Real Reward 4", 231, 0x55EE70),

    FFTALocationData("Into The Woods Reward 1", 232, 0x55eeb0),
    FFTALocationData("Into The Woods Reward 2", 232, 0x55eeb2),
    FFTALocationData("Into The Woods Reward 3", 232, 0x55EEB4),
    FFTALocationData("Into The Woods Reward 4", 232, 0x55EEB6),

    FFTALocationData("Jerky Days Reward 1", 233, 0x55eef6),
    FFTALocationData("Jerky Days Reward 2", 233, 0x55eef8),
    FFTALocationData("Jerky Days Reward 3", 233, 0x55EEFA),
    FFTALocationData("Jerky Days Reward 4", 233, 0x55EEFC),

    FFTALocationData("New Fields Reward 1", 234, 0x55ef3c),
    FFTALocationData("New Fields Reward 2", 234, 0x55ef3e),
    FFTALocationData("New Fields Reward 3", 234, 0x55EF40),
    FFTALocationData("New Fields Reward 4", 234, 0x55EF42),

    FFTALocationData("Strange Fires Reward 1", 235, 0x55ef82),
    FFTALocationData("Strange Fires Reward 2", 235, 0x55ef84),
    FFTALocationData("Strange Fires Reward 3", 235, 0x55EF86),
    FFTALocationData("Strange Fires Reward 4", 235, 0x55EF88),

    FFTALocationData("Better Living Reward 1", 236, 0x55efc8),
    FFTALocationData("Better Living Reward 2", 236, 0x55efca),
    FFTALocationData("Better Living Reward 3", 236, 0x55EFCC),
    FFTALocationData("Better Living Reward 4", 236, 0x55EFCE),

    FFTALocationData("Malboro Hunt Reward 1", 237, 0x55f00e),
    FFTALocationData("Malboro Hunt Reward 2", 237, 0x55f010),
    FFTALocationData("Malboro Hunt Reward 3", 237, 0x55F012),
    FFTALocationData("Malboro Hunt Reward 4", 237, 0x55F014),

    FFTALocationData("Chocobo Work Reward 1", 238, 0x55f054),
    FFTALocationData("Chocobo Work Reward 2", 238, 0x55f056),
    FFTALocationData("Chocobo Work Reward 3", 238, 0x55F058),
    FFTALocationData("Chocobo Work Reward 4", 238, 0x55F05A),

    FFTALocationData("Party Night Reward 1", 239, 0x55f09a),
    FFTALocationData("Party Night Reward 2", 239, 0x55f09c),
    FFTALocationData("Party Night Reward 3", 239, 0x55F09E),
    FFTALocationData("Party Night Reward 4", 239, 0x55F0A0),

    FFTALocationData("Mama's Taste Reward 1", 240, 0x55f0e0),
    FFTALocationData("Mama's Taste Reward 2", 240, 0x55f0e2),
    FFTALocationData("Mama's Taste Reward 3", 240, 0x55F0E4),
    FFTALocationData("Mama's Taste Reward 4", 240, 0x55F0E6),

    FFTALocationData("The Well Maze Reward 1", 241, 0x55f126),
    FFTALocationData("The Well Maze Reward 2", 241, 0x55f128),
    FFTALocationData("The Well Maze Reward 3", 241, 0x55F12A),
    FFTALocationData("The Well Maze Reward 4", 241, 0x55F12C),

    FFTALocationData("She's Gone Reward 1", 242, 0x55f16c),
    FFTALocationData("She's Gone Reward 2", 242, 0x55f16e),
    FFTALocationData("She's Gone Reward 3", 242, 0x55F170),
    FFTALocationData("She's Gone Reward 4", 242, 0x55F172),

    FFTALocationData("Magic Vellum Reward 1", 243, 0x55f1b2),
    FFTALocationData("Magic Vellum Reward 2", 243, 0x55f1b4),
    FFTALocationData("Magic Vellum Reward 3", 243, 0x55F1B6),
    FFTALocationData("Magic Vellum Reward 4", 243, 0x55F1B8),

    FFTALocationData("Novel Ascent Reward 1", 244, 0x55f1f8),
    FFTALocationData("Novel Ascent Reward 2", 244, 0x55f1fa),
    FFTALocationData("Novel Ascent Reward 3", 244, 0x55F1FC),
    FFTALocationData("Novel Ascent Reward 4", 244, 0x55F1FE),

    FFTALocationData("Shiver Reward 1", 245, 0x55f23e),
    FFTALocationData("Shiver Reward 2", 245, 0x55f240),
    FFTALocationData("Shiver Reward 3", 245, 0x55F242),
    FFTALocationData("Shiver Reward 4", 245, 0x55F244),

    FFTALocationData("Bread Woes Reward 1", 246, 0x55f284),
    FFTALocationData("Bread Woes Reward 2", 246, 0x55f286),
    FFTALocationData("Bread Woes Reward 3", 246, 0x55F288),
    FFTALocationData("Bread Woes Reward 4", 246, 0x55F28A),

    FFTALocationData("Book Mess Reward 1", 247, 0x55f2ca),
    FFTALocationData("Book Mess Reward 2", 247, 0x55f2cc),
    FFTALocationData("Book Mess Reward 3", 247, 0x55F2CE),
    FFTALocationData("Book Mess Reward 4", 247, 0x55F2D0),

    FFTALocationData("One More Tail Reward 1", 248, 0x55f310),
    FFTALocationData("One More Tail Reward 2", 248, 0x55f312),
    FFTALocationData("One More Tail Reward 3", 248, 0x55F314),
    FFTALocationData("One More Tail Reward 4", 248, 0x55F316),

    FFTALocationData("Relax Time! Reward 1", 249, 0x55f356),
    FFTALocationData("Relax Time! Reward 2", 249, 0x55f358),
    FFTALocationData("Relax Time! Reward 3", 249, 0x55F35A),
    FFTALocationData("Relax Time! Reward 4", 249, 0x55F35C),

    FFTALocationData("Foma Jungle Reward 1", 250, 0x55f39c),
    FFTALocationData("Foma Jungle Reward 2", 250, 0x55f39e),
    FFTALocationData("Foma Jungle Reward 3", 250, 0x55F3A0),
    FFTALocationData("Foma Jungle Reward 4", 250, 0x55F3A2),

    FFTALocationData("For A Flower Reward 1", 251, 0x55f3e2),
    FFTALocationData("For A Flower Reward 2", 251, 0x55f3e4),
    FFTALocationData("For A Flower Reward 3", 251, 0x55F3E6),
    FFTALocationData("For A Flower Reward 4", 251, 0x55F3E8),

    FFTALocationData("Giza Plains Reward 1", 252, 0x55f428),
    FFTALocationData("Giza Plains Reward 2", 252, 0x55f42a),
    FFTALocationData("Giza Plains Reward 3", 252, 0x55F42C),
    FFTALocationData("Giza Plains Reward 4", 252, 0x55F42E),

    FFTALocationData("Lutia Pass Reward 1", 253, 0x55f46e),
    FFTALocationData("Lutia Pass Reward 2", 253, 0x55f470),
    FFTALocationData("Lutia Pass Reward 3", 253, 0x55F472),
    FFTALocationData("Lutia Pass Reward 4", 253, 0x55F474),

    FFTALocationData("Eluut Sands Reward 1", 254, 0x55f4b4),
    FFTALocationData("Eluut Sands Reward 2", 254, 0x55f4b6),
    FFTALocationData("Eluut Sands Reward 3", 254, 0x55F4B8),
    FFTALocationData("Eluut Sands Reward 4", 254, 0x55F4BA),

    FFTALocationData("Ulei River Reward 1", 255, 0x55f4fa),
    FFTALocationData("Ulei River Reward 2", 255, 0x55f4fc),
    FFTALocationData("Ulei River Reward 3", 255, 0x55F4FE),
    FFTALocationData("Ulei River Reward 4", 255, 0x55F500),

    FFTALocationData("Aisenfield Reward 1", 256, 0x55f540),
    FFTALocationData("Aisenfield Reward 2", 256, 0x55f542),
    FFTALocationData("Aisenfield Reward 3", 256, 0x55F544),
    FFTALocationData("Aisenfield Reward 4", 256, 0x55F546),

    FFTALocationData("The Nubswood Reward 1", 257, 0x55f586),
    FFTALocationData("The Nubswood Reward 2", 257, 0x55f588),
    FFTALocationData("The Nubswood Reward 3", 257, 0x55F58A),
    FFTALocationData("The Nubswood Reward 4", 257, 0x55F58C),
    
    FFTALocationData("Roda Volcano Reward 1", 258, 0x55f5cc),
    FFTALocationData("Roda Volcano Reward 2", 258, 0x55f5ce),
    FFTALocationData("Roda Volcano Reward 3", 258, 0x55F5D0),
    FFTALocationData("Roda Volcano Reward 4", 258, 0x55F5D2),

    FFTALocationData("Travel Aid Reward 1", 259, 0x55f612),
    FFTALocationData("Travel Aid Reward 2", 259, 0x55f614),
    FFTALocationData("Travel Aid Reward 3", 259, 0x55F616),
    FFTALocationData("Travel Aid Reward 4", 259, 0x55F618),

    FFTALocationData("The Salikwood Reward 1", 260, 0x55f658),
    FFTALocationData("The Salikwood Reward 2", 260, 0x55f65a),
    FFTALocationData("The Salikwood Reward 3", 260, 0x55F65C),
    FFTALocationData("The Salikwood Reward 4", 260, 0x55F65E),

    FFTALocationData("Nargai Cave Reward 1", 261, 0x55f69e),
    FFTALocationData("Nargai Cave Reward 2", 261, 0x55f6a0),
    FFTALocationData("Nargai Cave Reward 3", 261, 0x55F6A2),
    FFTALocationData("Nargai Cave Reward 4", 261, 0x55F6A4),

    FFTALocationData("Kudik Peaks Reward 1", 262, 0x55f6e4),
    FFTALocationData("Kudik Peaks Reward 2", 262, 0x55f6e6),
    FFTALocationData("Kudik Peaks Reward 3", 262, 0x55F6E8),
    FFTALocationData("Kudik Peaks Reward 4", 262, 0x55F6EA),

    FFTALocationData("Jeraw Sands Reward 1", 263, 0x55f72a),
    FFTALocationData("Jeraw Sands Reward 2", 263, 0x55f72c),
    FFTALocationData("Jeraw Sands Reward 3", 263, 0x55F72E),
    FFTALocationData("Jeraw Sands Reward 4", 263, 0x55F730),

    FFTALocationData("Uladon Bog Reward 1", 264, 0x55f770),
    FFTALocationData("Uladon Bog Reward 2", 264, 0x55f772),
    FFTALocationData("Uladon Bog Reward 3", 264, 0x55F774),
    FFTALocationData("Uladon Bog Reward 4", 264, 0x55F776),

    FFTALocationData("Gotor Sands Reward 1", 265, 0x55f7b6),
    FFTALocationData("Gotor Sands Reward 2", 265, 0x55f7b8),
    FFTALocationData("Gotor Sands Reward 3", 265, 0x55F7BA),
    FFTALocationData("Gotor Sands Reward 4", 265, 0x55F7BC),

    FFTALocationData("Delia Dunes Reward 1", 266, 0x55f7fc),
    FFTALocationData("Delia Dunes Reward 2", 266, 0x55f7fe),
    FFTALocationData("Delia Dunes Reward 3", 266, 0x55F800),
    FFTALocationData("Delia Dunes Reward 4", 266, 0x55F802),

    FFTALocationData("Bugbusters Reward 1", 267, 0x55f842),
    FFTALocationData("Bugbusters Reward 2", 267, 0x55f844),
    FFTALocationData("Bugbusters Reward 3", 267, 0x55F846),
    FFTALocationData("Bugbusters Reward 4", 267, 0x55F848),

    FFTALocationData("Tubola Cave Reward 1", 268, 0x55f888),
    FFTALocationData("Tubola Cave Reward 2", 268, 0x55f88a),
    FFTALocationData("Tubola Cave Reward 3", 268, 0x55F88C),
    FFTALocationData("Tubola Cave Reward 4", 268, 0x55F88E),

    FFTALocationData("Deti Plains Reward 1", 269, 0x55f8ce),
    FFTALocationData("Deti Plains Reward 2", 269, 0x55f8d0),
    FFTALocationData("Deti Plains Reward 3", 269, 0x55F8D2),
    FFTALocationData("Deti Plains Reward 4", 269, 0x55F8D4),

    FFTALocationData("Siena Gorge Reward 1", 270, 0x55f914),
    FFTALocationData("Siena Gorge Reward 2", 270, 0x55f916),
    FFTALocationData("Siena Gorge Reward 3", 270, 0x55F918),
    FFTALocationData("Siena Gorge Reward 4", 270, 0x55F91A),

    FFTALocationData("Jagd Ahli Reward 1", 271, 0x55f95a),
    FFTALocationData("Jagd Ahli Reward 2", 271, 0x55f95c),
    FFTALocationData("Jagd Ahli Reward 3", 271, 0x55F95E),
    FFTALocationData("Jagd Ahli Reward 4", 271, 0x55F960),

    FFTALocationData("Jagd Helje Reward 1", 272, 0x55f9a0),
    FFTALocationData("Jagd Helje Reward 2", 272, 0x55f9a2),
    FFTALocationData("Jagd Helje Reward 3", 272, 0x55F9A4),
    FFTALocationData("Jagd Helje Reward 4", 272, 0x55F9A6),

    FFTALocationData("Jagd Dorsa Reward 1", 273, 0x55f9e6),
    FFTALocationData("Jagd Dorsa Reward 2", 273, 0x55f9e8),
    FFTALocationData("Jagd Dorsa Reward 3", 273, 0x55F9EA),
    FFTALocationData("Jagd Dorsa Reward 4", 273, 0x55F9EC),

    FFTALocationData("Ambervale Reward 1", 274, 0x55fa2c),
    FFTALocationData("Ambervale Reward 2", 274, 0x55fa2e),
    FFTALocationData("Ambervale Reward 3", 274, 0x55FA30),
    FFTALocationData("Ambervale Reward 4", 274, 0x55FA32),

    FFTALocationData("Ozmonfield Reward 1", 275, 0x55fa72),
    FFTALocationData("Ozmonfield Reward 2", 275, 0x55fa74),
    FFTALocationData("Ozmonfield Reward 3", 275, 0x55FA76),
    FFTALocationData("Ozmonfield Reward 4", 275, 0x55FA78),

    FFTALocationData("Swords in Cyril Reward 1", 276, 0x55fab8),
    FFTALocationData("Swords in Cyril Reward 2", 276, 0x55faba),
    FFTALocationData("Swords in Cyril Reward 3", 276, 0x55FABC),
    FFTALocationData("Swords in Cyril Reward 4", 276, 0x55FABE),

    FFTALocationData("Newbie Hall Reward 1", 277, 0x55fafe),
    FFTALocationData("Newbie Hall Reward 2", 277, 0x55fb00),
    FFTALocationData("Newbie Hall Reward 3", 277, 0x55FB02),
    FFTALocationData("Newbie Hall Reward 4", 277, 0x55FB04),

    FFTALocationData("Voodoo Doll Reward 1", 278, 0x55fb44),
    FFTALocationData("Voodoo Doll Reward 2", 278, 0x55fb46),
    FFTALocationData("Voodoo Doll Reward 3", 278, 0x55FB48),
    FFTALocationData("Voodoo Doll Reward 4", 278, 0x55FB4A),

    FFTALocationData("Come On Out Reward 1", 279, 0x55fb8a),
    FFTALocationData("Come On Out Reward 2", 279, 0x55fb8c),
    FFTALocationData("Come On Out Reward 3", 279, 0x55FB8E),
    FFTALocationData("Come On Out Reward 4", 279, 0x55FB90),

    FFTALocationData("Food for Truth Reward 1", 280, 0x55fbd0),
    FFTALocationData("Food for Truth Reward 2", 280, 0x55fbd2),
    FFTALocationData("Food for Truth Reward 3", 280, 0x55FBD4),
    FFTALocationData("Food for Truth Reward 4", 280, 0x55FBD6),

    FFTALocationData("Alba Cave Reward 1", 281, 0x55fc16),
    FFTALocationData("Alba Cave Reward 2", 281, 0x55fc18),
    FFTALocationData("Alba Cave Reward 3", 281, 0x55FC1A),
    FFTALocationData("Alba Cave Reward 4", 281, 0x55FC1C),

    FFTALocationData("The Performer Reward 1", 282, 0x55fc5c),
    FFTALocationData("The Performer Reward 2", 282, 0x55fc5e),
    FFTALocationData("The Performer Reward 3", 282, 0x55FC60),
    FFTALocationData("The Performer Reward 4", 282, 0x55FC62),

    FFTALocationData("One More Time Reward 1", 283, 0x55fca2),
    FFTALocationData("One More Time Reward 2", 283, 0x55fca4),
    FFTALocationData("One More Time Reward 3", 283, 0x55FCA6),
    FFTALocationData("One More Time Reward 4", 283, 0x55FCA8),

    FFTALocationData("Spring Tree Reward 1", 284, 0x55fce8),
    FFTALocationData("Spring Tree Reward 2", 284, 0x55fcea),
    FFTALocationData("Spring Tree Reward 3", 284, 0x55FCEC),
    FFTALocationData("Spring Tree Reward 4", 284, 0x55FCEE),

    FFTALocationData("Who Am I Reward 1", 285, 0x55fd2e),
    FFTALocationData("Who Am I Reward 2", 285, 0x55fd30),
    FFTALocationData("Who Am I Reward 3", 285, 0x55FD32),
    FFTALocationData("Who Am I Reward 4", 285, 0x55FD34),

    FFTALocationData("Reaper Rumors Reward 1", 286, 0x55fd74),
    FFTALocationData("Reaper Rumors Reward 2", 286, 0x55fd76),
    FFTALocationData("Reaper Rumors Reward 3", 286, 0x55FD78),
    FFTALocationData("Reaper Rumors Reward 4", 286, 0x55FD7A),

    FFTALocationData("Dog Days Reward 1", 287, 0x55fdba),
    FFTALocationData("Dog Days Reward 2", 287, 0x55fdbc),
    FFTALocationData("Dog Days Reward 3", 287, 0x55FDBE),
    FFTALocationData("Dog Days Reward 4", 287, 0x55FDC0),

    FFTALocationData("Good Bread Reward 1", 288, 0x55fe00),
    FFTALocationData("Good Bread Reward 2", 288, 0x55fe02),
    FFTALocationData("Good Bread Reward 3", 288, 0x55FE04),
    FFTALocationData("Good Bread Reward 4", 288, 0x55FE06),

    FFTALocationData("Sword Needed Reward 1", 289, 0x55fe46),
    FFTALocationData("Sword Needed Reward 2", 289, 0x55fe48),
    FFTALocationData("Sword Needed Reward 3", 289, 0x55FE4A),
    FFTALocationData("Sword Needed Reward 4", 289, 0x55FE4C),

    FFTALocationData("El Ritmo Reward 1", 290, 0x55fe8c),
    FFTALocationData("El Ritmo Reward 2", 290, 0x55fe8e),
    FFTALocationData("El Ritmo Reward 3", 290, 0x55FE90),
    FFTALocationData("El Ritmo Reward 4", 290, 0x55FE92),

    FFTALocationData("Her Big Move Reward 1", 291, 0x55fed2),
    FFTALocationData("Her Big Move Reward 2", 291, 0x55fed4),
    FFTALocationData("Her Big Move Reward 3", 291, 0x55FED6),
    FFTALocationData("Her Big Move Reward 4", 291, 0x55FED8),

    FFTALocationData("Don't Look! Reward 1", 292, 0x55ff18),
    FFTALocationData("Don't Look! Reward 2", 292, 0x55ff1a),
    FFTALocationData("Don't Look! Reward 3", 292, 0x55FF1C),
    FFTALocationData("Don't Look! Reward 4", 292, 0x55FF1E),

    FFTALocationData("Janitor Duty Reward 1", 293, 0x55ff5e),
    FFTALocationData("Janitor Duty Reward 2", 293, 0x55ff60),
    FFTALocationData("Janitor Duty Reward 3", 293, 0x55FF62),
    FFTALocationData("Janitor Duty Reward 4", 293, 0x55FF64),

    FFTALocationData("Unlucky Star Reward 1", 294, 0x55ffa4),
    FFTALocationData("Unlucky Star Reward 2", 294, 0x55ffa6),
    FFTALocationData("Unlucky Star Reward 3", 294, 0x55FFA8),
    FFTALocationData("Unlucky Star Reward 4", 294, 0x55FFAA),

    FFTALocationData("Corral Care Reward 1", 295, 0x55ffea),
    FFTALocationData("Corral Care Reward 2", 295, 0x55ffec),
    FFTALocationData("Corral Care Reward 3", 295, 0x55FFEE),
    FFTALocationData("Corral Care Reward 4", 295, 0x55FFF0),

    FFTALocationData("Beastly Gun Reward 1", 296, 0x560030),
    FFTALocationData("Beastly Gun Reward 2", 296, 0x560032),
    FFTALocationData("Beastly Gun Reward 3", 296, 0x560034),
    FFTALocationData("Beastly Gun Reward 4", 296, 0x560036),

    FFTALocationData("Blade & Turtle Reward 1", 297, 0x560076),
    FFTALocationData("Blade & Turtle Reward 2", 297, 0x560078),
    FFTALocationData("Blade & Turtle Reward 3", 297, 0x56007A),
    FFTALocationData("Blade & Turtle Reward 4", 297, 0x56007C),

    FFTALocationData("Valuable Fake Reward 1", 298, 0x5600bc),
    FFTALocationData("Valuable Fake Reward 2", 298, 0x5600be),
    FFTALocationData("Valuable Fake Reward 3", 298, 0x5600C0),
    FFTALocationData("Valuable Fake Reward 4", 298, 0x5600C2),

    FFTALocationData("Weaver's War Reward 1", 299, 0x560102),
    FFTALocationData("Weaver's War Reward 2", 299, 0x560104),
    FFTALocationData("Weaver's War Reward 3", 299, 0x560106),
    FFTALocationData("Weaver's War Reward 4", 299, 0x560108),

    FFTALocationData("Fabled Sword Reward 1", 300, 0x560148),
    FFTALocationData("Fabled Sword Reward 2", 300, 0x56014a),
    FFTALocationData("Fabled Sword Reward 3", 300, 0x56014C),
    FFTALocationData("Fabled Sword Reward 4", 300, 0x56014E),

    FFTALocationData("Refurbishing Reward 1", 301, 0x56018e),
    FFTALocationData("Refurbishing Reward 2", 301, 0x560190),
    FFTALocationData("Refurbishing Reward 3", 301, 0x560192),
    FFTALocationData("Refurbishing Reward 4", 301, 0x560194),

    FFTALocationData("Stone Secret Reward 1", 302, 0x5601d4),
    FFTALocationData("Stone Secret Reward 2", 302, 0x5601d6),
    FFTALocationData("Stone Secret Reward 3", 302, 0x5601D8),
    FFTALocationData("Stone Secret Reward 4", 302, 0x5601DA),

    FFTALocationData("Sword Stuff Reward 1", 303, 0x56021a),
    FFTALocationData("Sword Stuff Reward 2", 303, 0x56021c),
    FFTALocationData("Sword Stuff Reward 3", 303, 0x56021E),
    FFTALocationData("Sword Stuff Reward 4", 303, 0x560220),

    FFTALocationData("A Stormy Night Reward 1", 304, 0x560260),
    FFTALocationData("A Stormy Night Reward 2", 304, 0x560262),
    FFTALocationData("A Stormy Night Reward 3", 304, 0x560264),
    FFTALocationData("A Stormy Night Reward 4", 304, 0x560266),

    FFTALocationData("Minstrel Song Reward 1", 305, 0x5602a6),
    FFTALocationData("Minstrel Song Reward 2", 305, 0x5602a8),
    FFTALocationData("Minstrel Song Reward 3", 305, 0x5602AA),
    FFTALocationData("Minstrel Song Reward 4", 305, 0x5602AC),

    FFTALocationData("Gun Crazy Reward 1", 306, 0x5602ec),
    FFTALocationData("Gun Crazy Reward 2", 306, 0x5602ee),
    FFTALocationData("Gun Crazy Reward 3", 306, 0x5602F0),
    FFTALocationData("Gun Crazy Reward 4", 306, 0x5602F2),

    FFTALocationData("Black Hat Reward 1", 307, 0x560332),
    FFTALocationData("Black Hat Reward 2", 307, 0x560334),
    FFTALocationData("Black Hat Reward 3", 307, 0x560336),
    FFTALocationData("Black Hat Reward 4", 307, 0x560338),

    FFTALocationData("Hat For A Girl Reward 1", 308, 0x560378),
    FFTALocationData("Hat For A Girl Reward 2", 308, 0x56037a),
    FFTALocationData("Hat For A Girl Reward 3", 308, 0x56037C),
    FFTALocationData("Hat For A Girl Reward 4", 308, 0x56037E),

    FFTALocationData("Armor & Turtle Reward 1", 309, 0x5603be),
    FFTALocationData("Armor & Turtle Reward 2", 309, 0x5603c0),
    FFTALocationData("Armor & Turtle Reward 3", 309, 0x5603C2),
    FFTALocationData("Armor & Turtle Reward 4", 309, 0x5603C4),

    FFTALocationData("Dark Armor Reward 1", 310, 0x560404),
    FFTALocationData("Dark Armor Reward 2", 310, 0x560406),
    FFTALocationData("Dark Armor Reward 3", 310, 0x560408),
    FFTALocationData("Dark Armor Reward 4", 310, 0x56040A),

    FFTALocationData("Fashion World Reward 1", 311, 0x56044a),
    FFTALocationData("Fashion World Reward 2", 311, 0x56044c),
    FFTALocationData("Fashion World Reward 3", 311, 0x56044E),
    FFTALocationData("Fashion World Reward 4", 311, 0x560450),

    FFTALocationData("Fashion Hoopla Reward 1", 312, 0x560490),
    FFTALocationData("Fashion Hoopla Reward 2", 312, 0x560492),
    FFTALocationData("Fashion Hoopla Reward 3", 312, 0x560494),
    FFTALocationData("Fashion Hoopla Reward 4", 312, 0x560496),

    # Extra missions
    FFTALocationData("Reconciliation Reward 1", 374, 0x561584),
    FFTALocationData("Reconciliation Reward 2", 374, 0x561586),
    FFTALocationData("Reconciliation Reward 3", 374, 0x561588),
    FFTALocationData("Reconciliation Reward 4", 374, 0x56158A),

    FFTALocationData("With Babus Reward 1", 376, 0x561610),
    FFTALocationData("With Babus Reward 2", 376, 0x561612),
    FFTALocationData("With Babus Reward 3", 376, 0x561614),
    FFTALocationData("With Babus Reward 4", 376, 0x561616),

    # Ritz might be required to be recruited
    FFTALocationData("Mortal Snow Reward 1", 377, 0x561656),
    FFTALocationData("Mortal Snow Reward 2", 377, 0x561658),
    FFTALocationData("Mortal Snow Reward 3", 377, 0x56165A),
    FFTALocationData("Mortal Snow Reward 4", 377, 0x56165C),

    FFTALocationData("Cleanup Time Reward 1", 379, 0x5616e2),
    FFTALocationData("Cleanup Time Reward 2", 379, 0x5616e4),
    FFTALocationData("Cleanup Time Reward 3", 379, 0x5616E6),
    FFTALocationData("Cleanup Time Reward 4", 379, 0x5616E8),

    FFTALocationData("No Arms Rule Reward 1", 385, 0x561886),
    FFTALocationData("No Arms Rule Reward 2", 385, 0x561888),
    FFTALocationData("No Arms Rule Reward 3", 385, 0x56188A),
    FFTALocationData("No Arms Rule Reward 4", 385, 0x56188C),

    FFTALocationData("Kissing Rule Reward 1", 386, 0x5618cc),
    FFTALocationData("Kissing Rule Reward 2", 386, 0x5618ce),
    FFTALocationData("Kissing Rule Reward 3", 386, 0x5618D0),
    FFTALocationData("Kissing Rule Reward 4", 386, 0x5618D2),

    FFTALocationData("Immunity Pass Reward 1", 387, 0x561912),
    FFTALocationData("Immunity Pass Reward 2", 387, 0x561914),
    FFTALocationData("Immunity Pass Reward 3", 387, 0x561916),
    FFTALocationData("Immunity Pass Reward 4", 387, 0x561918),

    FFTALocationData("No Full HP Reward 1", 388, 0x561958),
    FFTALocationData("No Full HP Reward 2", 388, 0x56195a),
    FFTALocationData("No Full HP Reward 3", 388, 0x56195C),
    FFTALocationData("No Full HP Reward 4", 388, 0x56195E),

    FFTALocationData("No Literacy Reward 1", 389, 0x56199e),
    FFTALocationData("No Literacy Reward 2", 389, 0x5619a0),
    FFTALocationData("No Literacy Reward 3", 389, 0x5619A2),
    FFTALocationData("No Literacy Reward 4", 389, 0x5619A4),

    FFTALocationData("Favoritism Reward 1", 390, 0x5619e4),
    FFTALocationData("Favoritism Reward 2", 390, 0x5619e6),
    FFTALocationData("Favoritism Reward 3", 390, 0x5619E8),
    FFTALocationData("Favoritism Reward 4", 390, 0x5619EA),

    FFTALocationData("No Answers Reward 1", 391, 0x561a2a),
    FFTALocationData("No Answers Reward 2", 391, 0x561a2c),
    FFTALocationData("No Answers Reward 3", 391, 0x561A2E),
    FFTALocationData("No Answers Reward 4", 391, 0x561A30),

    FFTALocationData("No Jumping Reward 1", 392, 0x561a70),
    FFTALocationData("No Jumping Reward 2", 392, 0x561a72),
    FFTALocationData("No Jumping Reward 3", 392, 0x561A74),
    FFTALocationData("No Jumping Reward 4", 392, 0x561A76),
]

bitflag_index = 2
byte_i = 0
# Setting up the mission complete flags
for index in range(0, len(FFTALocations), 4):
    #if byte_i == 2 and bitflag_index == 5:
    #    bitflag_index = 6

    if byte_i == 3 and bitflag_index == 1:
        bitflag_index = 3

    elif byte_i == 8 and bitflag_index == 5:
        bitflag_index = 6

    # Skipping the league mission bitflags for now
    elif byte_i == 13 and bitflag_index == 2:
        bitflag_index = 6

    elif byte_i == 14 and bitflag_index == 2:
        bitflag_index = 3

    elif byte_i == 15 and bitflag_index == 1:
        bitflag_index = 7
        
    elif byte_i == 39 and bitflag_index == 3:
        byte_i = 47
        bitflag_index = 0

    elif byte_i == 47 and bitflag_index == 0:
        bitflag_index = 1

    elif byte_i == 47 and bitflag_index == 1:
        bitflag_index = 2

    elif byte_i == 47 and bitflag_index == 4:
        bitflag_index = 5

    elif byte_i == 47 and bitflag_index == 6:
        bitflag_index = 3
        byte_i = 48

    # Immunity pass
    #elif byte_i == 48 and bitflag_index == 4:
    #    bitflag_index = 5
    #    byte_i = 48

    # Add dispatch missions to dispatch mission group
    if 125 <= FFTALocations[index].mission_id <= 312:
        DispatchMissionGroups.append(tuple([[FFTALocations[index], FFTALocations[(index + 1)], FFTALocations[(index + 2)], FFTALocations[(index + 3)]], bitflags[bitflag_index], byte_i]))

    else:
        MissionGroups.append(tuple([[FFTALocations[index], FFTALocations[(index + 1)], FFTALocations[(index + 2)], FFTALocations[(index + 3)]], bitflags[bitflag_index], byte_i]))
        
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



