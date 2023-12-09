#!/usr/bin/env python3
"""Unit tests for the Review Class.
Unit test classes:
    TestReviewInstantiation
    TestReviewSave
    TestReviewToDict
"""

import unittest
import os
from datetime import datetime
from time import sleep
from models import storage
from models.review import Review
from models.base_model import BaseModel
import uuid


class TestReviewInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    @classmethod
    def setUpClass(cls):
        """Set up the unit test."""
        cls.review = Review()
        cls.review.user_id = str(uuid.uuid4())
        cls.review.place_id = str(uuid.uuid4())
        cls.review.text = "St. Petersburg"

    @classmethod
    def tearDownClass(cls):
        """Clean up resources."""
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_no_args_instantiates(self):
        """Test that Review is instantiated with no arguments."""
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        """Test that a new Review instance is stored in objects."""
        self.assertIn(Review(), storage.all().values())

    def test_id_is_public_str(self):
        """Test that the id attribute is a public string."""
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        """Test that created_at attribute is a public datetime."""
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test that updated_at attribute is a public datetime."""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        """Test that place_id attribute is a public class attribute."""
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_user_id_ispublicclassattribute(self):
        """Test that user_id attribute is a public class attribute."""
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_text_is_public_class_attribute(self):
        """Test that text attribute is a public class attribute."""
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_two_reviews_unique_ids(self):
        """Test that two reviews have unique ids."""
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_two_reviews_different_created_at(self):
        """Test that two reviews have different created_at times."""
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_two_reviews_different_updated_at(self):
        """Test that two reviews have different updated_at times."""
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def test_str_representation(self):
        """Test the string representation of a Review instance."""
        dt = datetime.today()
        dt_repr = repr(dt)
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        rvstr = rv.__str__()
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)

    def test_args_unused(self):
        """Test that unused arguments are not stored in __dict__."""
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rv = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rv.id, "345")
        self.assertEqual(rv.created_at, dt)
        self.assertEqual(rv.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation with None as keyword arguments."""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReviewSave(unittest.TestCase):
    """Unittest for testing the save method of the Review class."""

    @classmethod
    def setUpClass(cls):
        """Set up the unit test."""
        cls.review = Review()
        cls.review.user_id = str(uuid.uuid4())
        cls.review.place_id = str(uuid.uuid4())
        cls.review.text = "St. Petersburg"

    @classmethod
    def tearDownClass(cls):
        """Clean up resources."""
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_validatesave(self):
        """Test that the save method updates the updated_at attribute."""
        updated_at_1 = self.review.updated_at
        self.review.save()
        updated_at_2 = self.review.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_one_save(self):
        """Test that one save updates the updated_at attribute."""
        pl = Review()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        self.assertLess(first_updated_at, pl.updated_at)

    def test_two_saves(self):
        """Test that two saves update the updated_at attribute."""
        pl = Review()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        second_updated_at = pl.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        pl.save()
        self.assertLess(second_updated_at, pl.updated_at)

    def test_save_with_arg(self):
        """Test that save with an argument raises TypeError."""
        pl = Review()
        with self.assertRaises(TypeError):
            pl.save(None)


class TestReviewToDict(unittest.TestCase):
    """Unittest for testing the to_dict method of the Review class."""

    @classmethod
    def setUpClass(cls):
        """Set up the unit test."""
        cls.review = Review()
        cls.review.user_id = str(uuid.uuid4())
        cls.review.place_id = str(uuid.uuid4())
        cls.review.text = "St. Petersburg"

    @classmethod
    def tearDownClass(cls):
        """Clean up resources."""
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_to_dict_type(self):
        """Test that to_dict returns a dictionary."""
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict contains the correct keys."""
        pl = Review()
        self.assertIn("id", pl.to_dict())
        self.assertIn("created_at", pl.to_dict())
        self.assertIn("updated_at", pl.to_dict())
        self.assertIn("__class__", pl.to_dict())

    def test_to_dicthasttributes(self):
        """Test that to_dict contains added attributes."""
        pl = Review()
        pl.middle_name = "Holberton"
        pl.my_number = 98
        self.assertEqual("Holberton", pl.middle_name)
        self.assertIn("my_number", pl.to_dict())

    def test_to_dictdatetime_attributes(self):
        """Test that datetime attributes in to_dict are strings."""
        pl = Review()
        pl_dict = pl.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of to_dict method."""
        dt = datetime.today()
        pl = Review()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(pl.to_dict(), tdict)

    def test_contrastdict(self):
        """Test the contrast between to_dict and __dict__."""
        pl = Review()
        self.assertNotEqual(pl.to_dict(), pl.__dict__)

    def test_to_dictarg(self):
        """Test the to_dict method with an argument."""
        pl = Review()
        with self.assertRaises(TypeError):
            pl.to_dict(None)


if __name__ == "__main__":
    unittest.main()
