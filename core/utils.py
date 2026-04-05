from typing import Callable

def filter_items(inventory: Inventory, predicate: Callable[[Item], bool]) -> list[Item]:
    """Returns items matching the predicate."""
    return list(filter(predicate, inventory)) # predicate takes Item and returns bool
