#!/usr/bin/python3
# Authors: Rosita J Uqueio & Joseph Dada

import uuid
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
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute with current datetime"""
        self.updated_at = datetime.now()

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
    