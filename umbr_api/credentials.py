#!/usr/bin/env python3
"""Check provided credentails or read them from file."""

from base64 import b64encode
from json import load
from os import path
from re import match

from logzero import logger

CFG_FILENAME = "umbrella.json"


def get_key(key=None, filename=CFG_FILENAME):
    """Return Umbrella Enforcement API customer key."""
    key_to_return = _read_cfg(
        default_value=key, filename=filename, key_to_read="enforcement"
    )
    if not(isinstance(key_to_return, str) and len(key_to_return) == 36 and
           match('^[0-9A-Za-z-]*$', key_to_return)):
        print('Error: Key is invalid')
        raise SystemExit(1)
    return key_to_return


def get_orgid(orgid=None, filename=CFG_FILENAME):
    """Return orgid string."""
    orgid_to_return = _read_cfg(
        default_value=orgid, filename=filename, key_to_read="orgid"
    )
    return orgid_to_return


def _read_cfg(default_value=None, filename=None, key_to_read=None):
    """Return a value from file if default value is not provided.

    Can use parameters if provided or read them from the default cfg file.
    """
    assert key_to_read
    # if credentials are provided, just check ascii format
    if default_value:
        if not(isinstance(default_value, str)
               and match('^[0-9A-Za-z-:]*$', default_value)):
            print('Error: string has illegal characters')
            raise SystemExit(1)
    else:
        logger.debug('No defaults were provided in the call')
        logger.debug('Reading the configuration file: %s', filename)
        json_config_file_name = path.join(path.dirname(__file__),
                                          'data', filename)
        try:
            file = open(json_config_file_name, 'r')
        except FileNotFoundError as msg:
            print('Error: Cannot find `{}`.'.format(json_config_file_name))
            print('Please provide credentials via json file or the keyring.')
            logger.debug(msg)
            raise SystemExit(2)
        try:
            json_data = load(file)
            default_value = json_data[key_to_read]
        except KeyError as msg:
            print('Error: Cannot find data with in `%s`', filename)
            logger.debug(msg)
            raise SystemExit(1)
        finally:
            file.close()
    return default_value


def get_base64(cred=None, filename=CFG_FILENAME, api=None):
    """Return base64 encoded string."""
    assert api
    credentials = _read_cfg(
        default_value=cred, filename=filename, key_to_read=api
    )
    output = b64encode("{}".format(credentials).encode(encoding="ascii"))
    return output.decode("ascii")


def main():
    """Test if executed directly."""
    logger.debug('Testing getting the key from ``get_key`` API call')
    test_key = '12345678-980a-bcde-fghi-jklmnopqrstu'
    new_key = get_key(test_key)
    assert test_key == new_key
    logger.debug('Keys match each other')
    logger.debug("")
    logger.debug('Testing reading API key from file')
    logger.debug('API key from file: %s',
                 get_key(filename='umbrella_example.json'))
    logger.debug("")
    logger.debug("Testing getting the base64 encoded credentials")
    test_credentials = "Aladdin:OpenSesame"
    new_base64 = get_base64(cred=test_credentials, api="management")
    assert new_base64 == "QWxhZGRpbjpPcGVuU2VzYW1l"
    logger.debug("Encoded strings match each other")
    logger.debug("")
    logger.debug("Testing getting the base64 encoded credentials from file")
    new_base64 = get_base64(filename="umbrella_example.json", api="management")
    assert new_base64 == "WW91cktleUlzSGVyZTpZb3VyU2VjcmV0SXNIZXJl"
    logger.debug("Encoded strings match each other")


if __name__ == '__main__':
    main()
