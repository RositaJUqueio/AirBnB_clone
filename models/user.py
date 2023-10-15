#!/usr/bin/python3
"""Defines a User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a User class

    Attributes:
         email: The user's email adress.
         password: The user's password.
         first_name : The user's first name.
         last_name: The user's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
