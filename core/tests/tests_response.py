from django.test import TestCase
from rest_framework import status

from core.responses import CreateTextResponse, ListTextsResponse
from core.results import CreateTextResult, ListTextsResult
from core.tests.utils import create_test_text


class CreateTextResponseTests(TestCase):
    
    def test_response_should_have_body_when_result_has_text(self):
        # Given
        text = create_test_text(id=1)
        result = CreateTextResult(text)

        # When
        response = CreateTextResponse(result)

        # Then
        self.assertIsInstance(response.body, dict)
        self.assertEqual(response.body, text.__dict__)
        self.assertEqual(response.status, status.HTTP_201_CREATED)
    
    def test_response_should_have_error_body_when_result_does_not_have_text(self):
        # Given
        result = CreateTextResult()

        # When
        response = CreateTextResponse(result)

        # Then
        expected_response_body = {"Error": "contanct the server maintainers."}

        self.assertDictEqual(response.body, expected_response_body)
        self.assertEqual(response.status, status.HTTP_500_INTERNAL_SERVER_ERROR)


class ListTextResponseTests(TestCase):
    
    def test_response_should_have_body_when_result_has_texts(self):
        # Given
        text_count = 3
        texts = [create_test_text(id=i) for i in range(text_count)]
        result = ListTextsResult(texts)

        # When
        response = ListTextsResponse(result)
        expected_text: dict = response.body[0]

        # Then
        self.assertEqual(expected_text.get("id"), texts[0].id)
        self.assertEqual(expected_text.get("title"), texts[0].title)
        self.assertEqual(expected_text.get("author"), texts[0].author)
        self.assertEqual(expected_text.get("text"), texts[0].text)
        self.assertEqual(len(response.body), text_count)
        self.assertIsInstance(response.body, list)
        self.assertEqual(response.status, status.HTTP_200_OK)
    
    def test_response_should_have_error_body_when_result_does_not_have_text(self):
        # Given
        result = ListTextsResult()

        # When
        response = ListTextsResponse(result)

        # Then
        expected_response_body = {"Error": "contanct the server maintainers."}

        self.assertDictEqual(response.body, expected_response_body)
        self.assertEqual(response.status, status.HTTP_500_INTERNAL_SERVER_ERROR)

