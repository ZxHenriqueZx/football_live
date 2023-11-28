from os import environ as env
from app.api_football import Api

if __name__ == "__main__":
    headers = {
        "X-RapidAPI-Key": env['API_KEY'],
        "X-RapidAPI-Host": env['API_HOST'],
    }

    football_live = Api(headers)


