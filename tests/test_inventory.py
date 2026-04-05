import pytest
from core.models import Electronics, Grocery
from core.inventory import Inventory
from core.utils import filter_items, sort_items, most_expensive, below_quantity_threshold
from core.exceptions import ItemNotFoundException, DuplicateItemException, InvalidValueException

# shared fixtures
def make_items():
    e  = Electronics("E1", "Phone",  10,  699.99, 24)
    e2 = Electronics("E2", "Laptop",  5, 1299.99, 12)
    g  = Grocery("G1", "Apple", 100, 0.99, "2026-06-01")
    g2 = Grocery("G2", "Milk",   50, 2.49, "2024-12-01")
    return e, e2, g, g2

def make_inventory():
    inv = Inventory()
    for item in make_items():
        inv.add_item(item)
    return inv

def test_add_and_contains():
    inv = make_inventory()
    assert len(inv) == 4
    assert "E1" in inv
    assert "G1" in inv

def test_update_quantity():
    inv = make_inventory()
    inv.update_quantity("E1", 5)
    assert inv._items["E1"].quantity == 5

def test_items_by_category():
    inv = make_inventory()
    assert len(list(inv.items_by_category("Electronics"))) == 2

def test_remove_item():
    inv = make_inventory()
    inv.remove_item("G1")
    assert len(inv) == 3
    assert "G1" not in inv

def test_from_list():
    inv = Inventory.from_list(list(make_items()))
    assert len(inv) == 4
    assert "E1" in inv
    assert "G2" in inv

def test_is_valid_id():
    assert Inventory.is_valid_id("E1") == True
    assert Inventory.is_valid_id("ABC123") == True
    assert Inventory.is_valid_id("") == False
    assert Inventory.is_valid_id("E-1") == False
    assert Inventory.is_valid_id("E 1") == False

def test_filter_items():
    inv = make_inventory()
    expensive = filter_items(inv, lambda item: item.price > 100)
    assert len(expensive) == 2
    assert all(item.price > 100 for item in expensive)

    cheap = filter_items(inv, lambda item: item.price < 5)
    assert len(cheap) == 2

    electronics_only = filter_items(inv, lambda item: item.category() == "Electronics")
    assert len(electronics_only) == 2

def test_sort_items():
    inv = make_inventory()
    sorted_by_price = sort_items(inv, key_fn=lambda item: item.price)
    prices = [item.price for item in sorted_by_price]
    assert prices == sorted(prices)

    sorted_desc = sort_items(inv, key_fn=lambda item: item.price, reverse=True)
    prices_desc = [item.price for item in sorted_desc]
    assert prices_desc == sorted(prices_desc, reverse=True)

    sorted_by_name = sort_items(inv, key_fn=lambda item: item.name)
    assert sorted_by_name[0].name == "Apple"

def test_most_expensive():
    inv = make_inventory()
    assert most_expensive(inv).name == "Laptop"

def test_below_quantity_threshold():
    inv = make_inventory()
    low_stock = below_quantity_threshold(inv, threshold=15)
    assert len(low_stock) == 2


def test_item_not_found():
    inv = make_inventory()
    with pytest.raises(ItemNotFoundException) as exc_info:
        inv.remove_item("FAKE")
    assert exc_info.value.item_id == "FAKE"

    with pytest.raises(ItemNotFoundException) as exc_info:
        inv.update_quantity("FAKE", 10)
    assert exc_info.value.item_id == "FAKE"

def test_duplicate_item():
    inv = make_inventory()
    with pytest.raises(DuplicateItemException) as exc_info:
        inv.add_item(Electronics("E1", "Duplicate Phone", 5, 499.99, 12))
    assert exc_info.value.item_id == "E1"

def test_invalid_value():
    inv = make_inventory()
    with pytest.raises(InvalidValueException):
        inv.update_quantity("E1", -5)

    with pytest.raises(InvalidValueException):
        inv._items["E1"].price = -100