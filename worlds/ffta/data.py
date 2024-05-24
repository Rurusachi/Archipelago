
from random import Random
from typing import List, NamedTuple, Optional, Set


class FFTAObject:
    memory = 0
    displayName = ''

    def __init__(self, memory, displayName):
        self.memory = memory
        self.displayName = displayName


human_jobs = [0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C]
bangaa_jobs = [0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13]
mou_jobs = [0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B]
viera_jobs = [0x1C, 0x1D, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23]
moogle_jobs = [0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B]
monster_jobs = [0x2C, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3A,
                0x3B, 0x3C, 0x3D, 0x3E, 0x3F, 0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47]

all_jobs = human_jobs + bangaa_jobs + mou_jobs + viera_jobs + moogle_jobs
all_jobs_with_monster = human_jobs + bangaa_jobs + mou_jobs + viera_jobs + moogle_jobs + monster_jobs
attacker_jobs = [0x02, 0x03, 0x04, 0x05, 0x06, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x13, 0x1C, 0x21, 0x22, 0x23,
                 0x25, 0x26, 0x27, 0x28, ]
magic_jobs = [0x08, 0x09, 0x0A, 0x12, 0x15, 0x17, 0x18, 0x1B, 0x1D, 0x1E, 0x20, 0x2A]
support_jobs = [0x07, 0x14, 0x16, 0x1F, 0x24, 0x2B]

mission_item_memory = 0x2002B08
mission_items = []
for i in range(64):
    mission_items.append(mission_item_memory)
    mission_item_memory += 0x04

laws = [20, 74, 64, 75, 37, 43, 65, 21, 30, 4, 68, 22, 72, 47, 23, 50, 44, 67, 34, 70, 41, 38, 20, 4, 74, 25, 69,
        68, 42, 5, 44, 71, 30, 37, 11, 40, 64, 16, 22, 66, 50, 75, 71, 41, 18, 69, 3, 38, 44, 21, 10, 63, 14, 61,
        6, 65, 24, 9, 46, 33, 23, 72, 24, 14, 8, 62, 39, 10, 67, 35, 45, 13, 21, 48, 12, 16, 22, 2, 70, 30, 40, 76,
        49, 36, 46, 62, 7, 14, 17, 68, 82, 10, 25, 13, 34, 1, 43, 15, 3, 63, 45, 1, 82, 42, 33, 39, 8, 73, 3, 14, 50,
        47, 2, 36, 38, 19, 76, 72, 24, 66, 3, 82, 14, 19, 1, 8, 42, 2, 47, 17, 24, 33, 76, 38, 66, 35, 72, 39, 73, 61]

