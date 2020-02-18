import unittest
from models.base_model import BaseModel
from models.user import User
from tests.test_models.test_base_model import TestBaseModel
from uuid import UUID
from datetime import datetime as dt


class TestUser(TestBaseModel):
    '''
    =========================
    User tests
    =========================
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_class = User
        self.test_name = "User"

    def test_email(self):
        self.assertIsInstance(self.test_class.email, str)

    def test_password(self):
        self.assertIsInstance(self.test_class.password, str)

    def test_first_name(self):
        self.assertIsInstance(self.test_class.first_name, str)

    def test_last_name(self):
        self.assertIsInstance(self.test_class.last_name, str)
