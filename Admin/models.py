from django.db import models

# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=25)
class Adminreg(models.Model):
    name=models.CharField(max_length=25)
    contact=models.IntegerField(max_length=20)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=25)

