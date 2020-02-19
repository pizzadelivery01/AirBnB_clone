#!/usr/bin/python3
'''
State class
'''
from models.base_model import BaseModel


class State(BaseModel):
    '''
    State class inherits from BaseModel
    '''
    name = ''


def __init__(self, *args, **kwargs):
    """
    init
    """
    super().__init__(*args, **kwargs)
