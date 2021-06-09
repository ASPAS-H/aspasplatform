from django.shortcuts import render
from surdo.services import DeafService

# Create your views here.

def showIndex(request):
    return render(request, "hospital_index.html")
<<<<<<< HEAD
def hospital_informacoes(request):
    return render(request, "hospital_informacoes.html")
def hospital_consultas(request):
    consults = DeafService.get_hospitals_consults(1)
    return render(request, "hospital_consultas.html", {"consults": consults})
=======

def showInfo(request):
    return render(request, "hospital_info.html")

def showTest(request):
    return render(request, "hospital_new.html")
>>>>>>> 5bbf7e0380d97804437e603abc406541ad6bd345
