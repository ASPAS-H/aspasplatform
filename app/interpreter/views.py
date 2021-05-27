from django.shortcuts import render, get_object_or_404
from surdo.services import DeafService
#Create your views here.

def solicitationView(request):
    consults = DeafService.getPendingConsults()
    return render(request,'solicitationView.html', {'consults':consults})

def infoSolicitationView(request,id): #
    #consult = get_object_or_404(consult, pk=id)
    #consult = DeafService.getConsults(id)
    return render(request,'infoSolicitationView.html')#, {'consults':consult})

def index(request):
    return render(request,'telaInicial.html')

def viewConsults(request):
    return render(request,'viewConsults.html')

def registerViewInterpreter(request):
    return render(request,'registerViewInterpreter.html')

def datesView(request):
    return render(request,'datesView.html')

def infoDatesView(request):
    return render(request,'infoDatesView.html')