# (recruit, type, other)
mission_data = [(0, 11, 0), (0, 11, 0), (0, 11, 0), (0, 11, 0), (0, 11, 0), (0, 13, 0), (0, 11, 0), (0, 11, 0),
                (0, 11, 0), (0, 11, 0), (0, 11, 0), (0, 13, 0), (0, 9, 0), (0, 11, 0), (0, 13, 0), (0, 11, 0),
                (0, 11, 0), (0, 11, 0), (0, 11, 0), (0, 13, 0), (0, 11, 0), (0, 13, 0), (0, 13, 0), (0, 13, 0),
                (0, 13, 0), (3, 10, 0), (41, 10, 0), (15, 10, 0), (23, 10, 0), (32, 10, 0), (3, 10, 0), (1, 10, 0),
                (1, 10, 0), (1, 10, 0), (1, 10, 0), (111, 10, 0), (1, 10, 0), (41, 10, 0), (94, 10, 0), (94, 10, 0),
                (50, 10, 0), (64, 10, 0), (80, 10, 0), (140, 10, 0), (1, 10, 0), (1, 10, 0), (1, 10, 0), (1, 10, 0),
                (32, 10, 0), (1, 10, 0), (1, 10, 0), (94, 10, 0), (80, 10, 0), (80, 10, 0), (64, 10, 0), (1, 10, 0),
                (1, 10, 0), (1, 10, 0), (1, 10, 0), (1, 10, 0), (50, 10, 0), (1, 10, 0), (1, 10, 0), (146, 10, 0),
                (111, 10, 0), (1, 10, 0), (111, 10, 0), (0, 10, 0), (1, 10, 0), (1, 10, 0), (1, 210, 0), (1, 10, 0),
                (1, 10, 0), (1, 10, 0), (1, 10, 0), (1, 10, 0), (1, 82, 0), (1, 10, 0), (1, 146, 0), (1, 10, 0),
                (1, 10, 0), (1, 10, 0), (1, 10, 0), (1, 18, 0), (111, 10, 0), (111, 10, 0), (111, 10, 0), (111, 10, 0),
                (80, 82, 0), (3, 10, 0), (41, 10, 0), (1, 10, 0), (1, 10, 0), (1, 10, 0), (1, 10, 0), (1, 10, 0),
                (32, 10, 0), (15, 10, 0), (1, 10, 0), (1, 10, 0), (1, 10, 0), (94, 9, 0), (94, 9, 0), (1, 9, 1),
                (15, 9, 0), (23, 9, 0), (32, 9, 0), (41, 9, 0), (1, 9, 0), (1, 9, 0), (1, 9, 1), (1, 9, 0), (0, 9, 0),
                (32, 9, 0), (1, 9, 0), (1, 9, 0), (111, 9, 0), (94, 9, 0), (50, 9, 0), (0, 9, 0), (3, 0, 72),
                (15, 0, 72), (23, 0, 72), (32, 0, 72), (41, 0, 72), (1, 0, 144), (1, 0, 8), (1, 0, 200), (1, 0, 144),
                (1, 0, 144), (1, 0, 144), (1, 0, 144), (1, 0, 80), (1, 0, 80), (1, 0, 80), (1, 0, 136), (1, 0, 144),
                (1, 0, 80), (1, 0, 136), (1, 0, 200), (1, 0, 136), (1, 0, 216), (1, 0, 144), (1, 0, 144), (1, 0, 200),
                (1, 0, 136), (1, 0, 152), (1, 0, 88), (1, 0, 144), (1, 0, 200), (1, 0, 136), (1, 0, 72), (1, 0, 208),
                (1, 0, 136), (1, 0, 136), (1, 0, 72), (1, 0, 136), (1, 0, 80), (1, 0, 136), (1, 0, 136), (1, 0, 136),
                (1, 0, 8), (1, 0, 72), (1, 0, 72), (1, 0, 72), (1, 0, 8), (1, 0, 72), (1, 0, 80), (1, 0, 80),
                (1, 0, 72), (1, 0, 144), (1, 0, 208), (1, 0, 216), (1, 0, 8), (1, 0, 80), (1, 0, 200), (1, 0, 144),
                (1, 0, 88), (1, 0, 136), (1, 0, 136), (1, 0, 8), (1, 0, 200), (1, 0, 72), (1, 0, 144), (1, 0, 8),
                (1, 0, 200), (1, 0, 88), (1, 0, 72), (1, 0, 152), (1, 0, 216), (1, 0, 152), (1, 0, 208), (1, 0, 136),
                (1, 0, 80), (1, 0, 8), (1, 0, 72), (1, 0, 200), (1, 0, 144), (1, 0, 152), (1, 0, 200), (1, 0, 216),
                (1, 0, 216), (1, 0, 8), (1, 0, 8), (1, 0, 144), (1, 0, 8), (1, 144, 200), (1, 0, 80), (1, 0, 208),
                (1, 0, 208), (1, 0, 16), (1, 0, 144), (1, 0, 72), (1, 0, 136), (1, 0, 136), (1, 0, 80), (1, 0, 200),
                (1, 0, 136), (1, 0, 136), (1, 0, 200), (1, 0, 136), (1, 0, 88), (1, 0, 80), (1, 0, 72), (1, 0, 136),
                (1, 0, 200), (1, 0, 136), (1, 0, 144), (1, 0, 136), (1, 0, 80), (1, 0, 136), (1, 0, 72), (1, 0, 72),
                (1, 0, 72), (1, 0, 136), (1, 0, 72), (1, 0, 136), (1, 0, 200), (1, 0, 136), (1, 0, 200), (1, 0, 200),
                (1, 0, 200), (1, 0, 72), (1, 0, 80), (1, 0, 152), (1, 0, 8), (1, 0, 8), (1, 0, 136), (1, 0, 136),
                (1, 0, 200), (1, 0, 200), (1, 0, 144), (1, 16, 216), (1, 16, 216), (1, 208, 216), (1, 80, 216),
                (1, 144, 216), (1, 208, 216), (1, 16, 216), (1, 80, 88), (1, 208, 88), (1, 144, 88), (1, 80, 88),
                (1, 208, 88), (1, 144, 216), (1, 80, 216), (1, 16, 216), (1, 80, 216), (1, 144, 216), (1, 208, 152),
                (1, 16, 152), (1, 80, 216), (1, 16, 216), (1, 208, 216), (1, 144, 216), (1, 144, 216), (1, 0, 80),
                (1, 0, 136), (1, 0, 72), (1, 0, 136), (1, 0, 8), (1, 0, 16), (1, 0, 200), (1, 0, 200), (1, 0, 144),
                (1, 0, 200), (1, 0, 136), (1, 0, 136), (1, 0, 72), (1, 0, 144), (1, 0, 152), (1, 0, 200), (1, 0, 152),
                (1, 0, 8), (1, 0, 216), (1, 0, 136), (1, 0, 136), (1, 0, 144), (1, 0, 136), (1, 0, 88), (1, 0, 208),
                (1, 0, 8), (1, 0, 208), (1, 0, 16), (1, 0, 16), (1, 0, 208), (1, 0, 208), (1, 0, 208), (1, 0, 136),
                (1, 0, 144), (1, 0, 152), (1, 0, 136), (1, 0, 72), (0, 13, 0), (0, 13, 0), (0, 13, 0), (0, 13, 0),
                (0, 13, 0), (0, 13, 0), (0, 13, 0), (0, 13, 0), (0, 13, 0), (0, 13, 0), (94, 0, 200), (94, 0, 200),
                (94, 0, 200), (94, 0, 200), (94, 0, 200), (94, 0, 200), (111, 0, 88), (111, 0, 88), (111, 0, 88),
                (1, 0, 144), (0, 210, 0), (0, 18, 0), (0, 82, 0), (0, 146, 0), (0, 210, 0), (0, 18, 0), (0, 82, 0),
                (0, 146, 0), (0, 210, 0), (0, 18, 0), (0, 82, 0), (0, 146, 0), (0, 210, 0), (0, 18, 0), (0, 82, 0),
                (0, 146, 0), (0, 210, 0), (0, 18, 0), (0, 82, 0), (0, 146, 0), (0, 210, 0), (0, 18, 0), (0, 82, 0),
                (0, 13, 0), (3, 0, 72), (15, 0, 72), (23, 0, 72), (32, 0, 72), (41, 0, 72), (0, 26, 32), (0, 26, 32),
                (0, 26, 32), (0, 26, 96), (0, 26, 96), (0, 26, 96), (0, 26, 160), (0, 26, 160), (0, 26, 160),
                (0, 2, 224), (0, 2, 224), (0, 2, 224), (150, 10, 0), (0, 0, 136), (152, 10, 0), (154, 10, 0),
                (0, 0, 136), (158, 10, 0), (0, 10, 0), (150, 0, 72), (152, 0, 72), (154, 0, 72), (158, 0, 72),
                (0, 10, 0), (0, 10, 0), (0, 10, 0), (0, 10, 0), (0, 10, 0), (0, 10, 0), (0, 10, 0), (0, 10, 0),
                (0, 10, 0), (0, 12, 0), (0, 12, 0), (0, 12, 0), (156, 12, 0), (0, 12, 0), (0, 12, 0), (0, 12, 0),
                (0, 12, 0), (0, 12, 0), (0, 12, 0), (0, 0, 0), (0, 0, 0)]

