from django import forms
from .models import *
from easy_select2 import *
from django_select2.forms import *

class DrugsForm(forms.ModelForm):
    drug = forms.ModelChoiceField(queryset=Leki.objects.all())


    class Meta:
        model = Drugs
        widgets = { 'field': apply_select2(forms.Select)}
        fields = '__all__'



class DocForm(forms.ModelForm):
    symptoms_choices=(('fever','kaszel'),('diarrhea','biegunka'),('vomit','wymioty'))
    symptoms = forms.ChoiceField(choices= symptoms_choices, label='Symptomy ')
    class Meta:
        model = Doctor
        fields = '__all__'

