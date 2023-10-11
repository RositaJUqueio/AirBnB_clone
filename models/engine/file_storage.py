#!/usr/bin/python3
"""File storage module"""

import json
import os


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
        """
        Serialization of objects to json file.
        the path: __file_path
        """
        data = {}
        for key, val in FileStorage.__objects.items():
            data[key] = val.to_dict()
            
        """Writting the serialization data to json file"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """
        Deserialize the JSON file into __objects if the file exists;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised.
        """
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as f:
                    data = json.load(f)
                    FileStorage.__objects = data
            except FileNotFoundError:
                pass
