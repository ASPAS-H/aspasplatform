from .forms import ConsultForm
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