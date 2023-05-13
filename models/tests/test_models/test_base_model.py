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
        self.my_inst.id = str(uuid.uuid4())
        self.my_inst.created_at = datetime.now()
        self.my_inst.updated_at = self.my_inst.created_at

        self.assertIsInstance(self.my_inst.id, str)
        self.assertIsInstance(self.my_inst.created_at, datetime)
        self.assertIsInstance(self.my_inst.updated_at, datetime)

        self.assertIsNotNone(self.my_inst.id)
        self.assertIsNotNone(self.my_inst.created_at)
        self.assertIsNotNone(self.my_inst.updated_at)
    
    def test__str__meth(self):
        """"""