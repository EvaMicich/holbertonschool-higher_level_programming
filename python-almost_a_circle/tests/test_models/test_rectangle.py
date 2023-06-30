"""unittest for rectangle module"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    test class Rectangle,
    checks that variables can be added
    deiiferen number of args
    """
    def test_args(self):
        """arguments correctly assigned"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)
