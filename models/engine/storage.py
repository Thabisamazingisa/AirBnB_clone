#!/usr/bin/python3

import json
from models.base_model import BaseModel as bsm
from models.user import User as us
from models.state import State as st
from models.city import City as ct
from models.amenity import Amenity as am
from models.place import Place as pl
from models.review import Review as rv

class Storage():
    __file_path = "file.json"
    __object = {}

    def all(self):
        return Storage.__object

    def new(self, obj):
        if obj:
            key = "{} {}".format(obj.__class__.__name__, obj.id)
            Storage.__object[key] = obj

    def save(self):
        new_dict = {}
        for key, value in Storage.__object.items():
            new_dict[key] = value.to_dict().copy()
        with open(Storage.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):

        try:
            with open(Storage.__file_path, 'r') as file:
                Storage.__object = json.load(file)

            for key, value in Storage.__object.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                Storage.__object[key] = obj
        except FileNotFoundError:
            pass
