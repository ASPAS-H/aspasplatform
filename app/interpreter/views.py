from surdo.models import RejectedConsults
from django.http import request
from account.models import User
from surdo.models import Consult
from django.shortcuts import render
from surdo.services import DeafService
from .forms import NewInterpreter
from account.forms import NewUserForm
from address.forms import AddressForm
from .services import InterpreterService
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
import logging
logger = logging.getLogger(__name__)
#Create your views here.

@login_required(redirect_field_name='', login_url='/account/login')
def solicitationView(request):
    consults = DeafService.getPendingConsultsForInterpreter(request.user.id)
    return render(request,'solicitationView.html', {'consults':consults})


@login_required(redirect_field_name='', login_url='/account/login')
def infoSolicitationView(request,id):
    consult = DeafService.getConsult(id)
    return render(request,'infoSolicitationView.html', {'consult':consult})


@login_required(redirect_field_name='', login_url='/account/login')
def index(request):
    return render(request,'telaInicial.html')


@login_required(redirect_field_name='', login_url='/account/login')
def viewConsults(request):
    consults = DeafService.getInterpreterConsults(InterpreterService.getInterpreter(request.user.id))
    return render(request,'viewConsults.html', {'consults':consults})


def registerViewInterpreter(request):
    interpreter = None
    if request.method == 'POST':
        userForm = NewUserForm(request.POST)
        interpreterForm = NewInterpreter(request.POST)
        addressForm = AddressForm(request.POST)

        if userForm.is_valid() and interpreterForm.is_valid() and addressForm.is_valid():
            address = addressForm.save(commit=False)
            address.country = 'BR'
            address.save()

            user = userForm.save(commit=False)
            user.user_type = 1
            user.address = address
            user.password = make_password(request.POST['password'])
            user.save()

            interpreter = interpreterForm.save(commit=False)
            interpreter.address = address
            interpreter.cash = 0
            interpreter.user = user
            interpreter.save()
            return render(request, 'interpreterStatus.html',{'messages':'Conta Criada com Sucesso'})

        else:
            errors = [userForm.errors, addressForm.errors,interpreterForm.errors]

            return render(request, 'registerViewInterpreter.html', {'errors': errors})

    return render(request,'registerViewInterpreter.html')


@login_required(redirect_field_name='', login_url='/account/login')
def paymentView(request):
    return render(request,'paymentView.html')


@login_required(redirect_field_name='', login_url='/account/login')
def updateAcceptConsult(request,id):
    consult = DeafService.getConsult(id)

    consult.status = 2
    consult.interpreter = InterpreterService.getInterpreter(request.user.id)
    
    consult.save()

    consults = DeafService.getPendingConsults()
    return render(request,'solicitationView.html', {'consults':consults})


@login_required(redirect_field_name='', login_url='/account/login')
def markOffConsult(request,id):
    consult = DeafService.getConsult(id)
    consult.status = 1
    consult.interpreter = None

    consult.save()

    consults = DeafService.getInterpreterConsults(InterpreterService.getInterpreter(request.user.id))
    return render(request,'viewConsults.html', {'consults':consults})


@login_required(redirect_field_name='', login_url='/account/login')
def infoDatesView(request,id):
    consult = DeafService.getConsult(id)
    return render(request,'infoDatesView.html', {'consult':consult})


def addRejectConsult(request,id):
    
    
    consults = DeafService.getPendingConsults()

    rejectConsult = RejectedConsults()
    rejectConsult.interpreter = InterpreterService.getInterpreter(request.user.id)
    rejectConsult.consult = DeafService.getConsult(id)
    rejectConsult.save()

    return render(request,'solicitationView.html', {'consults':consults})