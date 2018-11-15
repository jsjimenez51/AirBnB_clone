#!/usr/bin/python3
"""
This module contains the Unittest for the Amenity Class
"""
import unittest
import os
import pep8
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """ Defines Test Cases for Amenity Class """
    def test_pep8(self):
        """ Validate Pep8 style check """
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/amenity.py'])
        self.assertEqual(f.total_errors, 0, "Pep8 Style Error(s) found")

    def test_docstringCheck(self):
        """ Checks for Class/Method Documentation """
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)
        self.assertIsNotNone(Amenity.__str__.__doc__)
        self.assertIsNotNone(Amenity.to_dict.__doc__)
        self.assertIsNotNone(Amenity.save.__doc__)

    @classmethod
    def setUpClass(cls):
        """ Sets up an amenity class before each test """
        cls.amen = Amenity()
        cls.amen.name = "Jesus"

    @classmethod
    def tearDown(cls):
        """ Deletes the dummy amenity class after each test """
        del cls.amen

    def tearDown(self):
        """ Deletes the JSON file after each test """
        try:
            os.remove('file.json')
        except BaseException:
            pass

    def test_init(self):
        """ Test Class initialization """
        self.assertTrue(isinstance(self.amen, Amenity))

    def test_subClass(self):
        """ Verifies that it is a subclass """
        self.assertTrue(issubclass(self.amen.__class__, Amenity))

    def test_inheritance(self):
        """ Verifies that attributes were inherited from BaseModel """
        self.assertTrue(hasattr(Amenity(), "__init__"))
        self.assertTrue(hasattr(Amenity(), "created_at"))
        self.assertTrue(hasattr(Amenity(), "updated_at"))
        self.assertTrue(hasattr(Amenity(), "id"))

    def test_hasAttributes(self):
        """ Checks Amenity Class attributes """
        self.assertTrue(hasattr(Amenity, "name"))

    def test_dicTributes(self):
        """ Checks Amenity attributes in dictionary """
        self.assertTrue('id' in self.amen.__dict__)
        self.assertTrue('name' in self.amen.__dict__)
        self.assertTrue('created_at' in self.amen.__dict__)
        self.assertTrue('updated_at' in self.amen.__dict__)

    def test_PassedArgs(self):
        """ Checks for Keys/Args that can be passed """
        self.assertEqual(type(self.amen).__name__, "Amenity")
        self.assertTrue(hasattr(self.amen, "name"))
        self.assertTrue(hasattr(self.amen, "__class__"))
        self.assertTrue(hasattr(self.amen, "id"))
        self.assertTrue(hasattr(self.amen, "created_at"))
        self.assertTrue(hasattr(self.amen, "updated_at"))

    def test_AttValues(self):
        """ Checks if correct values were set """
        self.assertTrue(self.amen.name, "Jesus")

    def test_save(self):
        """ Tests if save works correctly """
        self.amen.save()
        self.assertNotEqual(self.amen.created_at, self.amen.updated_at)

    def test_toDict(self):
        """ Tests the to_dict method """
        amen_dict = self.amen.to_dict()
        self.assertEqual(self.amen.__class__.__name__, 'Amenity')
        self.assertIsInstance(amen_dict['name'], str)
        self.assertIsInstance(amen_dict['created_at'], str)
        self.assertIsInstance(amen_dict['updated_at'], str)

    def test_dictStr(self):
        """ Tests to see if the dictionary string is made correctly """
        test = self.amen.__str__()
        self.assertEqual(test, "[Amenity] ({}) {}".format(
            self.amen.id, self.amen.__dict__))

if __name__ == "__main__":
    unittest.main()