# Does not include first 6 formations (i.e. formation_types[0] = ffta_data.formations[6].formation_type)
formation_types = [20, 21, 22, 23, 24, 25, 26, 56, 15, 16, 17, 76, 23, 1, 1, 8, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 12, 1, 1, 1, 1, 1, 32,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1, 30, 57, 58, 59,
                   60, 61, 62, 63, 1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1, 29, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 12, 1,
                   1, 1, 1, 1, 1, 1, 9, 31, 64, 65, 66, 67, 68, 69, 70, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 28, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 4, 12, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 9, 14, 72, 73, 81, 71, 71,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 28, 29, 32,
                   30, 1, 9, 10, 13, 14, 1, 1, 81, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 82, 82, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 12, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 84, 84, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   4, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 83, 83, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 83,
                   83, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 81, 81, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 81, 81, 1, 1, 1,
                   1, 1, 1, 1, 1, 81, 81, 1, 1, 1, 1, 1, 1, 1, 1, 81, 81, 1, 1, 1,
                   1, 1, 1, 1, 1, 81, 81, 1, 1, 1, 1, 1, 1, 1, 1, 81, 81, 81, 1, 1,
                   1, 81, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 6, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 2, 6, 8,
                   14, 15, 16, 17, 18, 19, 20, 21, 24, 2, 6, 8, 26, 25, 56, 76, 27, 23, 28, 71,
                   29, 2, 6, 8, 72, 30, 31, 32, 73, 36, 45, 48, 49, 2, 6, 1, 50, 51, 52, 53,
                   54, 55, 74, 75, 2, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 2, 6, 8, 1, 1, 1, 1, 1, 1, 1, 2, 6, 8, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 2, 6, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2,
                   6, 8, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 8, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 2, 6, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 8, 1,
                   1, 1, 1, 1, 1, 1, 1, 2, 6, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   2, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 8, 1, 1, 1, 1,
                   1, 1, 1, 1, 2, 6, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 8,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 8, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 2, 6, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 8, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 8, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 2, 6, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 8, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 2, 6, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 9, 4, 12, 13,
                   4, 12, 13, 10, 9, 1, 1, 1, 1, 1, 91, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 92, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 90, 91, 92, 1, 1, 1, 1, 1, 10, 14, 1, 1, 9, 1, 1, 1, 4, 1,
                   1, 1, 1, 1]


