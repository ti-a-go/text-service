import json
from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APIClient

from core.models import TextModel


class CreateTextViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_should_not_create_text_when_data_is_not_valid(self):
        # When
        response = self.client.post("/texts/", {})

        # Then
        response_body = json.loads(response.content.decode())

        expected_response_body = {
            "title": [
                "This field is required."
            ],
            "author": [
                "This field is required."
            ],
            "text": [
                "This field is required."
            ]
        }

        self.assertDictEqual(response_body, expected_response_body)
        
    def test_should_not_create_text_when_database_raises_exception(self):
        with patch.object(TextModel, "save") as mock_method:
            mock_method.side_effect = Exception("Test database raise exception.")

            # Given
            data = {
                "title": "test",
                "author": "test",
                "text": "test"
            }
            
            # When
            response = self.client.post("/texts/", data)

            # Then
            response_body = json.loads(response.content.decode())

            expected_response_body = {"Error": "contanct the server maintainers."}

            self.assertDictEqual(response_body, expected_response_body)

    def test_should_create_text(self):
        # Given
        data = {
            "title": "test",
            "author": "test",
            "text": "test"
        }
        
        # When
        response = self.client.post("/texts/", data)

        # Then
        response_body = json.loads(response.content.decode())

        expected_response_body = data
        expected_response_body["id"] = 1

        self.assertDictEqual(response_body, expected_response_body)