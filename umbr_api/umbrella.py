#!/usr/bin/env python3
"""Command-line utility to access Umbrella Enforcement API.

Examples:
    .. code:: bash

        umbrella --add www.example.com http://www.example.com/images
        umbrella --remove-domain www.example.com
        umbrella --remove-id 297XXXXX --k YOUR-CUSTOMER-KEY-IS-HERE-0123456789
        umbrella --get-list 100
        umbrella --get-list --key YOUR-CUSTOMER-KEY-IS-HERE-0123456789
        umbrella --keyring-add YOUR-CUSTOMER-KEY-IS-HERE-0123456789

References:
    https://docs.umbrella.com/developer/enforcement-api/

"""

import sys
import argparse
import logging
from os import path
import keyring
import logzero
from logzero import logger
from umbr_api.get import get_list
from umbr_api.add import add
from umbr_api.remove import remove

LOG_FORMAT = '%(asctime)s.%(msecs)03d %(module)13s[%(lineno)4d] ' + \
             '%(threadName)10s %(color)s%(levelname)8s%(end_color)s ' + \
             '%(message)s'

FORMATTER = logzero.LogFormatter(fmt=LOG_FORMAT, datefmt='%H:%M:%S')
logzero.setup_default_logger(formatter=FORMATTER, level=logging.WARNING)


def create_parser():
    """Create argparse parser, return args."""
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.
                                     RawDescriptionHelpFormatter,
                                     epilog='')

    group = parser.add_mutually_exclusive_group()

    group.add_argument('--add',
                       help='Add domain to the block list; The first '
                       'argument represent DNS domain name, the second '
                       'URL address; Two arguments are required.',
                       nargs=2,
                       type=str)

    group.add_argument('--remove-domain',
                       help='Remove a record from the block list '
                       'by DNS domain name',
                       nargs=1,
                       type=str)

    group.add_argument('--remove-id',
                       help='Remove a record from the block list '
                       'by record id',
                       nargs=1,
                       type=str)

    group.add_argument('--get-list',
                       help='Get the block list',
                       nargs='?',
                       const=10,
                       type=int)

    parser.add_argument('--key',
                        help='Specify API key',
                        nargs=1,
                        type=str)

    parser.add_argument('--keyring-add',
                        help='Add API key to the keyring (MacOS)',
                        nargs=1,
                        type=str)

    parser.add_argument('-v', '--verbose',
                        help='Enable detail messages; Option is additive, '
                             'can be used up to 2 times',
                        action='count')

    parser.add_argument('-V', '--version',
                        help='Show version and continue',
                        action='count')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        raise SystemExit(1)

    return parser.parse_args()


def setup_logging_level(verbose_level):
    """Define logging level.

    By default ``logging.WARNING`` level is enabled. ``-v`` arguments can be
    used to increase logging level. Two levels are supported:
    ``logging.INFO`` and ``logging.DEBUG``.
    """
    if verbose_level == 1:
        logzero.setup_default_logger(formatter=FORMATTER,
                                     level=logging.INFO)
    elif verbose_level >= 2:
        logzero.setup_default_logger(formatter=FORMATTER,
                                     level=logging.DEBUG)


def get_version():
    """Read and return package version number."""
    logger.debug('Opening "__about__.py" to read version')

    about = {}
    with open(path.join(path.dirname(__file__), "__about__.py")) as py_file:
        # pylint: disable=W0122
        exec(py_file.read(), about)
    return about['__version__']


def main():
    """Execute main body, console_script entry point."""
    key = None

    args = create_parser()

    response = None

    if args.verbose:
        setup_logging_level(args.verbose)

    logger.info('%s is started', __name__, )
    logger.debug('Debug turned on')
    logger.debug('Run with arguments: %s', str(args))

    if args.version:
        print('Version: {}'.format(get_version()))
        raise SystemExit(0)

    if args.keyring_add:
        logger.debug('Save API key to keyring')
        keyring.set_password('umbrella', 'umbr_api', args.keyring_add[0])
        raise SystemExit(0)

    if args.key:
        key = args.key[0]
        logger.debug('Use API key from command-line arguments')
    else:
        logger.debug('Try to read API key from a keyring')
        key = keyring.get_password('umbrella', 'umbr_api')

    if args.get_list:
        response = get_list(page=1, limit=args.get_list, key=key)

    if args.add:
        response = add(domain=args.add[0], url=args.add[1], key=key)

    if args.remove_domain:
        response = remove(domain_name=args.remove_domain[0], key=key)

    if args.remove_id:
        response = remove(record_id=args.remove_id[0], key=key)

    if response:
        return_code = response.status_code
    else:
        return_code = 0

    logger.debug('Return code: %d', return_code)
    return return_code


if __name__ == '__main__':
    main()
