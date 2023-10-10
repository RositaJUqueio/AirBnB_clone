#!/usr/bin/python3
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


"""
Defines unittests for models/base_model.py

Test Class: TestBaseModel_Instance
"""
class TestBaseModel_Instances(unittest.TestCase):
    """ Unittests to test the instantiation of BaseModel class."""

    def test_no_argsuments(self):
        self.assertEqual(BaseModel, type(BaseModel()))
    
    def test_public_id_str(self):
        self.assertEqual(str, type(BaseModel().id))
    
    def test_created_at_public(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_public(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_new_instance_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())


    def test_models_unique_ids(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_models_created_at(self):
        model1 = BaseModel()
        sleep(0.05)
        model2 = BaseModel()
        self.assertLess(model1.created_at, model2.created_at)

    def test_models_updated_at(self):
        model1 = BaseModel()
        sleep(0.05)
        model2 = BaseModel()
        self.assertLess(model1.updated_at, model2.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_rep = repr(date)
        model = BaseModel()
        model.id = "123456"
        model.created_at = model.updated_at = date
        model_str = model.__str__()
        self.assertIn("[BaseModel] (123456)", model_str)
        self.assertIn("'id': '123456'", model_str)
        self.assertIn("'created_at': " + date_rep, model_str)
        self.assertIn("'updated_at': " + date_rep, model_str)

    def test_args_unused(self):
        model = BaseModel(None)
        self.assertNotIn(None, model.__dict__.values())

    def test_with_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        model = BaseModel(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(model.id, "345")
        self.assertEqual(model.created_at, date)
        self.assertEqual(model.updated_at, date)

    def test_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_with_args_and_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        model = BaseModel("12", id="123", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(model.id, "123")
        self.assertEqual(model.created_at, date)
        self.assertEqual(model.updated_at, date)