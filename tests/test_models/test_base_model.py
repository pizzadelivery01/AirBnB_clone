import unittest
import pep8
from uuid import UUID
import json
from datetime import DateTime as dt
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''
    =========================
    BaseModel tests
    =========================
    '''
    def __init__(self, *args, **kwargs):
        self.test_class = BaseModel
        self.test_name = 'BaseModel'

    def test_id(self):
        self.assertIsInstance(self.test_class.id, str)
        self.assertIsInstance(self.class_name.id, UUID)

    def test_created_at(self):
        base = self.test_class
        now = dt.now()
        self.assertIsInstance(base.created_at, dt)

    def test_updated_at(self):
        base = self.test_class
        now = dt.now()
        base.dt.now
        self.assertNotEqual(base.dt, now)
