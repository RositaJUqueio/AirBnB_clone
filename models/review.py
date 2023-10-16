#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Represents the review class

    Attributes:
        place_id: The place id.
        user_id: The user id.
        text: The review text.
    """

    place_id = ""
    user_id = ""
    text = ""
