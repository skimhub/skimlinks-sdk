import requests
import json

class MerchantAPI():

    account_type = None
    account_id = None
    apikey = None

    API_HOST = "https://merchants.skimapis.com/"
    API_VERSION = "v3"

    SEARCH_PARAMETERS = ["id", "a_id", "search", "vertical", "country", "favorite_type", "limit", "offset", "sort_by", "sort_dir"]
    OFFER_PARAMETERS = ["search", "merchant_id", "a_id", "vertical", "country", "period", "favourite_type", "limit", "offset", "sort_by", "sort_dir"]

    def __init__(self, account_type, account_id, public_key):
        assert account_type in ["publisher_admin", "publisher_user"]
        assert isinstance(account_id, int)
        assert len(public_key) == 32

        self.account_id = account_id
        self.account_type = account_type
        self.apikey = public_key

    def format_url(self,endpoint):
        return "{}/{}/{}".format(
            self.API_HOST,
            self.API_VERSION,
            endpoint
        )

    def base_params(self):
        return {
            "account_type": self.account_type,
            "account_id": self.account_id,
            "apikey": self.apikey
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
        res = requests.get(self.format_url("verticals"), params=self.base_params())
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