from os import environ as env
from app.api_football import Api
from app.menu import Menu

if __name__ == "__main__":
    headers = {
        "X-RapidAPI-Key": env['API_KEY'],
        "X-RapidAPI-Host": env['API_HOST'],
    }

    football_live = Api(headers)

    cli = Menu('FOOTBALL LIVE', football_live)

    cli.start()

    #football_live.fixtures()
