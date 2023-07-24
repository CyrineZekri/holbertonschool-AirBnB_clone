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
            """If user adds other attributes"""
            for key, value in kwargs.items():
                """ In Case the user wants to set updated_at or created_at"""
                if key == 'created_at' or key == 'updated_at':
                    setattr(
                        self, key, datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    """To ensure user only passes valid arguments"""
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
        obj_dict = self.__dict__.copy()
        """ To isolate from the data stored in self.__dict__"""
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
