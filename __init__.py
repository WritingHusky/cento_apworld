from typing import ClassVar
from worlds.generic.Rules import exclusion_rules
from BaseClasses import Region, Entrance, Tutorial, Item
from worlds.AutoWorld import World, WebWorld
from multiprocessing import Process
from worlds.LauncherComponents import (
    Component,
    components,
    icon_paths,
    launch as launch_component,
    Type,
)
from .Items import ITEM_TABLE, CentoItem
from .Locations import LOCATION_TABLE, CentoLocation
from .options import CentoOptions


def launch_client(*args: str):
    from .CentoClient import launch

    launch_component(launch, name="CentoClient", args=args)


print("test")

components.append(
    Component(
        "Cento Client",
        func=launch_client,
        component_type=Type.CLIENT,
    )
)


class CentoWeb(WebWorld):
    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Archipelago cento software on your computer. This guide covers "
            "single-player, multiworld, and related software.",
            "English",
            "setup_en.md",
            "setup/en",
            ["Hash"],
        )
    ]


class CentoWorld(World):
    """
    Cento is a rythm game
    """

    game = "Cento"
    options_dataclass = CentoOptions
    options: CentoOptions
    web: ClassVar[CentoWeb] = CentoWeb()

    item_name_to_id = {name: data.code for name, data in ITEM_TABLE.items()}
    location_name_to_id = {name: data.code for name, data in LOCATION_TABLE.items()}

    item_pool: list[CentoItem] = []

    def get_filler_item_name(self):
        return "test"

    def create_items(self):
        data = ITEM_TABLE["test"]
        self.item_pool.append(CentoItem("test", self.player, data))

        for item in self.item_pool:
            self.multiworld.itempool.append(item)
        return

    def set_rules(self):
        pass

    def create_regions(self):
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)  # or use += [menu_region...]

        main_region = Region("Main Area", self.player, self.multiworld)

        main_region.locations.append(
            CentoLocation(self.player, "test", LOCATION_TABLE["test"])
        )
        self.multiworld.regions.append(main_region)

        menu_region.connect(main_region)

    def fill_slot_data(self):
        return self._get_cento_data()

    def _get_cento_data(self):
        return {}

    def create_item(self, name: str) -> Item:
        item_data = ITEM_TABLE[name]
        item = CentoItem(name, item_data.classification, item_data.code, self.player)
        return item
