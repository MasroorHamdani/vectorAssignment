"""
API view For Document like post, get method for any document.
"""
import json
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Continent, Country, City
from ..serializers import CountrySerializer, CitySerializer, ContinentSerializer
# from ..services.logstash import LogstashService

import logging
# LOGGER = LogstashService()

logger = logging.getLogger(__name__)


class CountryAddView(APIView):
    """
    View for /country API.
    This view will handle all the Methods, POST/GET...
    For now only POST and DELETE are defined!
    """
    def post(self, request, *args, **kwargs):
        """
        POST API - This api will first call the serializer to validate the format and type of data passed.
        Once that is valid, it will call a custom validate method to verify all the edge cases.
        If the function returns success, the data will be saved in DB, otherwise and an Error will be raised.
        Error have been logged, where as the end user will get a high level Error Message

        Same function is being used for POST and update both! the URL will contain country_id in case of an update operation.
        :param request:
        :return: 200/400/500 status
        """
        country_id = kwargs.get('id')
        try:
            data = request.data
            serializer = CountrySerializer(data=data)
            if serializer.is_valid():
                data = serializer.data
                if serializer.validate_data(data, country_id):
                    try:
                        if country_id:
                            country_data = Country.objects.get(id=int(country_id))
                            country_data.name=data.get('name')
                            country_data.population=data.get('population')
                            country_data.area=data.get('area')
                            country_data.continent_id=Continent.objects.get(pk=data.get('continent_id'))
                            country_data.no_of_hospital=data.get('no_of_hospital')
                            country_data.no_of_nationalparks=data.get('no_of_nationalparks')
                            country_data.no_of_rivers=data.get('no_of_rivers')
                            country_data.no_of_schools=data.get('no_of_schools')
                            country_data.save()
                        else:
                            country_data = Country(name=data.get('name'),
                                population=data.get('population'), area=data.get('area'),
                                continent_id=Continent.objects.get(pk=data.get('continent_id')),
                                no_of_hospital=data.get('no_of_hospital'), no_of_nationalparks=data.get('no_of_nationalparks'),
                                no_of_rivers=data.get('no_of_rivers'), no_of_schools=data.get('no_of_schools'))
                            country_data.save()
                        return Response(data, status=200)
                    except IntegrityError as err:
                        logger.error('Error: {}'.format(err))
                        return Response({'Error': 'Database Error Found'}, status=400)
                else:
                    logger.error('Error: Data Validation failed | Some of the data from DB mismatches')
                    return Response({'Error': 'Data Validation failed | Some of the data from DB mismatches'}, status=400)
            else:
                logger.error('Error: Validation Error')
                return Response({'Error': 'Validation Error'}, status=500)
        except Exception as ex:
            logger.error('Error: {}'.format(ex))
            return Response({'Error': ex}, status=500)

    def delete(self, request, *args, **kwargs):
        """
        DELETE function for Country model.
        url will contain the country_id, this function will change its is_deleted bit to true.
        """
        country_id = kwargs.get('id')
        try:
            country_data = Country.objects.get(id=int(country_id))
            country_data.is_deleted = True
            country_data.save()
            return Response({'Message': 'Record Deleted'}, status=200)
        except ObjectDoesNotExist as err:
            logger.error('Error: {}'.format(err))
            return Response({'Error': 'Record not found'}, status=400)
        except Exception as ex:
            logger.error('Error: {}'.format(ex))
            return Response({'Error': ex}, status=500)

