#!/usr/bin/python3
"""Define a user class inhereted from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """This represent a class User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
