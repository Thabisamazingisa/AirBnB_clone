#!/usr/bin/python3
"""state class inherited from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """class State"""

    name = ""

    def __init__(self, *args, **kwargs):
        """The initializing State class"""
        super().__init__(*args, **kwargs)
