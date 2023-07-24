#!/usr/bin/python3
""" module  that serializes and deserializes instances """
import json
class FileStorage:
    __file_path=""
    __objects={}
    def all(self):
        """ returns all objects"""
        return self.__objects
    def new(self,obj):
        """adds a new object to the __objects() dict"""
        key=f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key]=obj
    def save(self):
        """serializes the objects"""
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(FileStorage.__objects, json_file)
    def reload(self):
        """deserializes objects"""
        with open(FileStorage.__file_path,"r") as json_file: 
            FileStorage.__objects=json.load(json_file)    