import logging
from typing import Optional

from django.db.models.query import QuerySet

from core.domain import Text
from core.models import TextModel


logger = logging.getLogger(__name__)


class TextRepository:

    def create_text(self, text: Text) -> Optional[Text]:
        text_model = text.to_model()

        try:
            text_model.save()

        except Exception as e:
            logger.error(
                f"Error when trying to create a text: {text}. Exception: {str(e)}"
            )

            return None

        text.id = text_model.id

        logger.info(f"Text created: {text}")

        return text

    def list_texts(self) -> Optional[list[Text]]:
        try:
            query_set = TextModel.objects.all()

        except Exception as e:
            logger.error("Exception raised while trying to list 'Texts'")

            return None

        return [Text.from_model(text) for text in query_set]
