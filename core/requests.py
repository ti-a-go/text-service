from typing import Optional

from rest_framework.request import Request

from core.serializers import CreateTextModelSerializer
from core.models import TextModel
from core.domain import Text


class CreateTextRequest:
    _serializer_class = CreateTextModelSerializer

    def __init__(self, request: Request):
        self._request = request

    def is_valid(self) -> bool:
        self._serializer = self._serializer_class(data=self._request.data)

        return self._serializer.is_valid()

    @property
    def validation_error_messages(self):
        return self._serializer.errors

    @property
    def text_to_be_created(self) -> Optional[TextModel]:

        if self.is_valid():
            return Text.for_creation(self._serializer.validated_data)
