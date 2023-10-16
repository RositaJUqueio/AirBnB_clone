#!/usr/bin/python3
""" Unittesting for console.py

Unittest classes:
    TestHBNBCommand_prompt
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""

import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

class TestHBNBCommand_prompt(unittest.TestCase):
    """Unittests for testing the prompt of the console"""
    def test_prompt_string(self):
        self.assertEqual("(hbnb)", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

class TestHBNBCommand_help(unittest.TestCase):
    """test for testing the help command"""
    def test_help_quit(self):
        h = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())