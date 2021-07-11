from django.db import models
from django.db.models.aggregates import Max
from django.db import models

# Create your models here.
class user(models.Model):
    username  = models.CharField(max_length=100)
    password  = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}" 


class account(models.Model):
    username  = models.CharField(max_length=100)
    password  = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}" 