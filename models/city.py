#!/usr/bin/python3
'''
City class
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    State class inherits from BaseModel
    '''
    state_id = ''
    name = ''


def __init__(self, *args, **kwargs):
    """
    init
    """
    super().__init__(*args, **kwargs)
