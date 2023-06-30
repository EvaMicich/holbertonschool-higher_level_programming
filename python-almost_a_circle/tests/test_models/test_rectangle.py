"""unittest for rectangle module"""
import unittest
from models.rectangle import Rectangle
import io
import sys

class TestRectangle(unittest.TestCase):
    """
    test class Rectangle,
    checks that variables can be added
    deiiferen number of args
    """
    def test_args_work(self):
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

    def test_rect_args_str(self):
        """string argument throws error at every argument position"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, "3", 4)
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 2, 3, "4")

    def test_rect_args_negative(self):
        """negative/zero argument throws error at every argument position"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 2, 3, -4)
        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r6 = Rectangle(1, 0)

    def test_rectangle_area(self):
        """area is correctly calcultaed for rectangle"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.area(), 2)

    def test_rectangle_string(self):
        """the string method delivers expected custom message"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_display(self):
        """the string method delivers expected custom message"""
        out = io.StringIO()
        sys.stdout = out
        r1 = Rectangle(1, 1)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "#\n")
