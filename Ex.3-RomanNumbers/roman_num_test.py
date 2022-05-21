import unittest
from unittest import TestCase
import roman_num


class KnownArabicRomanValues(TestCase):
    known_values = ((1, 'I'),
                    (2, 'II'),
                    (3, 'III'),
                    (4, 'IV'),
                    (5, 'V'),
                    (6, 'VI'),
                    (7, 'VII'),
                    (8, 'VIII'),
                    (9, 'IX'),
                    (10, 'X'),
                    (50, 'L'),
                    (100, 'C'),
                    (500, 'D'),
                    (1000, 'M'),
                    (31, 'XXXI'),
                    (148, 'CXLVIII'),
                    (294, 'CCXCIV'),
                    (312, 'CCCXII'),
                    (421, 'CDXXI'),
                    (528, 'DXXVIII'),
                    (621, 'DCXXI'),
                    (782, 'DCCLXXXII'),
                    (870, 'DCCCLXX'),
                    (941, 'CMXLI'),
                    (1043, 'MXLIII'),
                    (1110, 'MCX'),
                    (1226, 'MCCXXVI'),
                    (1301, 'MCCCI'),
                    (1485, 'MCDLXXXV'),
                    (1509, 'MDIX'),
                    (1607, 'MDCVII'),
                    (1754, 'MDCCLIV'),
                    (1832, 'MDCCCXXXII'),
                    (1993, 'MCMXCIII'),
                    (2074, 'MMLXXIV'),
                    (2152, 'MMCLII'),
                    (2212, 'MMCCXII'),
                    (2343, 'MMCCCXLIII'),
                    (2499, 'MMCDXCIX'),
                    (2574, 'MMDLXXIV'),
                    (2646, 'MMDCXLVI'),
                    (2723, 'MMDCCXXIII'),
                    (2892, 'MMDCCCXCII'),
                    (2975, 'MMCMLXXV'),
                    (3051, 'MMMLI'),
                    (3185, 'MMMCLXXXV'),
                    (3250, 'MMMCCL'),
                    (3313, 'MMMCCCXIII'),
                    (3408, 'MMMCDVIII'),
                    (3501, 'MMMDI'),
                    (3610, 'MMMDCX'),
                    (3743, 'MMMDCCXLIII'),
                    (3844, 'MMMDCCCXLIV'),
                    (3888, 'MMMDCCCLXXXVIII'),
                    (3940, 'MMMCMXL'),
                    (3999, 'MMMCMXCIX'),
                    (4000, 'MMMM'),
                    (4500, 'MMMMD'),
                    (4888, 'MMMMDCCCLXXXVIII'),
                    (4999, 'MMMMCMXCIX'))

    def test_to_roman_known_values(self):
        for integer, numeral in self.known_values:
            with self.subTest(integer=integer, numeral=numeral):
                result = roman_num.from_arabic_to_roman(integer)
                self.assertEqual(numeral, result)

    def test_from_roman_known_values(self):
        for integer, numeral in self.known_values:
            with self.subTest(integer=integer, numeral=numeral):
                result = roman_num.from_roman_to_arabic(numeral)
                self.assertEqual(integer, result)


class FromArabicToRomanBadInput(TestCase):
    def test_too_large(self):
        self.assertRaises(roman_num.OutOfRangeError, roman_num.from_arabic_to_roman, 5000)

    def test_zero(self):
        self.assertRaises(roman_num.OutOfRangeError, roman_num.from_arabic_to_roman, 0)

    def test_negative(self):
        self.assertRaises(roman_num.OutOfRangeError, roman_num.from_arabic_to_roman, -1)

    def test_nonInteger(self):
        self.assertRaises(roman_num.NotIntegerError, roman_num.from_arabic_to_roman, 0.5)


class FromRomanToArabicBadInput(TestCase):
    def test_too_many_repeated_numerals(self):
        for s in ('MMMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            with self.subTest(s=s):
                self.assertRaises(roman_num.InvalidRomanNumeralError, roman_num.from_roman_to_arabic, s)

    def test_repeated_pairs(self):
        for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            with self.subTest(s=s):
                self.assertRaises(roman_num.InvalidRomanNumeralError, roman_num.from_roman_to_arabic, s)

    def test_malformed_antecedent(self):
        for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            with self.subTest(s=s):
                self.assertRaises(roman_num.InvalidRomanNumeralError, roman_num.from_roman_to_arabic, s)

    def test_blank(self):
        self.assertRaises(roman_num.InvalidRomanNumeralError, roman_num.from_roman_to_arabic, "")


class RomanNumeralSanityCheck(TestCase):
    def testSanity(self):
        for integer in range(1, 5000):
            with self.subTest(integer=integer):
                numeral = roman_num.from_arabic_to_roman(integer)
                result = roman_num.from_roman_to_arabic(numeral)
                self.assertEqual(integer, result)


class RomanNumeralCaseCheck(TestCase):
    def testToRomanCase(self):
        for integer in range(1, 5000):
            with self.subTest(integer=integer):
                numeral = roman_num.from_arabic_to_roman(integer)
                self.assertEqual(numeral, numeral.upper())

    def testFromRomanCase(self):
        for integer in range(1, 5000):
            with self.subTest(integer=integer):
                numeral = roman_num.from_arabic_to_roman(integer)
                roman_num.from_roman_to_arabic(numeral.upper())
                self.assertRaises(roman_num.InvalidRomanNumeralError,
                                  roman_num.from_roman_to_arabic, numeral.lower())


if __name__ == "__main__":
    unittest.main()