from .models import Hospital
from address.models import Address
from surdo.models import Consult

# Create your services here.

import logging
logger = logging.getLogger(__name__)

class HospitalService():

    def getAllHospitals():
        hospitals = Hospital.objects.all()
        return hospitals
    
    def getHospital(id):
        return Hospital.objects.get(id=id)

    def getHospitalsFromState(state):
        hospitals = []
        all_hospitals = Hospital.objects.all()
        for hospital in all_hospitals:
            if hospital.address.state == state:
                hospitals.append(hospital)
                
        return hospitals

    def get_pending_consults_from_hospital(hospital_id):
        try:
            return Consult.objects.filter(hospital_id = hospital_id, status=0)
        except Consult.DoesNotExist:
            return []

    #for videocall screen
    #def get_consults_accepted_by_interpreters(hospital_id):
    #    try:
    #        return Consult.objects.filter(hospital_id = hospital_id, status=2)
    #    except Consult.DoesNotExist:
    #        return []
