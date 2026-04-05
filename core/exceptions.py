class InventoryException(Exception):
    """Base class for inventory exceptions, gathers errors under one category"""
    pass

class ItemNotFoundException(InventoryException):
    def __init__(self, item_id: str, msg: str = "Error: Item not found."):
        super().__init__(msg)
        self.item_id = item_id
