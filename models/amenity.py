#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representz an amenity class.

    Attributes:
        name: Name of the amenity.
    """

    name = ""