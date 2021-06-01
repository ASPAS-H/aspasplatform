from .forms import ConsultForm
from .models import Consult
from hospital.services import HospitalService
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
            consult = {"not_found": True}
        return consult

    def get_hospitals_consults(hospital_id):
        hospitals = Consult.objects.filter(hospital_id=hospital_id)
        return hospitals