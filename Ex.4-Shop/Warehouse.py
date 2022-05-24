from abc import ABC


class OutOfStock(Exception):
    pass


class LackOfProduct(Exception):
    pass


class Warehouse(ABC):
    def __init__(self, items=[]):
        self.__items = items

    def find_by_name(self, name):
        return next((inv for inv in self.__items if inv.name == name), None)

    def add(self, product):
        if not self.find_by_name(product.name):
            self.__items.append(product)
            return product
        else:
            self.update(product)
            return product

    def delete(self, product):
        self.__items.remove(product)

    def update(self, product):
        for i in self.__items:
            if i.id == product.id:
                i.quantity = product.quantity + i.quantity

    def returning(self, products):
        for i in products:
            for j in self.__items:
                if i == j.name:
                    j.quantity = j.quantity + 1

    def buying(self, products):
        for i in products:
            if not self.find_by_name(i):
                raise LackOfProduct
            else:
                for j in self.__items:
                    if i == j.name:
                        if j.quantity != 0:
                            j.quantity = j.quantity - 1
                        else:
                            raise OutOfStock

    @property
    def data_source(self):
        return self.__items

    @data_source.setter
    def data_source(self, value):
        self.__items = value
