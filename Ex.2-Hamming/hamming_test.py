import unittest
from hamming_distance import hamming


class HammingTest(unittest.TestCase):
    def test_empty_strands(self):
        self.assertEqual(hamming("", ""), 0)

    def test_single_letter_identical_strands(self):
        self.assertEqual(hamming("A", "A"), 0)

    def test_single_letter_different_strands(self):
        self.assertEqual(hamming("G", "T"), 1)

    def test_long_identical_strands(self):
        self.assertEqual(hamming("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)

    def test_long_different_strands(self):
        self.assertEqual(hamming("GGACGGATTCTG", "AGGACGGATTCT"), 9)

    def test_disallow_first_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming("AATG", "AAA")

    def test_disallow_second_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming("ATA", "AGTG")

    def test_disallow_left_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming("", "G")

    def test_disallow_right_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming("G", "")

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")