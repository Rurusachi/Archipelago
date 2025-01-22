from BaseClasses import Entrance, ItemClassification, Region, Location, LocationProgressType

from .locations import FFXLocation, FFXTreasureLocations


def create_regions(world, player) -> None:
    def create_region_locations(region, treasures):
        for treasure_id in treasures:
            location = FFXTreasureLocations[treasure_id]
            new_location = FFXLocation(player, location.name, location.rom_address, region)
            if location.missable:
                new_location.progress_type = LocationProgressType.EXCLUDED
            region.locations.append(new_location)

    menu_region = Region("Menu", player, world.multiworld)
    world.multiworld.regions.append(menu_region)

    test_region = Region("Test", player, world.multiworld)
    menu_region.connect(test_region)

    for location in FFXTreasureLocations:
        new_location = FFXLocation(player, location.name, location.rom_address, test_region)
        new_location.progress_type = LocationProgressType.EXCLUDED
        test_region.locations.append(new_location)

    baaj_1_region = Region("Baaj Temple 1st visit", player, world.multiworld)
    create_region_locations(baaj_1_region, [0, 1, 2, 3, 6, 7, 219, 213])  # + Klikk

    al_bhed_ship_region = Region("Al Bhed Ship", player, world.multiworld)
    create_region_locations(al_bhed_ship_region, [296])  # + Tros, Al Bhed Primer I

    baaj_2_region = Region("Baaj Temple 2nd visit", player, world.multiworld)
    create_region_locations(baaj_2_region, [204, 205, 5])  # + Anima




    besaid_1_region = Region("Besaid Island 1st visit", player, world.multiworld)
    create_region_locations(besaid_1_region, [268, 9, 283, 285, 284, 282, 90, 91, 92, 13, 14, 215, 216, 15, 459])  # + Al Bhed Primer II, Yuna, Lulu, Wakka, Valefor, Brotherhood



    besaid_2_region = Region("Besaid Island 2nd visit", player, world.multiworld)
