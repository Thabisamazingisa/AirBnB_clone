#!/user/bin/python3
'''This is the base models '''

import uuid as uid
from datetime import datetime as dat
import models as mod


class BaseModel():
    '''Base model class'''
    def __init__(self, **kwargs):
        ''' base model constructor for the class '''
        if kwargs:
            kwargs['created_at'] = dat.strptime(kwargs['created_at'], '%Y-%m-%d');
            kwargs['updated_at'] = dat.strptime(kwargs['updated_at'], '%Y-%m-%d');
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uid.uuid4())
            self.created_at = dat.now()
            self.updated_at = dat.now()
            mod.storage.new(self)

    def __str__(self):
        ''' returns a string representation of the object '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__);