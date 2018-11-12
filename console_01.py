#!/usr/bin/python3
"""
This module defines the Console Interpreter for the HBNB Clone
"""
import cmd
import json
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand Class that defines Commands that can be executed
    """
    prompt = '(hbnb)'
    classnames = ["BaseModel"]

    def create(self, arg):
        """
        Creates a new instance of specified class
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg is not in self.classnames:
            print("** class doesn't exist **")
            return
        else:
            new_insta = eval("{}()".format(arg))
            new_insta.save()
            print(new_insta.id)

    def help_create(self):
        """
        Documentation for create usage
        """
        print("create <classname> : to create a new class instance")

    def do_show(self,   ):
        """
        Prints the string representation of an instance
        """
        

    def do_quit(self, arg):
        """
        Exit the program ( quit )
        """
        raise SystemExit

    def help_quit(self):
        """
        Documentation for ( quit ) usage
        """
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """
        Exit the program type EOF or ( Ctrl-D )
        """
        print()
        raise SystemExit

    def help_EOF(self):
        """
        Documentation for ( Ctrl-D ) usage
        """
        print("EOF command or (Ctrl-D) to exit the program\n")

    def emptyline(self):
        """
        Executes nothing if no args passed to Command Line
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
