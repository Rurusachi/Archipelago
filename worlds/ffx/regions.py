from BaseClasses import Entrance, ItemClassification, Region, Location

from .locations import FFXLocation, FFXTreasureLocations


def create_regions(world, player) -> None:

    menu_region = Region("Menu", player, world.multiworld)
    world.multiworld.regions.append(menu_region)

    test_region = Region("Test", player, world.multiworld)
    menu_region.connect(test_region)

    for location in FFXTreasureLocations:
        new_location = FFXLocation(player, location.name, location.rom_address, test_region)
        test_region.locations.append(new_location)
