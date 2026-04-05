class InventoryException(Exception):
    """Base class for inventory exceptions, gathers errors under one category"""
    pass

class ItemNotFoundException(InventoryException):
    def __init__(self, item_id: str, msg: str = "Item not found."):
        super().__init__(msg)
        self.item_id = item_id

class DuplicateItemException(InventoryException):
    def __init__(self, item_id: str, msg: str = "Item with this ID already exists in inventory."):
        super().__init__(msg)
        self.item_id = item_id

class InvalidValueException(InventoryException):
    def __init__(self, msg: str = "Quantity must be a non-negative integer."):
        super().__init__(msg) 

