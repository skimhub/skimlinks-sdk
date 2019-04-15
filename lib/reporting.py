import requests
import time

from hashlib import md5

class ReportingAPI():

    token = None
    publisher_id = None

    API_HOST = "https://reporting.skimapis.com"
    REPORT_PARAMETERS = [
        'report_by',
        'start_date',
        'end_date',
        'sort_by',
        'sort_dir',
        'limit',
        'offset',
        'time_period',
        'a_id',
        'domain_id',
        'device_type',
        'user_country',
        'domain_id',
        'page_search',
        'link_search',
        'merchant_search'
    ]

    def __init__(self, token, publisher_id):
        self.token = token
        self.publisher_id = publisher_id

    def format_url(self):
        request_url = "{}/publisher/{}/reports".format(
            self.API_HOST,
            self.publisher_id
        )
        return request_url

    def report(self, **kwargs):
        api_params = {
            "access_token": self.token
        }

        for key, value in kwargs.iteritems():
            assert key in self.REPORT_PARAMETERS

            api_params[key] = value
        
        res = requests.get(self.format_url(), params=api_params)

        assert res.status_code == 200

        return res.json()

