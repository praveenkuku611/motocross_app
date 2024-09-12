from django.db import models

class Employee(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length = 100)


