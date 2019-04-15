import requests
import json

class MerchantAPI():

    token = None
    publisher_id = 1023

    API_HOST = "https://merchants.skimapis.com"
    API_VERSION = "v4"

    SEARCH_PARAMETERS = ["id", "a_id", "search", "vertical", "country", "favorite_type", "limit", "offset", "sort_by", "sort_dir"]
    OFFER_PARAMETERS = ["search", "merchant_id", "a_id", "vertical", "country", "period", "favourite_type", "limit", "offset", "sort_by", "sort_dir"]

    def __init__(self, token, publisher_id):
        self.token = token
        self.publisher_id = publisher_id

    def format_url(self,endpoint):
        return "{}/{}/publisher/{}/{}".format(
            self.API_HOST,
            self.API_VERSION,
            self.publisher_id,
            endpoint
        )

    def base_params(self):
        return {
            "access_token": self.token
        }

    def search(self, **kwargs):
        api_params = self.base_params()

        for key, value in kwargs.iteritems():
            assert key in self.SEARCH_PARAMETERS

            api_params[key] = value
        
        res = requests.get(self.format_url("merchants"), params=api_params)

        assert res.status_code == 200

        return res.json()

    def verticals(self):
        res = requests.get("{}/{}/verticals".format(self.API_HOST, self.API_VERSION), params=self.base_params())
        
        assert res.status_code == 200

        return res.json()

    def domains(self):
        res = requests.get(self.format_url("domains"), params=self.base_params())
        assert res.status_code == 200

        return res.json()

    def offers(self, **kwargs):

        api_params = self.base_params()

        for key, value in kwargs.iteritems():
            assert key in self.OFFER_PARAMETERS

            api_params[key] = value
        
        res = requests.get(self.format_url("offers"), params=api_params)

        assert res.status_code == 200

        return res.json()