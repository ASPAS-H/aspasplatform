from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'telaInicial.html')

def viewConsults(request):
    return render(request,'viewConsults.html')

def infoView(request):
    return render(request,'infoView.html')

def registerViewInterpreter(request):
    return render(request,'registerViewInterpreter.html')

