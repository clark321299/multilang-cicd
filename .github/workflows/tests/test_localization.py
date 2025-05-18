import unittest
from app.app import app

class TestLocalization(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def test_default_language(self):
        response = self.app.get('/')
        self.assertIn('Привіт, світ', response.data.decode())
        
    def test_english_language(self):
        response = self.app.get('/?lang=en')
        self.assertIn('Hello World', response.data.decode())
        
    def test_german_language(self):
        response = self.app.get('/?lang=de')
        self.assertIn('Hallo Welt', response.data.decode())

if __name__ == '__main__':
    unittest.main()
