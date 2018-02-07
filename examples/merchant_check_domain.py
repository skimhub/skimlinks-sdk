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

    parser.add_argument('--domain',  required=True, 
        help='Domain to check')

    args = parser.parse_args()
    return args

def cmdline_main():
    args = parse_args()

    api = MerchantAPI(
        account_type=args.account_type,
        account_id=args.account_id,
        public_key=args.public_key
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
