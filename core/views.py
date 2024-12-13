import logging

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from core.requests import CreateTextRequest
from core.usecases import CreateTextUseCase
from core.responses import CreateTextResponse


logger = logging.getLogger(__name__)


class ListCreateTextView(APIView):

    def post(self, request: Request) -> Response:

        create_text_request = CreateTextRequest(request)

        if not create_text_request.is_valid():

            errors = create_text_request.validation_error_messages

            logger.info(f"Invalid body: {errors}")

            return Response(errors, status.HTTP_400_BAD_REQUEST)

        logger.info(
            f"Starting 'Text' creation: {create_text_request.text_to_be_created}"
        )

        usecase = CreateTextUseCase()

        result = usecase.run(create_text_request.text_to_be_created)

        response = CreateTextResponse(result)

        if response.have_error:
            logger.error(
                f"Error while trying to create 'Text': {create_text_request.text_to_be_created}"
            )

            return Response(response.body)

        return Response(response.body, response.status)
