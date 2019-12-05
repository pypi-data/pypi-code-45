import unittest
from n2d.controller import Controller


class TestDataLoader(unittest.TestCase):
    def test___init__(self):
        controller = Controller()
        self.assertTrue(controller)

    def test_train(self):
        pass


if __name__ == '__main__':
    unittest.main()
