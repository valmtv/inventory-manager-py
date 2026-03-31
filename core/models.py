from abc import ABC, abstractmethod

class Item(ABC):

    # disbles __dict__ (states no more attributes can be added)
    __slots__ = ('_item_id', '_name', '_quantity', '_price')

    def __init__(self, item_id: str, name: str, quantity: int, price: float):
        # self.atribute will trigger the setters, so will be protected at the very end
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    # Properties
    @property
    def item_id(self) -> str:
        return self._item_id

    @item_id.setter
    def item_id(self, value: str) -> None:
        self._item_id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        self._quantity = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        self._price = value


    # Abstract methods to be implemented by subclasses
    @abstractmethod
    def display(self) -> str:
        pass

    @abstractmethod
    def category(self) -> str:
        pass

    # String parser ( called dunder methods) 
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(item_id='{self.item_id}', name='{self.name}', quantity={self.quantity}, price={self.price})"

    def __str__(self) -> str:
        return f"Item: {self.name} (ID: {self.item_id}), Quantity: {self.quantity}, Price: ${self.price:.2f}"


