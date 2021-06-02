from django.shortcuts import render, get_object_or_404
from surdo.services import DeafService
#Create your views here.

def solicitationView(request):
    consults = DeafService.getPendingConsults()
    return render(request,'solicitationView.html', {'consults':consults})

def infoSolicitationView(request,id):
    consult = DeafService.getConsult(id)
    return render(request,'infoSolicitationView.html', {'consult':consult})

def index(request):
    return render(request,'telaInicial.html')

def viewConsults(request):
    return render(request,'viewConsults.html')

def registerViewInterpreter(request):
    return render(request,'registerViewInterpreter.html')

def paymentView(request):
    return render(request,'paymentView.html')

def infoDatesView(request,id):
    consult = DeafService.getConsult(id)
    return render(request,'infoDatesView.html', {'consult':consult})



