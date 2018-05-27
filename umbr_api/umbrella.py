#!/usr/bin/env python3
"""Command-line utility to access Umbrella Enforcement API.

Examples:
    .. code:: bash

        umbrella add www.example.com http://www.example.com/images
        umbrella del www.example.com
        umbrella del 297XXXXX --key YOUR-CUSTOMER-KEY-IS-HERE-0123456789
        umbrella -vv get 50
        umbrella get --key YOUR-CUSTOMER-KEY-IS-HERE-0123456789
        umbrella keyring --add YOUR-CUSTOMER-KEY-IS-HERE-0123456789

References:
    https://docs.umbrella.com/developer/enforcement-api/

"""

import sys
import argparse
import logging
import keyring
import logzero
from logzero import logger
import umbr_api
from umbr_api.get import get_list
from umbr_api.add import add
from umbr_api.remove import remove

LOG_FORMAT = '%(asctime)s.%(msecs)03d %(module)14s[%(lineno)4d] ' \
             + '%(threadName)10s %(color)s%(levelname)8s%(end_color)s ' \
             + '%(message)s'

FORMATTER = logzero.LogFormatter(fmt=LOG_FORMAT, datefmt='%H:%M:%S')
logzero.setup_default_logger(formatter=FORMATTER, level=logging.WARNING)


def create_parser():
    """Create argparse parser, return args."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        prog='umbrella',
        formatter_class=argparse.
        RawDescriptionHelpFormatter,
        epilog='',
        )

    # optional arguments
    parser.add_argument(
        '-V', '--version',
        help='Show version',
        action='version',
        version=umbr_api.__version__,
        )
    parser.add_argument(
        '-v', '--verbose',
        help='Enable detailed logging; Option is additive, '
             'can be used up to 2 times',
        action='count',
        )
    subparsers = parser.add_subparsers(
        title='commands',
        dest='command',
        )

    # add command
    parser_add = subparsers.add_parser(
        'add',
        help='Add domain to the block list',
        )
    parser_add.add_argument(
        'dns_name',
        help='DNS address to block',
        type=str,
        )
    parser_add.add_argument(
        'url',
        help='URL address to block',
        type=str,
        )
    parser_add.add_argument(
        '--force',
        help='Bypass Domain Acceptance Process '
        'while adding',
        action='store_true'
        )
    parser_add.add_argument(
        '--key',
        help='Specify API key',
        type=str,
        )
    # get command
    parser_get = subparsers.add_parser(
        'get',
        help='Show the current block list',
        )
    parser_get.add_argument(
        '--key',
        help='Specify API key',
        type=str,
        default=None,
        )
    parser_get.add_argument(
        'max_records',
        help='Limit maximum number records to return',
        type=int,
        nargs='?',
        default=10,
        )
    # del command
    parser_del = subparsers.add_parser(
        'del',
        help='Remove a record from the block '
        'list',
        )
    parser_del.add_argument(
        '--key',
        help='Specify API key',
        type=str,
        )
    parser_del.add_argument(
        'record_id',
        help='DNS domain name or record ID to remove '
        'from the block list',
        type=str,
        )
    # keyring command
    parser_keyring = subparsers.add_parser(
        'keyring',
        help='Remove a record from the '
        'block list',
        )
    group_keyring = parser_keyring.add_mutually_exclusive_group()
    group_keyring.add_argument(
        '--add',
        dest='key_to_add',
        help='Add API key to the keyring',
        type=str,
        )
    group_keyring.add_argument(
        '--show',
        help='Read and show API key from the keyring',
        action='store_true',
        default=True,
        )

    # print short usage description if no args was provided
    if len(sys.argv) == 1:
        parser.print_usage(sys.stderr)
        raise SystemExit(0)

    return parser.parse_args()


def save_key(key):
    """Save API key to the keychain."""
    logger.debug('Saving API key to keyring')
    keyring.set_password('python', umbr_api.__title__, key)
    read_key = keyring.get_password('python', umbr_api.__title__)
    print('Note: Any python program may have an access to this record '
          'in the keychain under your credentials.')
    if read_key == key:
        print('OK')
    else:
        print('Error: Provided key doesn''t match to saved key.')
        logging.error('Provided key doesn''t match to saved key.')
    return 0 if read_key == key else 1


def show_key():
    """Read and show API key from the keyring."""
    logger.debug('Reading API key from keyring')
    try:
        read_key = keyring.get_password('python', umbr_api.__title__)
    except RuntimeError:
        read_key = None

    if read_key:
        print('API key:', read_key)
    else:
        logging.warning('No API key is accessible.')
    return 0 if read_key else 1


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


def main(args=None):
    """Execute main body, console_script entry point."""
    response = None
    exit_code = 0
    if not args:
        args = create_parser()

    if args.verbose:
        setup_logging_level(args.verbose)

    logger.info('%s is started', __name__, )
    logger.debug('Debug turned on')
    logger.debug('Run with arguments: %s', str(args))

    if args.command == 'keyring':
        if args.key_to_add:
            exit_code = save_key(args.key_to_add)
        elif args.show:
            exit_code = show_key()
        raise SystemExit(exit_code)

    if args.command:
        if args.key is None:
            logger.debug('Reading API key from a keychain')
            args.key = keyring.get_password('python', umbr_api.__title__)

    if args.command == 'get':
        response = get_list(page=1, limit=args.max_records, key=args.key)
        exit_code = response.status_code

    if args.command == 'add':
        response = add(domain=args.dns_name, url=args.url,
                       key=args.key, bypass=args.force)
        exit_code = response.status_code

    if args.command == 'del':
        response = remove(record_id=args.record_id, key=args.key)
        exit_code = response.status_code

    logger.debug('Exit code: %d', exit_code)
    raise SystemExit(exit_code)


if __name__ == '__main__':
    main()
