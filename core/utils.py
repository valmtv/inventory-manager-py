from typing import Callable, Any
from core.models import Item 
from core.inventory import Inventory

# Dependancy injection function wrappers
def filter_items(inventory: Inventory, predicate: Callable[[Item], bool]) -> list[Item]:
    """Returns items matching the predicate."""
    return list(filter(predicate, inventory)) # predicate takes Item and returns bool

def sort_items(inventory: Inventory, key_fn: Callable[[Item], Any], reverse: bool = False) -> list[Item]:
    """Returns items sorted by the given key function."""
    return sorted(inventory, key=key_fn, reverse=reverse)

def most_expensive(inventory: Inventory) -> Item:
    """Returns the item with the highest price."""
    return max(inventory, key=lambda item: item.price)
