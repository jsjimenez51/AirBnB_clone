#!/usr/bin/python3
"""
This module contains the BaseModel class to be used by all other instances
"""
import models
import uuid
from datetime import datetime


class BaseModel():
    """
    The BaseModel Class that defines attributes and methods for classes
    """
    def __init__(self, *args, **kwargs):
        """
        Instantiation of the BaseModel Class

        Attr:
            id (str): UUID generated when an instance is created
            created_at (datetime): assigned to an instance when created
            updated_at (datetime): updated when an instance is changed
        """
        if (kwargs):
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(self.created_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Method to Overload
        """
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__))

    def save(self):
        """
        Updates: 'updated_at' attribute with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns dictionary containing all keys/values of the instance
        """
        insta_dict = self.__dict__
        insta_dict['__class__'] = self.__class__.__name__
        insta_dict['created_at'] = self.created_at.isoformat()
        insta_dict['updated_at'] = self.updated_at.isoformat()
        return insta_dict
