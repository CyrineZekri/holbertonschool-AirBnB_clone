#!/usr/bin/python3
"""
module that defines the Base Model 
"""
import uuid
from datetime import datetime
class BaseModel:
    """ The base class"""
    def __init__(self,*args,**kwargs):
        """Instanciation Method"""
        for key, value in kwargs.items():
         print(f"{key}:{value}")       
        self.id=str(uuid.uuid4())
        self.created_at= datetime.now()
        self.updated_at=self.created_at
    def __str__(self):
        """Print method"""
        return f"[{BaseModel.__name__}] ({self.id}) <{self.__dict__}>"
    def save(self):
        """updates the time"""
        self.updated_at=datetime.now()
    def to_dict(self):
        """converts an instance to a dictionary"""
        obj_dict=self.__dict__
        obj_dict["__class__"]=self.__class__.__name__
        obj_dict["created_at"]=self.created_at.isoformat()
        obj_dict["updated_at"]=self.updated_at.isoformat()