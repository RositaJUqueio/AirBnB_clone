#!/usr/bin/python3
"""The console module"""
import cmd
import importlib #for importing module dynamically
import json
import shlex #For parsing command arguments
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    class for the console interface
    the prompt id what it will display
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """ to quit the program"""
        return True
    
    def do_EOF(self, arg):
        """this will exit the programm ctr+d"""
        return True
    
    def do_emptyline(self):
        """ overwriting emptyline"""
        return False

    def do_create(self, arg):
        """for creating a new instances of basemodel"""
        args = shlex.split(arg)
        """For splitting the arguments """
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        """setting the class name to the arguments"""
        try:
            """bringing each class dynamically"""
            module = importlib.import_module("models." + class_name.lower())
            class_to_create = getattr(module, class_name)
            instance = class_to_create()
            instance.save()
            print(instance.id)
        except AttributeError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        this method prints strings representation of an
        instance
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        try:
            class_show = getattr(BaseModel, class_name)
            instances = class_show.all()
            key = class_name + "." + instance_id
            if key in instances:
                print(instances[key])
            else:
                print("** no instance found **")
        except AttributeError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Method that delete an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        try:
            class_destroy = getattr(BaseModel, class_name)
            instances = class_destroy.all()
            key = class_name + "." + instance_id
            if key in instances:
                del instances[key]
                class_destroy.save()
            else:
                print("** class doesn't test **")
        except AttributeError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """This method prints all instances"""
        args = shlex.split(arg)
        if args and args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            try:
                list_class = getattr(BaseModel, "BaseModel")
                instances = list_class.all
                print([str(instance) for instance in instances.values()])
            except AttributeError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Method that update all instances"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        try:
            class_update = getattr(BaseModel, class_name)
            instances = class_update.all()
            key = class_name + "." + instance_id
            if key in instances:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attr_name = args[2]
                    attr_val = args[3]
                    instance = instances[key]
                    setattr(instance, attr_name, attr_val)
                    instance.save()
            else:
                print("** no instance found **")
        except AttributeError:
            print("** class doesn't exist **")

if __name__ == "__main__":
     HBNBCommand().cmdloop()