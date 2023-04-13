
from django.db import models
from datetime import datetime

# Create your models here.
class Drinks(models.Model):
    tag = models.CharField(max_length=30,blank=True)
    name = models.CharField(max_length=100,blank=True)
    price = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    brief = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    name2 = models.CharField(max_length=100,blank=True)
    price2 = models.CharField(max_length=100,blank=True)
    image2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    brief2 = models.CharField(max_length=100, blank=True)
    description2 = models.TextField(blank=True)
    name3 = models.CharField(max_length=100,blank=True)
    price3 = models.CharField(max_length=100,blank=True)
    image3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    brief3 = models.CharField(max_length=100, blank=True)
    description3 = models.TextField(blank=True)
    name4 = models.CharField(max_length=100,blank=True)
    price4 = models.CharField(max_length=100,blank=True)
    image4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    brief4 = models.CharField(max_length=100, blank=True)
    description4 = models.TextField(blank=True)
    postingDate = models.DateTimeField(default=datetime.now, blank=True)
    



    def __str__(self):
        return self.tag