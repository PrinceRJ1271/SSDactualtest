import unittest
from app import app

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_form_submission(self):
        response = self.app.post('/', data=dict(search="test"))
        self.assertIn(b"Search Term Result", response.data)

if __name__ == '__main__':
    unittest.main()
