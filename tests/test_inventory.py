from core.models import Electronics, Grocery
from core.inventory import Inventory
from core.utils import filter_items

# Basic functionality
inv = Inventory()
e = Electronics("E1", "Phone", 10, 699.99, 24)
e2 = Electronics("E2", "Laptop", 5, 1299.99, 12)
g = Grocery("G1", "Apple", 100, 0.99, "2026-06-01")
g2 = Grocery("G2", "Milk", 50, 2.49, "2024-12-01")

inv.add_item(e)
inv.add_item(e2)
inv.add_item(g)
inv.add_item(g2)

assert len(inv) == 4
assert "E1" in inv
assert "G1" in inv

inv.update_quantity("E1", 5)
assert inv._items["E1"].quantity == 5

assert len(list(inv.items_by_category("Electronics"))) == 2


inv.remove_item("G1")
assert len(inv) == 3
assert "G1" not in inv


# from_list
inv2 = Inventory.from_list([e, e2, g, g2])
assert len(inv2) == 4
assert "E1" in inv2
assert "G2" in inv2

# is_valid_id
assert Inventory.is_valid_id("E1") == True
assert Inventory.is_valid_id("ABC123") == True
assert Inventory.is_valid_id("") == False
assert Inventory.is_valid_id("E-1") == False
assert Inventory.is_valid_id("E 1") == False

# filter_items
expensive = filter_items(inv, lambda item: item.price > 100)
assert len(expensive) == 2  # Phone and Laptop
assert all(item.price > 100 for item in expensive)

cheap = filter_items(inv2, lambda item: item.price < 5)
assert len(cheap) == 2  # Apple and Milk

electronics_only = filter_items(inv, lambda item: item.category() == "Electronics")
assert len(electronics_only) == 2

print("All correct")
