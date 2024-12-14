from typing import Optional

from core.domain import Text


class CreateTextResult:

    def __init__(self, text: Optional[Text] = None):
        self.text = text


class ListTextsResult:

    def __init__(self, texts: Optional[Text] = None):
        self.texts = texts
