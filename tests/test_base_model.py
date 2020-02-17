import unittest
import pep8
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''
    =========================
    Setup and style tests
    =========================
    '''
    def test_pep8(self):
        pep8_style = pep8.StyleGuide(quit=True)
        pep8_check = pep8_style.check_files(['models/base_model.py'])
        self.assertEqual(pep8_check.total_errors, 0, 'Pep8 Error in file')

    def test_docstrings(self):
        self.assertIsNotNone(BaseModel.__doc__)

    def test_uuid(self):
        
