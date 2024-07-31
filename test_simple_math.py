# test_simple_math.py

import unittest
from simple_math import add

class TestSimpleMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_add_with_floats(self):
        self.assertEqual(add(1.5, 2.5), 4.0)
        self.assertEqual(add(-1.5, 1.5), 0.0)

if __name__ == '__main__':
    unittest.main()
