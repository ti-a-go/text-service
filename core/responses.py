from rest_framework import status

from core.results import CreateTextResult
from core.serializers import CreateTextModelSerializer


class CreateTextResponse:
    __serializer_class = CreateTextModelSerializer

    def __init__(self, result: CreateTextResult):
        self.__result = result

    @property
    def body(self):
        if self.have_error:
            return {"Error": "contanct the server maintainers."}

        return self.__serializer_class(self.__result.text).data

    @property
    def status(self):
        if self.__result.text is None:
            return status.HTTP_500_INTERNAL_SERVER_ERROR

        return status.HTTP_201_CREATED
    
    @property
    def have_error(self):
        if self.__result.text is None:
            return True
        return False
