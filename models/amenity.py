#!/usr/bin/python3
"""amenity class inhereted from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class amenity"""

    name = ""

    def __init__(self, *args, **kwargs):
        """initializing the amenity class"""
        super().__init__(*args, **kwargs)
