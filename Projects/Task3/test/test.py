import unittest
from unittest import mock
import Task3


class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.trian = Task3.Triangle("test", 12, 15, 7)

    def test_square_calc_for_correct_calculation(self):
        expected = 41.23
        result = round(self.trian.square_calc(), 2)
        self.assertTrue(result == expected)

    def test_square_calc_for_mistaken_calculation(self):
        expected = 0.0
        self.trian.a = 2
        self.trian.b = 7
        self.trian.c = 9
        result = round(self.trian.square_calc(), 2)
        self.assertTrue(expected == result)

    def test_square_calc_for_string_error(self):
        expected = TypeError
        self.trian.a = "wdc"
        self.trian.b = "dcw"
        self.trian.c = "wec"
        self.assertRaises(expected, self.trian.square_calc)

    def test_square_calc_for_minus_expretions(self):
        expected = 17.41
        self.trian.a = -5
        self.trian.b = -7
        self.trian.c = -9
        result = round(self.trian.square_calc(), 2)
        self.assertTrue(expected == result)

    def test_str_for_correct_output(self):
        expected = "[test]: 41.23 cm"
        result = self.trian.__str__()
        self.assertNotEqual(result, expected, "Incorrect output")

    def test_str_for_wrong_output(self):
        expected = "[Test]: 41.23 cm"
        result = self.trian.__str__()
        self.assertEqual(result, expected, "Incorrect output")

if __name__ == '__main__':
    unittest.main()