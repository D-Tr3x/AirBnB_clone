#!/usr/bin/python3
"""Defines a class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents an AirBnB user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
