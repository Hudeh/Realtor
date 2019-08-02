from django.db import models
from datetime import datetime

class Newsletter(models.Model):
    newsemail = models.CharField(max_length=50)
    def __str__(self):
        return self.newsemail

class Blogs(models.Model):
    title= models.CharField(max_length=100)
    description= models.TextField()
    author= models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now, blank=True)
    photo= models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.title