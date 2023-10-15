#!/usr/bin/env python3
"""The Console module"""
import cmd
import json
import models
from models import storage
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBComand(cmd.Cmd):
    """HBnBComnd class Defines the comand-line interpreter for HBnB.

    Attributes:
        prompt (str): The comnd prompt.
        __models (set): defines a set of valid model class names.
    """

    prompt = "(hbnb) "

    __models = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def do_quit(self, arg):
        """Quit comnd to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program."""
        return True

    def emptyline(self):
        """Does nothing after receiving an empty line."""
        pass

    def do_create(self, arg):
        """
        Instantiates a new object of BaseModel & stores it in the JSON file.
        then prints the ID of the new instance
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBComand.__models:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Displays string representation of class instance
        based on the class name and id.
        Then prints the string representation of the specified instance
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBComand.__models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objcts_dict = models.storage.all()
            key_instance = "{}.{}".format(args[0], args[1])
            instance = objcts_dict.get(key_instance)
            if instance:
                print(instance)
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Displays string representations of all instances
        based on the class name.
        """
        objcts_dict = models.storage.all()
        instance_list = []

        if not arg:
            for key in objcts_dict:
                instance_list.append(str(objcts_dict[key]))
        else:
            class_name = arg.strip()
            if class_name in self.__models:
                for key, value in objcts_dict.items():
                    if value.__class__.__name__ == class_name:
                        instance_list.append(str(value))
            else:
                print("** class doesn't exist **")
                return

        print(instance_list)

    def do_destroy(self, arg):
        """Deletes a class instance of a given id."""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBComand.__models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objcts_dict = models.storage.all()
            key_instance = "{}.{}".format(args[0], args[1])
            instance = objcts_dict.get(key_instance)
            if instance:
                del objcts_dict[key_instance]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.__models:
            print("** class doesn't exist **")
            return

        if len(args) <= 1:
            print("** instance id missing **")
            return

        instance_id = args[1]
        obj_key = "{}.{}".format(class_name, instance_id)
        obj_dict = storage.all()

        if obj_key not in obj_dict:
            print("** no instance found **")
            return

        instance = obj_dict[obj_key]

        if len(args) <= 2:
            print("** attribute name missing **")
            return

        atr_name = args[2]
        if len(args) <= 3:
            print("** value missing **")
            return

        atr_value = args[3]
        setattr(instance, atr_name, atr_value)
        instance.save()

    def do_count(self, arg):
        """
        Counts the number of instances of a specified class.
        Usage:
           counts instances of a specific class: count <class_name>
           counts instances of the class from an instance: <class_name>.count()
        """

        args = arg.split()
        """Checking if a class name is provided"""
        if len(args) == 0:
            print("Missing class name")
            return

        class_name = args[0]
        if class_name not in self.__models:
            print("Class doesn't exist")
            return

        count = 0
        objcts_dict = models.storage.all()

        for key, value in objcts_dict.items():
            if value.__class__.__name__ == class_name:
                count += 1
        print(count)

    def precmd(self, user_input):
        """
        Preprocesses the user's comnd line input for execution.
        Args:
           user_input (str): The original user input.
        Returns:
           str: The preprocessed comnd line.
        """
        comand_parts = user_input.split('.', 1)
        if len(comand_parts) == 2:
            comnd = comand_parts[0]
            argument_str = comand_parts[1]

            arg_parts = argument_str.split('(', 1)
            cmd = arg_parts[0]

            newln = cmd + " " + comnd

            if len(arg_parts) == 2:
                args = arg_parts[1].split(')', 1)
                args = args[0].split(",")

                a_id = args[0].strip()
                newln = cmd + " " + comnd + " " + a_id

                if len(args) > 1:
                    other_args = args[1:]
                    conctd_args = ""
                    for arg in other_args:
                        conctd_args += arg
                    conctd_args = conctd_args.replace("\"", "").strip()

                    newln = cmd + " " + comnd + " " + a_id + " " + conctd_args

            return newln
        return user_input


if __name__ == '__main__':
    HBNBComand().cmdloop()
