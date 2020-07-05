from django.db import models
from realtors.models import Realtor
from datetime import datetime


class Blog(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    title = models.CharField(max_length=500)
    description = models.TextField()
    comments = models.CharField(max_length=500, default='comment')
    tag = models.CharField(max_length=500)
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now, blank=True)
    name= models.CharField(max_length=100,default='name')
    email=models.CharField(max_length=100, default='email')
    def __str__(self):
        return self.title
       