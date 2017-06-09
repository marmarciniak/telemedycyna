from django import forms
from .models import *
from easy_select2 import *
from django_select2.forms import *
from django.forms import ModelForm, Textarea

class DrugsForm(forms.ModelForm):

    class Meta:
        model = Drugs
        fields = '__all__'



class DocForm(forms.ModelForm):
    symptoms_choices=(('none','brak'),('kaszel','kaszel'),('biegunka','biegunka'),('wymioty','wymioty'),('zaczerwienione gardło','zaczerwienione gardło'),
                      ('ból ucha','ból ucha'), ('zwiększoneślinienie','zwiększone ślinienie'),('wysypka','wysypka'))
    symptoms = forms.MultipleChoiceField(choices= symptoms_choices)
    class Meta:
        model = Doctor
        fields = '__all__'

class InfoForm(forms.ModelForm):

    class Meta:
        model = BabyInfo
        fields = '__all__'

class ContactForm(forms.ModelForm):

    doctor_choices = (('marek.kowalski', 'dr Marek Kowalskii'),('aneta.nowak','dr Aneta Nowak'),('olaf.kos','dr Olaf Kos'))
    doctor_choice = forms.ChoiceField(choices = doctor_choices, label = 'Wybierz lekarza')
    class Meta:
        model = DoctorContatct
        fields = '__all__'

