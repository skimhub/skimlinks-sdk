import logging
from lib.reporting import ReportingAPI
import click

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

ACCOUNT_TYPES = ['publisher_admin', 'publisher_user']
REPORT_TYPES = ['page', 'date', 'device', 'country', 'domain', 'link', 'merchant']


@click.command()
@click.option('--account-type', required=True, type=click.Choice(ACCOUNT_TYPES),
              help='The authenticated account\'s type. check https://developers.skimlinks.com for more info')
@click.option('--account-id', required=True, type=int,
              help='The authenticated account\'s id. check https://developers.skimlinks.com for more info')
@click.option('--private-key', required=True,
              help='The authenticated account\'s private key. check https://developers.skimlinks.com for more info')
@click.option('--start-date', required=True,
              help='The start date of the report you want to get')
@click.option('--end-date', required=True,
              help='The end date of the report you want to get')
@click.option('--report-by', required=True, type=click.Choice(REPORT_TYPES),
              help='The end date of the report you want to get')
def cmdline_main(account_type, account_id, private_key, start_date, end_date, report_by):

    api = ReportingAPI(
        account_type=account_type,
        account_id=account_id,
        private_key=private_key
    )

    res = api.report(
        report_by=report_by,
        start_date=start_date,
        end_date=end_date,
    )

    LOGGER.info(res)

if __name__ == '__main__':
    cmdline_main()
