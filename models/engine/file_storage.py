    #!/usr/bin/python3
""" module  that serializes and deserializes instances """
import json
class FileStorage:
    __file_path="file.json"
    __objects={}
    def all(self):
        """ returns all objects"""
        return self.__objects
    def new(self,obj):
        """adds a new object to the __objects() dict"""
        key=f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key]=obj
    def save(self):
        """serializes the objects"""
        new_dict={}
        for key, obj in self.__objects.items():
            new_dict[key]=obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects,f)
    def reload(self):
        """deserializes objects"""
        try:
            #do nthg if the file doesnt exist
            with open(FileStorage.__file_path,"r") as f: 
                FileStorage.__objects=json.load(f)
        except FileNotFoundError:
            pass 