from django.test import TestCase

from core.domain import Text
from core.models import TextModel


class TextTests(TestCase):

    def test_text_for_creation_should_return_text_for_creation(self):
        # Given
        data = {
            "id": "test id",
            "title": "test title",
            "author": "test author",
            "text": "test text",
        }

        expected_data = data
        expected_data["id"] = None

        # When
        text = Text.for_creation(data)

        # Then
        self.assertIsInstance(text, Text)
        self.assertDictEqual(text.__dict__, expected_data)

    def test_text_for_creation_should_return_none_when_data_has_no_text(self):
        # Given
        data = {
            "title": "test title",
            "author": "test author",
        }

        # When
        text = Text.for_creation(data)

        # Then
        self.assertIsNone(text)

    def test_text_for_creation_should_return_none_when_data_has_no_title(self):
        # Given
        data = {"author": "test author", "text": "test text"}

        # When
        text = Text.for_creation(data)

        # Then
        self.assertIsNone(text)

    def test_text_for_creation_should_return_none_when_data_has_no_author(self):
        # Given
        data = {
            "title": "test title",
            "text": "test text",
        }

        # When
        text = Text.for_creation(data)

        # Then
        self.assertIsNone(text)

    def test_text_to_model_should_return_database_model(self):
        # Given
        text = Text(title="test title", author="test author", text="test text")

        # When
        model = text.to_model()

        # Then
        self.assertIsInstance(model, TextModel)
