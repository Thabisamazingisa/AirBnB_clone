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
        ''' Create a new  '''
        args = args.split()
        if len(args) == 0:
            print("*** Class name is required***")
        elif args[0] not in HBNBCommand.__classes__:
            print("*** Class doesn't exist***")
        else:
            new_creation = eval(args[0]+'()')
            mod.sto.save()
            print(new_creation.id)

    def do_show(self, args):
        str = args.split()
        if len(str) == 0:
            print("*** class name missing ***")
        elif str[0] not in HBNBCommand.__classes:
            print("*** class doesn't exist ***")
        elif len(str) == 1:
            print("*** missing instance id ***")
        else:
            obj = mod.sto.all()
            key_value = str[0] + '.' + str[1]
            if key_value in obj:
                print(obj[key_value])
            else:
                print("*** no instance found ***")

    def do_destroy(self, args):
        args = args.split()
        obj = mod.sto.all()

        if len(args) == 0:
            print('*** class name missing ***')
        elif args[0] not in HBNBCommand.__classes:
            print("*** class doesn't exist ***")
        elif len(args) == 1:
            print('*** instance id missing ***')
        else:
            key_find = args[0] + '.' + args[1]
            if key_find in obj.keys():
                obj.pop(key_find, None)
                mod.sto.save()
            else:
                print('*** no instance found ***')
    def do_all(self, args):
        args = args.split()
        obj = mod.sto.all()
        new_list = []

        if len(args) == 0:
            for obj in obj.values():
                new_list.append(obj.__str__())
            print(new_list)
        elif args[0] not in HBNBCommand.__classes:
            print("*** class doesn't exist ***")
        else:
            for obj in obj.values():
                if obj.__class__.__name__ == args[0]:
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, args):
        obj = mod.sto.all()
        args = args.split(" ")

        if len(args) == 0:
            print("*** class name missing ***")
        elif args[0] not in HBNBCommand.__classes:
            print("***- class doesn't exist ***")
        elif len(args) == 1:
            print("*** instance id missing ***")
        elif len(args) == 2:
            print("*** attribute name missing ***")
        elif len(args) == 3:
            print("*** value missing ***")
        else:
            key_find = args[0] + '.' + args[1]
            obj = obj.get(key_find, None)

            if not obj:
                print("*** no instance found ***")
                return

            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            mod.storage.save()
    def check_class_name(self, name=""):
        ''' Check class name exists in the storage '''
        if len(name) == 0:
            print("*** class name missing ***")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        ''' Check if class id exists in the storage '''
        if len(name.split(' ')) == 1:
            print("*** instance id missing ***")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        ''' Check if class name exists in the storage '''
        if self.check_class_name(name):
            args = shl.split(name)
            if args[0] in HBNBCommand.__classes:
                if self.check_class_id(name):
                    key = args[0] + '.' + args[1]
                    return key
                else:
                    print("*** class doesn't exist ***")
                    return None

    def do_quit(self, args):
        '''  '''
        return True

    def do_EOF(self, args):
        '''  '''
        return True

    def empty_line(self):
        ''' Handles empty line '''
        pass
