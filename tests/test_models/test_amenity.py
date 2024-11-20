#!/usr/bin/python3
""" Unit tests for Amenity """

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Test cases for Amenity """

    def setUp(self):
        """ Sets up the test cases """
        self.amenity = Amenity()

    def test_name(self):
        """ Test `name` has correct attributes """
        self.assertIsInstance(self.amenity.name, str)
        self.assertEqual(self.amenity.name, "")


if __name__ == '__main__':
    unittest.main()
