#!/usr/bin/python3
"""
Module to test console
"""
import unittest
from console import HBNBCommand


class test_Console(unittest.TestCase):
    """ Unittest for console """
    def test_console(self):
        """ Tests if console has prompt """
        my_console = HBNBCommand()
        self.assertEqual(my_console.prompt, '(hbnb) ')

if __name__ == 'main':
    unittest.main()
