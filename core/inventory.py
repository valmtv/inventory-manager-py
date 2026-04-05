from typing import Iterator
from core.models import Item
import functools
from datetime import datetime
from core.exceptions import (
    InvalidValueException,
    ItemNotFoundException,
    DuplicateItemException,
    InventoryException
)
from core.models import Electronics, Grocery, Item
import csv

def log_operation(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        start = datetime.now()
        print(f"[{start.strftime('%Y-%m-%d %H:%M:%S')}] Calling {func.__name__}...")
        try:
            result = func(self, *args, **kwargs)
        except Exception as e:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {func.__name__} failed: {e}")
            raise
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
    @log_operation
    def add_item(self, item: Item) -> None:
        if not Inventory.is_valid_id(item.item_id): # just to use the method at least once, ofc in real life would be much more complex etc
            raise InvalidValueException(f"Invalid item ID: '{item.item_id}'")
        if item.item_id in self: # triggers __contains__
            raise DuplicateItemException(item.item_id, f"Item with ID '{item.item_id}' already exists in inventory.")
        self._items[item.item_id] = item

    @log_operation
    def remove_item(self, item_id: str) -> None:
        try:
            del self._items[item_id]
        except KeyError as e:
            raise ItemNotFoundException(item_id, f"Item with ID '{item_id}' not found.") from e

    @log_operation
    def update_quantity(self, item_id: str, quantity: int) -> None:
        try:
            self._items[item_id].quantity = quantity
        except KeyError as e:
            raise ItemNotFoundException(item_id, f"Item with ID '{item_id}' not found.") from e

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

    @log_operation
    def read_from_file(self, filename: str) -> None:
        """Populates the inventory from a CSV file"""
        headers = ['item_id', 'category', 'name', 'quantity', 'price', 'extra']

        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file, fieldnames=headers)

                for row in reader:
                    # strip whitespaces just in case 
                    item_id = row['item_id'].strip()
                    category = row['category'].strip()
                    name = row['name'].strip()

                    # Typecast numeric values
                    quantity = int(row['quantity'].strip())
                    price = float(row['price'].strip())
                    extra = row['extra'].strip()

                    item: Item # prevent type error
                    if category == 'Electronics':
                        # extra represents warranty_months (int)
                        item = Electronics(item_id, name, quantity, price, int(extra))
                    elif category == 'Grocery':
                        # extra represents expiration_date (str)
                        item = Grocery(item_id, name, quantity, price, extra)
                    else:
                        # Skip unknown categories to prevent crashing
                        print(f"Warning: Unknown category '{category}' for item '{item_id}' Skipping...")
                        continue

                    self.add_item(item)

        except OSError as e:
            # Catches FileNotFoundError PermissionError etc...
            raise InventoryException(f"Failed to read from file '{filename}'") from e
        except ValueError as e:
            # Catches issues if the CSV has bad data (e.g. trying to int() a string like "abc")
            raise InventoryException(f"Data formatting error in file '{filename}'") from e
