from django.db import models

# Create your models here.

class Debit(models.Model):
    name = models.CharField(max_length=300)
    date = models.DateTimeField('date of receipt', blank=True, null=True)
    amount = models.FloatField(default=0)
    category = models.CharField(max_length=300)

class Credit(models.Model):
    name = models.CharField(max_length=300)
    date = models.DateTimeField('date received', blank=True, null=True)
    amount = models.FloatField(default=0)
    source = models.CharField(max_length=300)