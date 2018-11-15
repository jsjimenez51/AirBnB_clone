#!/usr/bin/python3
"""
This module contains the Unittest for the state model
"""
import unittest
import os
import pep8
from models.state import State

class test_StateModel(unittest.TestCase):
    """
    Defines Test Cases for State Class
    """
    def test_pep8(self):
        """ Validate Pep8 style check """
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/state.py'])
        self.assertEqual(f.total_errors, 0, "Pep8 Style Error(s) found")

    def test_docstringCheck(self):
        """ Checks for Class/Method Documentation """
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.__init__.__doc__)
        self.assertIsNotNone(State.__str__.__doc__)
        self.assertIsNotNone(State.to_dict.__doc__)
        self.assertIsNotNone(State.save.__doc__)

    @classmethod
    def setUpClass(cls):
        """ Setup class instance for tests """
        cls.us50 = State()
        cls.us50.name = "California"

    def test_init(self):
        """ Test Class initialization """
        self.assertTrue(isinstance(self.us50, State))

    def test_subClass(self):
        """ Verifies that it is a subclass """
        self.assertTrue(issubclass(self.us50.__class__, State), True)

    def test_inheritance(self):
        """ Verifies that attributes were inherited from BaseModel """
        self.assertTrue(hasattr(State(), "__init__"))
        self.assertTrue(hasattr(State(), "created_at"))
        self.assertTrue(hasattr(State(), "updated_at"))
        self.assertTrue(hasattr(State(), "id"))

    def test_hasAttributes(self):
        """ Checks State Class attributes """
        self.assertTrue(hasattr(State, "name"))

    def test_dicTributes(self):
        """ Checks State attributes in dictionary """
        self.assertTrue('id' in self.us50.__dict__)
        self.assertTrue('name' in self.us50.__dict__)
        self.assertTrue('created_at' in self.us50.__dict__)
        self.assertTrue('updated_at' in self.us50.__dict__)

    def test_PassedArgs(self):
        """ Checks for Keys/Args that can be passed """
        self.assertEqual(type(self.us50).__name__, "State")
        self.assertTrue(hasattr(self.us50, "name"))
        self.assertTrue(hasattr(self.us50, "__class__"))
        self.assertTrue(hasattr(self.us50, "id"))
        self.assertTrue(hasattr(self.us50, "created_at"))
        self.assertTrue(hasattr(self.us50, "updated_at"))

    def test_AttValues(self):
        """ Checks if correct values were set """
        self.assertTrue(self.us50.name, "California")

    def test_save(self):
        """ Tests if save works correctly """
        self.us50.save()
        self.assertNotEqual(self.us50.created_at, self.us50.updated_at)

    def test_toDict(self):
        """ Tests the to_dict method """
        state_dict = self.us50.to_dict()
        self.assertEqual(self.us50.__class__.__name__, 'State')
        self.assertIsInstance(state_dict['name'], str)

    def test_dictStr(self):
        """ Tests to see if the dictionary string is made correctly """
        sTest = self.us50.__str__()
        self.assertEqual(sTest, "[State] ({}) {}".format
                         (self.us50.id, self.us50.__dict__))

    @classmethod
    def teardown(cls):
        del cls.us50

    def tearDown(self):
        try:
                os.remove("file.json")
        except BaseException:
                pass

if __name__ == "__main__":
    unittest.main()
