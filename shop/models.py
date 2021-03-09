from django.db import models

# Create your models here.
class ShopCard(models.Model):
   name = models.CharField(max_length=100)
   slug = models.SlugField(unique=True)
   description = models.TextField(max_length=500)
   price = models.PositiveIntegerField()
   img = models.ImageField()
   def __str__(self):
      return self.name