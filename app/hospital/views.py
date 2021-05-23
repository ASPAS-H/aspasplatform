from django.shortcuts import render

# Create your views here.
def hospital_index(request):
    return render(request, "hospital_index.html")
def hospital_informacoes(request):
    return render(request, "hospital_informacoes.html")