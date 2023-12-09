#!/usr/bin/python3
"""Unit tests for the City Class.
Unit test classes:
    TestCityInstantiation
    TestCitySave
    TestCityToDict
"""

import unittest
from datetime import datetime
import time
import uuid
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCityInstantiation(unittest.TestCase):
    """Test case for instantiating the City class."""

    @classmethod
    def setUpClass(cls):
        """Set up the unit test."""
        cls.city = City()
        cls.city.state_id = str(uuid.uuid4())
        cls.city.name = "St. Petersburg"

    @classmethod
    def tearDownClass(cls):
        """Clean up resources."""
        del cls.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_no_args_instantiates(self):
        """Test that the City class can be instantiated with no arguments."""
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        """
        Test that a new instance of City is stored
        in the 'objects' attribute of storage.
        """
        self.assertIn(City(), storage.all().values())

    def test_id_is_public_str(self):
        """Test that the 'id' attribute of City is a public string."""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        """
        Test that the 'created_at' attribute of
        City is a public datetime.
        """
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_PublicDatetime(self):
        """
        Test that the 'updated_at' attribute
        of City is a public datetime.
        """
        self.assertEqual(datetime, type(City().updated_at))

    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel."""
        self.assertTrue(issubclass(self.city.__class__, BaseModel))

    def checkdoc(self):
        """Check if City has a docstring."""
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        """Test that City instance has the expected attributes."""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_state_idPublicClassAttribute(self):
        """Test that 'state_id' is a public class attribute of City."""
        c = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(c))
        self.assertNotIn("state_id", c.__dict__)

    def test_name_is_public_ClassAttribute(self):
        """Test that 'name' is a public class attribute of City."""
        c = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(c))
        self.assertNotIn("name", c.__dict__)

    def test_attributes_are_string(self):
        """Test that 'state_id' and 'name' attributes of City are strings."""
        self.assertIs(type(self.city.state_id), str)
        self.assertIs(type(self.city.name), str)

    def test_save(self):
        """Test the save method of City."""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of City."""
        self.assertTrue('to_dict' in dir(self.city))


if __name__ == "__main__":
    unittest.main()
