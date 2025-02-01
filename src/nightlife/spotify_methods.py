import requests
import time
from credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

# Variables globales pour stocker les jetons et l'heure d'expiration
access_token = None
refresh_token = None
token_expiry = 0

def is_user_connected():
    global access_token, token_expiry
    # Vérifier si le jeton d'accès est valide
    if access_token and time.time() < token_expiry:
        return True
    return False

def get_authorization_url():
    url = 'https://accounts.spotify.com/authorize'
    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'scope': 'user-follow-read'  # Ajoutez les scopes nécessaires
    }
    response = requests.get(url, params=params)
    return response.url

def get_tokens(auth_code):
    global access_token, refresh_token, token_expiry
    url = 'https://accounts.spotify.com/api/token'
    data = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        json_result = response.json()
        access_token = json_result['access_token']
        refresh_token = json_result['refresh_token']
        token_expiry = time.time() + json_result['expires_in']
        return access_token, refresh_token
    else:
        print(f"Error: {response.status_code}")
        return None, None

def refresh_access_token():
    global access_token, token_expiry
    url = 'https://accounts.spotify.com/api/token'
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        json_result = response.json()
        access_token = json_result['access_token']
        token_expiry = time.time() + json_result['expires_in']
        return access_token
    else:
        print(f"Error: {response.status_code}")
        return None
    
def get_auth_headers(token):
    return {"Authorization": "Bearer "+ token}

def spotify_search(search_type, search_query):
    global access_token
    url = 'https://api.spotify.com/v1/search'
    headers = get_auth_headers(access_token)
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
