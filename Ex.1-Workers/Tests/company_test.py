import unittest
from Files.company import Company
from Files.office_worker import OfficeWorker
from Files.physical_worker import PhysicalWorker
from Files.trader_worker import TraderWorker


class CompanyTestCase(unittest.TestCase):
    def setUp(self):
        self.worker = Company()
        self.office = OfficeWorker('9709071234', 'Hyo', 'Lee', 24, 5, "ul. Losowa 4", "Sopot", 111)
        self.physical = PhysicalWorker('9807061234', 'Joo', 'Choi', 23, 3, "ul. Taka 8", "Gdynia", 88)
        self.trader = TraderWorker('9205131234', 'Minsoo', 'Kim', 29, 8, "ul. Radosna 13", "Sopot", "HIGH", 55)

    def test_add_list(self):
        self.worker.add_worker(self.office, self.physical)
        self.assertEqual(2, len(self.worker.worker_list))

    def test_add_in(self):
        self.worker.add_worker(self.office)
        self.assertIn(self.office, self.worker.worker_list)

    def test_delete_true1(self):
        self.worker.add_worker(self.office, self.physical)
        self.worker.delete_worker('9709071234')
        self.assertNotIn(self.office, self.worker.worker_list)

    def test_delete_true2(self):
        self.worker.add_worker(self.office, self.physical)
        self.worker.delete_worker('9709071234')
        self.assertEqual(1, len(self.worker.worker_list))

    def test_delete_false1(self):
        self.worker.add_worker(self.office, self.physical)
        check = self.worker.delete_worker('123456789')
        self.assertFalse(check)

    def test_delete_false2(self):
        self.worker.add_worker(self.office, self.physical)
        self.worker.delete_worker('123456789')
        self.assertEqual(2, len(self.worker.worker_list))

    def test_filter1(self):
        self.worker.add_worker(self.office, self.physical, self.trader)
        check = self.worker.filter("Sopot")
        self.assertEqual(2, len(check))

    def test_filter2(self):
        self.worker.add_worker(self.office, self.physical, self.trader)
        check = self.worker.filter("Sopot")
        self.assertEqual(check, [self.office, self.trader])

    def test_sort_true(self):
        self.worker.add_worker(self.office, self.physical, self.trader)
        check = self.worker.sorted("age")
        self.assertEqual(check, [self.physical, self.office, self.trader])

    def test_sort_false(self):
        self.worker.add_worker(self.office, self.physical, self.trader)
        check = self.worker.sorted("name")
        self.assertFalse(check)

    def test_value(self):
        self.worker.add_worker(self.office, self.physical, self.trader)
        check = self.worker.value()
        self.assertEqual(check, [[self.office, 555], [self.physical, 11.48], [self.trader, 960]])


if __name__ == '__main__':
    unittest.main()