class MissionOffsets:
    type = 0x02
    rank = 0x03
    cancellation = 0x04
    unlockflag1 = 0x05
    unlockflag2 = 0x08
    unlockflag3 = 0x0b
    pub_visibility = 0x0e
    days_available = 0x0f
    rewardItem1 = 0x22
    rewardItem2 = 0x24
    cardItem1 = 0x26
    cardItem2 = 0x28
    clan_reward = 0x2A
    gil_reward = 0x33
    ap_reward = 0x34
    recruit = 0x35
    required_item1 = 0x36
    required_item2 = 0x37
    required_skill = 0x38
    required_job = 0x39
    price = 0x3e
    timeout_days = 0x40
    mission_display = 0x41
    dispatch_ability = 0x43  # Set to 0 for all to be jumpy time
    mission_location = 0x45


class FFTAMission(FFTAObject):
    recruit: int = 0
    mission_type: int = 0
    other: int = 0

    def __init__(self, memory, name: Optional[str], recruit: int, mission_type: int, other: int):
        self.memory = memory
        self.name = name
        self.recruit = recruit
        self.mission_type = mission_type
        self.other = other


class FFTAItem(FFTAObject):

    def __init__(self, memory, name: Optional[str]):
        self.memory = memory
        self.name = name


class JobOffsets:
    sprite_index = 0x07
    equip_items = 0x2D
    ability_start = 0x2E
    ability_end = 0x2F
    job_requirement = 0x30


