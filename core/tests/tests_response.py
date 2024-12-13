from django.test import TestCase
from rest_framework import status

from core.responses import CreateTextResponse
from core.results import CreateTextResult
from core.tests.utils import create_test_text


class CreateTextResponseTests(TestCase):
    
    def test_response_should_have_body_when_result_has_text(self):
        # Given
        text = create_test_text()
        result = CreateTextResult(text)

        # When
        response = CreateTextResponse(result)

        # Then
        self.assertIsInstance(response.body, dict)
        self.assertEqual(response.status, status.HTTP_201_CREATED)
    
    def test_response_should_not_have_body_when_result_does_have_not_text(self):
        # Given
        result = CreateTextResult()

        # When
        response = CreateTextResponse(result)

        # Then
        expected_response_body = {"Error": "contanct the server maintainers."}

        self.assertDictEqual(response.body, expected_response_body)
        self.assertEqual(response.status, status.HTTP_500_INTERNAL_SERVER_ERROR)
