"""
API view For Document like post, get method for any document.
"""
import logging
import json
from django.db import IntegrityError
from django.core.serializers import serialize
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Continent, Country, City
from ..serializers import CountrySerializer

LOGGER = logging.getLogger("application_logs")


class CountryAddtView(APIView):
    """
    View for /country API.
    This view will handle all the Methods, POST/GET...
    For now only POST is defined!
    """
    def post(self, request, *args, **kwargs):
        """
        POST API - This api will first call the serializer to validate the format and type of data passed.
        Once that is valid, it will call a custom validate method to verify all the edge cases.
        If the function returns success, the data will be saved ion DB, otherwise and Error will be raised.
        Error have been logged (for now as print statement), where as the end user will get a high level Error Message
        :param request:
        :return: 200/400/500 status
        """
        try:
            data = request.data
            serializer = CountrySerializer(data=data)
            if serializer.is_valid():
                data = serializer.data
                if serializer.validate_data(data):
                    try:
                        country_data = Country(name=data.get('name'),
                            population=data.get('population'), area=data.get('area'),
                            continent_id=Continent.objects.get(pk=data.get('continent_id')),
                            no_of_hospital=data.get('no_of_hospital'), no_of_nationalparks=data.get('no_of_nationalparks'),
                            no_of_rivers=data.get('no_of_rivers'), no_of_schools=data.get('no_of_schools'))
                        country_data.save()
                        return Response(data, status=200)
                    except IntegrityError as err:
                        print(err, 'Error')
                        return Response({'Error': 'Database Error Found'}, status=400)
                else:
                    print('Data Validation failed | Some of the data from DB mismatches')
                    return Response({'Error': 'Data Validation failed | Some of the data from DB mismatches'}, status=400)
            else:
                print ('Validation Error')
                return Response({'Error': 'Validation Error'}, status=500)
        except Exception as ex:
            print(ex, "Error")
            return Response({'Error': ex}, status=500)