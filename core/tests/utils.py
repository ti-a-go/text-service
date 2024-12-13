from typing import Optional

from core.domain import Text

def create_test_text(id: Optional[int] = None) -> Text:
    return Text(title="test title", author="test author", text="test text")
