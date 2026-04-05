from abc import ABC, abstractmethod
from core.exceptions import InvalidValueException

class Item(ABC):

    # disables __dict__ (states no more attributes can be added)
    __slots__ = ('_item_id', '_name', '_quantity', '_price')

    def __init__(self, item_id: str, name: str, quantity: int, price: float):
        # self.attribute will trigger the setters, so will be protected at the very end
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
        if value < 0:
            raise InvalidValueException("Quantity cannot be negative.") from None
        self._quantity = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise InvalidValueException("Price cannot be negative.") from None
        self._price = value

    @abstractmethod
    def display(self) -> str:
        pass

    @abstractmethod
    def category(self) -> str:
        pass

    # String representations (are dunder(__a__) methods) 
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(item_id='{self.item_id}', name='{self.name}', quantity={self.quantity}, price={self.price})"

    def __str__(self) -> str:
        return f"Item: {self.name} (ID: {self.item_id}), Quantity: {self.quantity}, Price: ${self.price:.2f}"


class Electronics(Item):
    __slots__ = ('_warranty_months',) # ',' makes it treated like a tuple

    def __init__(self, item_id: str, name: str, quantity: int, price: float, warranty_months: int):
        super().__init__(item_id, name, quantity, price)
        self.warranty_months = warranty_months

    @property
    def warranty_months(self) -> int:
        return self._warranty_months

    @warranty_months.setter
    def warranty_months(self, value: int) -> None:
        self._warranty_months = value


    def display(self) -> str:
        return (f"[Electronics] ID: {self.item_id} | Name: {self.name} | Qty: {self.quantity} " 
        f"| Price: {self.price:.2f} | Warranty: {self.warranty_months} months")


    def category(self) -> str:
        return self.__class__.__name__


class Grocery(Item):
    __slots__ = ('_expiration_date',)

    def __init__(self, item_id: str, name: str, quantity: int, price: float, expiration_date: str):
        super().__init__(item_id, name, quantity, price)
        self.expiration_date = expiration_date

    @property
    def expiration_date(self) -> str:
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value: str) -> None:
        self._expiration_date = value


    def display(self) -> str:
        return (f"[Grocery] ID: {self.item_id} | Name: {self.name} | Qty: {self.quantity} " 
                f"| Price: {self.price:.2f} | Expires: {self.expiration_date}")


    def category(self) -> str:
        return self.__class__.__name__
