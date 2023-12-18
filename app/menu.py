from app.utils import input_filter
import os
from time import sleep
from datetime import *

class Menu:
    def __init__(self, name, api):
        self.name = name
        self.api = api
        self._options = [
            'Definir Time favorito',
            'Calendário',
            'Sair'
        ]

    def options(self):
        for i, option in enumerate(self._options):
            print(f'{i} - {option}')

        index_option = input_filter('Escolha uma opção: ', int) 
        return index_option

    def start(self):
        while True:
            print(f'=== {self.name} ===')

            if self.api.team == None or self.api.team == 'Não Definido': 
                self.api.team = 'Não Definido'
                print('Time favorito:', self.api.team)
            else:
                print('Time favorito:', self.api.team['team']['name'])

            option = self.options()

            if self._options[option] == "Definir Time favorito":
                os.system('clear')
                team_name = input_filter('Digite o nome do time: ', str)
                self.api.team_fav(team_name)

                if self.api.team == 'Não Definido':
                    sleep(2)
                else:
                    self.api.team_leagues()

                os.system('clear')
    
            if self._options[option] == "Calendário":
                if self.api.team == 'Não Definido':
                    print('Time favorito não definido')
                    sleep(2)
                    os.system('clear')
                    continue

                self.api.fixtures()
                data = [self.api.last_games]
                self.calendario(fixtures=data)

            if self._options[option] == "Sair":
                break

       
    def calendario(fixtures):
        for i in fixtures:
            home_name = i['teams']['home']['name']
            home_goals = i['goals']['home'] 
        
            away_name = i['teams']['away']['name']
            away_goals = i['goals']['away']
        
            placar = f'{home_name} {home_goals} X {away_goals} {away_name}'
            estadio = i['fixture']['venue']['name']
        
            data_str = i['fixture']['date']
            tz_sp = timezone(timedelta(hours=-3))
            data = datetime.fromisoformat(data_str).astimezone(tz_sp) 
        
            print(i)
            print(placar)
            print(data.strftime('%d/%m/%Y - %H:%M:%S'))
            print(f'Estádio: {estadio}')
            print()
