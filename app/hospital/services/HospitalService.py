from .models import Hospital
from address.models import Address

def getAllHospitals():
    hospitals = Hospital.objects.all()
    return hospitals