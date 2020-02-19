#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    '''
    FileStorage test
    '''

    def test_file_save(self):
        '''
        File creation test
        '''
        new = BaseModel()
        self.assertTrue(os.path.exists('JSONstorage.json'))

    def tearDown(self):
        '''
        Destroy JSON file
        '''
        try:
            os.remove('JSONstorage.json')
        except:
            pass

    def test_file_empty(self):
        '''
        File empty test
        '''
        base = BaseModel()
        my_dict = base.to_dict()
        base.save()
        base2 = BaseModel(**my_dict)
        self.assertEqual(os.path.getsize('JSONstorage.json'), 5008)
