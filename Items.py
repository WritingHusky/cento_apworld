from BaseClasses import Item, ItemClassification as IC
from typing import NamedTuple


class CentoItem(Item):
    game: str = "Cento"


class CentoItemData(NamedTuple):
    id: int
    classification: IC
    count: int


cento_items: dict[str, CentoItemData] = {
    "Acto Gift": CentoItemData(1, IC.progression, 4),
    "Cashu Gift": CentoItemData(2, IC.progression, 4),
    "Inagi Gift": CentoItemData(3, IC.progression, 4),
    "Tula Gift": CentoItemData(4, IC.progression, 4),
    "Chitose Gift": CentoItemData(5, IC.progression, 4),
    "Hutaai Gift": CentoItemData(6, IC.progression, 4),
    "Ruquel Gift": CentoItemData(7, IC.progression, 4),
    "Zhu Gift": CentoItemData(8, IC.progression, 4),
    "Orzo Gift": CentoItemData(10, IC.progression, 4),
    "Tomatoma Gift": CentoItemData(11, IC.progression, 4),
    "LPH Gift": CentoItemData(12, IC.progression, 4),
    "Gulai Gift": CentoItemData(13, IC.progression, 4),
    # "Cloak Gift": CentoItemData(18, IC.progression, 4),
    "Cravis Gift": CentoItemData(19, IC.progression, 4),
    "Darlo Gift": CentoItemData(20, IC.progression, 4),
    "Kazakiri Gift": CentoItemData(21, IC.progression, 4),
    "Kohaku Gift": CentoItemData(22, IC.progression, 4),
    "Allium Gift": CentoItemData(23, IC.progression, 4),
    "Tetori Gift": CentoItemData(24, IC.progression, 4),
}
