import requests

BASE_URL = "https://mypost.israelpost.co.il/"

def get_deliveries(user: str, name: str) -> list:
    response = requests.post(BASE_URL)
    return []
