from django import forms
from django.db import models
from unicodedata import name
# Create your models here.


class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=100)


class Menu(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(
        MenuCategory, on_delete=models.PROTECT, default=None, related_name='category_name')
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.name + " : " + self.type


class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    time_log = models.TimeField(help_text="Enter exact time")


class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField("Phone Number", max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name
