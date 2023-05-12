#!/usr/bin/python3
"""defining a class city"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """class city
    public class attr: state_id
                       name
    """
    state_id = ""
    name = ""
