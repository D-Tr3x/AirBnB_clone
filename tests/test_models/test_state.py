#!/usr/bin/python3
""" Unit tests for State """

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Test cases for State """

    def setUp(self):
        """ Sets up the test cases """
        self.my_state = State()

    def test_name(self):
        """ Tests if state has correct attributes """
        self.assertIsInstance(self.my_state.name, str)
        self.assertEqual(self.my_state.name, "")


if __name__ == '__main__':
    unittest.main()
