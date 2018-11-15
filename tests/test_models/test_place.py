#!/usr/bin/python3
"""
This module contains the Unittest for the Place Class
"""
import unittest
import os
import pep8
from models.place import Place


class test_Place(unittest.TestCase):
    """ Defines Test Cases for Place Class """
    def test_pep8(self):
        """ Validate Pep8 style check """
        style = pep8.StyleGuide(quiet=True)
        f = style.check_files(['models/place.py'])
        self.assertEqual(f.total_errors, 0, "Pep8 Style Error(s) found")

    def test_docstringCheck(self):
        """ Checks for Class/Method Documentation """
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)
        self.assertIsNotNone(Place.__str__.__doc__)
        self.assertIsNotNone(Place.to_dict.__doc__)
        self.assertIsNotNone(Place.save.__doc__)

    @classmethod
    def setUpClass(cls):
        """ Sets up an amenity class before each test """
        cls.my_place = Place()
        cls.my_place.city_id = "City.12345"
        cls.my_place.user_id = "User.12345"
        cls.my_place.name = "Bob"
        cls.my_place.description = "A quaint lil place"
        cls.my_place.number_rooms = 3
        cls.my_place.number_bathrooms = 2
        cls.my_place.max_guest = 5
        cls.my_place.price_by_night = 100
        cls.my_place.latitude = 3.1
        cls.my_place.longitude = 3.1
        cls.my_place.amenity_ids = "Amenity.12345"

    @classmethod
    def tearDown(cls):
        """ Deletes the dummy place class after each test """
        del cls.my_place

    def tearDown(self):
        """ Deletes the JSON file after each test """
        try:
            os.remove('file.json')
        except BaseException:
            pass

    def test_init(self):
        """ Test Class initialization """
        self.assertTrue(isinstance(self.my_place, Place))

    def test_subClass(self):
        """ Verifies that it is a subclass """
        self.assertTrue(issubclass(self.my_place.__class__, Place))

    def test_inheritance(self):
        """ Verifies that attributes were inherited from BaseModel """
        self.assertTrue(hasattr(Place(), "__init__"))
        self.assertTrue(hasattr(Place(), "created_at"))
        self.assertTrue(hasattr(Place(), "updated_at"))
        self.assertTrue(hasattr(Place(), "id"))

    def test_hasAttributes(self):
        """ Checks Place Class attributes """
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))

    def test_dicTributes(self):
        """ Checks Amenity attributes in dictionary """
        self.assertTrue('id' in self.my_place.__dict__)
        self.assertTrue('name' in self.my_place.__dict__)
        self.assertTrue('created_at' in self.my_place.__dict__)
        self.assertTrue('updated_at' in self.my_place.__dict__)

    def test_PassedArgs(self):
        """ Checks for Keys/Args that can be passed """
        self.assertEqual(type(self.my_place).__name__, "Place")
        self.assertTrue(hasattr(self.my_place, "name"))
        self.assertTrue(hasattr(self.my_place, "__class__"))
        self.assertTrue(hasattr(self.my_place, "id"))
        self.assertTrue(hasattr(self.my_place, "created_at"))
        self.assertTrue(hasattr(self.my_place, "updated_at"))

    def test_AttValues(self):
        """ Checks if correct values were set """
        self.assertTrue(self.my_place.city_id, "City.12345")
        self.assertTrue(self.my_place.user_id, "User.12345")
        self.assertTrue(self.my_place.name, "Bob")
        self.assertTrue(self.my_place.description, "A quaint lil place")
        self.assertTrue(self.my_place.number_rooms, 3)
        self.assertTrue(self.my_place.number_bathrooms, 2)
        self.assertTrue(self.my_place.max_guest, 5)
        self.assertTrue(self.my_place.price_by_night, 100)
        self.assertTrue(self.my_place.latitude, 3.1)
        self.assertTrue(self.my_place.longitude, 3.1)
        self.assertTrue(self.my_place.amenity_ids, "Amenity.12345")

    def test_save(self):
        """ Tests if save works correctly """
        self.my_place.save()
        self.assertNotEqual(self.my_place.created_at, self.my_place.updated_at)

    def test_toDict(self):
        """ Tests the to_dict method """
        my_place_dict = self.my_place.to_dict()
        self.assertEqual(self.my_place.__class__.__name__, 'Place')
        self.assertIsInstance(my_place_dict['name'], str)
        self.assertIsInstance(my_place_dict['created_at'], str)
        self.assertIsInstance(my_place_dict['updated_at'], str)

    def test_dictStr(self):
        """ Tests to see if the dictionary string is made correctly """
        test = self.my_place.__str__()
        self.assertEqual(test, "[Place] ({}) {}".format(
            self.my_place.id, self.my_place.__dict__))

if __name__ == "__main__":
    unittest.main()
