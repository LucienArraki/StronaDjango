from django.db import models
from django.contrib import admin

# Create your models here.


class Animal_type(models.Model):
    type = models.CharField(max_length=120)

    def __unicode__(self):
        return self.type

    def __str__(self):
        return  self.type

    def __eq__(self, other):
        return str(self) == str(other)

class Animal_category(models.Model):
    animal_type = models.ForeignKey(Animal_type)
    animal_category = models.CharField(max_length=120)
    start_date = models.DateField()
    endDate = models.DateField()

    def __unicode__(self):
        return self.animal_category

    def __str__(self):
        return  self.animal_category

    def __eq__(self, other):
        return str(self) == str(other)