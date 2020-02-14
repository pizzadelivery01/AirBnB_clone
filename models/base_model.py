#!/usr/bin/python3

'''
Write a class BaseModel that defines all common attributes/methods
for other classes
'''
import uuid
from datetime import datetime


class BaseModel:
    '''
    BaseModel class
    '''

    def __init__(self, *args, **kwargs):
        '''
        Constructor method
        '''
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__.update(kwargs)
            del self.__dict__['__class__']

    def save(self):
        '''
        Update public instance with current datetime
        '''
        self.updated_at = datetime.now()

    def __str__(self):
        '''
        String reprsentation
        '''
        return '[{}] ({}) {}'.format(
            type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        '''
        Dictionary containing all
        keys/values of __dict__
        '''
        my_dict = dict(self.__dict__)
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = type(self).__name__
        return my_dict
