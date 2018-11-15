#!/usr/bin/python3
"""
This module defines the Place Class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    The Place class inherits from the BaseModel class

    Public Attributes Initialized:
    (str) city_id : empty : City.id
    (str) user_id : empty : User.id
    (str) name : empty
    (str) description : empty
    (int) number_rooms : 0
    (int) number_bathrooms : 0
    (int) max_guest : 0
    (int) price_by_night : 0
    (float) latitude : 0.0
    (float) longitude: 0.0
    (str) amenity_ids : list of strs : Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
