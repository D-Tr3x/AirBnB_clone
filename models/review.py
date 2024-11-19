#!/usr/bin/python3
"""Defines class Review that inherits from BaseModel"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Represents the review for the hbnb"""

    place_id = ""
    user_id = ""
    text = ""
