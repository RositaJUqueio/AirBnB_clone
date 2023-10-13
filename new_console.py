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


class HBNBCommand(cmd.Cmd):
    """HBnBCommand class: Defines the command-line interpreter for HBnB.

    Attributes:
        prompt (str): The command prompt.
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
        """Quit command to exit the program\n"""
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
        elif args[0] not in HBNBCommand.__models:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)  

    def do_show(self, arg):
        """
        Displays string representation of a class instance
        based on class name and id.
        then prints the string representation of the specified instance
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__models:
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
        elif args[0] not in HBNBCommand.__models:
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
