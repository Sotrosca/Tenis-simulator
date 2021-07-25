import requests
import json

# Opening JSON file
f = open('x-rapidapi-key.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

tournament_id = '1143'

url = data['api-url-endpoint'] + data['api-matches-by-tournament-id-endpoint'] + tournament_id

headers = {
    'x-rapidapi-key': data['x-rapidapi-key'],
    'x-rapidapi-host': data['x-rapidapi-host']
    }

response = requests.request("GET", url, headers=headers)


with open(f'matches-{tournament_id}.json', 'wb') as outf:
    outf.write(response.content)