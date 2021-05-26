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
        consult.save()
        logger.error(consult)
        return consult
    
    def getConsults(user):
        consults = Consult.objects.filter(user_id=user.id)
        return consults

    def getPendingConsults():
        consults = Consult.objects.filter(status=1)
        return consults
        