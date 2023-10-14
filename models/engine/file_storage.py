#!/usr/bin/python3

import json


class Storage():
    __file_path = "app_data.json"
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
        with open(Storage.__file_path, 'w', encoding='utf-8') as file:
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
