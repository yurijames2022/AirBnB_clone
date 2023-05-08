#!/usr/bin/env python3
"""defining a base model superclass"""


import uuid
import datetime


class BaseModel:
    """Class BaseModel"""
    def __init__(self, id, created_at, updated_at):
        """object instantiation
        attributes: id
                created-at
                updated_at"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """returns string representation of class name, id, and dictionary
        ready to print"""
        return '[' + str(self.__class__.__name__) + '] ('
        + str(self.id) + ') ' + str(self.__dict__)
