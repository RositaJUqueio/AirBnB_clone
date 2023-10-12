#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModelInstantiation
    TestBaseModelSave
    TestBaseModelToDict
"""

import os
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModelInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        from models import storage
        self.assertIn(BaseModel(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        current_time = datetime.today()
        current_time_repr = repr(current_time)
        base_model = BaseModel()
        base_model.id = "123456"
        base_model.created_at = base_model.updated_at = current_time
        base_model_str = base_model.__str__()
        self.assertIn("[BaseModel] (123456)", base_model_str)
        self.assertIn("'id': '123456'", base_model_str)
        self.assertIn("'created_at': " + current_time_repr, base_model_str)
        self.assertIn("'updated_at': " + current_time_repr, base_model_str)

    def test_args_unused(self):
        base_model = BaseModel(None)
        self.assertNotIn(None, base_model.__dict__.values())

    def test_instantiation_with_kwargs(self):
        current_time = datetime.today()
        current_time_iso = current_time.isoformat()
        base_model = BaseModel(id="345", created_at=current_time_iso, updated_at=current_time_iso)
        self.assertEqual(base_model.id, "345")
        self.assertEqual(base_model.created_at, current_time)
        self.assertEqual(base_model.updated_at, current_time)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        current_time = datetime.today()
        current_time_iso = current_time.isoformat()
        base_model = BaseModel("12", id="345", created_at=current_time_iso, updated_at=current_time_iso)
        self.assertEqual(base_model.id, "345")
        self.assertEqual(base_model.created_at, current_time)
        self.assertEqual(base_model.updated_at, current_time)
