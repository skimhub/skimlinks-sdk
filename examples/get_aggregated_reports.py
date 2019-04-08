import logging
import argparse
from lib.reporting import ReportingAPI
from lib.authentication import AuthenticationAPI

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

REPORT_TYPES = ['page', 'date', 'device', 'country', 'domain', 'link', 'merchant']

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--client-id', required=True, type=str, 
        help='Your Client ID. Check https://developers.skimlinks.com for more info')

    parser.add_argument('--client-secret', required=True, type=str, 
        help='Your Client Secret. Check https://developers.skimlinks.com for more info')

    parser.add_argument('--publisher-id', required=True, type=int, 
        help='Your Publisher ID')

    parser.add_argument('--start-date', required=True, type=str, 
        help='Report Start date')

    parser.add_argument('--end-date', required=True, type=str, 
        help='Report End date')

    parser.add_argument('--report-by', required=True, type=str, choices=REPORT_TYPES,
        help='Report type')

    args = parser.parse_args()
    return args

def cmdline_main():
    args = parse_args()
    auth = AuthenticationAPI(
        args.client_id,
        args.client_secret
    )

    token = auth.get_token()

    api = ReportingAPI(
        token=token.get("access_token"),
        publisher_id=args.publisher_id
    )

    res = api.report(
        report_by=args.report_by,
        start_date=args.start_date,
        end_date=args.end_date,
    )

    LOGGER.info(res)

if __name__ == '__main__':
    cmdline_main()
