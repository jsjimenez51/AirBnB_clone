#!/usr/bin/python3
"""
This module contains the Unittest for user_model
"""
import unittest
import os
import pep8
from models.user import User


class test_UserModel(unittest.TestCase):
    """
    Defines Test Cases for User Class
    """
    def test_pep8(self):
        """ Validate Pep8 style check """
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/user.py'])
        self.assertEqual(f.total_errors, 0, "Pep8 Style Error(s) found")

    def test_docstringCheck(self):
        """ Checks for Class/Method Documentation """
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)
        self.assertIsNotNone(User.__str__.__doc__)
        self.assertIsNotNone(User.to_dict.__doc__)
        self.assertIsNotNone(User.save.__doc__)

    @classmethod
    def setUpClass(cls):
        """ Setup class instance for tests """
        cls.tester = User()
        cls.tester.email = "User@test.com"
        cls.tester.password = "testuser"
        cls.tester.first_name = "Test"
        cls.tester.last_name = "User"

    def test_init(self):
        """ Test Class initialization """
        self.assertTrue(isinstance(self.tester, User))

    def test_subClass(self):
        """ Verifies that it is a subclass """
        self.assertTrue(issubclass(self.tester.__class__, User), True)

    def test_inheritance(self):
        """ Verifies that attributes were inherited from BaseModel """
        self.assertTrue(hasattr(User(), "__init__"))
        self.assertTrue(hasattr(User(), "created_at"))
        self.assertTrue(hasattr(User(), "updated_at"))
        self.assertTrue(hasattr(User(), "id"))

    def test_hasAttributes(self):
        """ Checks User Class attributes """
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))

    def test_dictTributes(self):
        """ Checks User attributes in dictionary """
        self.assertTrue('email' in self.tester.__dict__)
        self.assertTrue('first_name' in self.tester.__dict__)
        self.assertTrue('last_name' in self.tester.__dict__)
        self.assertTrue('password' in self.tester.__dict__)
        self.assertTrue('created_at' in self.tester.__dict__)
        self.assertTrue('updated_at' in self.tester.__dict__)

    def test_PassedArgs(self):
        """ Checks for Keys/Args that can be passed """
        self.assertEqual(type(self.tester).__name__, "User")
        self.assertFalse(hasattr(self.tester, "name"))
        self.assertTrue(hasattr(self.tester, "__class__"))
        self.assertTrue(hasattr(self.tester, "id"))
        self.assertTrue(hasattr(self.tester, "created_at"))
        self.assertTrue(hasattr(self.tester, "updated_at"))

    def test_AttValues(self):
        """ Checks if correct values were set """
        self.assertTrue(self.tester.email, "User@test.com")
        self.assertTrue(self.tester.password, "testuser")
        self.assertTrue(self.tester.first_name, "Test")
        self.assertTrue(self.tester.last_name, "User")

    def test_save(self):
        """ Tests if save works correctly """
        self.tester.save()
        self.assertNotEqual(self.tester.created_at, self.tester.updated_at)

    def test_toDict(self):
        """ Tests the to_dict method """
        user_dict = self.tester.to_dict()
        self.assertEqual(self.tester.__class__.__name__, 'User')
        self.assertIsInstance(user_dict['email'], str)
        self.assertIsInstance(user_dict['password'], str)
        self.assertIsInstance(user_dict['first_name'], str)
        self.assertIsInstance(user_dict['last_name'], str)

    def test_dictStr(self):
        """ Tests to see if the dictionary string is made correctly """
        uTest = self.tester.__str__()
        self.assertEqual(uTest, "[User] ({}) {}".format
                         (self.tester.id, self.tester.__dict__))

    @classmethod
    def teardown(cls):
        del cls.tester

    def tearDown(self):
        try:
            os.remove("file.json")
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
