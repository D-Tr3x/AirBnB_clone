#!/usr/bin/python3
""" Unit tests for City """

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ Test cases for City """

    def setUp(self):
        """ Sets up the test cases """
        self.my_city = City()

    def test_state_id(self):
        """ Test that `state_id` has correct attributes """
        self.assertIsInstance(self.my_city.state_id, str)
        self.assertEqual(self.my_city.state_id, "")

    def test_name(self):
        """ Test that `name` has correct attributes """
        self.assertIsInstance(self.my_city.name, str)
        self.assertEqual(self.my_city.name, "")


if __name__ == '__main__':
    unittest.main()
