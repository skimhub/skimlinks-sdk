import argparse
import logging
from lib.merchant import MerchantAPI

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--account-type', choices=['publisher_admin', 'publisher_user'], 
        required=True, help='The authenticated account\'s type. check https://developers.skimlinks.com for more info')

    parser.add_argument('--account-id',  required=True, type=int,
        help='The authenticated account\'s id. check https://developers.skimlinks.com for more info')

    parser.add_argument('--public-key',  required=True, 
        help='Your public key. check https://developers.skimlinks.com for more info')

    args = parser.parse_args()
    return args

def cmdline_main():
    args = parse_args()

    api = MerchantAPI(
        account_type=args.account_type,
        account_id=args.account_id,
        public_key=args.public_key
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
