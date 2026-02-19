import requests

class FlightAPI:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://test.api.amadeus.com"
        self.token = self._get_access_token()

    
    def _get_access_token(self):
        url = f"{self.base_url}/v1/security/oauth2/token"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }


        data = {
        "grant_type": "client_credentials",
        "client_id": self.api_key,
        "client_secret": self.api_secret
        }


        response = requests.post(url, headers=headers, data=data)

        print("Status code:", response.status_code)
        print("Resposta:", response.text)

        response.raise_for_status()

        return response.json()["access_token"]


    def buscar_voos(self, origem, destino, data_ida):
        url = f"{self.base_url}/v2/shopping/flight-offers"

        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        params = {
            "originLocationCode": origem,
            "destinationLocationCode": destino,
            "departureDate": data_ida,
            "adults": 1,
            "max": 5,
        }

        response = requests.get(url, headers=headers, params=params)
        return response.json()
