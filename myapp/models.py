from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Drugs(models.Model):

    weight = models.IntegerField(default=1, validators=[MinValueValidator(1)], verbose_name='Wybierz masę dziecka (w kg)')
    other_drug = models.TextField(default = 0,verbose_name='Jeśli leku nie ma na liście wpisz dawkę na kg masy ciała')


    class Meta:
        db_table = 'drugs'


class Doctor(models.Model):
    age = models.IntegerField(default=0, validators=[MinValueValidator(0)],verbose_name='Wybierz wiek dziecka w miesiącach ')
    fever=models.DecimalField(max_digits = 3, decimal_places = 1, verbose_name = 'Podaj temperature dziecka')
    symptoms=models.TextField()

class Fever(models.Model):
    kategoria_wiek = models.IntegerField()
    dolny = models.DecimalField(max_digits=3, decimal_places = 1)
    gorny = models.DecimalField(max_digits=3, decimal_places = 1)
    kategoria_goraczka = models.IntegerField()
    objawy = models.TextField()
    zalecenia = models.TextField()

    class Meta:
        db_table = 'fever'
        managed = False

class BabyInfo(models.Model):


    baby_name = models.TextField()
    weight = models.IntegerField()
    age = models.DateField( default=datetime.now)
    user = models.ForeignKey(to = User, related_name='baby_f', blank=True,null=True)


class DoctorContatct(models.Model):
    doctor_choice= models.TextField()
    description = models.TextField()
    user = models.ForeignKey(to = User, related_name='contact_f', blank=True,null=True)

