from django.db import models
from datetime import datetime

# Create your models here.
class Register(models.Model):
    firstname = models.CharField(max_length=100,blank=True)
    lastname = models.CharField(max_length=100,blank=True)
    email = models.CharField(max_length=100,blank=True)
    password = models.CharField(max_length=100,blank=True)
    password2 = models.CharField(max_length=100, blank=True)
    postingDate = models.DateTimeField(default=datetime.now, blank=True)
    

    def __init__(self):
        return self.email

