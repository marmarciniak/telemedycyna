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

def doctor(request):
    doctor_f = Doctor()
    form = DocForm(request.POST or None, instance = doctor_f)

    if form.is_valid():
        doctor_f = form.save()
        return redirect(main_doc)

    ctx = {'form': form, 'DocForm': DocForm}
    return TemplateResponse(request, 'doctor.html', ctx)

def home(request):
    return TemplateResponse(request, 'mainp.html')

def main(request):
    return render(request, 'base.html')
def main_drug(request):

    objectslist = Drugs.objects.all()
    number= len(objectslist) - 1
    weight = int(objectslist[number].weight)
    dose = (objectslist[number].other_drug)
    warning ='Przed podaniem upewnij się czy lek jest odpowiedni dla dzieci w tym wieku'
    drug_dose = int(dose)*int(weight)


    return render(request, "calculate.html", {'drug_dose':drug_dose, 'warning':warning})

def main_doc(request):
    objectslist = Doctor.objects.all()
    number =  len(objectslist) - 1
    age = int(objectslist[number].age)
    fever = float(objectslist[number].fever)
    symptoms = str(objectslist[number].symptoms)
    #age category
    if age<6:
        age_cat = 1
    elif age <=12:
        age_cat = 2

    #36-37 no symptoms cat 1
    if symptoms == 'none':
        if fever<37 :
            fev_cat = 1
        #37-37,5 no symptoms cat 2
        if fever >= 37 and fever <37.5:
            fev_cat = 2
        #37,5-38 no symptoms cat 3
        if fever >= 37.5 and fever <38:
            fev_cat = 3
        #38-38,5 no symptoms cat 4
        if fever >= 38 and fever <38.5:
            fev_cat = 4
        #38,5-39 no symptoms cat 5
        if fever >= 38.5 and fever <39:
            fev_cat = 5
        #39-40 no symptoms cat6
        if fever >=39:
            fev_cat = 6
    else:
        if fever < 38:
            fev_cat = 7
        if fever >38:
            fev_cat = 8

    base = Fever.objects.all()
    for i in range(len(base)):
        if fev_cat < 7:
            if age_cat == base[i].kategoria_wiek and fev_cat == base[i].kategoria_goraczka:
                recommend = base[i].zalecenia
                break
        else:
            if age_cat == base[i].kategoria_wiek and fev_cat == base[i].kategoria_goraczka and symptoms == base[i].objawy:
                recommend = base[i].zalecenia
                break

    return render(request, "doctor_recommendation.html", {'recommendation': recommend})


