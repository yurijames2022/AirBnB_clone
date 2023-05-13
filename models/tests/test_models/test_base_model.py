#!/usr/bin/python3
"""module creates test cases for BaseModel"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime


class BaseModel_tests(unittest.TestCase):
    """BaseModel test cases"""

    def setUp(self):
        self.my_inst = BaseModel()

    def test_inst_attr(self):
        """tests if the type of attributes is correct"""
        self.my_inst.id = str(uuid.uuid4())
        self.my_inst.created_at = datetime.now()
        self.my_inst.updated_at = self.my_inst.created_at

        self.assertIsInstance(self.my_inst.id, str)
        self.assertIsInstance(self.my_inst.created_at, datetime)
        self.assertIsInstance(self.my_inst.updated_at, datetime)

    def test_if_has_attributes(self):
        """to test if the attributes have values"""
        self.assertIsNotNone(self.my_inst.id)
        self.assertIsNotNone(self.my_inst.created_at)
        self.assertIsNotNone(self.my_inst.updated_at)

    def test_save(self):
        """to test if the save method works"""
        first_created_at = self.my_inst.created_at
        first_updated_at = self.my_inst.updated_at
        self.my_inst.save()

        self.assertIsInstance(self.my_inst.id, str)
        self.assertIsInstance(self.my_inst.created_at, datetime)
        self.assertIsInstance(self.my_inst.updated_at, datetime)

        self.assertEqual(self.my_inst.created_at, first_created_at)
        self.assertNotEqual(self.my_inst.updated_at, first_updated_at)

    def test_to_dict(self):
        """to test to_dict method"""
        dict1 = self.my_inst.to_dict()

        self.assertIsInstance(dict1, dict)

        self.assertIn('id', dict1)
        self.assertIn('created_at', dict1)
        self.assertIn('updated_at', dict1)
        self.assertIn('__class__', dict1)

        self.assertEqual(dict1['id'], self.my_inst.id)
        self.assertEqual(dict1['created_at'], self.my_inst.created_at)
        self.assertEqual(dict1['updated_at'], self.my_inst.updated_at)
        self.assertEqual(dict1['__class__'], 'BaseModel')


if __name__ == '__main__':
    unittest.main()
