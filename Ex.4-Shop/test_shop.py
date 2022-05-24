import unittest
from doubles import allow
from unittest.mock import Mock
from InvoiceRepository import InvoiceRepository
from Shop import Shop
from Invoice import Invoice
from Warehouse import Warehouse, LackOfProduct, OutOfStock
from Product import Product


class ShopTests(unittest.TestCase):
    def test_while_buy_the_repository_add_should_be_called(self):
        spy_repository = Mock(InvoiceRepository)
        dum_repository = Mock(Warehouse)
        shop = Shop(spy_repository, dum_repository)
        shop.buy(customer="Jan", items_list=["cukierki"])
        spy_repository.add.assert_called_once()

    def test_while_returning_goods_the_repository_returns_false_when_not_find(self):
        stub_repository = Mock(InvoiceRepository)
        dum_repository = Mock(Warehouse)
        shop = Shop(stub_repository, dum_repository)
        stub_repository.find_by_number.return_value = None
        result = shop.returning_goods(Mock(Invoice))
        self.assertEqual(result, False)

    def test_while_returning_goods_the_repository_delete_should_be_called_when_find(self):
        spy_repository = Mock(InvoiceRepository)
        dum_repository = Mock(Warehouse)
        shop = Shop(spy_repository, dum_repository)
        spy_repository.find_by_number.return_value = Invoice()
        shop.returning_goods(Mock(Invoice))
        spy_repository.delete.assert_called_once()

    def test_buy_goods_return_correct(self):
        spy_repository = Mock(InvoiceRepository)
        dum_repository = Mock(Warehouse)
        shop = Shop(spy_repository, dum_repository)
        invoice = Invoice(number=spy_repository.get_next_number(), customer="AK", items=["i don't know"])
        result = shop.buy(customer="AK", items_list=["i don't know"])
        self.assertEqual(result, invoice)

    def test_returning_goods_when_find_true(self):
        spy_repository = Mock(InvoiceRepository)
        dum_repository = Mock(Warehouse)
        shop = Shop(spy_repository, dum_repository)
        spy_repository.find_by_number.return_value = Invoice()
        result = shop.returning_goods(Mock(Invoice))
        self.assertTrue(result)

    def test_warehouse_buying_called_once(self):
        dum_repository = Mock(InvoiceRepository)
        spy_repository = Mock(Warehouse)
        shop = Shop(dum_repository, spy_repository)
        shop.buy(customer="Alex", items_list=["knowledge", "clean code"])
        spy_repository.buying.asser_called_once_with(["knowledge", "clean code"])

    def test_warehouse_buying_error_lop(self):
        stub_repository = Mock(Warehouse)
        stub_repository.buying.side_effect = LackOfProduct
        self.assertRaises(LackOfProduct, stub_repository.buying)

    def test_warehouse_buying_error_oos(self):
        stub_repository = Mock(Warehouse)
        stub_repository.buying.side_effect = OutOfStock
        self.assertRaises(OutOfStock, stub_repository.buying)

    def test_raise_error_lop(self):
        ware_repository = Mock(Warehouse)
        allow(ware_repository).buying.and_raise(LackOfProduct)
        try:
            ware_repository.buying(["1"])
        except LackOfProduct:
            pass
        else:
            raise AssertionError('Expected test to raise LackOfProduct.')

    def test_raise_error_oos(self):
        ware_repository = Mock(Warehouse)
        allow(ware_repository).buying.and_raise(OutOfStock)
        try:
            ware_repository.buying(["1"])
        except OutOfStock:
            pass
        else:
            raise AssertionError('Expected test to raise OutOfStock.')

    def test_warehouse_return_called_once(self):
        spy_repository = Mock(InvoiceRepository)
        spy_repository2 = Mock(Warehouse)
        shop = Shop(spy_repository, spy_repository2)
        spy_repository.find_by_number.return_value = Invoice()
        dummy = Mock(Invoice)
        shop.returning_goods(dummy)
        spy_repository2.returning.assert_called_once()

    def test_warehouse_return_called_with(self):
        spy_repository = Mock(InvoiceRepository)
        spy_repository2 = Mock(Warehouse)
        shop = Shop(spy_repository, spy_repository2)
        spy_repository.find_by_number.return_value = Invoice()
        dummy1 = Mock(Product)
        dummy2 = Mock(Product)
        shop.returning_goods(Mock(Invoice, items=[dummy1, dummy2]))
        spy_repository2.returning.assert_called_once_with([dummy1, dummy2])

    def test_return_some_goods(self):
        spy_repository = Mock(InvoiceRepository)
        spy_repository2 = Mock(Warehouse)
        pro = Mock(Product)
        pro2 = Mock(Product)
        shop = Shop(spy_repository, spy_repository2)
        shop.returning_some_goods(Mock(Invoice, items=[pro, pro2]), [pro])
        spy_repository.add.assert_called_once()
        spy_repository.delete.assert_called_once()

    def test_return_some_goods_false(self):
        spy_repository = Mock(InvoiceRepository)
        dum_repository = Mock(Warehouse)
        pro = Mock(Product)
        pro2 = Mock(Product)
        shop = Shop(spy_repository, dum_repository)
        spy_repository.find_by_number.return_value = None
        result = shop.returning_some_goods(Mock(Invoice, items=[pro, pro2]), [pro])
        self.assertFalse(result)

    def test_supply_add(self):
        spy_repository = Mock(Warehouse)
        shop = Shop(None, spy_repository)
        dummy = Mock(Product)
        shop.supply([dummy])
        spy_repository.find_by_name.return_value = None
        spy_repository.add.assert_called_once()

    def test_supply_add_multi(self):
        spy_repository = Mock(Warehouse)
        shop = Shop(None, spy_repository)
        dummy = Mock(Product)
        dummy2 = Mock(Product)
        dummy3 = Mock(Product)
        shop.supply([dummy, dummy2, dummy3])
        result = spy_repository.add.call_count
        self.assertEqual(result, 3)
