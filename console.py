#!/usr/bin/python3
"""
This module defines the Console Interpreter for the HBNB Clone
"""
import shlex
import cmd
import json
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand Class that defines Commands that can be executed
    """
    prompt = '(hbnb) '
    classnames = ["BaseModel"]

    def do_create(self, arg):
        """
        Creates a new instance of specified class
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.classnames:
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
        print("create <classname> : to create a new class instance\n")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        """
        arg = shlex.split(line)
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.classnames:
            print("** class doesn't exist **")
            return
        elif len(arg) < 2:
            print("** instance id missing **")
            return
        instance_obj = storage.all()
        key_check = "{}.{}".format(arg[0], arg[1])
        if key_check not in instance_obj.keys():
            print("** no instance found **")
            return
        print(instance_obj[key_check])

    def help_show(self):
        """
        Documentation for ( show ) usage
        """
        print("show <classname> <id> : print string\
              representation of instance\n")

    def do_destroy(self, line):
        """
        Deletes an instance and saves to JSON file
        """
        arg = shlex.split(line)
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.classnames:
            print("** class doesn't exist **")
            return
        elif len(arg) < 2:
            print("** instance id missing **")
            return
        else:
            instance_obj = storage.all()
            key_check = "{}.{}".format(arg[0], arg[1])
            if key_check not in instance_obj.keys():
                print("** no instance found **")
                return
            else:
                instance_obj.pop(key_check)
                storage.save()
                return

    def help_destroy(self):
        """
        Documentation for ( destroy ) usage
        """
        print("destroy <classname> <id> : deletes an instance\n")

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the
        class name
        """
        arg = shlex.split(line)
        my_list = []
        if len(arg) == 0:
            for i in storage.all():
                my_list.append(str(storage.all()[i]))
        else:
            if arg[0] not in self.classnames:
                print("** class doesn't exist **")
            else:
                for i in storage.all():
                    if i.startswith(arg[0]):
                        my_list.append(str(storage.all()[i]))
        if my_list != []:
        	print(my_list)

    def help_all(self):
        """
        Documentation for ( all ) usage
        """
        print("Prints all string representations of all instances \
              based or not on class name\n")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save change into the JSON file).
        """
        arg = shlex.split(line)
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in self.classnames:
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        else:
            instance_obj = storage.all()
            key_check = "{}.{}".format(arg[0], arg[1])
            if key_check not in instance_obj.keys():
                print("** no instance found **")
                return
        if len(arg) == 2:
            print("** attribute name missing **")
            return
        if len(arg) == 3:
            print("** value missing **")
            return
        value = instance_obj[key_check]
        try:
            attr = getattr(value, arg[2])
            setattr(value, arg[2], type(attr)(arg[3]))
        except:
            setattr(value, arg[2], arg[3])
        storage.save()

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
