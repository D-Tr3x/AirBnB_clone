#!/usr/bin/python3
"""Defines State class that inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state (place) for hbnb"""

    name = ""
