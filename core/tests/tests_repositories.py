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

    def test_repository_create_text_should_return_none_when_database_raises_error_while_creating_text(self):
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
