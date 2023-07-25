#!/usr/bin/python3
"""
module that defines the Base Model
"""
import uuid
from datetime import datetime
from models import storage
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
            storage.new(self)

    def __str__(self):
        """Print method"""
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """updates the updated_at attribute"""
        self.updated_at = datetime.now()
        if storage:
            storage.save()
    def to_dict(self):
        """converts an instance to a dictionary"""
        obj_dict = self.__dict__.copy()
        for key, value in obj_dict.items():
            if isinstance(value, datetime):
                obj_dict[key] = value.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
