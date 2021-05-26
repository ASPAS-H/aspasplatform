from .models import Address
import requests
import os
import logging
logger = logging.getLogger(__name__)

class AddressService():
    def getZIPCoords(cep):
        cep = AddressService.get_cep_numbers(cep)
        url = f"https://www.cepaberto.com/api/v3/cep?cep={cep}"
        headers = {'Authorization': "Token token=35f9cb346092abca1d8251546b77a1cc"}
        response = requests.get(url, headers=headers)
        coords = {"latitude": response.json()["latitude"], "longitude": response.json()["longitude"]}
        return coords

    def getCoords(address_id):
        address = Address.objects.get(id=address_id)
        return AddressService.getZIPCoords(address.zipCode)
    
    def get_cep_numbers(cep):
        cep_formatted = str(cep).replace('-', '')
        if len(cep_formatted) != 8:
            cep_formatted = "0" + cep_formatted
        return cep_formatted