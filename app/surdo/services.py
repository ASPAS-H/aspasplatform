from django.http import request
from .forms import ConsultForm
from .models import Consult
from hospital.services import HospitalService
from interpreter.services import InterpreterService
import logging
logger = logging.getLogger(__name__)
class DeafService():

    def createConsult(data, user):
        hospital = HospitalService.getHospital(data["hospital"])
        consult = ConsultForm(data)
        consult = consult.save(commit=False)
        consult.user_id = user.id
        consult.hospital = hospital
        consult.status = 0
        consult.save()
        logger.error(consult)
        return consult
    
    def getConsults(user):
        consults = Consult.objects.filter(user_id=user.id)
        return consults

    def getPendingConsults():
        consults = Consult.objects.filter(status=1)
        return consults
    
    def getConsult(id):
        try:
            consult = Consult.objects.get(id=id)
        except Consult.DoesNotExist:
            consult = {"not_found": True,"id":id}
        return consult
    
    def getInterpreterConsults(interpreter_id):
        try:
            consults = Consult.objects.filter(interpreter=interpreter_id)
        except Consult.DoesNotExist:
            consults = {"not_found": True}
        return consults

    def get_hospitals_consults(hospital_id):
        hospitals = Consult.objects.filter(hospital_id=hospital_id)
        return hospitals

    def change_consult_status(consult, status):
        consult = DeafService.getConsult(consult)
        consult.status = status
        consult.save()
        return consult

    
    def getPendingConsultsForInterpreter(user_id):
        allConsults = Consult.objects.filter(status=1)
        consults = []


        for consult in allConsults:
            consults.append(consult)
            rejected_consults = InterpreterService.getRejectedConsults(consult.id)

            for rejected_consult in rejected_consults:
                logger.error(rejected_consult.interpreter.id,user_id)
                if user_id == rejected_consult.interpreter.id:
                    consults.pop(-1)


        return consults