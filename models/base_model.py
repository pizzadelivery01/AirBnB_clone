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
        self.created_at = datetime.datetime.isoformat(datetime.datetime.now())
        self.updated_at = datetime.datetime.isoformat(datetime.datetime.now())

    def save(self):
        '''
        Update public instance with current datetime
        '''
        self.updated_at = datetime.datetime.isoformat(datetime.datetime.now())

    def to_dict(self):
        '''
        Dictionary containing all
        keys/values of __dict
        '''
        my_dict = {}
        my_dict.update(__dict__)
        return my_dict


    def __str__(self):
        return '[{}] ({}) {}'.format(
            BaseModel.__class__.__name__, self.id, self.__dict__)
