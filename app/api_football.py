import requests
import dotenv
import os

dotenv.load_dotenv()

if __name__ == '__main__':
    headers = {
        "X-RapidAPI-Key": os.environ['API_KEY'],
        "X-RapidAPI-Host":os.environ['API_HOST'],
    }
    with requests.get(os.environ['URL_API'] + 'timezone', headers=headers) as re:
        print(re.json())
