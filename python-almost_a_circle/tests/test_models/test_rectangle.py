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
        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        r3 = Rectangle(1, 2, 3)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        r4 = Rectangle(1, 2)
        self.assertEqual(r4.width, 1)
        self.assertEqual(r4.height, 2)

    def test_args(self):
        """string argument throws error at every argument position"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r1.width = "1"
        r2 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r2.height = "2"
        r3 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r3.x = "3"
        r4 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r4.y = "4"
