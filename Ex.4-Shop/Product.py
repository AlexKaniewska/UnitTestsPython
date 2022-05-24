from abc import ABC


class Product(ABC):
    def __init__(self, id=None, name=None, quantity=None, price=None):
        self._id = id
        self._name = name
        self._quantity = quantity
        self._price = price

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, record):
        self._id = record

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, record):
        self._name = record

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, record):
        self._quantity = record

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, record):
        self._price = record
