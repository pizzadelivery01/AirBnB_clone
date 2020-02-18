import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from uuid import UUID
from datetime import datetime as dt
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
        now = dt.now()
        self.assertIsInstance(base.created_at, dt)
        self.assertTrue(now >= base.created_at)

    def test_updated_at(self):
        base = self.test_class()
        now = base.updated_at
        self.assertIsInstance(base.updated_at, dt)
        base.updated_at = dt.now

    def test_str(self):
        base = self.test_class()
        form = '[' + self.test_name + "] ({}) {}".format(
        base.id, str(base.__dict__))
        self.assertEqual(str(base), form)
