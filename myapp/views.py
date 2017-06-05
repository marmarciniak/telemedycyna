from django.shortcuts import redirect
from django.template.response import TemplateResponse


from django.shortcuts import render
from myapp.models import *
from myapp.forms import *


def lek(request):
    drugs_f = Drugs()
    form = DrugsForm(request.POST or None, instance = drugs_f)

    if form.is_valid():
        drugs_f = form.save()
        return redirect(main_drug)

    ctx = {'form': form, 'DrugsForm': DrugsForm}
    return TemplateResponse(request, 'drugs.html', ctx)

def home(request):
    return TemplateResponse(request, 'mainp.html')

def main(request):
    return render(request, 'base.html')
def main_drug(request):

    objectslist = Drugs.objects.all()
    number= len(objectslist) - 1
    weight = int(objectslist[number].weight)
    age = int(objectslist[number].age)
    drug = str(objectslist[number].drug)
    other_drug = (objectslist[number].other_drug)

    dose_table=[]
    if drug !='inny':
        base = Leki.objects.all()
        for i in range(len(base)):
            if base[i].nazwa == drug:
                dose_table.append(base[i].dawka)
                dose_table.append(base[i].wiek)
                dose_table.append(base[i].jednostka)
                break
    else:
        dose_table.append(other_drug)
        dose_table.append('Przed podaniem upewnij się czy lek jest odpowiedni dla dzieci w tym wieku')
        dose_table.append('ml/mg')

    dose = dose_table[0]
    age_for_drug = dose_table[1]
    jednostka = dose_table[2]
    if str(type(age_for_drug))== "<class 'str'>":
        drug_dose = int(dose)*int(weight)
        warning = age_for_drug
    elif age<age_for_drug:
        drug_dose = 'Dziecko może być za małe aby podać mu ten lek. Proszę skonsultować się z lekarzem lub farmaceutą'
        warning = ''
    else:
        drug_dose = int(dose)*int(weight)
        warning = ''
    return render(request, "calculate.html", {'drug_dose':drug_dose, 'warning':warning, 'jednostka':jednostka})

def doktor(request):
    doc_f = Doctor()
    form = DocForm(request.POST or None, instance = doc_f)

    if form.is_valid():
        doc_f = form.save()
        return redirect(main)

    ctx = {'form': form, 'DrugsForm': DrugsForm}
    return TemplateResponse(request, 'doctor.html', ctx)
