from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return HttpResponse('Você já está logado!')
        
    if request.method == 'GET':
        return render(request, 'login.html')

    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    if user:
        if user.is_active:
            auth_login(request, user)
            return HttpResponse('Bem vindo de volta ' + user.name)
        else:
            return HttpResponse('Sua conta foi inativada!')
    return HttpResponse('Usuario e senha inválidos')


