#!/usr/bin/python3
"""The console module"""
import cmd

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
    
    def emptyline(self):
        """this is doing nothing for now"""
        
        pass

if __name__ == "__main__":
     HBNBCommand().cmdloop()