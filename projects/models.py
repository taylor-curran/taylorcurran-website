from django.db import models

# Create your models here.
# Each Row is an Object of the Class  

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=30)
    image = models.FilePathField(path="/projects/img")