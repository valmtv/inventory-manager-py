from core.models import Electronics, Grocery

e = Electronics("E1", "Phone", 10, 699.99, 24)

assert e.item_id == "E1"
assert e.name == "Phone"
assert e.quantity == 10
assert e.price == 699.99
assert e.warranty_months == 24
assert e.category() == "Electronics"
assert "Warranty: 24 months" in e.display()
print("Electronics:\n", e.display())
print("repr:\n", repr(e))

g = Grocery("G1", "Apple", 100, 0.99, "2026-06-01")

assert g.item_id == "G1"
assert g.expiration_date == "2026-06-01"
assert g.category() == "Grocery"
assert "Expires: 2026-06-01" in g.display()
print("Grocery:\n", g.display())
