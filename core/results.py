from typing import Optional

from django.db.models.query import QuerySet

from core.domain import Text


class CreateTextResult:

    def __init__(self, text: Optional[Text] = None):
        self.text = text


class ListTextsResult:

    def __init__(self, texts: Optional[QuerySet] = None):
        self.texts = texts
