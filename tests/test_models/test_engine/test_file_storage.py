#!/usr/bin/python3
""" Unit tests for Storage """

import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Test cases for storage """

    def setUp(self):
        """ Sets up the test cases """
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.obj_key = f"{self.obj.__class__.__name__}.{self.obj.id}"
        # all_objs = self.storage.all()

    def tearDown(self):
        """ Resets storage for each test """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """ Test that `all` returns the dictionary __objects """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """ Test that `new` sets in  __objects with its key """
        self.storage.new(self.obj)
        self.assertIn(self.obj_key, self.storage.all())

    def test_save(self):
        """ Test that `save` serializes __objects to a JSON file """
        self.storage.new(self.obj)
        self.storage.save()
        with open("file.json", "r") as file:
            obj_dict = json.load(file)
            self.assertIn(self.obj_key, obj_dict)

    def test_reload(self):
        """ Test that `reload` deserializes JSON file to __objects """
        self.storage.new(self.obj)
        self.storage.save()
        self.storage.reload()
        self.assertIn(self.obj_key, self.storage.all())
        reloaded = self.storage.all()[self.obj_key]
        self.assertEqual(reloaded.id, self.obj.id)
        self.assertEqual(reloaded.created_at, self.obj.created_at)
        self.assertEqual(reloaded.updated_at, self.obj.updated_at)

    def test_reload_nfile(self):
        """ Test that `reload` implements correctly if file doesn't exist """
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})


if __name__ == '__main__':
    unittest.main()
