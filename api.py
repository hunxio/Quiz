import requests
from access_tokens import API_URL


class Api:

    def __init__(self):
        self.api_url = API_URL

    def quiz_request(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data = response.json()
            quiz_list = data.get("results", [])
            return quiz_list
        else:
            return "Service not available right now."


if __name__ == "__main__":
    main()
