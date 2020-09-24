from django.db import models
from datetime import datetime
# Create your models here.

class Donors(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    address1 = models.TextField(max_length=80)
    address2 = models.TextField(max_length=80)
    gender = models.CharField(max_length=8)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=10)
    donor_type = models.CharField(max_length=30)
    photo = models.ImageField()
    comment = models.TextField()
    created = models.DateTimeField(default=datetime.now(), blank=True)


    def __str__(self):
        return  self.firstname +' '+ self.lastname
    class Meta:
        verbose_name_plural = 'Donors'

class Beneficiary(models.Model):
    benefactor = models.CharField(max_length=60)
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=255)
    photo = models.ImageField()
    created = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return  self.title
    class Meta:
        verbose_name_plural = 'Beneficiaries'
