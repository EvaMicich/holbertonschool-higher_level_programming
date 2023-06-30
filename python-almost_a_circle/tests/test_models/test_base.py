"""unittest for base module"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """test class Base"""
    def test_id(self):
        """Base assigns unique id"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertNotEqual(b1.id, b2.id)

    def test_id_plus_one(self):
        """Base assigns sequential id"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id + 1, b2.id)
        self.assertEqual(b2.id + 1, b3.id)

    def test_saving_id(self):
        """Test that checks id is correctly assigned"""
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_to_json_string(self):
        """Tests the method to_json_string for different input cases"""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")
