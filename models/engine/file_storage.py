#!/usr/bin/python3
""" file storage module """

import json
import os
from models.base_model import BaseModel
from models.user import User
import sys

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
    a public instance method that returns the dictionary object
    """
    return FileStorage.__objects


def new(self, obj):
    """a public instances that set object with key"""
    key = "{}.{}".format(obj.__class__name__, obj.id)
    FileStorage.__objests[key] = obj


def save(self):
    """Serialization of objects to json file. the path: __file_path"""
    data = {}
    for key in FileStorage.__objects:
        data[key] = FileStorage.__objects[key].to_dict()

    """Writting the serialization data to json file"""
    with open(FileStorage.__file_path, 'w') as f:
        json.dump(data, f)
        

def reload(self):
    """
    Deserializing the json file to __objects if the json file
    (__file_path) exits; otherwise do nothing
     If the file doesnt exist, no exception should be raised
    """
    if os.path.isfile(self.__file_path):
        with open(self.__file_path, "r") as f:
            my_data = json.load(f)
                for key, value in my_data.items():
                    name = sys.modules[__name__]
                    my_class = getattr(name, value['__class__'])
                    self.__objects[key] = my_class(**value)