class CityAddView(APIView):
    """
    View for /city API.
    This view will handle all the Methods, POST/GET...
    For now only POST and DELETE are defined!
    """
    def post(self, request, *args, **kwargs):
        """
        POST API - This api will first call the serializer to validate the format and type of data passed.
        Once that is valid, it will call a custom validate method to verify all the edge cases.
        If the function returns success, the data will be saved in DB, otherwise and an Error will be raised.
        Error have been logged, where as the end user will get a high level Error Message

        Same function is being used for POST and update both! the URL will contain city_id in case of an update operation.
        :param request:
        :return: 200/400/500 status
        """
        city_id = kwargs.get('id')
        try:
            data = request.data
            serializer = CitySerializer(data=data)
            if serializer.is_valid():
                data = serializer.data
                if serializer.validate_data(data, city_id):
                    try:
                        if city_id:
                            city_data = City.objects.get(id=int(city_id))
                            city_data.name=data.get('name')
                            city_data.population=data.get('population')
                            city_data.area=data.get('area')
                            city_data.country_id=Country.objects.get(pk=data.get('country_id'))
                            city_data.no_of_roads=data.get('no_of_roads')
                            city_data.no_of_trees=data.get('no_of_trees')
                            city_data.no_of_shops=data.get('no_of_shops')
                            city_data.no_of_schools=data.get('no_of_schools')
                            city_data.save()
                        else:
                            city_data = City(name=data.get('name'),
                                population=data.get('population'), area=data.get('area'),
                                country_id=Country.objects.get(pk=data.get('country_id')),
                                no_of_roads=data.get('no_of_roads'), no_of_trees=data.get('no_of_trees'),
                                no_of_shops=data.get('no_of_shops'), no_of_schools=data.get('no_of_schools'))
                            city_data.save()
                        return Response(data, status=200)
                    except IntegrityError as err:
                        logger.error('Error: {}'.format(err))
                        return Response({'Error': 'Database Error Found'}, status=400)
                else:
                    logger.error('Error: Data Validation failed | Some of the data from DB mismatches')
                    return Response({'Error': 'Data Validation failed | Some of the data from DB mismatches'}, status=400)
            else:
                logger.error('Error: Validation Error')
                return Response({'Error': 'Validation Error'}, status=500)
        except Exception as ex:
            logger.error('Error: {}'.format(ex))
            return Response({'Error': ex}, status=500)

    def delete(self, request, *args, **kwargs):
        """
        DELETE function for City model.
        url will contain the city_id, this function will change its is_deleted bit to true.
        """
        city_id = kwargs.get('id')
        try:
            city_data = City.objects.get(id=int(city_id))
            city_data.is_deleted = True
            city_data.save()
            return Response({'Message': 'Record Deleted'}, status=200)
        except ObjectDoesNotExist as err:
            logger.error('Error: {}'.format(err))
            return Response({'Error': 'Record not found'}, status=400)
        except Exception as ex:
            logger.error('Error: {}'.format(ex))
            return Response({'Error': ex}, status=500)

class ContinentAddView(APIView):
    """
    View for /city API.
    This view will handle all the Methods, POST/GET...
    For now only POST and DELETE are defined!
    """
    def post(self, request, *args, **kwargs):
        """
        POST API - This api will first call the serializer to validate the format and type of data passed.
        Once that is valid, the data will be saved in DB, otherwise an Error will be raised.
        Error have been logged, where as the end user will get a high level Error Message

        Same function is being used for POST and update both! the URL will contain continent_id in case of an update operation.
        :param request:
        :return: 200/400/500 status
        """
        continent_id = kwargs.get('id')
        # LOGGER.log('info', 'Test log message')
        
        try:
            data = request.data
            serializer = ContinentSerializer(data=data)
            if serializer.is_valid():
                data = serializer.data
                try:
                    if continent_id:
                        continent_data = Continent.objects.get(id=int(continent_id))
                        continent_data.name=data.get('name')
                        continent_data.population=data.get('population')
                        continent_data.area=data.get('area')
                        continent_data.save()
                    else:
                        continent_data = Continent(name=data.get('name'),
                            population=data.get('population'), area=data.get('area'))
                        continent_data.save()
                    return Response(data, status=200)
                except IntegrityError as err:
                    logger.error('Error: {}'.format(err))
                    return Response({'Error': 'Database Error Found'}, status=400)
            else:
                logger.error('Error: Validation Error')
                return Response({'Error': 'Validation Error'}, status=500)
        except Exception as ex:
            logger.error('Error: {}'.format(ex))
            return Response({'Error': ex}, status=500)

    def delete(self, request, *args, **kwargs):
        """
        DELETE function for City model.
        url will contain the city_id, this function will change its is_deleted bit to true.
        """
        continent_id = kwargs.get('id')
        try:
            continent_data = Continent.objects.get(id=int(continent_id))
            continent_data.is_deleted = True
            continent_data.save()
            return Response({'Message': 'Record Deleted'}, status=200)
        except ObjectDoesNotExist as err:
            logger.error('Error: {}'.format(err))
            return Response({'Error': 'Record not found'}, status=400)
        except Exception as ex:
            logger.error('Error: {}'.format(ex))
            return Response({'Error': ex}, status=500)