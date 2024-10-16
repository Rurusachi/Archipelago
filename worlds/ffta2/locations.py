import typing
from typing import Dict, Optional, List, Tuple
import re

from BaseClasses import Location, Region

from .data import FFTA2Data, ffta2_data, QuestOffsets


class FFTA2Location(Location):
    game: str = "Final Fantasy Tactics A2"

    def __init__(self, player: int, name: str = '', address: Optional[int] = None, parent: Optional[Region] = None):
        super().__init__(player, name, address, parent)


class FFTA2LocationData(typing.NamedTuple):
    name: str
    quest_id: int
    rom_address: int


QuestGroups: Tuple[List[FFTA2LocationData], int, int] = []
bitflags = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]

unused_quests = ["-",  # Dummy quests
                   "The Two Grimoires",  # Final quest
                   "Stranger in the Woods",  # Story quests break when changing story progress
                   "A Paw Full of Feathers",
                   "The Yellow Wings",
                   "You Say Tomato",
                   "Wanted: Ugohr",
                   "Wanted: Gilmunto",
                   "Now That's a Fire!",
                   "Pearls in the Deep",
                   "Mountain Watch",
                   "Grounded!",
                   "Rumors Abound",
                   "Sleepless Nights",
                   "Making Music",
                   "Making Music part 2",
                   "Seeking the Stone",
                   "Wanted: Sky Pirate Vaan",
                   "A Request",
                   "The Rift",
                   "The Dig",
                   "Through Another's Eyes",
                   "Pirate Problems",
                   "The Ritual",
                   "From the Rift",
                   "The Search",  # Heritor quests? Work but there is no indicator where to go
                   "Gifted",  # instant-loss without Adelle
                   "An Elegant Encounter",
                   "Where Could He Be?",
                   "A Moment's Respite",
                   "I've Been Had, Kupo!",
                   "A Refined Recruit",
                   "I'm Back, Kupo!",
                   "Wanted: Friends, Kupo!",
                   "A Lost Companion",
                   "Help!",
                   "Woman of the Wood",
                   "The Beast of Aisenfield",
                   "Shrine of the Paling Gods",
                   "Bringer of Doom",
                   "Unplumbed Depths",
                   "A Dashing Duel",
                   "Brightmoon Tor",
                   "Brightmoon Tor, 2nd Ascent",
                   "Brightmoon Tor, 3rd Ascent",
                   #"The Moon Seal",  # Not available in pub for some reason (possibly fixed)
                   ]

FFTA2Locations: List[List[FFTA2LocationData]] = [
        [FFTA2LocationData(f"{quest.name} Reward 1", id, quest.memory + QuestOffsets.reward_1),
         FFTA2LocationData(f"{quest.name} Reward 2", id, quest.memory + QuestOffsets.reward_2),
         FFTA2LocationData(f"{quest.name} Reward 3", id, quest.memory + QuestOffsets.reward_3),
         #FFTA2LocationData(f"{quest.name} Reward 4", id, quest.memory + QuestOffsets.reward_4),
         ] for id, quest in enumerate(ffta2_data.quests) if quest.region != 0 and quest.name not in unused_quests and re.search("part [0-9]*\Z", quest.name) is None  # and quest.battle != 0
    ]

duplicates = []
# Setting up the quest complete flags
for quest in FFTA2Locations:
    byte_index = (quest[0].quest_id // 8)
    bitflag_index = quest[0].quest_id % 8

    QuestGroups.append(tuple([quest, bitflags[bitflag_index], byte_index]))


def create_location_label_to_id_map() -> Dict[str, int]:
    """
    Creates a map from location labels to their AP location id (address)
    """
    label_to_id_map: Dict[str, int] = {}
    for location_list in FFTA2Locations:
        for location in location_list:
            label_to_id_map[location.name] = location.rom_address

    return label_to_id_map


location_flags: Dict
