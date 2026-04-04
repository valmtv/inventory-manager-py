from core.models import Electronics, Grocery
from core.inventory import Inventory

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
print("All correct")
