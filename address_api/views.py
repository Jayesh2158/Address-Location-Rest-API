from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AddressSerializer
from .services import LocationService


class AddressAPIView(APIView):
    def post(self, request):
        """
        It takes a request, validates it, and then returns the response from the LocationService

        :param request: The request object
        :return: A dictionary with the keys:
            - lat
            - lng
            - formatted_address
            - status
        """
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return LocationService.get_lat_long(
                line1=serializer.data["address"],
                output_type=serializer.data["output_format"],
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
