import requests
import json

f = open('x-rapidapi-key.json')

data = json.load(f)

tournament_id = '1143'

url = data['api-url-endpoint'] + data['api-matches-by-tournament-id-endpoint'] + tournament_id

headers = {
    'x-rapidapi-key': data['x-rapidapi-key'],
    'x-rapidapi-host': data['x-rapidapi-host']
    }

response = requests.request("GET", url, headers=headers)

if response.status_code == 200:

    with open(f'matches-{tournament_id}.json', 'wb') as outf:
        outf.write(response.content)
else:
    print(f'Error ocurred with status code: {response.status_code}')