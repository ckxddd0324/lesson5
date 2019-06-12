import unittest

from sum import *

class TestSum(unittest.TestCase):
    
    def test_sum_1(self):
        self.assertEqual(add_numbers(1,2), 3, "Expected sum of 1 and 2 to be 3 bit got " + str(add_numbers(1, 2)))
    
    def test_sum_2(self):
        self.assertEqual(add_numbers(10, 20), 30)

    def test_sum_3(self):
        self.assertEqual(add_three_numbers(10, 20, 30), 60)

if __name__ == "__main__":
    unittest.main()