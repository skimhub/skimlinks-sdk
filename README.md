# Skimlinks SDK

The Skimlinks SDK is a Python 2.7 wrapper around the public Skimlinks APIs (documentation at https://developers.skimlinks.com). It provides a couple of easy to use libraries to interact with the APIs in a convenient and standardized way

## Installation

1. Clone the project
2. Run `pip install -r requirements.txt` to install dependencies
3. Run `pip install -e .` to install the libraries

## Examples

The repo provides example scripts for the most common tasks requested by Skimlinks' publishers. Check out the files located in the `examples` folder. 

In order to run the examples simply execute them from the command line. For example:

```python examples/merchant_get_monetizable_domains.py --account-type=publisher_admin --account-id=your_account_id --public-key=public_key```
