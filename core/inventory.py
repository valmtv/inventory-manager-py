from typing import Iterator
from core.models import Item
import functools
from datetime import datetime

def log_operation(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        start = datetime.now()
        print(f"[{start.strftime('%Y-%m-%d %H:%M:%S')}] Calling {func.__name__}...")
        result = func(self, *args, **kwargs)
        end = datetime.now()
        print(f"[{end.strftime('%Y-%m-%d %H:%M:%S')}] {func.__name__} completed in {(end - start).total_seconds():.4f}s")
        return result
    return wrapper

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
    # TODO: Simple for now, later with exceptions and checks
    @log_operation
    def add_item(self, item: Item) -> None:
        self._items[item.item_id] = item

    @log_operation
    def remove_item(self, item_id: str) -> None:
        del self._items[item_id]

    @log_operation
    def update_quantity(self, item_id: str, quantity: int) -> None:
        self._items[item_id].quantity = quantity

    def display_inventory(self) -> None:
        # Works because of __iter__
        for item in self:
            print(item.display())

    def items_by_category(self, category: str):
        """Yields items matching the given category."""
        for item in self:
            if item.category() == category:
                yield item

    @classmethod
    def from_list(cls, items: list[Item]) -> "Inventory":
        """Creates an Inventory instance from a list of Item objects"""
        inventory = cls()
        for item in items:
            inventory.add_item(item)
        return inventory

    @staticmethod
    def is_valid_id(item_id: str) -> bool:
        """Checks if the given item ID is valid (e.g. non-empty and alphanumeric)"""
        return bool(item_id) and item_id.isalnum() # isalnum will reject "E-1" or with '_'
