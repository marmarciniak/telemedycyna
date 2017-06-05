from django import forms
from .models import *
from easy_select2 import *
from django_select2.forms import *

class DrugsForm(forms.ModelForm):

    class Meta:
        model = Drugs
        fields = '__all__'



class DocForm(forms.ModelForm):
    symptoms_choices=(('none','brak'),('kaszel','kaszel'),('biegunka','biegunka'),('wymioty','wymioty'),('zaczerwienione gardło','zaczerwienione gardło'),
                      ('ból ucha','ból ucha'), ('zwiększone ślinienie','zwiększone ślinienie'),('wysypka','wysypka'))
    symptoms = forms.ChoiceField(choices= symptoms_choices, label='Symptomy ')
    class Meta:
        model = Doctor
        fields = '__all__'

