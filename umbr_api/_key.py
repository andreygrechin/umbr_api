#!/usr/bin/env python3
"""Return Umbrella Enforcement API key."""

import json
from os import path
from re import match
from logzero import logger


def get_key(key=None, filename='customer_key.json'):
    """Check API key if provided or read it from the file."""
    if not key:
        logger.debug('No customer API key was provided')
        logger.debug('Reading configuration file: %s', filename)
        json_config_file_name = path.join(path.split(__file__)[0],
                                          'data', filename)
        try:
            file = open(json_config_file_name, 'r')
        except FileNotFoundError as msg:
            print('Cannot find `{}`.'.format(filename))
            print('Please use `--key` optional argument.')
            logger.exception(msg)
            raise SystemExit(1)
        try:
            json_data = json.load(file)
            key = json_data['customer_key']
        except KeyError as msg:
            print('Cannot find data with in `%s`', filename)
            logger.exception(msg)
            raise SystemExit(1)

    assert isinstance(key, str)
    assert len(key) == 36

    assert match('^[0-9A-Za-z-]*$', key)

    return key


def main():
    """Test if executed directly."""
    logger.debug('Provided API key:\n%s',
                 get_key('12345678-980a-bcde-fghi-jklmnopqrstu'))
    logger.debug('Read API key from file:\n%s', get_key())


if __name__ == '__main__':
    main()
