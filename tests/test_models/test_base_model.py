#!/usr/bin/python3
""" Unit tests for Base Model """

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Test cases for Base Model"""

    def setUp(self):
        """ Sets up the test cases """
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.number = 89

    def test_creation(self):
        """ Test BaseModel with correct instances """
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_unique_id(self):
        """ Test that each instance has its own unique id """
        my_model1 = BaseModel()
        self.assertNotEqual(self.my_model.id, my_model1.id)

    def test_save(self):
        """ Test if `save` correctly updates `updated_at` """
        last_update = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, last_update)

    def test_to_dict(self):
        """ Test if `to_dict` is correctly implemented """
        my_model_dict = self.my_model.to_dict()
        self.assertIn("name", my_model_dict)
        self.assertIn("number", my_model_dict)
        self.assertEqual(my_model_dict["name"], "My First Model")
        self.assertEqual(my_model_dict["number"], 89)

    def test_str(self):
        """ Test that __str__ method is correctly implemented """
        my_string = str(self.my_model)
        my_name = self.my_model.__class__.__name__
        result = f"[{my_name}] ({self.my_model.id}) {self.my_model.__dict__}"
        self.assertEqual(my_string, result)


if __name__ == '__main__':
    unittest.main()
