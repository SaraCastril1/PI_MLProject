from queue import PriorityQueue
from django.db import models
from platform import architecture

# Create your models here.

class mlModels(models.Model):
   tittle = models.CharField(max_length=50)
   description = models.CharField(max_length=250)
   architecture = models.FileField(upload_to= 'ml_models/') #json file
   weights = models.FileField(upload_to= 'ml_models/') #h5 file
   priority = models.PositiveSmallIntegerField(null = True)