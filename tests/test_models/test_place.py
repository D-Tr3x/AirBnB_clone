#!/usr/bin/python3
""" Unit tests for Place """

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test cases for Place """

    def setUp(self):
        """ Sets up the test cases """
        self.my_place = Place()

    def test_city_id(self):
        """ Test `city_id` with default attributes """
        self.assertIsInstance(self.my_place.city_id, str)
        self.assertEqual(self.my_place.city_id, "")

    def test_user_id(self):
        """ Test `user_id` with default attributes """
        self.assertIsInstance(self.my_place.user_id, str)
        self.assertEqual(self.my_place.user_id, "")

    def test_name(self):
        """ Test `name` with default attributes """
        self.assertIsInstance(self.my_place.name, str)
        self.assertEqual(self.my_place.name, "")

    def test_desc(self):
        """ Test `description` with default attributes """
        self.assertIsInstance(self.my_place.description, str)
        self.assertEqual(self.my_place.description, "")

    def test_rooms(self):
        """ Test `number_rooms` with default attributes """
        self.assertIsInstance(self.my_place.number_rooms, int)
        self.assertEqual(self.my_place.number_rooms, 0)

    def test_bathrooms(self):
        """ Test `number_bathrooms` with default attributes """
        self.assertIsInstance(self.my_place.number_bathrooms, int)
        self.assertEqual(self.my_place.number_bathrooms, 0)

    def test_max_guest(self):
        """ Test `max_guest` with default attributes """
        self.assertIsInstance(self.my_place.max_guest, int)
        self.assertEqual(self.my_place.max_guest, 0)

    def test_ngt_price(self):
        """ Test `price_by_night` with default attributes """
        self.assertIsInstance(self.my_place.price_by_night, int)
        self.assertEqual(self.my_place.price_by_night, 0)

    def test_latitude(self):
        """ Test `latitude` with default attributes """
        self.assertIsInstance(self.my_place.latitude, float)
        self.assertEqual(self.my_place.latitude, 0.0)

    def test_longitude(self):
        """ Test `longitude` with default attributes """
        self.assertIsInstance(self.my_place.longitude, float)
        self.assertEqual(self.my_place.longitude, 0.0)

    def test_amenity_ids(self):
        """ Test `amenity_ids` with default attributes """
        self.assertIsInstance(self.my_place.amenity_ids, list)
        self.assertEqual(self.my_place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
