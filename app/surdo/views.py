from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewDeafForm
from address.forms import AddressForm
from account.forms import NewUserForm
from hospital.services import HospitalService
from .services import DeafService
from .forms import ConsultForm
from address.services import AddressService
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, date

import logging
logger = logging.getLogger(__name__)

def login(request):
    return render(request, 'auth/login.html')


@login_required(redirect_field_name='', login_url='/account/login')
def showIndex(request):
    return render(request, 'deaf_index.html')

def showMap(request):
    hospitals = AddressService.get_nearby_hospitals(request.user.address.id)
    return render(request, 'deaf_hospitals.html', {"hospitals": hospitals})

def showStatus(request):
    return render(request,'deaf_status.html',{'messages':'Hello world!'})

def showRegister(request):
    deaf = None
    if(request.method == 'POST'):
        userForm = NewUserForm(request.POST)
        deaf_form = NewDeafForm(request.POST)
        address_form = AddressForm(request.POST)
        if userForm.is_valid() and deaf_form.is_valid() and address_form.is_valid():
                address = address_form.save(commit=False)
                address.country = "BR"
                address.save()

                user = userForm.save(commit=False)
                user.address = address
                user.password = make_password(request.POST["password"])
                user.save()

                deaf = deaf_form.save(commit=False)
                deaf.address = address
                deaf.user = user
                deaf.save()
                return render(request, 'deaf_status.html', {'messages':'Sua conta foi registrada com sucesso.'})
        else:
            errors = [userForm.errors, address_form.errors, deaf_form.errors]
            return render(request, 'deaf_register.html', {'errors': errors})
    return render(request, 'deaf_register.html')

def newConsult(request):
    if request.method == "POST":
        consult_data = ConsultForm(request.POST)
        if consult_data.is_valid():
            consult = DeafService.createConsult(request.POST, request.user)
            return render(request, 'deaf_status.html', {'messages':'Consulta criada com sucesso [ID: ' + str(consult.id) + ']'})
        else:
            hospitals = AddressService.get_nearby_hospitals(request.user.address.id)
            return render(request, 'deaf_newconsults.html', {"hospitals": hospitals, "errors": consult_data.errors})

    hospitals = AddressService.get_nearby_hospitals(request.user.address.id)
    return render(request, 'deaf_newconsults.html', {"hospitals": hospitals})

def view_consults(request):
    consults = DeafService.getConsults(request.user)
    return render(request, 'deaf_consults.html', {"consults": consults})

def view_consult(request, consult_id):
    consult = DeafService.getConsult(consult_id)
    return render(request, 'deaf_consult.html', {"consult": consult})

def cancel_consult(request, consult_id):
    consult = DeafService.getConsult(consult_id)

    date = consult.confirmed_date

    if consult.status == 4:
        return render(request, 'deaf_consult.html', {"consult": consult, "error": "Está cosulta já esta cancelada"})

    if date == None:
        return render(request, 'deaf_consult.html', {"consult": consult, "error": "Está cosulta ainda não foi agendada"})
    
    maxDateToCancel = date - timedelta(days=1)
    
    logger.error(str(date.today()))
    if date.today() >= maxDateToCancel:
        return render(request, 'deaf_consult.html', {"consult": consult, "error": "O prazo para cancelamento são 2 dias antes da consulta"})
    
    if request.user.id != consult.user.id:
        return render(request, 'deaf_consult.html', {"consult": consult, "error": "Você não é o paciente desta consulta"}) 
    
    consult = DeafService.change_consult_status(consult.id, 4)
    return render(request, 'deaf_consult.html', {"consult": consult, "success": "Consulta cancelada com sucesso!"})

def newConsultWithHospital(request, hospital_id):
    hospitals = AddressService.get_nearby_hospitals(request.user.address.id)
    return render(request, 'deaf_newconsults.html', {"hospitals": hospitals, "hospital_id": hospital_id})