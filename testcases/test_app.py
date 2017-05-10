import os, sys
sys.path.append("..")
import app as Application
import unittest
import tempfile

class TestCase(unittest.TestCase):

    def setUp(self):
        Application.app.config['TESTING'] = True
        self.app = Application.app.test_client()

    def test_homepage(self):
        rv = self.app.get('/')
        assert rv.status_code == 200

if __name__ == '__main__':
    unittest.main()
