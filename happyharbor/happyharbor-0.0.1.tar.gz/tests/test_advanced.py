# -*- coding: utf-8 -*-

import unittest

import sample


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(sample.hmm())


if __name__ == '__main__':
    unittest.main()
