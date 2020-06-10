from django.db import models
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=30)
    article = models.CharField(max_length=10000)
    pub_date = models.DateTimeField(null=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return r'/blog/view/{id}'.format(id=self.id)





