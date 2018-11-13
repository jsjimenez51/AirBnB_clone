#!/usr/bin/python3
"""
This module defines the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class inherits the following attributes from the BaseModel class:

    Public Attributes Initialized:
    (str) email : empty
    (str) password: empty
    (str) first_name: empty
    (str) las_name: empty
    """
    email = ""
    passowrd = ""
    first_name = ""
    last_name = ""
