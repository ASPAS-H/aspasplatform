from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect
# Create your views here.

def login(request):
    if request.user.is_authenticated:
        # REDIRECIONAR PARA TELA DE LOGADO
        redirectLink = {
            0:  '/surdo',
            1: '/interpreter',
            2: '/hospital',
        }
        redirectTo = redirectLink.get(request.user.user_type, '/account/error')
        return redirect(redirectTo)
    if request.method == 'GET':
        return render(request, 'login.html')

    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    if user:
        if user.is_active:
            auth_login(request, user)
            return redirect('/surdo')
        else:
            loginError = "Sua conta está inativa!"
            return render(request, 'login.html', { 'error': loginError})
    loginError = "Usuário ou senha inválidos"
    return render(request, 'login.html', { 'error': loginError})
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('/account/login')
def error(request):
    return render(request, 'error.html')


