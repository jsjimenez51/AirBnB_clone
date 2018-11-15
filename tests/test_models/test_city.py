#!/usr/bin/python3
"""
This module contains the Unittest for the state model
"""
import unittest
import os
import pep8
from models.city import City


class test_CityModel(unittest.TestCase):
    """
    Defines Test Cases for City Class
    """
    def test_pep8(self):
        """ Validate Pep8 style check """
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/city.py'])
        self.assertEqual(f.total_errors, 0, "Pep8 Style Error(s) found")

    def test_docstringCheck(self):
        """ Checks for Class/Method Documentation """
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)
        self.assertIsNotNone(City.__str__.__doc__)
        self.assertIsNotNone(City.to_dict.__doc__)
        self.assertIsNotNone(City.save.__doc__)

    @classmethod
    def setUpClass(cls):
        """ Setup class instance for tests """
        cls.cClass = City()
        cls.cClass.name = "San Francisco"
        cls.cClass.state_id = "State"

    def test_init(self):
        """ Test Class initialization """
        self.assertTrue(isinstance(self.cClass, City))

    def test_subClass(self):
        """ Verifies that it is a subclass """
        self.assertTrue(issubclass(self.cClass.__class__, City), True)

    def test_inheritance(self):
        """ Verifies that attributes were inherited from BaseModel """
        self.assertTrue(hasattr(City(), "__init__"))
        self.assertTrue(hasattr(City(), "created_at"))
        self.assertTrue(hasattr(City(), "updated_at"))
        self.assertTrue(hasattr(City(), "id"))

    def test_hasAttributes(self):
        """ Checks State Class attributes """
        self.assertTrue(hasattr(City, "name"))
        self.assertTrue(hasattr(City, "state_id"))

    def test_dicTributes(self):
        """ Checks State attributes in dictionary """
        self.assertTrue('id' in self.cClass.__dict__)
        self.assertTrue('state_id' in self.cClass.__dict__)
        self.assertTrue('name' in self.cClass.__dict__)
        self.assertTrue('created_at' in self.cClass.__dict__)
        self.assertTrue('updated_at' in self.cClass.__dict__)

    def test_PassedArgs(self):
        """ Checks for Keys/Args that can be passed """
        self.assertEqual(type(self.cClass).__name__, "City")
        self.assertTrue(hasattr(self.cClass, "name"))
        self.assertTrue(hasattr(self.cClass, "__class__"))
        self.assertTrue(hasattr(self.cClass, "id"))
        self.assertTrue(hasattr(self.cClass, "state_id"))
        self.assertTrue(hasattr(self.cClass, "created_at"))
        self.assertTrue(hasattr(self.cClass, "updated_at"))

    def test_AttValues(self):
        """ Checks if correct values were set """
        self.assertTrue(self.cClass.name, "San Francisco")
        self.assertTrue(self.cClass.state_id, "State")

    def test_save(self):
        """ Tests if save works correctly """
        self.cClass.save()
        self.assertNotEqual(self.cClass.created_at, self.cClass.updated_at)

    def test_toDict(self):
        """ Tests the to_dict method """
        city_dict = self.cClass.to_dict()
        self.assertEqual(self.cClass.__class__.__name__, 'City')
        self.assertIsInstance(city_dict['name'], str)
        self.assertIsInstance(city_dict['state_id'], str)
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_dictStr(self):
        """ Tests to see if the dictionary string is made correctly """
        cTest = self.cClass.__str__()
        self.assertEqual(cTest, "[City] ({}) {}".format
                         (self.cClass.id, self.cClass.__dict__))

    @classmethod
    def teardown(cls):
        del cls.cClass

    def tearDown(self):
        try:
                os.remove("file.json")
        except BaseException:
                pass

if __name__ == "__main__":
    unittest.main()
