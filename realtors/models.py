from django.db import models


class Realtor(models.Model):
	name =  models.CharField(max_length=200)
	photo = models.ImageField(upload_to='photos/%y/%M/%d/')
	description = models.CharField(max_length=2000, blank=True)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	is_mvp = models.BooleanField(default=False)
	def __str__(self):
		return self.name