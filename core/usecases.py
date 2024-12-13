from core.domain import Text
from core.repositories import TextRepository
from core.results import CreateTextResult


class CreateTextUseCase:
    _repository = TextRepository()

    def run(self, text: Text):
        text = self._repository.create_text(text)

        if text is None:
            return CreateTextResult()

        return CreateTextResult(text)
