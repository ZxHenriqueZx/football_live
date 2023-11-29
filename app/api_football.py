import requests
import dotenv
import datetime
from os import environ as env
from app.utils import is_int, input_filter

dotenv.load_dotenv()

class Api:
    def __init__(self, headers):
        self.url = env['URL_API']
        self.endpoints = {
            "times": "teams",
            "campeonatos": "leagues",
            "jogos": "fixtures",
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
        self.get(
            "campeonatos", 
            {"team": self.team['team']['id'],"season": 2023}
        )

        current_leagues = []
        for i in self.data:
            current_leagues.append(dict(
                nome=i['league']['name'],
                id=i['league']['id']
            ))
        
        self.leagues = current_leagues


    def fixtures(self):
        self.get(
            "jogos",
            {"team": 121, "last": 5}
        )

        for i in self.data:
            home_name = i['teams']['home']['name']
            home_goals = i['goals']['home'] 

            away_name = i['teams']['away']['name']
            away_goals = i['goals']['away']

            placar = f'{home_name} {home_goals} X {away_goals} {away_name}'
            data_str = i['fixture']['date']

            data = datetime.datetime.fromisoformat(data_str)
    
            print(placar)
            print(data.strftime('%d/%m/%Y - %H:%M:%S'))
