from django.db import models

# Create your models here.
class Weather(models.Model):
    reporter = models.CharField(max_length= 20)


    def __str__(self):
        return self.reporter