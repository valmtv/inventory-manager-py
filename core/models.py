from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def __init__(self, _item_id: str, name: str, quantity: int, price: float):
        self._item_id = _item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    @property
    def item_id(self) -> str:
        return self._item_id

    @item_id.setter
    def item_id(self, value) -> None:
        self._item_id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value) -> None:
        self._name = value

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value) -> None:
        self._quantity = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value) -> None:
        self._price = value



