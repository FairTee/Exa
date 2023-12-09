#!/usr/bin/env python3
"""Defines unittests for models/user.py.
Unittest classes:
    TestUserInstantiation
    TestUserSave
    TestUserToDict
"""

import unittest
import os
from models import storage
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import uuid


class TestUserInstantiation(unittest.TestCase):
    """User model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.user = User()
        cls.user.email = "me@example.com"
        cls.user.password = "123i123"
        cls.user.first_name = "John"
        cls.user.last_name = "Swag"

    def test_the_instantiation(self):
        """Test instantiation of User class."""
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_noargs_instantiates(self):
        """Test that User is instantiated with no arguments."""
        self.assertEqual(User, type(User()))

    def test_new_instance_of_objects(self):
        """Test that a new User instance is stored in objects."""
        self.assertIn(User(), storage.all().values())

    def testidispublicstr(self):
        """Test that the id attribute is a public string."""
        self.assertEqual(str, type(User().id))

    def test_created_at_publicdatetime(self):
        """Test that created_at attribute is a public datetime."""
        self.assertEqual(datetime, type(User().created_at))

    def testAttributes(self):
        """Test that User instance has expected attributes."""
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def testAttributes_str(self):
        """Test that User attributes are of type string."""
        self.assertIs(type(self.user.email), str)
        self.assertIs(type(self.user.password), str)
        self.assertIs(type(self.user.first_name), str)
        self.assertIs(type(self.user.last_name), str)

    def testSubclass(self):
        """Test that User is a subclass of BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def testEmailAttribute(self):
        """
        Test that User has the email attribute
        initialized as an empty string.
        """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def testPasswordAttribute(self):
        """
        Test that User has the password attribute
        initialized as an empty string.
        """
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def testFirstNameAttribute(self):
        """
        Test that User has the first_name attribute
        initialized as an empty string.
        """
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def testLastNameAttribute(self):
        """
        Test that User has the last_name
        attribute initialized as an empty string.
        """
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def testString(self):
        """Test the string representation of a User instance."""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))

    def testSave(self):
        """Test the save method of the User class."""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def testDict(self):
        """Test the to_dict method of the User class."""
        self.assertTrue('to_dict' in dir(self.user))

    def test_to_dict_CreatesDict(self):
        """
        Test that to_dict method creates a dictionary
        with proper attributes.
        """
        X = User()
        nd = X.to_dict()
        self.assertEqual(type(nd), dict)
        for attr in X.__dict__:
            self.assertTrue(attr in nd)
            self.assertTrue("__class__" in nd)

    def test_to_DictValues(self):
        """
        Test that values in the dictionary returned
        from to_dict are correct.
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        X = User()
        nd = X.to_dict()
        self.assertEqual(nd["__class__"], "User")
        self.assertEqual(type(nd["created_at"]), str)
        self.assertEqual(type(nd["updated_at"]), str)
        self.assertEqual(nd["created_at"], X.created_at.strftime(t_format))
        self.assertEqual(nd["updated_at"], X.updated_at.strftime(t_format))


if __name__ == "__main__":
    unittest.main()
