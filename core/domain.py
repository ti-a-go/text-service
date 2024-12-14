from __future__ import annotations
from typing import Optional

from core.models import TextModel


class Text:

    def __init__(
        self,
        title: str,
        author: str,
        text: str,
        id: Optional[str] = None,
    ):
        self.title = title
        self.author = author
        self.id = id
        self.text = text

    @staticmethod
    def for_creation(data: dict) -> Text:

        if (
            data.get("title") is None
            or data.get("author") is None
            or data.get("text") is None
        ):
            return None

        return Text(
            title=data.get("title"), author=data.get("author"), text=data.get("text")
        )

    def to_model(self):
        return TextModel(title=self.title, author=self.author, text=self.text)

    def __str__(self):
        return f"Text '{self.title}' by {self.author}."

    @staticmethod
    def from_model(model: TextModel) -> Text:
        return Text(
            id=model.id, title=model.title, author=model.author, text=model.text
        )
