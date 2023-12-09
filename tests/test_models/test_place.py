#!/usr/bin/env python3

"""
Unit tests for the Place Class
"""

import unittest
import os
from models.place import Place
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
import uuid


class TestPlaceInstantiation(unittest.TestCase):
    """Test case for instantiating the Place class."""

    @classmethod
    def setUpClass(cls):
        """Set up the unit test."""
        cls.place = Place()
        cls.place.city_id = str(uuid.uuid4())
        cls.place.user_id = str(uuid.uuid4())
        cls.place.name = "Any place in the world"
        cls.place.description = "Sunny Beach"
        cls.place.number_rooms = 0
        cls.place.number_bathrooms = 0
        cls.place.max_guest = 0
        cls.place.price_by_night = 0
        cls.place.latitude = 0.0
        cls.place.longitude = 0.0
        cls.place.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        """Clean up resources."""
        del cls.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """Test that Place is a subclass of BaseModel."""
        self.assertTrue(issubclass(self.place.__class__, BaseModel))

    def checking_for_doc(self):
        """Check if Place has a docstring."""
        self.assertIsNotNone(Place.__doc__)

    def test_has_attributes(self):
        """Test that Place instance has the expected attributes."""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)

    def test_attributes_are_string(self):
        """Test that attributes of Place are of the correct types."""
        self.assertIs(type(self.place.city_id), str)
        self.assertIs(type(self.place.user_id), str)
        self.assertIs(type(self.place.name), str)
        self.assertIs(type(self.place.description), str)
        self.assertIs(type(self.place.number_rooms), int)
        self.assertIs(type(self.place.max_guest), int)
        self.assertIs(type(self.place.price_by_night), int)
        self.assertIs(type(self.place.latitude), float)
        self.assertIs(type(self.place.longitude), float)
        self.assertIs(type(self.place.amenity_ids), list)

    def test_save(self):
        """Test the save method of Place."""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_one_save(self):
        """Test the save method with one save."""
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        self.assertLess(first_updated_at, pl.updated_at)

    def test_two_saves(self):
        """Test the save method with two saves."""
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        second_updated_at = pl.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        pl.save()
        self.assertLess(second_updated_at, pl.updated_at)

    def test_save_with_arg(self):
        """Test the save method with an argument."""
        pl = Place()
        with self.assertRaises(TypeError):
            pl.save(None)


class TestPlaceToDict(unittest.TestCase):
    """Unit tests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        """Test that to_dict method returns a dictionary."""
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict contains the correct keys."""
        pl = Place()
        self.assertIn("id", pl.to_dict())
        self.assertIn("created_at", pl.to_dict())
        self.assertIn("updated_at", pl.to_dict())
        self.assertIn("__class__", pl.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test that to_dict includes added attributes."""
        pl = Place()
        pl.middle_name = "Holberton"
        pl.my_number = 98
        self.assertEqual("Holberton", pl.middle_name)
        self.assertIn("my_number", pl.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test that datetime attributes in to_dict are strings."""
        pl = Place()
        pl_dict = pl.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of to_dict method."""
        dt = datetime.today()
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(pl.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test the contrast between to_dict and __dict__."""
        pl = Place()
        self.assertNotEqual(pl.to_dict(), pl.__dict__)

    def test_to_dict_with_arg(self):
        """Test the to_dict method with an argument."""
        pl = Place()
        with self.assertRaises(TypeError):
            pl.to_dict(None)


if __name__ == "__main__":
    unittest.main()
