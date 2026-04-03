from core.models import Electronics, Grocery
from core.inventory import Inventory

inv = Inventory()
e = Electronics("E1", "Phone", 10, 699.99, 24)
g = Grocery("G1", "Apple", 100, 0.99, "2026-06-01")

inv.add_item(e)
inv.add_item(g)

assert len(inv) == 2
assert "E1" in inv
assert "G1" in inv

inv.update_quantity("E1", 5)
assert inv._items["E1"].quantity == 5

inv.remove_item("G1")
assert len(inv) == 1
assert "G1" not in inv
print("All correct")
