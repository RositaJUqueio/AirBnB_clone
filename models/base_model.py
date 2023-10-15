#!/usr/bin/python3
# Authors: Rosita J Uqueio & Ridwan Dada

import uuid
import json
from datetime import datetime

"""Defines a BaseModel class"""


class BaseModel:
    """
    BaseModel that defines all common attributes/methods for other classes:
    Atributes:
            id: Is the BaseMode id.
            created_at: The date & time of creation.
            updated_at: The time of Creation
    """
    def __init__(self, *args, **kwargs):
        """ checking if kwargs is empty or not """
        if kwargs:
            """ if it not empty iterate the key-value" pairs in kwargs"""
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    """
                    converting the created_at and updated_at strings to
                    datetime objects
                    """
                    setattr(self, key,
                            datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    """skipping '__class__' from kwargs"""
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        from models import storage
        """Updates the updated_at attribute with current datetime"""
        self.updated_at = datetime.now()
        storage.save()
        storage.new(self)

    def to_dict(self):
        """
        Creates a dictionary containing
        all keys/values of __dict__ of the instance
        """
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj
