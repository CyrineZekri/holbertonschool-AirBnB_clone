#!/usr/bin/python3

"""
FileStorage Module
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.city import City
from models.amenity import Amenity


class FileStorage():
    """FileStorage  class that inherits from BaseModel class"""

    __file_path = "file.json"
    __objects = {}

    # all method
    def all(self):
        """method that returns the dictionary __objects"""
        return self.__objects

    # new method
    def new(self, obj):
        """method that sets in __objects the obj with key<obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    # save method
    def save(self):
        """method that serializes __objects to JSON file (path: __file_path)"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    # reload method
    def reload(self):
        """method that deserializes the JSON file"""
        if (os.path.isfile(self.__file_path)) is False:
            return
        with open(self.__file_path, 'r') as file:
            obj = json.loads(file.read())
        for key, value in obj.items():
            class_name, id = key.split('.')
            self.__objects[key] = eval(class_name)(**value)