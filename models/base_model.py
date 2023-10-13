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
            kwargs['created_at'] = dat.strptime(kwargs['created_at'],
                                                '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = dat.strptime(kwargs['updated_at'],
                                                '%Y-%m-%dT%H:%M:%S.%f')

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
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        ''' updates the object in the storage '''
        self.updated_at = dat.now()
        mod.storage.save()

    def to_dict(self):
        ''' returns the dictionary representation of the object '''
        new_dict = dict(self.__dict__)
        new_dict['created_at'] = self.new_dict['created_at'].isoformat()
        new_dict['updated_at'] = self.new_dict['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict