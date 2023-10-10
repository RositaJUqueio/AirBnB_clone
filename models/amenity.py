#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents the amenity class.

    Attributes:
        name: Name of the amenity.
    """

    name = ""