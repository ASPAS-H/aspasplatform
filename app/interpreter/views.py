from django.shortcuts import render, get_object_or_404
#from .models import Consult
# Create your views here.

def solicitationView(request):
    #consults = Consult.objects.all()
    return render(request,'solicitationView.html')#, {'consults':consults})

def infoConsultsView(request): #id
    #consult = get_object_or_404(Consult, pk=id)
    return render(request,'infoConsultsView.html')#, {'consult':consult})

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



