#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from uuid import UUID
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    '''
    =========================
    BaseModel tests
    =========================
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_class = BaseModel
        self.test_name = 'BaseModel'

    def test_id(self):
        base = self.test_class()
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(UUID(base.id), UUID)

    def test_created_at(self):
        base = self.test_class()
        now = datetime.now()
        self.assertIsInstance(base.created_at, datetime)
        self.assertTrue(now >= base.created_at)

    def test_updated_at(self):
        base = self.test_class()
        base.updated_at = datetime.now()
        store = base.updated_at
        self.assertIsInstance(base.updated_at, datetime)
        base.updated_at = datetime.now()
        self.assertNotEqual(base.updated_at, store)

    def test_str(self):
        base = self.test_class()
        self.assertEqual(str(base), '[{}] ({}) {}'.format
                         (self.name, base.id, base.__dict__))
