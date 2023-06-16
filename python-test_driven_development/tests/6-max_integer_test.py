#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_int(self):
        #test maximum value in list
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([100, 2, 3, 4]), 100)
        self.assertAlmostEqual(max_integer([1, 2, 300, 4]), 300)
