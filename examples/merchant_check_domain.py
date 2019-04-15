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

    parser.add_argument('--domain',  required=True, 
        help='Domain to check')

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

    res = api.search(
        search=args.domain
    )

    if len(res.get("merchants", [])):
        LOGGER.info("{} is monetizable".format(args.domain))
    else:
        LOGGER.info("{} is not monetizable".format(args.domain))

if __name__ == '__main__':
    cmdline_main()
