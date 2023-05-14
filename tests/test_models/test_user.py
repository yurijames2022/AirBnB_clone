#!/usr/bin/python3
"""unittests for user module"""
import unittest
from datetime import datetime
from models.user import User


class UserTests(unittest.TestCase):
    """class UserTests for user unittests"""
    def setUp(self):
        """setup method"""
        self.usr = User()

    def test_user_exists(self):
        """to test if the class exists"""
        self.assertIsNotNone(User)

    def test_user_attributes(self):
        """to test if the class has attributes,
        including inherited ones"""
        self.assertTrue(self.usr, 'email')
        self.assertTrue(self.usr, 'first_name')
        self.assertTrue(self.usr, 'last_name')
        self.assertTrue(self.usr, 'password')
        self.assertTrue(self.usr, 'id')
        self.assertTrue(self.usr, 'create_at')
        self.assertTrue(self.usr, 'updated_at')

    def test_attribute_types(self):
        """to test the type of attributes"""
        self.assertIsInstance(self.usr.email, str)
        self.assertIsInstance(self.usr.password, str)
        self.assertIsInstance(self.usr.first_name, str)
        self.assertIsInstance(self.usr.last_name, str)
        self.assertIsInstance(self.usr.id, str)
        self.assertIsInstance(self.usr.created_at, datetime)
        self.assertIsInstance(self.usr.updated_at, datetime)

    def test_inheritance(self):
        """to test inheritance of user"""
        self.assertIsInstance(self.usr, User)


if __name__ == '__main__':
    unittest.main()
