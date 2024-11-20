#!/usr/bin/python3
"""Unit tests for User"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ Test cases for User """

    def setUp(self):
        """ """
        self.new_user = User()

    def test_email(self):
        """ """
        self.assertIsInstance(self.new_user.email, str)

    def test_password(self):
        """ """
        self.assertIsInstance(self.new_user.password, str)

    def test_first_name(self):
        """ """
        self.assertIsInstance(self.new_user.first_name, str)

    def test_last_name(self):
        """ """
        self.assertIsInstance(self.new_user.last_name, str)


if __name__ == '__main__':
    unittest.main()
