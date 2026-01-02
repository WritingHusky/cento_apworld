from worlds.generic.Rules import exclusion_rules
from BaseClasses import Region, Entrance, Tutorial, Item
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components
from multiprocessing import Process


def run_client():
    print("running cento client")
    from .CentoClient import main  # lazy import

    p = Process(target=main)
    p.start()


components.append(Component("cento Client", "centoClient"))
# components.append(Component("cento Client", func=run_client))


def data_path(file_name: str):
    import pkgutil

    return pkgutil.get_data(__name__, "data/" + file_name)


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
