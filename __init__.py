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


def launch_client(*args: str):
    from .CentoClient import launch

    launch_component(launch, name="CentoClient", args=args)


components.append(
    Component(
        "Cento Client",
        "CentoClient",
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
            ["Mewlif"],
        )
    ]


class CentoWorld(World):
    """
    cento is an RPG where every choice you make matters. You could choose to hurt all the enemies, eventually
    causing genocide of the monster species. Or you can spare all the enemies, befriending them and freeing them
    from their underground prison.
    """

    game = "cento"
    options_dataclass = centoOptions
    options: centoOptions
    web = centoWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in advancement_table.items()}

    def get_filler_item_name(self):
        pass

    def create_items(self):
        pass

    def set_rules(self):
        pass

    def create_regions(self):
        pass

    def fill_slot_data(self):
        return self._get_cento_data()

    def _get_cento_data(self):
        return {}

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = centoItem(name, item_data.classification, item_data.code, self.player)
        return item
