from core.domain import Text

def create_test_text() -> Text:
    return Text(title="test title", author="test author", text="test text")
