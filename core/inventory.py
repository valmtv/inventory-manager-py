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


    # Core methods
    def add_item(self, item: Item) -> None:
        self._items[item.item_id] = item

    def remove_item(self, item_id: str) -> None:
        del self._items[item_id]

    def update_quantity(self, item_id: str, quantity: int) -> None:
        self._items[item_id].quantity = quantity

    def display_inventory(self) -> None:
        for item in self:
            print(item.display())
