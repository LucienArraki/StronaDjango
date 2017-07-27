from django.db import models

# Create your models here.

class information(models.Model):
    animalName = models.CharField(max_length=120)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

    def __unicode__(self):
        return self.animalName

    def __str__(self):
        return  self.animalName