#!/usr/bin/python3
"""
Unittest for file_storage.py
"""
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestFileStorage(unittest.TestCase):
    """
    The TestFileStorage runs unittesting for the
    file_storage class
    """

    def test_attributes(self):
        """
        Tests the attributes of the FileStorage class
        """
        tester = FileStorage()
        self.assertEqual(
            tester._FileStorage__file_path, 'file.json')
        self.assertEqual(
            tester._FileStorage__object, {})

    def test_all(self):
        """
        Tests the all method of the FileStorage class
        """
        tester = FileStorage()
        self.assertEqual(tester.all(), {})
        
    def test_new(self):
        """
        Tests the new method of the FileStorage class
        """
        tester = FileStorage()
        obj = BaseModel()
        key = obj.__class__.__name__ + '.' + obj.id
        tester.new(obj)

       
       
       

if __name__ == '__main__':
    unittest.main()
