import unittest
from task3.triangle_task import Triangle


class TestTriangle(unittest.TestCase):

    def test_square_calc_for_correct_calculation(self):
        expected = 41.23
        input_data = Triangle("n", 12, 15, 7)
        result = round(input_data.square_calc(), 2)
        self.assertEqual(result, expected)

    def test_square_calc_for_mistaken_calculation(self):
        expected = 0.0
        input_data = Triangle("n", 2, 7, 9)
        result = round(input_data.square_calc(), 2)
        self.assertEqual(expected, result)

    def test_square_calc_for_string_error(self):
        with self.assertRaises(ValueError):
            Triangle("n", "wdc", "dcw", "wec")

    def test_square_calc_for_minus_expretions(self):
        expected = 17.41
        input_data = Triangle("n", -5, -7, -9)
        result = round(input_data.square_calc(), 2)
        self.assertEqual(expected, result)

    def test_str_for_correct_output(self):
        expected = "[test]: 41.23 cm"
        result = Triangle("n", 2, 7, 9)
        self.assertNotEqual(result, expected)

    def test_str_for_wrong_output(self):
        expected = "[Test]: 41.23 cm"
        input_data = Triangle("Test", 12, 15, 7)
        input_data.square_calc()
        result = input_data.__str__()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
