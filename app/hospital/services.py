from .models import Hospital
from address.models import Address

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