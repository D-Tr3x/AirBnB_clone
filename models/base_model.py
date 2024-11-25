#!/usr/bin/python3
""" Module defines class for all models """

import uuid
from datetime import datetime


class BaseModel:
    """ Base class for all our models """

    def __init__(self, *args, **kwargs):
        """ Initializes new instance attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            from models import storage
            storage.new(self)

    def save(self):
        """ Updates `updated_at` with the current datetime """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/value of __dict__ """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """ Returns a string representation of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
