from django.test import TestCase
from unittest.mock import patch

from core.repositories import TextRepository
from core.usecases import CreateTextUseCase, ListTextsUseCase
from core.tests.utils import create_test_text


class CreateTextUseCaseTests(TestCase):

    def test_usecase_should_return_result_without_text_when_repository_could_not_create_the_text(
        self,
    ):
        with patch.object(
            TextRepository, "create_text", return_value=None
        ) as mock_method:
            # Give
            text = create_test_text()

            usecase = CreateTextUseCase()

            # When
            result = usecase.run(text)

            # Then
            mock_method.assert_called_once_with(text)
            self.assertIsNone(result.text)

    def test_usecase_should_return_result_with_created_text_when_repository_could_create_the_text(
        self,
    ):
        # Setup
        text = create_test_text()

        with patch.object(
            TextRepository, "create_text", return_value=text
        ) as mock_method:
            # Give
            usecase = CreateTextUseCase()

            # When
            result = usecase.run(text)

            # Then
            mock_method.assert_called_once_with(text)
            self.assertIs(result.text, text)


class ListTextsUseCaseTests(TestCase):

    def test_usecase_should_return_result_without_texts_when_repository_could_not_list_the_texts(
        self,
    ):
        with patch.object(
            TextRepository, "list_texts", return_value=None
        ) as mock_method:
            # Give
            usecase = ListTextsUseCase()

            # When
            result = usecase.run()

            # Then
            mock_method.assert_called_once_with()
            self.assertIsNone(result.texts)

    def test_usecase_should_return_result_with_list_of_texts(self):
        # Setup
        texts = [create_test_text(id=i) for i in range(3)]

        with patch.object(
            TextRepository, "list_texts", return_value=texts
        ) as mock_method:
            # Give
            usecase = ListTextsUseCase()

            # When
            result = usecase.run()

            # Then
            mock_method.assert_called_once_with()
            self.assertIs(result.texts, texts)
