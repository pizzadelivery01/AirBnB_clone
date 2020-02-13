#!/usr/bin/python3

'''
Write a class BaseModel that defines all common attributes/methods for other classes
'''
import uuid
import datetime


class BaseModel:
    '''
    BaseModel class
    '''
    def __init__(self):
        '''
        Constructor method
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        '''
        Update public instance with current datetime
        '''
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        '''
        Dictionary containing all
        keys/values of __dict__
        '''
        my_dict = {}
        my_dict.update(self.__dict__)
        self.__dict__['created at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return my_dict


    def __str__(self):
        return '[{}] ({}) {}'.format(
            BaseModel.__class__.__name__, self.id, self.__dict__)
