from django.db import models

# Create your models here.

class User(models.Model):
    user = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length = 8)
    privilege = models.IntegerField(default = 3)

