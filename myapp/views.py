
from django.template.response import TemplateResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from myapp.models import *
from django.http import HttpResponseRedirect
from myapp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.core.mail import send_mail
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
@login_required(login_url='http://127.0.0.1:8000/signup/')
def info(request):

    baby_f = BabyInfo()
    form = InfoForm(request.POST or None, instance = baby_f)

    if form.is_valid():
        baby_f = form.save(commit=False)
        baby_f.user = request.user
        baby_f.save()
        return redirect(main_info)

    ctx = {'form': form, 'InfoForm': InfoForm}
    return TemplateResponse(request, 'info.html', ctx)

@login_required(login_url='http://127.0.0.1:8000/signup/')
def doc_cont(request):
    contact_f = DoctorContatct()
    form = ContactForm(request.POST or None, instance = contact_f)

    if form.is_valid():
        contact_f = form.save(commit = False)
        contact_f.user = request.user
        contact_f.save()
        return redirect(main_contact)

    ctx = {'form' : form, 'ContactForm' : ContactForm}
    return TemplateResponse(request, 'contact.html',ctx)

def main_contact(request):
    objectslist = DoctorContatct.objects.all()
    number = len(objectslist) - 1
    user = str(objectslist[number].user)
    subject = 'Mail from: ' + user
    message = str(objectslist[number].description)
    sent_to = str(objectslist[number].doctor_choice) + '@example.com'

    #send_mail(subject,message,(user + '@example.com'),[sent_to])

    return render(request, 'mail_send.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    return TemplateResponse(request, 'mainp.html')

def main_info(request):


    return render(request, 'formsave.html')
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
        if fever >=38:
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

def profil(request):

    babies = BabyInfo.objects.filter(user=request.user)
    messages = DoctorContatct.objects.filter(user=request.user)
    context = {"babies":babies,"messages":messages}


    return render(request,"profile.html", context)

def auth_logout(request):
  logout(request)
  return redirect('home')
