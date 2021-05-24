from .models import Hospital
from address.models import Address

class HospitalService():

    def getAllHospitals():
        hospitals = Hospital.objects.all()
        return hospitals
    
    def getHospital(id):
        return Hospital.objects.get(id=id)