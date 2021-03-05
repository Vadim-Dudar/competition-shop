from django.apps import AppConfig
from django.db import models

class Person(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.TextField()
    price = models.CharField(max_length=5)
    photo = models.ImageField(upload_to='shop/img/')
    def __str__(self):
        return self.title