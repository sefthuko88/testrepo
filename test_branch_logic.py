# test_branch_logic.py

import unittest
from branch_logic import categorize_number

class TestBranchLogic(unittest.TestCase):

    def test_negative_number(self):
        self.assertEqual(categorize_number(-1), "Negative")
        self.assertEqual(categorize_number(-100), "Negative")

    def test_zero(self):
        self.assertEqual(categorize_number(0), "Zero")

    def test_small_positive_number(self):
        self.assertEqual(categorize_number(1), "Small Positive")
        self.assertEqual(categorize_number(10), "Small Positive")

    def test_large_positive_number(self):
        self.assertEqual(categorize_number(11), "Large Positive")
        self.assertEqual(categorize_number(100), "Large Positive")

if __name__ == '__main__':
    unittest.main()
