from django.shortcuts import render

# Create your views here.

def showIndex(request):
    return render(request, "hospital_index.html")

def showInfo(request):
    return render(request, "hospital_info.html")

def showTest(request):
    return render(request, "hospital_new.html")