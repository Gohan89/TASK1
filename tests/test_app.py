import unittest
from app import app

class AnimeSuggestionTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_suggest_anime(self):
        response = self.app.get('/suggest')
        self.assertEqual(response.status_code, 200)
        self.assertIn('suggestion', response.json)

if __name__ == '__main__':
    unittest.main()
