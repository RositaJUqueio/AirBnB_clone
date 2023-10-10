#!/usr/bin/python3
""" file storage module """

import json
import os

""" a class filestorage """
class FileStorage:
    """
      setting it to a private class attribute
      the path to json file and 
      dictionary to store all objects
    """
    __file_path = "file.json" 
    __object = {}


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
    for key, val in FileStorage.__objects.item():
        data[key] = val.to_dict()

    """Writting the serialization data to json file"""
    with open(FileStorage.__file_path, 'w') as f:
        json.dump(data, f)

def reload(self):
    """
    Deserializing the json file to __objects if the json file
    (__file_path) exits; otherwise do nothing
     If the file doesn’t exist, no exception should be raised
    """
    if os.path.exists(FileStorage.__file_path):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                FileStorage.__objects = data
        except FileNotFoundError:
            pass