from typing import List, Dict, Any
import os
import requests

API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/'
AUTH_TOKEN = os.environ['AUTH_TOKEN']

def get_sales(date: str) -> List[Dict[str, Any]]:
    response = requests.get(
        url='https://fake-api-vycpfa6oca-uc.a.run.app/sales',
        params={'date': date, 'page': 2},
        headers={'Authorization': AUTH_TOKEN},
    )
    print("Response status code:", response.status_code)


    return response.json()

