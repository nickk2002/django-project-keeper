from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=120, blank=True)
    image = models.ImageField(null=True)
    data = models.DateField(blank=False, null=10/20/2009)
    objects = models.Manager()
