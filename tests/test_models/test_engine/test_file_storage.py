#!/usr/bin/python3
"""
Unittest for file_storage.py
"""
import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


def setUpModule():
    """
    Removes preexisting file.json
    """
    try:
        os.remove('file.json')
    except:
        pass


def tearDownModule():
    """
    Removes preexisting file.json
    """
    try:
        os.remove('file.json')
    except:
        pass


class TestFileStorage(unittest.TestCase):
    """
    The TestFileStorage runs unittesting for the
    file_storage class
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup class instance for tests
        """
        cls.fs = FileStorage()

    @classmethod
    def tearDown(cls):
        """
        Tears down created classes
        """
        del cls.fs

    def tearDown(self):
        """
        Removes JSON file and resets post test
        """
        try:
            os.remove("file.json")
        except:
            pass

    def test_attributes(self):
        """
        Tests the attributes of the FileStorage class
        """
        bm = BaseModel()
        key = bm.__class__.__name__ + '.' + bm.id
        self.assertEqual(
            self.fs._FileStorage__file_path, 'file.json')
        self.assertIn(key, self.fs._FileStorage__objects.keys())

    def test_all(self):
        """
        Tests the all method of the FileStorage class
        """
        self.assertEqual(self.fs._FileStorage__objects, {})
        bm = BaseModel()
        self.fs.new(bm)
        key = bm.__class__.__name__ + '.' + bm.id
        self.assertIn(key, self.fs._FileStorage__objects.keys())

    def test_new(self):
        """
        Tests the new method of the FileStorage class
        """
        bm = BaseModel()
        key = bm.__class__.__name__ + '.' + bm.id
        self.fs.new(bm)
        self.assertIn(key, self.fs._FileStorage__objects.keys())

    def test_save(self):
        """
        Tests the save method of the FileStorage class
        """
        bm = BaseModel()
        self.fs.new(bm)
        self.fs.save()
        key = bm.__class__.__name__ + '.' + bm.id
        with open('file.json', mode='r') as json_file:
            new_dict = json.load(json_file)
        self.assertIn(key, new_dict.keys())

    def test_reload(self):
        """
        Tests the reload method of the FileStorage class
        """
        bm = BaseModel()
        self.fs.new(bm)
        self.fs.save()
        self.fs.reload()
        key = bm.__class__.__name__ + '.' + bm.id
        with open('file.json', mode='r') as json_file:
            new_dict = json.load(json_file)
        self.assertIn(key, new_dict.keys())
        new_bm = BaseModel()
        self.fs.save()
        self.fs.reload()
        key2 = new_bm.__class__.__name__ + '.' + new_bm.id
        with open('file.json', mode='r') as json_file:
            new_dict = json.load(json_file)
        self.assertIn(key, new_dict.keys())
        self.assertIn(key2, new_dict.keys())

if __name__ == '__main__':
    unittest.main()
