#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import uuid
import datetime
import time
import re
import json
from models.engine.file_storage import FileStorage
from models import storage


class TestAmenity(unittest.TestCase):
    """Amenity model class test case"""

    @classmethod
    def setUpClass(cls):
        """Set up the unittest"""
        cls.amenity = Amenity()
        cls.amenity.name = "Wifi"

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel))

    def test_doc_string_exists(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

    def test_attributes_are_string(self):
        self.assertIs(type(self.amenity.name), str)

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.amenity)), res)

    def test_user_inheritance(self):
        """test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.amenity.name, str)
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime.datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime.datetime)

    def test_save(self):
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.amenity))


if __name__ == "__main__":
    unittest.main()
