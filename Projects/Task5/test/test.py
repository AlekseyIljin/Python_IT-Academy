import unittest
import Task5


class TestDigit(unittest.TestCase):
    def test_to_string_for_correct_interpretation(self):
        expected = "Восемьсот пятнадцать"
        result = Task5.Digit(415)
        self.assertTrue(result, expected)

    def test_to_string_for_correct_unit_interpretation(self):
        expected = "Ноль"
        result = Task5.Digit(0)
        self.assertTrue(result, expected)

    def test_to_string_for_correct_teens_interpretation(self):
        expected = "Одиннадцать"
        result = Task5.Digit(11)
        self.assertTrue(result, expected)

    def test_to_string_for_correct_tens_interpretation(self):
        expected = "Двадцать"
        result = Task5.Digit(20)
        self.assertTrue(result, expected)

    def test_to_string_for_correct_decimal_interpretation(self):
        expected = "Сорок один"
        result = Task5.Digit(41)
        self.assertTrue(result, expected)

    def test_to_string_for_correct_thousands_interpretation(self):
        expected = "Пять тысяч сто пятьдесят три"
        result = Task5.Digit(5153)
        self.assertTrue(result, expected)

    def test_to_string_for_correct_decimal_thousands_interpretation(self):
        expected = "Девяносто семь тысяч четыреста восемдесят один"
        result = Task5.Digit(97481)
        self.assertTrue(result, expected)

    def test_to_string_for_correct_tens_thousands_interpretation(self):
        expected = "Двенадцать тысяч восемьсот сорок семь"
        result = Task5.Digit(12847)
        self.assertTrue(result, expected)

