import requests
import dotenv
from os import environ as env
from app.utils import is_int, input_filter

dotenv.load_dotenv()

class Api:
    def __init__(self, headers):
        self.url = env['URL_API']
        self.endpoints = {
            "times": "teams",
            "campeonatos": "leagues"
        }

        self._headers = headers
        self.team = None

    def get(self, endpoint, params):
        with requests.get(
            self.url + self.endpoints[endpoint],
            headers=self._headers,
            params=params) as re:

            self.data = re.json()['response']

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


    def team_leagues(self):
        if self.team == None:
            print('Time favorito não está definido!')
            #return
       
        self.get("campeonatos", {"team": self.team['team']['id'], "season": 2023})

        current_leagues = []
        for i in self.data:
            current_leagues.append(dict(
                nome=i['league']['name'],
                id=i['league']['id']
            ))
        
        self.leagues = current_leagues


