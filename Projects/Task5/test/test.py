import unittest
from Task5 import Digit


class TestDigit(unittest.TestCase):
    def test_to_string_for_correct_interpretation(self):
        expected = "Восемьсот пятнадцать"
        result = Task5.Digit(415).to_string()
        self.assertTrue(result, expected)

    def test_to_string_for_correct_unit_interpretation(self):
        expected = "Ноль"
        result = Task5.Digit(0).to_string()
        self.assertTrue(result, expected)

    def test_to_string_for_correct_teens_interpretation(self):
        expected = "Одиннадцать"
        result = Task5.Digit(11).to_string()
        self.assertTrue(result, expected)

    def test_to_string_for_correct_tens_interpretation(self):
        expected = "Двадцать"
        result = Task5.Digit(20).to_string()
        self.assertTrue(result, expected)

    def test_to_string_for_correct_decimal_interpretation(self):
        expected = "Сорок один"
        result = Task5.Digit(41)
        self.assertTrue(result, expected)

    def test_to_string_for_correct_thousands_interpretation(self):
        expected = "Пять тысяч сто пятьдесят три"
        result = Task5.Digit(5153).to_string()
        self.assertTrue(result, expected)

    def test_to_string_for_correct_decimal_thousands_interpretation(self):
        expected = "Девяносто семь тысяч четыреста восемдесят один"
        result = Task5.Digit(97481).to_string()
        self.assertTrue(result, expected)

    def test_to_string_for_correct_tens_thousands_interpretation(self):
        expected = "Двенадцать тысяч восемьсот сорок семь"
        result = Task5.Digit(12847).to_string()
        self.assertTrue(result, expected)

    def test_to_string_for_incorrect_datatype(self):
        expected = TypeError
        result = Task5.Digit("khvv6")
        self.assertRaises(expected, result)

    def test_hundreds_calculation_for_zeroes_check(self):
        expected = "Семь"
        input_data = 0o07
        result = Task5.Digit(123).hundreds_calculation(input_data)
        self.assertTrue(result, expected)

    def test_to_string_for_mistaken_unit_interpretation(self):
        expected = 5
        result = Task5.Digit(5).to_string()
        self.assertNotEqual(result, expected)

    def test_to_string_for_mistaken_teens_interpretation(self):
        expected = "Один семь"
        result = Task5.Digit(17).to_string()
        self.assertNotEqual(result, expected)

    def test_to_string_for_mistaken_tens_interpretation(self):
        expected = 20
        result = Digit(20).to_string()
        self.assertNotEqual(result, expected)

    def test_to_string_for_mistaken_decimal_interpretation(self):
        expected = "Пятнадцать семь"
        result = Task5.Digit(57)
        self.assertNotEqual(result, expected)

    def test_to_string_for_mistaken_thousands_interpretation(self):
        expected = "Три тысяча 5 1"
        result = Task5.Digit(3051).to_string()
        self.assertNotEqual(result, expected)

    def test_to_string_for_mistaken_decimal_thousands_interpretation(self):
        expected = "Сорок пять тысяч восемьсот"
        result = Task5.Digit(45803).to_string()
        self.assertNotEqual(result, expected)

    def test_to_string_for_mistaken_tens_thousands_interpretation(self):
        expected = "тринадцать тысяч семьдесят восемьсот"
        result = Task5.Digit(13870).to_string()
        self.assertNotEqual(result, expected)