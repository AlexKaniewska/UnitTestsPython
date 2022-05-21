from Files.office_worker import OfficeWorker
import unittest


class OfficeWorkerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = OfficeWorker('9904041234', "Mino", "Kim", 33, 4, "ul. Niewiadoma 13", "Gdynia", 120)

    def test_data(self):
        self.assertEqual('Kim', self.worker.surname)

    def test_iq(self):
        self.assertEqual(120, self.worker._iq)

    def test_value(self):
        self.assertEqual(480, self.worker.worker_value())


if __name__ == '__main__':
    unittest.main()
