from django.contrib import admin
from myapp.models import Drugs
import myapp.models
from django.forms import TextInput, Textarea
from django.db import models

admin.site.register(myapp.models.Drugs)
admin.site.register(myapp.models.Doctor)
admin.site.register(myapp.models.Fever)
admin.site.register(myapp.models.BabyInfo)
admin.site.register(myapp.models.DoctorContatct)

class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'10'})},
        models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols':1})},
    }
