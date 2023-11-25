import requests
import dotenv
from os import environ as env

from utils import is_int, input_filter

dotenv.load_dotenv()

class Api:
    def __init__(self, headers):
        self.url = env['URL_API']
        self.endpoints = {
            "times": "teams",
        }

        self._headers = headers
        self.team = None

    def get(self, endpoint, params):
        with requests.get(
            self.url + self.endpoints[endpoint],
            headers=self._headers,
            params=params) as re:

            self.data = re.json()['response']
            #print(self.data)

    def team_fav(self, team_name):
        self.get("times", {'search': team_name})

        for i, item in enumerate(self.data):
            team_name = item['team']['name']
            team_country = item['team']['country']
            
            print(f'{i} - {team_name} - {team_country}')

        while True:
            index_team = input_filter('Escolha o time: ', int)

            if index_team in range(len(self.data)):
                self.team = self.data[index_team]
                break
            else:
                print('Index Errado, escolha umas das opções acima')

if __name__ == '__main__':
    headers = {
        "X-RapidAPI-Key": env['API_KEY'],
        "X-RapidAPI-Host": env['API_HOST'],
    }

    app = Api(headers)

    app.team_fav("fla")

    print(app.team)
