from django.db import models

# Create your models here.


class AlgoForm(models.Model):
    name = models.CharField(null=True, max_length=128, blank=True, default=None)
    email = models.CharField(null=True, max_length=128, blank=True, default=None)
    phone = models.CharField(null=True, max_length=128, blank=True, default=None)
    city = models.CharField(null=True, max_length=128, blank=True, default=None)
    state = models.CharField(null=True, max_length=128, blank=True, default=None)