class AbilityOffsets:
    mp_cost = 0x04
    weapon_required = 0x05


class UnitOffsets:
    type = 0x00
    job = 0x01
    level = 0x03
    unit_item1 = 0x08
    unit_item2 = 0x0a
    unit_item3 = 0x0c
    unit_item4 = 0x0e
    unit_item5 = 0x10
    abilities = 0x14
    ability_reaction = 0x28
    ability_support = 0x29


class UnitBattleOffsets:
    # 0x00 is name string
    character_id = 0x004
    first_item = 0x02A
    status_3 = 0x0EA


class ItemOffsets:
    buy_price = 0x04
    sell_price = 0x06
    item_flags = 0x0c  # bits 5 - 7 determine shop availability


class JobID:
    soldier = 0x02
    paladin = 0x03
    fighter = 0x04
    thiefhum = 0x05
    ninja = 0x06
    whitemagehum = 0x07
    blackmagehum = 0x08
    illusionisthum = 0x09
    bluemage = 0x0A
    archerhum = 0x0B
    hunter = 0x0C
    warrior = 0x0D
    dragoon = 0x0E
    defender = 0x0F
    gladiator = 0x10
    whitemonk = 0x11
    bishop = 0x12
    templar = 0x13
    whitemagemou = 0x14
    blackmagemou = 0x15
    timemagemou = 0x16
    illusionistmou = 0x17
    alchemist = 0x18
    beastmaster = 0x19
    morpher = 0x1A
    sage = 0x1B
    fencer = 0x1C
    elementalist = 0x1D
    redmage = 0x1E
    whitemagevra = 0x1F
    summoner = 0x20
    archervra = 0x21
    assassin = 0x22
    sniper = 0x23
    animist = 0x24
    mogknight = 0x25
    gunner = 0x26
    thiefmog = 0x27
    juggler = 0x28
    gadgeteer = 0x29
    blackmagemog = 0x2A
    timemagemog = 0x2B

    # Monsters
    goblin = 0x2C
    red_cap = 0x2D
    jelly = 0x2E
    ice_flan = 0x2F
    cream = 0x30
    bomb = 0x31
    grenade = 0x32
    icedrake = 0x33
    firewyrm = 0x34
    thundrake = 0x35
    lamia = 0x36
    lilith = 0x37
    antlion = 0x38
    jawbreaker = 0x39
    toughskin = 0x3A
    blade_biter = 0x3B
    tonberry = 0x3C
    masterberry = 0x3D
    red_panther = 0x3E
    coeurl = 0x3F
    malboro = 0x40
    big_malboro = 0x41
    floateye = 0x42
    ahriman = 0x43
    zombie = 0x44
    vampire = 0x45
    sprite = 0x46
    titania = 0x47


def master_abilities(address, index):
    address | (1 << index)


class UnitType:
    normal = 0x01
    marche = 0x02
    judge1 = 0x5A


class LocationData(NamedTuple):
    name: str
    label: str
    rom_address: int
    flag: int
    tags: Set[str]


class MemorySpace(NamedTuple):
    offset: int
    byteSize: int
    length: int


class Items(MemorySpace):
    offset = 0x51d1a0
    byteSize = 0x20
    length = 375


class MissionNames(MemorySpace):
    offset = 0x55a64c
    byteSize = 0x4
    length = 0x196


class Jobs(MemorySpace):
    offset = 0x521A14
    byteSize = 0x34
    length = 0x73


class Formation(MemorySpace):
    offset = 0x52cde0
    byteSize = 0x30
    length = 0xA46
    # 414 original length


class UnitInBattle(MemorySpace):
    offset = 0x2000080
    byteSize = 0x108
    length = 6
    # Maybe see if it applies to enemy units as well?


