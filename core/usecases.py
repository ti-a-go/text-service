from core.domain import Text
from core.repositories import TextRepository
from core.results import CreateTextResult, ListTextsResult


class CreateTextUseCase:
    _repository = TextRepository()

    def run(self, text: Text) -> CreateTextResult:
        text = self._repository.create_text(text)

        if text is None:
            return CreateTextResult()

        return CreateTextResult(text)


class ListTextsUseCase:
    _repository = TextRepository()

    def run(self):
        texts = self._repository.list_texts()

        if texts is None:
            return ListTextsResult()

        return ListTextsResult(texts)
