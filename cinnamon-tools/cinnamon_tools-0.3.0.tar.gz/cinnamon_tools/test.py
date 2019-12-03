import unittest

from cinnamon_tools.point import Point


class TestPoint(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Point(1, 2, 3) + Point(1, 2, 3), Point(2, 4, 6))

    def test_subtraction(self):
        self.assertEqual(Point(1, 2, 3) - Point(1, 2, 3), Point(0, 0, 0))

    def test_multiplication(self):
        self.assertEqual(Point(1, 2, 3) * 2, Point(2, 4, 6))

    def test_reverse_multiplication(self):
        self.assertEqual(2 * Point(1, 2, 3), Point(2, 4, 6))


if __name__ == '__main__':
    unittest.main()
