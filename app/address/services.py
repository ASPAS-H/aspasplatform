from .models import Address
from hospital.services import HospitalService
from math import sin, cos, sqrt, atan2, radians
import requests
import os
import logging
import json
logger = logging.getLogger(__name__)

class AddressService():
    def getZIPCoords(cep):
        cep = AddressService.get_cep_numbers(cep)
        url = f"https://www.cepaberto.com/api/v3/cep?cep={cep}"
        headers = {'Authorization': "Token token=35f9cb346092abca1d8251546b77a1cc"}
        response = ""
        error = False
        try:
            response = requests.get(url, headers=headers)
            response = response.json()
        except requests.exceptions.RequestException as e:
            error = True

        coords = dict()
        coords["latitude"] = response["latitude"]
        coords["longitude"] = response["longitude"]
        coords["error"] = error
        return coords

    def getCoords(address_id):
        address = Address.objects.get(id=address_id)
        if address.lat == None or address.lng == None:
            cep = AddressService.getZIPCoords(address.zipCode)
            if not cep["error"]:
                address.lat = cep["latitude"]
                address.lng = cep["longitude"]
                address.save()

        return address
    
    def get_cep_numbers(cep):
        cep_formatted = str(cep).replace('-', '')
        if len(cep_formatted) != 8:
            cep_formatted = "0" + cep_formatted
        return cep_formatted

    def get_distance(address1, address2):
        if address1.lat == None or address1.lng == None:
            address1 = AddressService.getCoords(address1.id)

        if address2.lat == None or address2.lng == None:
            address2 = AddressService.getCoords(address2.id)

        distance = AddressService.get_distance_between_cords(address1.lat, address1.lng, address2.lat, address2.lng)
        return distance

    def get_nearby_hospitals(address_id):
        MAX_DISTANCE = 15
        location = AddressService.getCoords(address_id)
        hospitals = HospitalService.getHospitalsFromState(location.state)
        nearby_hospitals = []

        for hospital in hospitals:
            distance = AddressService.get_distance(location, hospital.address)
            if distance <= MAX_DISTANCE:
                nearby_hospitals.append(hospital)
        
        return nearby_hospitals

    def get_distance_between_cords(latitude1, longitude1, latitude2, longitude2):
        # approximate radius of earth in km
        R = 6373.0
        lat1 = radians(float(latitude1))
        lon1 = radians(float(longitude1))
        lat2 = radians(float(latitude2))
        lon2 = radians(float(longitude2))

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        return distance
        
