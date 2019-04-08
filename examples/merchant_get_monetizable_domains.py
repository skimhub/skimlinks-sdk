import argparse
import logging
from lib.merchant import MerchantAPI
from lib.authentication import AuthenticationAPI

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--client-id', required=True, type=str, 
        help='Your Client ID. Check https://developers.skimlinks.com for more info')

    parser.add_argument('--client-secret', required=True, type=str, 
        help='Your Client Secret. Check https://developers.skimlinks.com for more info')

    parser.add_argument('--publisher-id', required=True, type=int, 
        help='Your Publisher ID')

    args = parser.parse_args()
    return args

def cmdline_main():
    args = parse_args()
    auth = AuthenticationAPI(
        args.client_id,
        args.client_secret
    )

    token = auth.get_token()

    api = MerchantAPI(
        token.get("access_token"),
        args.publisher_id
    )
    
    LOGGER.info("requesting list of domains")
    res = api.domains()
    distinct_domains = set([entry.get("domain") for entry in res.get("domains", [])])

    LOGGER.info("found {} unique merchant domains".format(len(distinct_domains)))

if __name__ == '__main__':
    cmdline_main()
