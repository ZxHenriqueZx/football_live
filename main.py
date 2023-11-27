import dotenv
from os import environ as env
from app.api_football import Api
from app.utils import is_int, input_filter

if __name__ == "__main__":
    headers = {
        "X-RapidAPI-Key": env['API_KEY'],
        "X-RapidAPI-Host": env['API_HOST'],
    }

    football_live = Api(headers)

    options = [
        'Definir Time preferido',
        'Sair',
    ]

    def menu():
        print()
        for i, op in enumerate(options):
            print(i, op)

        index_option = input_filter('Escolha uma opção: ', int)

        return index_option

    print('=== FOOTBALL LIVE ===')
    while True:
        print()
        option = menu()

        if options[option] == 'Definir Time preferido':
            football_live.team_fav(input_filter('Digite o nome do Time: ', str))
            continue 

        if options[option] == 'Sair':
            break

