from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewDeafForm
from address.forms import AddressForm
from account.forms import NewUserForm
from django.contrib.auth.hashers import make_password

def login(request):
    if(request.method != 'POST'):
        return render(request, 'auth/login.html')

def showIndex(request):
    return render(request, 'deaf_index.html')

def showConsults(request):
    return render(request, 'deaf_consults.html')

def showMap(request):
    return render(request, 'deaf_hospitals.html')

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
                return HttpResponse('Registrado!')
        else:
            errors = [userForm.errors, address_form.errors, deaf_form.errors]
            return render(request, 'deaf_register.html', {'errors': errors})
    return render(request, 'deaf_register.html')