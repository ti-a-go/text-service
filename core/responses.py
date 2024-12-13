from rest_framework import status

from core.results import CreateTextResult
from core.serializers import CreatedTextModelSerializer


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
