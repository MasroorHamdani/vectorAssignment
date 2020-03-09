from datetime import date
import json
from rest_framework import serializers
from .models import Country, City, Continent

class CountrySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    population = serializers.CharField(max_length=30)
    area = serializers.IntegerField()
    no_of_hospital = serializers.IntegerField()
    no_of_nationalparks = serializers.IntegerField()
    no_of_rivers = serializers.IntegerField()
    no_of_schools = serializers.IntegerField()
    continent_id = serializers.IntegerField()


    def validate_data(self, data, country_id):
        """
        This function will internally calls other small functions to validate the data passed
        All the validations like,
        total population of countries being part of a continent should be in 
        range of the population defined for that continent.
        Also the Area for all countries should fall in the range of area defined for the continent.

        Unique constraint is taked care by DB, where name is defined as unique.
        """
        continent_data = Continent.objects.get(pk=data.get('continent_id'))
        country_data = Country.objects.filter(continent_id=data.get('continent_id'))
        return self.validate_population_data(data, continent_data.population, country_data, country_id) and\
            self.validate_area_data(data, continent_data.area, country_data, country_id)


    def validate_population_data(self, data, continent_population, country_data, country_id=''):
        retValue = False
        population_count = self.valid_search(data, country_data, 'population', country_id)
        if population_count <= int(continent_population):
            retValue = True
        return retValue

    def validate_area_data(self, data, continent_area, country_data, country_id=''):
        retValue = False
        area_count = self.valid_search(data, country_data, 'area', country_id)
        if area_count <= continent_area:
            retValue = True
        return retValue

    def valid_search(self, passed_data, data, entity, id=''):
        count = 0
        for item in data:
            if not id:
                count = count + int(getattr(item, entity))
            elif id and item.id != int(id):
                count = count + int(getattr(item, entity))
        count+= int(passed_data.get(entity))
        return count

class CitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    population = serializers.CharField(max_length=30)
    area = serializers.IntegerField()
    no_of_roads = serializers.IntegerField()
    no_of_trees = serializers.IntegerField()
    no_of_shops = serializers.IntegerField()
    no_of_schools = serializers.IntegerField()
    country_id = serializers.IntegerField()


    def validate_data(self, data, city_id):
        """
        This function will internally calls other small functions to validate the data passed
        All the validations like,
        total population of countries being part of a continent should be in 
        range of the population defined for that continent.
        Also the Area for all countries should fall in the range of area defined for the continent.

        Unique constraint is taked care by DB, where name is defined as unique.
        """
        country_data = Country.objects.get(pk=data.get('country_id'))
        city_data = City.objects.filter(country_id=data.get('country_id'))
        return self.validate_population_data(data, country_data.population, city_data, city_id) and\
            self.validate_area_data(data, country_data.area, city_data, city_id) and\
            self.validate_school_data(data, country_data.no_of_schools, city_data, city_id)


    def validate_population_data(self, data, country_population, city_data, city_id=''):
        retValue = False
        population_count = 0
        population_count = self.valid_search(data, city_data, 'population', city_id)
        if population_count <= int(country_population):
            retValue = True
        return retValue

    def validate_area_data(self,  data, country_area, city_data, city_id=''):
        retValue = False
        area_count = 0
        area_count = self.valid_search(data, city_data, 'area', city_id)
        if area_count <= country_area:
            retValue = True
        return retValue

    def validate_school_data(self,  data, country_school, city_data, city_id=''):
        retValue = False
        school_count = 0
        school_count = self.valid_search(data, city_data, 'no_of_schools', city_id)
        if school_count <= country_school:
            retValue = True
        return retValue
    
    def valid_search(self, passed_data, data, entity, id=''):
        count = 0
        for item in data:
            if not id:
                count = count + int(getattr(item, entity))
            elif id and item.id != int(id):
                count = count + int(getattr(item, entity))
        count+= int(passed_data.get(entity))
        return count


class ContinentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    population = serializers.CharField(max_length=30)
    area = serializers.IntegerField()