#!/usr/bin/python3
"""Define a user class inherited from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """This represents a class User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
