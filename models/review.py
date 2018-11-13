#!/usr/bin/python3
"""
Module for Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    The Review class inherits the following attributes from BaseModel:

    (str) place_id: empty
    (str) user_id: empty
    (str) text: empty
    """

    place_id = ""
    user_id = ""
    text = ""
