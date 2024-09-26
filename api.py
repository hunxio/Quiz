import requests
from access_tokens import API_URL

class Api:

    def __init__(self):
        self.api_url = API_URL

    def request(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return "Service not available right now."
