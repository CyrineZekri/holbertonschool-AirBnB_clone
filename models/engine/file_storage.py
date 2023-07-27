 #!/usr/bin/python3
""" module  that serializes and deserializes instances """
import json
class FileStorage:
    __file_path="file.json"
    __objects={}
    def all(self):
        """ returns all objects """
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
            json.dump(new_dict,f)
    def reload(self):
        """deserializes objects"""
        try:
            #do nthg if the file doesnt exist
            with open(FileStorage.__file_path,"r") as f: 
                object=json.load(f.read())
                for key, value in object.items():
                    class_name, id=key.split('.')
                    self.__objects[key]=eval(class_name)(**value)
        except FileNotFoundError:
            pass 