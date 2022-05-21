import re


class RomanError(Exception):
    pass


class OutOfRangeError(RomanError):
    pass


class NotIntegerError(RomanError):
    pass


class InvalidRomanNumeralError(RomanError):
    pass


def validation(num):
    return bool(re.search(r"^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", num))


list_num = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"),
                         (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def from_arabic_to_roman(arabic_number):
    if arabic_number <= 0 or arabic_number > 4999:
        raise OutOfRangeError("Podana liczba musi być dodatnia, ale nie większa od 4999.")
    elif not isinstance(arabic_number, int):
        raise NotIntegerError("Podana liczba musi być typu int.")

    result = ""

    for number in list_num:
        while arabic_number >= number[0]:
            arabic_number -= number[0]
            result += number[1]
    return result


def from_roman_to_arabic(roman_number):
    if not validation(roman_number):
        raise InvalidRomanNumeralError("Podaj tylko cyfry rzymskie.")
    elif roman_number == "":
        raise InvalidRomanNumeralError("Podaj cyfry rzymskie.")

    i = 0
    result = 0

    for i_number, r_number in list_num:
        while roman_number[i:i + len(r_number)] == r_number:
            result += i_number
            i += len(r_number)
    return result
