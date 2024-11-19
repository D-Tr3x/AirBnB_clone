#!/usr/bin/python3
"""Defines City class that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city for the hbnb"""

    state_id = ""
    name = ""
