#!/usr/bin/python3
"""
Module for City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City inheirits the following attributes from BaseModel:

    (str) state_id: empty
    (str) name: empty
    """
    state_id = ""
    name = ""
