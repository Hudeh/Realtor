from django.db import models


class Newsletter(models.Model):
    newsemail = models.CharField(max_length=50)
    def __str__(self):
        return self.newsemail

