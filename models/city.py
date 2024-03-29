#!/usr/bin/python3
"""Defines the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Represents the state class
    Attributes:
        state_id: State id.
        name: Name of the city.
    """

    state_id = ""
    name = ""
