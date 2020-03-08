from datetime import date
import json
from rest_framework import serializers
from .models import Continent
from .models import Country

class CountrySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    population = serializers.CharField(max_length=30)
    area = serializers.IntegerField()
    no_of_hospital = serializers.IntegerField()
    no_of_nationalparks = serializers.IntegerField()
    no_of_rivers = serializers.IntegerField()
    no_of_schools = serializers.IntegerField()
    continent_id = serializers.IntegerField()


    def validate_data(self, data):
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
        return self.validate_population_data(data, continent_data.population, country_data) and\
            self.validate_area_data(data, continent_data.area, country_data)


    def validate_population_data(self, data, continent_population, country_data):
        retValue = False
        population_count = 0
        for item in country_data:
            population_count += int(item.population)
        population_count+= int(data.get('population'))
        if population_count <= int(continent_population):
            retValue = True
        return retValue

    def validate_area_data(self,  data, continent_area, country_data):
        retValue = False
        area_count = 0
        for item in country_data:
            area_count = area_count + item.area
        area_count+= data.get('area')
        if area_count <= continent_area:
            retValue = True
        return retValue