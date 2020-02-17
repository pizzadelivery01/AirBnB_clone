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
        bae = self.test_class()
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(UUID(base.id), UUID)

    def test_created_at(self):
        base = self.test_class
        now = dt.now()
        self.assertIsInstance(base.created_at, dt)

    def test_updated_at(self):
        base = self.test_class
        now = dt.now()
        base.dt.now
        self.assertNotEqual(base.dt, now)
