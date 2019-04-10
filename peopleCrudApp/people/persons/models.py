from django.db import models

class Person(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    birthday = models.DateField()
    zipcode = models.CharField(max_length=10)

