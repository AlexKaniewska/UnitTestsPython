from Files.trader_worker import TraderWorker
import unittest


class TraderWorkerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = TraderWorker('9904041234', "Mino", "Kim", 33, 4, "ul. Niewiadoma 13", "Gdynia", "MEDIUM", 34)

    def test_data(self):
        self.assertEqual('Mino', self.worker.name)

    def test_commission(self):
        self.assertEqual(34, self.worker._commission)

    def test_value_true(self):
        self.assertEqual(360, self.worker.worker_value())

    def test_value_false(self):
        add = TraderWorker('9904041234', "Mino", "Kim", 33, 4, "ul. Niewiadoma 13", "Gdynia", "EXTRA", 34)
        self.assertFalse(add.worker_value())


if __name__ == '__main__':
    unittest.main()
