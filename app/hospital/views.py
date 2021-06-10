from django.shortcuts import render
from surdo.services import DeafService
from .services import HospitalService

# Create your views here.

def showIndex(request):
    return render(request, "hospital_index.html")

def showConsults(request):
    consults = HospitalService.get_pending_consults_from_hospital(2)
    return render(request, "hospital_consults.html", {"consults": consults})

def showInfo(request):
    return render(request, "hospital_info.html")

def showTest(request):
    return render(request, "hospital_new.html")

def showPatientDetails(request):
    return render(request, "hospital_patient.html")

def showManage(request):
    return render(request, "hospital_manage.html")

def showVideocall(request):
    return render(request, "hospital_videocall.html")

def showPayment(request):
    return render(request,"hospital_payment.html")

def showConsultData(request):
    return render(request,"hospital_consultdata.html")