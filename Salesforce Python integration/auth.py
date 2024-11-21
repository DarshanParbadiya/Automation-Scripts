import requests
from consumer_details import CONSUMER_KEY, CONSUMER_SECRET, USERNAME, PASSOWRD, DOMAIN
def generate_access_token():
# Set up the request data
    data = {
        'grant_type': 'password',
        'client_id': CONSUMER_KEY,
        'client_secret': CONSUMER_SECRET,
        'username': USERNAME,
        'password': PASSOWRD
    }

    oauth_endpoint = '/services/oauth2/token'

    # Make the request
    response = requests.post(DOMAIN + oauth_endpoint, data=data)

    # Extract the access token from the response
    access_token = response.json()['access_token']
    return access_token