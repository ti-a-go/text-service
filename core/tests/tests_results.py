from django.test import TestCase

from core.results import CreateTextResult
from core.domain import Text
from core.tests.utils import create_test_text


class CreateTextResultTests(TestCase):

    def test_result_should_have_text_property(self):
        # Given
        text = create_test_text()

        # When
        result = CreateTextResult(text)

        # Then
        self.assertIsInstance(result.text, Text)
        self.assertIs(text, result.text)
    
    def test_result_should_not_have_text(self):
        # When
        result = CreateTextResult()

        # Then
        self.assertIsNone(result.text)