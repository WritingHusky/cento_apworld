from worlds.AutoWorld import World, WebWorld
from BaseClasses import Tutorial
from .Items import CentoItem, cento_items
from .Locations import CentoLocation, cento_locations
from .Options import CentoOptions
from .Regions import create_regions
from math import floor
from typing import Any, TextIO
from worlds.LauncherComponents import (
    Component,
    components,
    icon_paths,
    launch as launch_component,
    Type,
)


def launch_client(*args: str):
    from .Client import launch

    launch_component(launch, name="CentoClient", args=args)


components.append(
    Component(
        "Cento Client", "CentoClient", func=launch_client, component_type=Type.CLIENT
    )
)


class PizzaTowerWebWorld(WebWorld):
    theme = "stone"
    # option_groups = pt_option_groups
    # option_presets = pt_option_presets

    setup_en = Tutorial(
        "MultiWorld Setup Guide",
        "A guide to setting up Pizza Tower for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Hash"],
    )


class PizzaTowerWorld(World):
    """
    Down-on-his-luck pizza chef Peppino Spaghetti and his restaurant are threatened by a sentient floating pizza... and this time
    all of his abilities are gone, too! Climb up and bring down the Pizza Tower to save your restaurant in this cheesy, saucy,
    Wario Land 4-inspired platformer!
    """

    game = "Cento"
    topology_present = True
    options_dataclass = CentoOptions
    options: CentoOptions
    webworld = PizzaTowerWebWorld
    apworld_version = (1, 2, 5)

    item_name_to_id = {name: data.id for name, data in cento_items.items()}
    location_name_to_id = cento_locations

    # item_name_groups = pt_item_groups  # not extremely important for this world but it's here for completeness
    # location_name_groups = pt_location_groups

    def generate_early(self):
        pass

    def create_item(self, name: str) -> CentoItem:
        return CentoItem(
            name, cento_items[name].classification, cento_items[name].id, self.player
        )

    def create_regions(self):
        pass

    def create_items(self):
        pass

    def set_rules(self):
        pass

    def get_filler_item_name(self) -> str:
        return self.random.choice(cento_items.keys())
