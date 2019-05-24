import unittest
from task5.interpreter import Digit


class TestDigit(unittest.TestCase):
    def test_to_string_for_correct_interpretation(self):
        expected = "Восемьсот пятнадцать"
        result = Digit("815").to_string()
        self.assertEqual(result, expected)

    def test_to_string_for_correct_unit_interpretation(self):
        expected = "Ноль"
        result = Digit("0").to_string()
        self.assertEqual(result, expected)

    def test_to_string_for_correct_teens_interpretation(self):
        expected = "Одиннадцать"
        result = Digit("11").to_string()
        self.assertEqual(result, expected)

    def test_to_string_for_correct_tens_interpretation(self):
        expected = "Двадцать"
        result = Digit("20").to_string()
        self.assertEqual(result, expected)

    def test_to_string_for_correct_decimal_interpretation(self):
        expected = "Сорок один"
        result = Digit("41").to_string()
        self.assertEqual(result, expected)

    def test_to_string_for_correct_thousands_interpretation(self):
        expected = "Пять тыс сто пятьдесят три"
        result = Digit("5153").to_string()
        self.assertEqual(result, expected)

    def test_to_string_for_correct_decimal_thousands_interpretation(self):
        expected = "Девяносто семь тыс четыреста восемдесят один"
        result = Digit("97481").to_string()
        self.assertEqual(expected, result)

    def test_to_string_for_correct_tens_thousands_interpretation(self):
        expected = "Двенадцать тыс восемьсот сорок семь"
        result = Digit("12847").to_string()
        self.assertEqual(result, expected)

    def test_to_string_for_incorrect_datatype(self):
        expected = TypeError
        result = Digit("khvv6")
        self.assertRaises(expected, result)

    def test_hundreds_calculation_for_zeroes_check(self):
        expected = ' семь'
        input_data = 0o07
        result = Digit("123").hundreds_calculation(input_data)
        self.assertEqual(expected, result)

    def test_to_string_for_mistaken_unit_interpretation(self):
        expected = 5
        result = Digit("5").to_string()
        self.assertNotEqual(result, expected)

    def test_to_string_for_mistaken_teens_interpretation(self):
        expected = "Один семь"
        result = Digit("17").to_string()
        self.assertNotEqual(result, expected)

    def test_to_string_for_mistaken_tens_interpretation(self):
        expected = 20
        result = Digit("20").to_string()
        self.assertNotEqual(result, expected)

    def test_to_string_for_mistaken_decimal_interpretation(self):
        expected = "Пятнадцать семь"
        result = Digit("57")
        self.assertNotEqual(result, expected)

    def test_to_string_for_mistaken_thousands_interpretation(self):
        expected = "Три тыс 5 1"
        result = Digit("3051").to_string()
        self.assertNotEqual(result, expected)

    def test_to_string_for_mistaken_decimal_thousands_interpretation(self):
        expected = "Сорок пять тысяч восемьсот"
        result = Digit("45803").to_string()
        self.assertNotEqual(result, expected)

    def test_to_string_for_mistaken_tens_thousands_interpretation(self):
        expected = "тринадцать тысяч семьдесят восемьсот"
        result = Digit("13870").to_string()
        self.assertNotEqual(result, expected)