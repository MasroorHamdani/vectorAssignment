from django.db import models

class Continent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    population = models.CharField(max_length=30)
    area = models.IntegerField()

    class Meta: 
        ordering = ['name']

    # def __str__(self):
    #     return f'{self.name}'

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    population = models.CharField(max_length=30)
    area = models.IntegerField()
    continent_id = models.ForeignKey(Continent, on_delete=models.CASCADE)
    no_of_hospital = models.IntegerField()
    no_of_nationalparks = models.IntegerField()
    no_of_rivers = models.IntegerField()
    no_of_schools = models.IntegerField()

    # Metadata
    class Meta: 
        ordering = ['name']

    # def __str__(self):
    #     return f'{self.name}'

class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    population = models.CharField(max_length=30)
    area = models.IntegerField()
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    no_of_roads = models.IntegerField()
    no_of_trees = models.IntegerField()
    no_of_shops = models.IntegerField()
    no_of_schools = models.IntegerField()

    # Metadata
    class Meta: 
        ordering = ['name']

    # def __str__(self):
    #     return f'{self.name}'