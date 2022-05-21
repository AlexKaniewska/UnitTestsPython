from Files.physical_worker import PhysicalWorker
import unittest


class PhysicalWorkerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = PhysicalWorker('9904041234', "Mino", "Kim", 33, 4, "ul. Niewiadoma 13", "Gdynia", 77)

    def test_data(self):
        self.assertEqual('Gdynia', self.worker.city)

    def test_strength(self):
        self.assertEqual(77, self.worker._strength)

    def test_value(self):
        self.assertEqual(9.33, self.worker.worker_value())


if __name__ == '__main__':
    unittest.main()
