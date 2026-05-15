import unittest
from unittest.mock import Mock, patch

from app import app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_homepage_loads_successfully(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"AI Quote Generator", response.data)

    def test_quote_api_returns_json_quote(self):
        response = self.client.get("/api/quote")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertIn("quote", data)
        self.assertIn("total_quotes", data)
        self.assertIsInstance(data["quote"], str)

    @patch("app.requests.get")
    def test_generated_image_route_returns_image_content(self, mock_get):
        mock_response = Mock()
        mock_response.content = b"\xff\xd8\xff\xe0fake-jpeg-content"
        mock_response.headers = {"Content-Type": "image/jpeg"}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        response = self.client.get("/generated-image")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "image/jpeg")
        self.assertTrue(response.data.startswith(b"\xff\xd8"))


if __name__ == "__main__":
    unittest.main()
