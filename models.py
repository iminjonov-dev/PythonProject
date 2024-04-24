from django.db import models
class Bookmodel(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField()
    pages = models.PositiveIntegerField()

    def __str__(self):
        return self.name
# Create your models here.
