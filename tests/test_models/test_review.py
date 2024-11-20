#!/usr/bin/python3
""" Unit tests for Review """

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ Test cases fr Review """

    def setUp(self):
        """ Sets up the test cases """
        self.review = Review()

    def test_place_id(self):
        """ Test that `place_id` has default attributes """
        self.assertIsInstance(self.review.place_id, str)
        self.assertEqual(self.review.place_id, "")

    def test_user_id(self):
        """ Test that `user_id` has default attributes """
        self.assertIsInstance(self.review.user_id, str)
        self.assertEqual(self.review.user_id, "")

    def test_text(self):
        """ Test that `text` has default attributes """
        self.assertIsInstance(self.review.text, str)
        self.assertEqual(self.review.text, "")


if __name__ == '__main__':
    unittest.main()
