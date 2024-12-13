from django.test import TestCase
from unittest.mock import patch

from core.repositories import TextRepository
from core.usecases import CreateTextUseCase
from core.tests.utils import create_test_text


class CreateTextUseCaseTests(TestCase):

    def test_usecase_should_return_result_without_text_when_repository_could_not_create_the_text(self):
        with patch.object(TextRepository, "create_text", return_value=None) as mock_method:
            # Give
            text = create_test_text()

            usecase = CreateTextUseCase()

            # When
            result = usecase.run(text)

            # Then
            mock_method.assert_called_once_with(text)
            self.assertIsNone(result.text)
    
    def test_usecase_should_return_result_with_created_text_when_repository_could_create_the_text(self):
        # Setup
        text = create_test_text()
        
        with patch.object(TextRepository, "create_text", return_value=text) as mock_method:
            # Give
            usecase = CreateTextUseCase()

            # When
            result = usecase.run(text)

            # Then
            mock_method.assert_called_once_with(text)
            self.assertIs(result.text, text)