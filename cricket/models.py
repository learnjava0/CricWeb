from django.db import models

# Create your models here.
class Contact (models.Model):
    name = models.CharField( max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)






        