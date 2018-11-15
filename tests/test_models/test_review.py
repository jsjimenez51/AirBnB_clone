#!/usr/bin/python3
"""
This module contains the Unittest for the Review Class
"""
import unittest
import os
import pep8
from models.review import Review


class test_Place(unittest.TestCase):
    """ Defines Test Cases for Review Class """
    def test_pep8(self):
        """ Validate Pep8 style check """
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/review.py'])
        self.assertEqual(f.total_errors, 0, "Pep8 Style Error(s) found")

    def test_docstringCheck(self):
        """ Checks for Class/Method Documentation """
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)
        self.assertIsNotNone(Review.__str__.__doc__)
        self.assertIsNotNone(Review.to_dict.__doc__)
        self.assertIsNotNone(Review.save.__doc__)

    @classmethod
    def setUpClass(cls):
        """ Sets up an review class before each test """
        cls.five_star = Review()
        cls.five_star.place_id = "Place.12345"
        cls.five_star.user_id = "User.12345"
        cls.five_star.text = "It changed my life."

    @classmethod
    def tearDown(cls):
        """ Deletes the dummy review class after each test """
        del cls.five_star

    def tearDown(self):
        """ Deletes the JSON file after each test """
        try:
            os.remove('file.json')
        except BaseException:
            pass

    def test_init(self):
        """ Test Class initialization """
        self.assertTrue(isinstance(self.five_star, Review))

    def test_subClass(self):
        """ Verifies that it is a subclass """
        self.assertTrue(issubclass(self.five_star.__class__, Review))

    def test_inheritance(self):
        """ Verifies that attributes were inherited from BaseModel """
        self.assertTrue(hasattr(Review(), "__init__"))
        self.assertTrue(hasattr(Review(), "created_at"))
        self.assertTrue(hasattr(Review(), "updated_at"))
        self.assertTrue(hasattr(Review(), "id"))

    def test_hasAttributes(self):
        """ Checks Review Class attributes """
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))

    def test_dicTributes(self):
        """ Checks Review attributes in dictionary """
        self.assertTrue('id' in self.five_star.__dict__)
        self.assertTrue('text' in self.five_star.__dict__)
        self.assertTrue('created_at' in self.five_star.__dict__)
        self.assertTrue('updated_at' in self.five_star.__dict__)

    def test_PassedArgs(self):
        """ Checks for Keys/Args that can be passed """
        self.assertEqual(type(self.five_star).__name__, "Review")
        self.assertTrue(hasattr(self.five_star, "__class__"))
        self.assertTrue(hasattr(self.five_star, "id"))
        self.assertTrue(hasattr(self.five_star, "created_at"))
        self.assertTrue(hasattr(self.five_star, "updated_at"))

    def test_AttValues(self):
        """ Checks if correct values were set """
        self.assertTrue(self.five_star.place_id, "Place.12345")
        self.assertTrue(self.five_star.user_id, "User.12345")
        self.assertTrue(self.five_star.text, "It changed my life.")

    def test_save(self):
        """ Tests if save works correctly """
        self.five_star.save()
        self.assertNotEqual(
            self.five_star.created_at, self.five_star.updated_at)

    def test_toDict(self):
        """ Tests the to_dict method """
        five_star_dict = self.five_star.to_dict()
        self.assertEqual(self.five_star.__class__.__name__, 'Review')
        self.assertIsInstance(five_star_dict['text'], str)
        self.assertIsInstance(five_star_dict['created_at'], str)
        self.assertIsInstance(five_star_dict['updated_at'], str)

    def test_dictStr(self):
        """ Tests to see if the dictionary string is made correctly """
        test = self.five_star.__str__()
        self.assertEqual(test, "[Review] ({}) {}".format(
            self.five_star.id, self.five_star.__dict__))

if __name__ == "__main__":
    unittest.main()
