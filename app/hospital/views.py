from django.shortcuts import render
from surdo.services import DeafService

# Create your views here.
def hospital_index(request):
    return render(request, "hospital_index.html")
def hospital_informacoes(request):
    return render(request, "hospital_informacoes.html")
def hospital_consultas(request):
    consults = DeafService.get_hospitals_consults(1)
    return render(request, "hospital_consultas.html", {"consults": consults})