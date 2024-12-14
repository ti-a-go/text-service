from typing import Optional

from core.domain import Text


def create_test_text(id: Optional[int] = None) -> Text:
    if id is not None:
        return Text(id=id, title="test title", author="test author", text="test text")

    return Text(title="test title", author="test author", text="test text")