class Missions(MemorySpace):
    # 0x55ae4c original offset
    # 0x196 original length
    offset = 0x55af1e
    byteSize = 0x46
    length = 0x196


class Abilities(MemorySpace):
    offset = 0x55187C
    byteSize = 0x1C
    length = 0x15A


class HumanAbilities(MemorySpace):
    offset = 0x51bb6c
    byteSize = 0x8
    length = 0x8c


class BangaaAbilities(MemorySpace):
    offset = 0x51bfdc
    byteSize = 0x8
    length = 0x4c


class NuMouAbilities(MemorySpace):
    offset = 0x51c244
    byteSize = 0x8
    length = 0x5e


class VieraAbilities(MemorySpace):
    offset = 0x51c53c
    byteSize = 0x8
    length = 0x54


class MoogleAbilities(MemorySpace):
    offset = 0x51c7e4
    byteSize = 0x8
    length = 0x57


class FFTAFormations(FFTAObject):
    formation_type = 0

    def __init__(self, memory, formation_type):
        self.memory = memory
        self.formation_type = formation_type


class FFTAJobs(FFTAObject):

    def __init__(self, memory):
        self.memory = memory


class FFTAAbility(FFTAObject):

    def __init__(self, memory):
        self.memory = memory


class FFTARaceAbility(FFTAObject):

    def __init__(self, memory):
        self.memory = memory


