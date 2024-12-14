import json
from unittest.mock import patch

from django.test import TestCase
from rest_framework import status
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
            "title": ["This field is required."],
            "author": ["This field is required."],
            "text": ["This field is required."],
        }

        self.assertDictEqual(response_body, expected_response_body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_not_create_text_when_database_raises_exception(self):
        with patch.object(TextModel, "save") as mock_method:
            mock_method.side_effect = Exception("Test database raise exception.")

            # Given
            data = {"title": "test", "author": "test", "text": "test"}

            # When
            response = self.client.post("/texts/", data)

            # Then
            response_body = json.loads(response.content.decode())

            expected_response_body = {"Error": "contanct the server maintainers."}

            self.assertDictEqual(response_body, expected_response_body)
            self.assertEqual(
                response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def test_should_create_text(self):
        # Given
        data = {"title": "test", "author": "test", "text": "test"}

        # When
        response = self.client.post("/texts/", data)

        # Then
        response_body = json.loads(response.content.decode())

        expected_response_body = data
        expected_response_body["id"] = 1

        self.assertDictEqual(response_body, expected_response_body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ListTextViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_should_list_texts(self):
        # Given
        data = {
            "id": 1,
            "title": "test title",
            "author": "test author",
            "text": "test text",
        }
        TextModel(
            id=data["id"],
            title=data["title"],
            author=data["author"],
            text=data["text"],
        ).save()

        # When
        response = self.client.get("/texts/")

        # Then
        texts = json.loads(response.content.decode())
        text = texts[0]

        self.assertEqual(text["id"], data["id"])
        self.assertEqual(text["title"], data["title"])
        self.assertEqual(text["author"], data["author"])
        self.assertEqual(text["text"], data["text"])
        self.assertListEqual(texts, [data])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_not_list_texts_when_database_raises_exception(self):
        with patch.object(TextModel.objects, "all") as mock_method:
            mock_method.side_effect = Exception("Test database raise exception.")
            # Given
            data = {
                "id": 1,
                "title": "test title",
                "author": "test author",
                "text": "test text",
            }
            TextModel(
                id=data["id"],
                title=data["title"],
                author=data["author"],
                text=data["text"],
            ).save()

            # When
            response = self.client.get("/texts/")

            # Then
            response_body = json.loads(response.content.decode())
            expected_response_body = {"Error": "contanct the server maintainers."}

            self.assertEqual(
                response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            self.assertEqual(response_body, expected_response_body)


class UpdateTextViewTests(TestCase):

    def test_should_update_text(self):
        pass

    def test_should_not_update_text_when_no_data_is_provided_by_in_request(self):
        pass

    def test_should_not_update_text_when_database_raises_exception(self):
        pass

    def test_should_update_text_when_text_is_not_found(self):
        pass


class DeleteTextViewTests(TestCase):

    def test_should_delete_text(self):
        pass

    def test_should_not_delete_text_when_database_raises_exception(self):
        pass

    def test_should_not_delete_text_when_text_is_not_found(self):
        pass
