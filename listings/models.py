from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
	realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
	title = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	zip_code = models.CharField(max_length=20)
	description = models.TextField(blank=True)
	bedrooms = models.IntegerField()
	bathrooms = models.IntegerField()
	price = models.IntegerField()
	garage = models.IntegerField()
	sqft = models.IntegerField()
	locations = models.CharField(max_length=50)
	photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
	photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	is_published = models.BooleanField(default=True)
	list_date = models.DateField(default=datetime.now, blank=True)

	def __str__(self):
		return self.title
