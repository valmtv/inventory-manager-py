import pytest
from core.models import Electronics, Grocery
from core.exceptions import InvalidValueException

def test_electronics():
    e = Electronics("E1", "Phone", 10, 699.99, 24)
    assert e.item_id == "E1"
    assert e.name == "Phone"
    assert e.quantity == 10
    assert e.price == 699.99
    assert e.warranty_months == 24
    assert e.category() == "Electronics"
    assert "Warranty: 24 months" in e.display()

def test_grocery():
    g = Grocery("G1", "Apple", 100, 0.99, "2026-06-01")
    assert g.item_id == "G1"
    assert g.expiration_date == "2026-06-01"
    assert g.category() == "Grocery"
    assert "Expires: 2026-06-01" in g.display()

def test_invalid_quantity():
    with pytest.raises(InvalidValueException):
        Electronics("E1", "Phone", -1, 699.99, 24)

def test_invalid_price():
    with pytest.raises(InvalidValueException):
        Electronics("E1", "Phone", 10, -1.0, 24)