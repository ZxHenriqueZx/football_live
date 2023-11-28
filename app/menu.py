from app.utils import input_filter
import os

class Menu:
    def __init__(self, name, api):
        self.name = name
        self.api = api
        self._options = [
            'Definir Time favorito',
            'Sair'
        ]

    def options(self):
        for i, option in enumerate(self._options):
            print(f'{i} - {option}')

        index_option = input_filter('Escolha uma opção: ', int) 
        return index_option

    def start(self):
        while True:
            os.system('clear')
            print(23*'-')
            print(f'=== {self.name} ===')

            if self.api.team == None:
                self.api.team = 'Não Definido'
                print('Time favorito:', self.api.team)
            else:
                print('Time favorito:', self.api.team['team']['name'])

            option = self.options()

            if self._options[option] == "Definir Time favorito":
                team_name = input_filter('Digite o nome do time: ', str)
                self.api.team_fav(team_name)

            if self._options[option] == "Sair":
                break

            print(23*'-')

