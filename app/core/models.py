from django.db import models  # noqa


# Create your models here.

class Sample(models.Model):
    attachment = models.FileField()
