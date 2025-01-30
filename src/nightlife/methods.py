import base64
import json
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible

from requests import post
import requests
from credentials import CLIENT_ID, CLIENT_SECRET

@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)
    
def get_token():
    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET

    url = 'https://accounts.spotify.com/api/token'
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:
        json_result = response.json()
        token = json_result['access_token']
        return token
    else:
        print(f"Error: {response.status_code}")

def get_auth_headers(token):
    return {"Authorization": "Bearer "+ token}

def spotify_search(search_type, search_query):
    token = get_token()

    url = 'https://api.spotify.com/v1/search'
    headers = get_auth_headers(token)
    params = {
        'q': search_query,
        'type': search_type,
        'limit': 1,
        'offset': 0
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        json_result = response.json()[f"{search_type}s"]["items"]
        if len(json_result) == 0:
            print(f"Nothing found for {search_type}: {search_query}")
            return None
        return json_result[0]
    else:
        print(f"Error: {response.status_code}")