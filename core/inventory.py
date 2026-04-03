from typing import Iterator
from core.models import Item

class Inventory:
    def __init__(self):
        self._items: dict[str, Item] = {}

    # Dunder methods 
    def __len__(self) -> int:
        return len(self._items)

    def __contains__(self, item_id: str) -> bool:
        return item_id in self._items

    def __iter__(self) -> Iterator[Item]:
        # values, not keys
        return iter(self._items.values())

