#!/usr/bin/python3
"""module defines class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class inherites from class BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