class FFTAData:
    #itemJobNames: List[str]
    #abilityNames: List[str]
    missionNames: List[str]
    #locations: Dict[str, LocationData]
    #animations: List[int]
    formations: List[FFTAFormations]
    missions: List[FFTAMission]
    abilities: List[FFTAAbility]
    human_abilities: List[FFTARaceAbility]
    bangaa_abilities: List[FFTARaceAbility]
    numou_abilities: List[FFTARaceAbility]
    viera_abilities: List[FFTARaceAbility]
    moogle_abilities: List[FFTARaceAbility]
    all_abilities: List[FFTARaceAbility]
    jobs: List[FFTAJobs]
    items: List[FFTAItem]

    def __init__(self):
        #self.itemJobNames = self.initializeItemNames()
        #self.abilityNames = self.initializeAbilityNames()
        #self.missionNames = self.initializeMissionNames()
        self.formations = self.initializeFormations()
        self.missions = self.initializeMissions()
        self.abilities = self.initializeAbilities()
        self.human_abilities = self.initializeHumanAbilities()
        self.bangaa_abilities = self.initializeBangaaAbilities()
        self.numou_abilities = self.initializeNuMouAbilities()
        self.viera_abilities = self.initializeVieraAbilities()
        self.moogle_abilities = self.initializeMoogleAbilities()
        self.all_abilities = self.human_abilities + self.bangaa_abilities + self.numou_abilities + \
            self.viera_abilities + self.moogle_abilities
        self.jobs = self.initializeJobs()
        #self.lawSets = self.initializeLawSets()
        self.items = self.initializeItems()

    def initializeMissions(self):
        missions = []
        dataType = Missions(0x55af1e, 0x46, 0x196)
        for n in range(dataType.length):
            memory = dataType.offset + dataType.byteSize * n

            new_item = FFTAMission(memory, "Name", *mission_data[n])

            missions.append(new_item)

        return missions

    def initializeItems(self):
        items = []
        dataType = Items(0x51d1a0, 0x20, 375)
        for n in range(dataType.length):
            memory = dataType.offset + dataType.byteSize * n

            new_item = FFTAItem(memory, "Name")

            items.append(new_item)

        return items

    def initializeFormations(self):
        formations = []
        # 414 original length
        dataType = Formation(0x52cde0, 0x30, 0xA46)
        for n in range(dataType.length):
            memory = dataType.offset + dataType.byteSize * n

            if n >= 6:
                formation_type = formation_types[n-6]
            else:
                formation_type = -1
            new_item = FFTAFormations(memory, formation_type)

            formations.append(new_item)

        return formations

    def initializeJobs(self):
        jobs = []

        dataType = Jobs(0x521A14, 0x34, 0x73)
        for n in range(dataType.length):
            memory = dataType.offset + dataType.byteSize * n

            new_item = FFTAJobs(memory)

            jobs.append(new_item)

        return jobs

    def initializeAbilities(self):
        abilities = []

        dataType = Abilities(0x55187c, 0x1c, 0x15a)
        for n in range(dataType.length):
            memory = dataType.offset + dataType.byteSize * n

            new_item = FFTAAbility(memory)

            abilities.append(new_item)

        return abilities

    def initializeHumanAbilities(self):
        human_abilities = []
        dataType = HumanAbilities(0x51bb6c, 0x8, 0x8c)
        for n in range(dataType.length):
            memory = dataType.offset + dataType.byteSize * n

            new_item = FFTARaceAbility(memory)

            human_abilities.append(new_item)

        return human_abilities

    def initializeBangaaAbilities(self):
        bangaa_abilities = []
        dataType = BangaaAbilities(0x51bfdc, 0x8, 0x4c)
        for n in range(dataType.length):
            memory = dataType.offset + dataType.byteSize * n

            new_item = FFTARaceAbility(memory)

            bangaa_abilities.append(new_item)

        return bangaa_abilities

    def initializeNuMouAbilities(self):
        numou_abilities = []
        dataType = NuMouAbilities(0x51c244, 0x8, 0x5e)
        for n in range(dataType.length):
            memory = dataType.offset + dataType.byteSize * n

            new_item = FFTARaceAbility(memory)

            numou_abilities.append(new_item)

        return numou_abilities

    def initializeVieraAbilities(self):
        viera_abilities = []
        dataType = VieraAbilities(0x51c53c, 0x8, 0x54)
        for n in range(dataType.length):
            memory = dataType.offset + dataType.byteSize * n

            new_item = FFTARaceAbility(memory)

            viera_abilities.append(new_item)

        return viera_abilities

    def initializeMoogleAbilities(self):
        moogle_abilities = []
        dataType = MoogleAbilities(0x51c7e4, 0x8, 0x57)
        for n in range(dataType.length):
            memory = dataType.offset + dataType.byteSize * n

            new_item = FFTARaceAbility(memory)

            moogle_abilities.append(new_item)

        return moogle_abilities

    #def initializeMissionNames(self):
        #names = []
        #dataType = MissionNames()
        #for n in range(dataType.length):
            #memory = dataType.offset + dataType.byteSize * n
            #stringLookUpTable = self.rom.slice(memory, memory + dataType.byteSize)

            #address = FFTAUtils.getLittleEndianAddress(stringLookUpTable)

            #startingByte = address
            #endingByte = startingByte

            #Change into do while somehow
            #endingByte += 0x01
            #while self.rom[endingByte != 0]:
            #    endingByte += 0x01

            #names.append(FFTAUtils.decodeFFTAText(self.rom.slice(startingByte, endingByte)))

        #return names


def get_random_job(random: Random, random_pool: int):
    human = 0
    bangaa = 1
    mou = 2
    viera = 3
    moogle = 4
    monster = 5
    all = 6
    all_with_monster = 7

    random_job: int

    if random_pool == human:
        random_job = random.choice(human_jobs)
        return random_job

    elif random_pool == bangaa:
        random_job = random.choice(bangaa_jobs)
        return random_job

    elif random_pool == mou:
        random_job = random.choice(mou_jobs)
        return random_job

    elif random_pool == viera:
        random_job = random.choice(viera_jobs)
        return random_job

    elif random_pool == moogle:
        random_job = random.choice(moogle_jobs)
        return random_job

    elif random_pool == monster:
        random_job = random.choice(monster_jobs)
        return random_job

    elif random_pool == all:
        random_job = random.choice(all_jobs)
        return random_job

    elif random_pool == all_with_monster:
        random_job = random.choice(all_jobs_with_monster)
        return random_job
