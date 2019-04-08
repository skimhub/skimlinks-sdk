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

    offset = 0
    offer_count = 0

    while True:
        LOGGER.info("requesting with offset: {}".format(offset))
        res = api.offers(
            period="upcoming",
            offset=offset,
            limit=200
        )

        offer_count += len(res.get("offers", []))

        if not res.get("has_more"):
            break

        offset += 200

    LOGGER.info("found {} upcoming offers".format(offer_count))



if __name__ == '__main__':
    cmdline_main()
