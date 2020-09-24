from django.db import models
from datetime import datetime


class Faq(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Guideline'


class NigerianCases(models.Model):
    states = models.CharField(max_length=20)
    total_cases = models.CharField(max_length=250)
    active_cases = models.CharField(max_length=250)
    discharged = models.CharField(max_length=250)
    death_cases = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=datetime.now())

    def __str__(self):
        return self.states

    class Meta:
        verbose_name_plural = 'Cases'


class GlobalCases(models.Model):
    country = models.CharField(max_length=40, )
    country_total_cases = models.CharField(max_length=60, )
    country_recovery = models.CharField(max_length=60, )
    country_total_deaths = models.CharField(max_length=60, )
    date_added = models.DateTimeField(auto_now_add=datetime.now())

    def __str__(self):
        return self.country

    class Meta:
        verbose_name_plural = 'Global Cases'


class GlobalTotalCases(models.Model):
    global_total_cases = models.CharField(max_length=40)
    global_total_recovery = models.CharField(max_length=40)
    global_total_deaths = models.CharField(max_length=40)

    def __str__(self):
        return 'TOTAL GLOBAL RECORD'

    class Meta:
        verbose_name_plural = 'TOTAL GLOBAL RECORD'


class NigeriaTotalCases(models.Model):
    nigeria_total_cases = models.CharField(max_length=40)
    nigeria_active_cases = models.CharField(max_length=40)
    nigeria_total_discharge = models.CharField(max_length=40)
    nigeria_total_deaths = models.CharField(max_length=40)
    updated_on = models.DateTimeField(auto_now=datetime.now())

    def __str__(self):
        return 'TOTAL NIGERIA RECORD'

    class Meta:
        verbose_name_plural = 'TOTAL NIGERIA RECORD'
