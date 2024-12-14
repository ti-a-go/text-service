from rest_framework import status

from core.serializers import CreatedTextModelSerializer
from core.results import CreateTextResult, ListTextsResult
from core.serializers import ListTextsModelSerializer


class CreateTextResponse:
    _serializer_class = CreatedTextModelSerializer

    def __init__(self, result: CreateTextResult):
        self._result = result

    @property
    def body(self):
        if self.have_error:
            return {"Error": "contanct the server maintainers."}

        return self._serializer_class(self._result.text).data

    @property
    def status(self):
        if self.have_error:
            return status.HTTP_500_INTERNAL_SERVER_ERROR

        return status.HTTP_201_CREATED

    @property
    def have_error(self):
        if self._result.text is None:
            return True
        return False


class ListTextsResponse:
    _serializer_class = ListTextsModelSerializer

    def __init__(self, result: ListTextsResult):
        self._result = result

    @property
    def body(self):
        if self.have_error:
            return {"Error": "contanct the server maintainers."}

        return self._serializer_class(self._result.texts, many=True).data

    @property
    def status(self):
        if self.have_error:
            return status.HTTP_500_INTERNAL_SERVER_ERROR

        return status.HTTP_200_OK

    @property
    def have_error(self):
        if self._result.texts is None:
            return True
        return False
