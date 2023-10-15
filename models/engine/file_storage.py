#!/usr/bin/python3
"""The File storage module"""

import json
import os
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

""" a class filestorage """


class FileStorage:
    """
      setting it to a private class attribute
      the path to json file and
      dictionary to store all objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        A public instance method that returns the dictionary object
        """
        return FileStorage.__objects

    def new(self, obj):
        """A public instance method that sets an object with a key"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        from models import storage
        """Serialization of objects to json file. the path: __file_path"""
        data = {}
        for key in FileStorage.__objects:
            data[key] = FileStorage.__objects[key].to_dict()

        """Writting the serialization data to json file"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """Deserialization of the json file"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                my_data = json.load(f)
                for key, value in my_data.items():
                    class_name = key.split('.')[0]
                    """Returning the classes """
                    if class_name == 'Place':
                        my_class = Place
                    elif class_name == 'state':
                        my_class = State
                    elif class_name == 'City':
                        my_class = City
                    elif class_name == 'Amenity':
                        my_class = Amenity
                    elif class_name == 'Review':
                        my_class = Review
                    else:
                        my_class = BaseModel
                    self.__objects[key] = my_class(**value)
