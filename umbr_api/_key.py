#!/usr/bin/env python3
"""Return Umbrella Enforcement API key."""

from json import load
from os import path
from re import match
from logzero import logger


def get_key(key=None, filename='customer_key.json'):
    """Check API key if provided or read it from the file."""
    if not key:
        logger.debug('No customer API key was provided')
        logger.debug('Reading the configuration file: %s', filename)
        json_config_file_name = path.join(path.dirname(__file__),
                                          'data', filename)
        try:
            file = open(json_config_file_name, 'r')
        except FileNotFoundError as msg:
            print('Error: Cannot find `{}`.'.format(filename))
            print('Please use `--key` optional argument.')
            logger.exception(msg)
            raise SystemExit(2)

        try:
            json_data = load(file)
            key = json_data['customer_key']
        except KeyError as msg:
            print('Error: Cannot find data with in `%s`', filename)
            logger.exception(msg)
            raise SystemExit(1)
        finally:
            file.close()

    if not(isinstance(key, str) and len(key) == 36 and
           match('^[0-9A-Za-z-]*$', key)):
        print('Error: Key is invalid')
        raise SystemExit(1)

    return key


def main():
    """Test if executed directly."""
    logger.debug('Testing getting the key from ``get_key`` API call')
    test_key = '12345678-980a-bcde-fghi-jklmnopqrstu'
    new_key = get_key(test_key)
    assert test_key == new_key
    logger.debug('Keys match each other')
    logger.debug('Testing reading API key from file')
    logger.debug('API key from file: %s',
                 get_key(filename='customer_key_example.json'))


if __name__ == '__main__':
    main()
