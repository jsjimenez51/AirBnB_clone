#!/usr/bin/python3
"""
This module contains the FileStorage class that serializes/deserializes
an instance to/from a JSON file
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """
    The FileStorage Class that defines attributes and methods for
    storing objects in JSON files

    Attr:
        file_path (str): the path to the JSON file
        objects (dict): used to store all objects by <class name>
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets new object in dictionary with the formatted key
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        new_save = {}
        with open(self.__file_path, mode='w+', encoding='utf-8') as new_file:
            for key, value in self.__objects.items():
                new_save[key] = value.to_dict()
            json.dump(new_save, new_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as a_file:
                file_dict = json.load(a_file)
                for key, value in file_dict.items():
                    new_obj = eval(value['__class__'])(**value)
                    self.__objects[key] = new_obj

        except FileNotFoundError:
            pass
