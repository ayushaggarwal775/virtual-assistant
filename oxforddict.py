import requests
import json

def wordsearch(x):
    app_id = 'APP_ID'
    app_key = 'APP_KEY'

    language = 'en'


    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + x.lower()

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

    a = r.json()
    a = a['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
    print(a)
    return a
