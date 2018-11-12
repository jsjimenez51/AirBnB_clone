#!/usr/bin/python3
"""
This module defines the Console Interpreter for the HBNB Clone
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand Class that defines Commands that can be executed
    """
    prompt = '(hbnb)'

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
        print("EOF command: EOF or (Ctrl-D) to exit the program\n")

    def emptyline(self):
        """
        Executes nothing if no args passed to Command Line
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
