from django.shortcuts import render
from surdo.services import DeafService
from .services import HospitalService
import logging
logger = logging.getLogger(__name__)
# Create your views here.

def showIndex(request):
    return render(request, "hospital_index.html")

def showConsults(request):
    consults = HospitalService.get_pending_consults_from_hospital(HospitalService.getHospitalStaff(request.user.id).hospital.id)
    return render(request, "hospital_consults.html", {"consults": consults})

def showInfo(request, id):
    consult = DeafService.getConsult(id)
    return render(request, "hospital_info.html", {"consult": consult})

def showTest(request):
    return render(request, "hospital_new.html")

def showPatientDetails(request, id, consult):
    deaf = DeafService.getDeaf(id)
    return render(request, "hospital_patient.html", {"deaf": deaf, "consult_id": consult})

def showManage(request):
    return render(request, "hospital_manage.html")

def showVideocall(request):
    return render(request, "hospital_videocall.html")

def showPayment(request):
    return render(request,"hospital_payment.html")

def showConsultData(request):
    return render(request,"hospital_consultdata.html")