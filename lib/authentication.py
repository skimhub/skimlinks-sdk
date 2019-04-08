import requests

class AuthenticationAPI():

    API_HOST = "https://authentication.skimapis.com"

    client_id = None
    client_secret = None

    def __init__(self, client_id, client_secret):
        assert client_id and isinstance(client_id, str) and len(client_id) == 32
        assert client_secret and isinstance(client_secret, str) and len(client_secret) == 32

        self.client_id = client_id
        self.client_secret = client_secret

    def get_token(self):
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }
        
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post("{}/access_token".format(self.API_HOST), json=payload, headers=headers)

        assert response.status_code == 200
        return response.json()