#!/usr/bin/python3
'''
Amenity class
'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''
    Amenity class inherits from BaseModel
    '''
    name = ''


def __init__(self, *args, **kwargs):
    """
    init
    """
    super().__init__(*args, **kwargs)
