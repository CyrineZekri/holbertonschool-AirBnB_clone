#!/usr/bin/python3
"""
module that defines the Base Model
"""
import uuid
from datetime import datetime


class BaseModel:
    """ The base class"""

    def __init__(self, *args, **kwargs):
        """Instanciation Method"""
        if kwargs:
            for key, value in kwargs.items():
                # if user wants to enter created_at or updated_at attributes
                if key == 'created_at' or key == 'updated_at':
                    setattr(
                        self, key, datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Print method"""
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """updates the updated_at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """converts an instance to a dictionary"""
        inst_dict = self.__dict__.copy()
        # use a copy of self.__dict
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict