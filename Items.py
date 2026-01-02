from BaseClasses import Item, ItemClassification
from typing import NamedTuple


class CentoItem(Item):
    game: str = "Cento"


class CentoItemData(NamedTuple):
    id: int
    classification: ItemClassification


cento_items: dict[str, CentoItemData] = {
    "test": CentoItemData(1, ItemClassification.progression_skip_balancing),
}
