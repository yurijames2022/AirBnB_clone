#!/usr/bin/env python3
"""entry point of the command interpreter"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Interpreter class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        
        """
        return True

    def do_EOF(self, arg):
        """Method to check EOF"""
        return True

    def emptyline(self):
        """Method accomodates an empty line
        Enter does not execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
