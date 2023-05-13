#!/usr/bin/python3
"""
This is a class Review that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class holds the review attributes
    """
    place_id = ""
    user_id = ""
    text = ""
