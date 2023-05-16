#!/usr/bin/python3
"""module defines class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """class inherites from BaseModel class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
