from django.db import models

class user(models.Model):
    id1=models.IntegerField()
    password=models.CharField(max_length=20)



# Create your models here.
