#!/usr/bin/python3
''' Command line interpreter '''
import cmd
import shlex as shl
import models as mod
from datetime import datetime as dat
from models.base_model import BaseModel as bsm
from models import storage as sto
from models.user import User as us
from models.state import State as st
from models.city import City as ct
from models.amenity import Amenity as am
from models.place import Place as pl
from models.review import Review as rv

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes__ = [
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
    ]

    def do_create(self, args):
        args = args.split()
        if len(args) == 0:
            print("*** Class name is required***")
        elif args[0] not in HBNBCommand.__classes__:
            print("*** Class doesn't exist***")
        else:
            new_creation = eval(args[0]+'()')
            mod.storage.save()
            print(new_creation.id)

    # def do_show(self, args):

