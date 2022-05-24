from abc import ABC
from Invoice import Invoice


class Shop(ABC):
    def __init__(self, inv_repository=None, ware_repository=None):
        self.__invoice_repository = inv_repository
        self.__warehouse_repository = ware_repository

    def buy(self, customer, items_list):
        invoice = Invoice(number=self.invoice_repository.get_next_number(), customer=customer, items=items_list)
        self.invoice_repository.add(invoice)
        self.warehouse_repository.buying(items_list)
        return invoice

    def returning_goods(self, invoice):
        if self.invoice_repository.find_by_number(invoice.number):
            self.invoice_repository.delete(invoice)
            self.warehouse_repository.returning(invoice.items)
            return True
        else:
            return False

    def returning_some_goods(self, invoice, items_list):
        all_items = invoice.items
        result = all(elem in all_items for elem in items_list)
        if result:
            if self.invoice_repository.find_by_number(invoice.number):
                self.invoice_repository.delete(invoice)
                new_list = list(set(all_items).difference(items_list))
                invoice2 = Invoice(number=self.invoice_repository.get_next_number(), customer=invoice.customer, items=new_list)
                self.invoice_repository.add(invoice2)
                self.warehouse_repository.returning(items_list)
                return True
            else:
                return False
        else:
            return False

    def supply(self, items_list):
        for i in items_list:
            self.__warehouse_repository.add(i)

    @property
    def invoice_repository(self):
        return self.__invoice_repository

    @property
    def warehouse_repository(self):
        return self.__warehouse_repository
