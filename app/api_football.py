import requests
import dotenv
from os import environ as env

dotenv.load_dotenv()

class Api:
    def __init__(self, headers):
        self.url = env['URL_API']
        self.endpoints = {
            "times": "teams",
        }

        self._headers = headers

    def get(self, endpoint, params):
        with requests.get(
            self.url + self.endpoints[endpoint],
            headers=self._headers,
            params=params
        ) as re:

            self._data = re.json()
            print(self._data)

if __name__ == '__main__':
    headers = {
        "X-RapidAPI-Key": env['API_KEY'],
        "X-RapidAPI-Host": env['API_HOST'],
    }

    app = Api(headers)

    app.get("times", {"id":121})

