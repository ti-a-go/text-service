import logging
from unittest.mock import patch

from django.test import TestCase
from django.conf import settings

from core.repositories import TextRepository
from core.models import TextModel
from core.domain import Text
from core.tests.utils import create_test_text


if not settings.ENABLE_TEST_LOGS:
    logging.disable(logging.CRITICAL)


class TextRepositoryTests(TestCase):

    def setUp(self):
        self.repository = TextRepository()

    def test_repository_create_text_should_return_none_when_database_raises_exception(
        self,
    ):
        with patch.object(TextModel, "save") as mock_method:
            mock_method.side_effect = Exception("Test database raise exception")
            # Given
            text = create_test_text()

            # When
            created_text = self.repository.create_text(text)

            # Then
            self.assertIsNone(created_text)

    def test_repository_create_text_should_return_text_when_created_successfully(self):
        # Given
        text = create_test_text()

        # When
        created_text = self.repository.create_text(text)

        # Then
        self.assertIsInstance(created_text, Text)
        self.assertIsNotNone(created_text.id)

    def test_repository_list_texts_should_return_all_texts_from_database(self):
        # Given
        first_data = {
            "id": 1,
            "title": "test title",
            "author": "test author",
            "text": "test text",
        }
        seconde_data = {
            "id": 2,
            "title": "test title",
            "author": "test author",
            "text": "test text",
        }

        first_model = TextModel(
            title=first_data["title"],
            author=first_data["author"],
            text=first_data["text"],
        )
        second_model = TextModel(
            title=seconde_data["title"],
            author=seconde_data["author"],
            text=seconde_data["text"],
        )

        first_model.save()
        second_model.save()

        # When
        texts = self.repository.list_texts()
        text = texts[0]

        # Then
        self.assertEqual(len(texts), 2)
        self.assertIsInstance(text, Text)
        self.assertDictEqual(first_data, text.__dict__)

    def test_repository_list_texts_should_return_none_when_database_reises_exception(
        self,
    ):
        with patch.object(TextModel.objects, "all") as mock_method:
            mock_method.side_effect = Exception("Test database raise exception.")

            # Given
            data = {
                "id": 1,
                "title": "test title",
                "author": "test author",
                "text": "test text",
            }

            model = TextModel(
                title=data["title"], author=data["author"], text=data["text"]
            )

            model.save()

            # When
            texts = self.repository.list_texts()

            # Then
            self.assertIsNone(texts)
            mock_method.assert_called_once_with()
