#!/usr/bin/python3
"""entry point of the command interpreter"""

import cmd
import sys
import models
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Interpreter class"""
    prompt = '(hbnb) '

    classes = ["BaseModel", "User", "Place", "State",
               "City", "Amenity", "Review"]

    cmnds = ['create', 'show', 'destroy', 'all', 'update',
             'count']

    def precmd(self, arg):
        """command parses the command input
        before execution by any other command"""
        if '.' in arg and '(' in arg and ')' in arg:
            clas = arg.split('.')
            cd = clas[1].split('(')
            args = cd[1].split(')')
            if clas[0] in HBNBCommand.classes and cd[0] in HBNBCommand.cmnds:
                arg = cd[0] + ' ' + clas[0] + ' ' + args[0]
        return arg

    def do_create(self, arg):
        """Command creates new instance of BaseModel
        saves it and prints its unique id"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.strip()
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        new_inst = eval(class_name)()
        new_inst.save()
        print(new_inst.id)

    def do_show(self, arg):
        """command prints string representation
        instance based on class name and id"""
        if not arg:
            print("** class name missing **")
            return

        arguments = arg.split()
        class_name = arguments[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(arguments) < 2:
            print("** instance id missing **")
            return
        inst_id = arguments[1]
        key = "{}.{}".format(class_name, inst_id)
        py_objs = models.storage.all()

        if key in py_objs:
            instance = py_objs[key]
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """command deletes instance based on class name and id
        also saves change to JSON file"""
        if not arg:
            print("** class name missing **")
            return
        arguments = arg.split()
        class_name = arguments[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(arguments) < 2:
            print("** instance id missing **")
            return
        inst_id = arguments[1]
        key = "{}.{}".format(class_name, inst_id)
        py_objects = models.storage.all()

        if key in py_objects:
            del py_objects[key]
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ prints all string representation of all instances
        based on or not on the class name """
        if arg and arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        all_objects = storage.all()

        obj_list = []
        for object in all_objects.values():
            obj_list.append(str(object))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all().keys():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        value = args[3]

        instance = storage.all()[key]
        setattr(instance, attribute_name, value)
        instance.save()

    def do_count(self, arg):
        """command method retrieves the number of
        instances of a class"""
        count = 0
        objs = storage.all()
        for key, val in objs.items():
            ky = key.split('.')
            if ky[0] == arg:
                count += 1
        print(count)

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
