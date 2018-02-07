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

    verticals = api.verticals()
    vertical_ids = []
    for vertical_group in verticals.get("vertical_groups", []):
        if vertical_group.get("name") == "Automotive":
            for vertical in vertical_group.get("verticals"):
                vertical_ids.append(vertical.get("id"))

    LOGGER.info("found {} verticals in the Automotive group".format(len(vertical_ids)))

    merchants = []
    for vertical_id in vertical_ids:
        offset = 0
        LOGGER.info("processing vertical id: {}".format(vertical_id))
        while True:
            res = api.search(
                vertical=vertical_id,
                offset=offset,
                limit=200
            )

            merchants += res.get("merchants", [])

            if not res.get("has_more"):
                break

            offset += 200

    LOGGER.info("found {} merchants".format(len(merchants)))


if __name__ == '__main__':
    cmdline_main()
