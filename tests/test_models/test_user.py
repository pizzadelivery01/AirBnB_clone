#!/usr/bin/python3
from models.user import User
from tests.test_models.test_base_model import TestBaseModel


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
        user = self.self_class()
        self.assertEqual(type(user.email), str)

    def test_password(self):
        user = self.self_class()
        self.assertEqual(type(user.password), str)

    def test_firstName(self):
        user = self.self_class()
        self.assertEqual(type(user.first_name), str)

    def test_lastName(self):
        user = self.self_class()
        self.assertEqual(type(user.last_name), str)
