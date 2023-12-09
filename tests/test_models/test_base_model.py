#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModelInstantiation
    TestBaseModelInstancePrint
    TestBaseModelSave
    TestBaseModelFromJsonString
    TestBaseModelToDict
"""
from fileinput import lineno
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep
import time
import uuid
import json
import os
import re


class TestBaseModelInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_is_instance_of(self):
        """Test instance"""
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertEqual(
                str(type(b)),
                "<class 'models.base_model.BaseModel'>"
                )
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_contains_id(self):
        """Test if id attribute exists"""
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))

    def test_id_type(self):
        """Test if `id` attribute type"""
        b = BaseModel()
        self.assertEqual(type(b.id), str)

    def test_compare_two_instances_id(self):
        """Compare distinct instances ids"""
        b = BaseModel()
        v = BaseModel()
        self.assertNotEqual(b.id, v.id)

    def test_uuid(self):
        """Test that id is a valid uuid"""
        b = BaseModel()
        v = BaseModel()
        for inst in [b, v]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(b.id, v.id)

    def test_unique_id(self):
        """Tests for unique user ids."""
        u = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(u)), len(u))

    def test_two_models_unique_ids(self):
        b = BaseModel()
        v = BaseModel()
        self.assertNotEqual(b.id, v.id)

    def test_new_instanceinObjects(self):
        self.assertIn(BaseModel(), storage.all().values())

    def test_contains_created_at(self):
        """Checks `created_at` attribute existence"""
        b = BaseModel()
        self.assertTrue(hasattr(b, "created_at"))

    def test_created_at_inst(self):
        """Checks `created_at` attribute's type"""
        b = BaseModel()
        self.assertIsInstance(b.created_at, datetime)

    def test_updated_at(self):
        """Checks `updated_at` attribute existence"""
        b = BaseModel()
        self.assertTrue(hasattr(b, "updated_at"))

    def test_updated_at_inst(self):
        """Check `updated_at` attribute type"""
        b = BaseModel()
        self.assertIsInstance(b.updated_at, datetime)

    def test_datetime_created(self):
        """Tests if updated_at & created_at are current at creation."""
        date_now = datetime.now()
        b = BaseModel()
        differ = b.updated_at - b.created_at
        self.assertTrue(abs(differ.total_seconds()) < 0.01)
        differ = b.created_at - date_now
        self.assertTrue(abs(differ.total_seconds()) < 0.1)

    def test_id_isPublic(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_isPublicDatetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_isPublicDatetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_str_rep(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        b = BaseModel()
        b.id = "123456"
        b.created_at = b.updated_at = dt
        bstr = b.__str__()
        self.assertIn("[BaseModel] (123456)", bstr)
        self.assertIn("'id': '123456'", bstr)
        self.assertIn("'created_at': " + dt_repr, bstr)
        self.assertIn("'updated_at': " + dt_repr, bstr)

    def test_args_unused(self):
        b = BaseModel(None)
        self.assertNotIn(None, b.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        b = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(b.id, "345")
        self.assertEqual(b.created_at, dt)
        self.assertEqual(b.updated_at, dt)

    def test_instantiationKwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiationArgsKwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        b = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(b.id, "345")
        self.assertEqual(b.created_at, dt)
        self.assertEqual(b.updated_at, dt)


class TestBaseModelInstancePrint(unittest.TestCase):
    """Unittest for testing the __str__ method."""

    def test_str_return(self):
        """Unittest for testing the return value of __str__ method."""
        b = BaseModel()
        Dika = "[{}] ({}) {}".format("BaseModel", b.id, str(b.__dict__))
        self.assertEqual(str(b), Dika)

    def test_str(self):
        """test that the str method has the correct output"""
        b = BaseModel()
        string = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(string, str(b))

    def test_of_str(self):
        """Tests for __str__ method."""
        b = BaseModel()
        ret = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = ret.match(str(b))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), b.id)
        x = res.group(3)
        x = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", x)
        d = json.loads(x.replace("'", '"'))
        d2 = b.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)


class TestBaseModelSaveMethod(unittest.TestCase):
    """Unittest for testing the save method."""

    def test_validatesave(self):
        """Check save models"""
        b = BaseModel()
        updated_at_1 = b.updated_at
        b.save()
        updated_at_2 = b.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_onesave(self):
        b = BaseModel()
        sleep(0.05)
        first_updated_at = b.updated_at
        b.save()
        self.assertLess(first_updated_at, b.updated_at)

    def test_twosaves(self):
        b = BaseModel()
        sleep(0.05)
        first_updated_at = b.updated_at
        b.save()
        second_updated_at = b.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        b.save()
        self.assertLess(second_updated_at, b.updated_at)

    def test_savearg(self):
        b = BaseModel()
        with self.assertRaises(TypeError):
            b.save(None)


class TestBaseModelToDictMethod(unittest.TestCase):
    """Unittest for testing the to_dict method of the BaseModel class."""

    def test_classnamepresent(self):
        """Test class name present"""
        b = BaseModel()
        dic = b.to_dict()
        self.assertNotEqual(dic, b.__dict__)

    def test_attributeIsoformat(self):
        """Test datetime field isoformated"""
        b = BaseModel()
        dic = b.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)

    def test_todictType(self):
        b = BaseModel()
        self.assertTrue(dict, type(b.to_dict()))

    def test_todictContainscorrectkeys(self):
        b = BaseModel()
        self.assertIn("id", b.to_dict())
        self.assertIn("created_at", b.to_dict())
        self.assertIn("updated_at", b.to_dict())
        self.assertIn("__class__", b.to_dict())

    def test_toDicthasAddedAttributes(self):
        b = BaseModel()
        b.name = "Holberton"
        b.my_number = 98
        self.assertIn("name", b.to_dict())
        self.assertIn("my_number", b.to_dict())

    def test_toDictDatetimeAttributes(self):
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertEqual(str, type(b_dict["created_at"]))
        self.assertEqual(str, type(b_dict["updated_at"]))

    def test_toDictOutput(self):
        dt = datetime.today()
        b = BaseModel()
        b.id = "123456"
        b.created_at = b.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(b.to_dict(), tdict)

    def test_contrasttoDict(self):
        b = BaseModel()
        self.assertNotEqual(b.to_dict(), b.__dict__)

    def test_to_dictarg(self):
        b = BaseModel()
        with self.assertRaises(TypeError):
            b.to_dict(None)


if __name__ == "__main__":
    unittest.main()
