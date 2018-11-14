#!/usr/bin/python3
"""
This module contains the Unittest for base_model
"""
import unittest
import os
import pep8
from models.base_model import BaseModel


class test_BaseModel(unittest.TestCase):
    """
    Defines Test Cases for BaseModel Class
    """
    def test_pep8(self):
        """ Validate Pep8 style check """
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/base_model.py'])
        self.assertEqual(f.total_errors, 0, "Pep8 Style Error(s) found")

    def test_docstringCheck(self):
        """ Checks for Class/Method Documentation """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)

    @classmethod
    def setUpClass(cls):
        """ Setup class instance for tests """
        cls.bModel = BaseModel()
        cls.bModel.name = "ITestBaseModel"

    def test_init(self):
        """ Test Class initialization """
        self.assertTrue(isinstance(self.bModel, BaseModel))

    def test_hasAttributes(self):
        """ Checks BaseModel attributes """
        self.assertTrue(hasattr(self.bModel, "__init__"))
        self.assertTrue(hasattr(self.bModel, "id"))
        self.assertTrue(hasattr(self.bModel, "to_dict"))
        self.assertTrue(hasattr(self.bModel, "save"))
        self.assertTrue("created_at" in self.bModel.__dict__)
        self.assertTrue("updated_at" in self.bModel.__dict__)

    def test_PassedArgs(self):
        """ Checks for Keys/Args that can be passed """
        self.assertEqual(type(self.bModel).__name__, "BaseModel")
        self.assertTrue(hasattr(self.bModel, "name"))
        self.assertTrue(hasattr(self.bModel, "__class__"))
        self.assertTrue(hasattr(self.bModel, "id"))
        self.assertTrue(hasattr(self.bModel, "created_at"))
        self.assertTrue(hasattr(self.bModel, "updated_at"))

    def test_AttType(self):
        """ Test the attribute type """
        bModel_dict = self.bModel.to_dict()
        self.assertEqual(self.bModel.__class__.__name__, "BaseModel")
        self.assertIsInstance(bModel_dict['created_at'], str)
        self.assertIsInstance(bModel_dict['updated_at'], str)

    def test_save(self):
        """ Tests if save works correctly """
        self.bModel.save()
        self.assertNotEqual(self.bModel.created_at, self.bModel.updated_at)

    def test_dictStr(self):
        """ Tests to see if the dictionary string is made correctly """
        pModel = self.bModel.__str__()
        self.assertEqual(pModel, "[BaseModel] ({}) {}".format
                         (self.bModel.id, self.bModel.__dict__))

    def test_toDict(self):
        """ Tests the to_dict method """
        mod_dict = self.bModel.__dict__
        self.assertEqual(type(self.bModel).__name__, "BaseModel")
        self.assertTrue(hasattr(self.bModel, "__class__"))
        self.assertTrue(type(mod_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(mod_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(mod_dict['id']), 'str')

    @classmethod
    def teardown(cls):
        """ Tearsdown the created class """
        del cls.bModel

    def tearDown(self):
        """ Removes JSON file and Resets post test """
        try:
            os.remove("file.json")
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
