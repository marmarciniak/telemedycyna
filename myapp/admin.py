from django.contrib import admin
from myapp.models import Drugs
import myapp.models
from easy_select2 import select2_modelform
from .forms import DrugsForm

# Register your models here.

DrugForm= select2_modelform(Drugs, attrs={'width': '250px'})
class DrugAdmin(admin.ModelAdmin):
    form = DrugForm

admin.site.register(myapp.models.Leki)
admin.site.register(myapp.models.Drugs)
admin.site.register(myapp.models.Doctor)
admin.site.register(myapp.models.Fever)