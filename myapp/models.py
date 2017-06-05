from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal
# Create your models here.

class Drugs(models.Model):


    weight = models.IntegerField(default=1, validators=[MinValueValidator(1)], verbose_name='Wybierz masę dziecka (w kg)')
    age = models.IntegerField(default=0, validators=[MinValueValidator(0)],verbose_name='Wybierz wiek dziecka w latach (0 jeśli poniżej roku)')
    drug = models.TextField()
    other_drug = models.TextField(default = 0,verbose_name='Jeśli leku nie ma na liście wpisz dawkę na kg masy ciała')



    class Meta:
        db_table = 'drugs'


class Leki(models.Model):
    nazwa = models.TextField(db_column='Nazwa', blank=True, null=True)
    wiek = models.IntegerField(db_column='Wiek', blank=True, null=True)
    dawka = models.TextField(db_column='Dawka', blank=True, null=True)
    jednostka = models.TextField(db_column='Jednostka')

    class Meta:
        db_table = 'leki'
        managed = False


    def __str__(self):
        return self.nazwa

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

