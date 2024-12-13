import logging

from core.models import TextModel
from core.domain import Text


logger = logging.getLogger(__name__)


class TextRepository:

    def create_text(self, text: Text) -> Text:
        text_model = text.to_model()

        try:
            text_model.save()

        except Exception as e:
            logger.error(
                f"Error when trying to create a 'Text' {text}. Exception: {str(e)}"
            )

            return None

        text.id = text_model.id

        logger.info(f"'Text' created: {text}")

        return text
