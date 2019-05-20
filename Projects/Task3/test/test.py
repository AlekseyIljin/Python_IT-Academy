import unittest
import Task3

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.trian = Task3.Triangle("test", "12", "15", "7")
    def test_square_calc_for_correct_calculation (self):
        expected = 41.23
        result = self.trian.square_calc()
        print(result)
        assert (result == expected)