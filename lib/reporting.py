import requests
import time

from hashlib import md5


ACCOUNT_TYPES = ['publisher_admin', 'publisher_user']


class ReportingAPI():

    account_type = None
    account_id = None
    apikey = None

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

    def __init__(self, account_type, account_id, private_key):
        assert account_type in ACCOUNT_TYPES
        assert isinstance(account_id, int)
        assert len(private_key) == 32

        self.account_id = account_id
        self.account_type = account_type
        self.apikey = private_key

    def format_url(self):
        timestamp = int(time.time())
        token = md5("{}{}".format(timestamp, self.apikey)).hexdigest().lower()

        request_url = "{}/{}/{}/reports?timestamp={}&token={}".format(
            self.API_HOST,
            self.account_type,
            self.account_id,
            timestamp,
            token
        )
        return request_url

    def report(self, **kwargs):
        api_params = {}

        for key, value in kwargs.iteritems():
            assert key in self.REPORT_PARAMETERS

            api_params[key] = value
        
        res = requests.get(self.format_url(), params=api_params)

        assert res.status_code == 200

        return res.json()

