#!/usr/bin/python3
"""module defines a class"""


from models.base_model import BaseModel


class User(BaseModel):
    """class user that inherits from BaseModel
    public class attributes:email
                            password
                            first_name
                            last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation of User objects"""
        super().__init__(*args, **kwargs)
