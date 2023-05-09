#!/usr/bin/env python3
"""defining a base model superclass"""


import uuid
from datetime import datetime


class BaseModel:
    """Class BaseModel"""
    def __init__(self, *args, **kwargs):
        """object instantiation
        attributes: id
                created-at
                updated_at"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, format)
                if key != '__class__':
                    self.__dict__[key] = value

    def __str__(self):
        """returns string representation of class name, id, and dictionary
        ready to print"""
        return '[' + str(self.__class__.__name__) + '] ('\
            + str(self.id) + ') ' + str(self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at with the
        current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance"""
        self.__dict__["id"] = self.id
        self.__dict__["created_at"] = (self.created_at).isoformat()
        self.__dict__["updated_at"] = (self.updated_at).isoformat()
        self.__dict__["__class__"] = self.__class__.__name__

        return self.__dict__
