from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewDeafForm
from address.forms import AddressForm

def create(request):
    deaf = None
    if(request.method == 'POST'):
        form = NewDeafForm(request.POST)
        address_form = AddressForm(request.POST)
        address_form.country = "BR"
        address = address_form.save()
        if form.is_valid():
            deaf = form.save(commit=False)
            deaf.address = address
            deaf.save()
            return HttpResponse('Ola')
        else:
            return render(request, 'auth/register.html', {'form': form, 'deaf': 'error'})
    
    form = NewDeafForm()
    return render(request, 'auth/register.html', {'form': form, 'deaf': deaf})

def login(request):
    if(request.method != 'POST'):
        return render(request, 'auth/login.html')
