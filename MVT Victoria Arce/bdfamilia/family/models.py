from django.db import models

class Relative(models.Model):
    name = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    conection = models.CharField(max_length = 20)
    age = models.IntegerField()
    lives_in_bahia = models.BooleanField()
