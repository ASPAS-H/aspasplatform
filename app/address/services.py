import requests

class AccountService():
    def getCEPCoords(cep):
    url = f"https://www.cepaberto.com/api/v3/cep?cep={cep}"

    headers = {'Authorization': 'Token token=35f9cb346092abca1d8251546b77a1cc'}
    response = requests.get(url, headers=headers)
    coords = {"latitude", response.json()["latitude"], "longitude": response.json()["longitude"]}
    return coords
