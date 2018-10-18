#!/usr/bin/env python3
"""Command-line utility to access Umbrella APIs.

Examples:
    .. code:: bash

        umbrella add www.example.com http://www.example.com/images
        umbrella del www.example.com
        umbrella del 297XXXXX --key YOUR-CUSTOMER-KEY-IS-HERE-0123456789
        umbrella -vv get 50
        umbrella get --key YOUR-CUSTOMER-KEY-IS-HERE-0123456789
        umbrella networks
        umbrella recent github.com
        umbrella keyring --add-enforcement YOUR-CUSTOMER-KEY-IS-HERE-0123456789

APIs references:
    https://docs.umbrella.com/developer/enforcement-api/
    https://docs.umbrella.com/umbrella-api/reference
    https://docs.umbrella.com/umbrella-api/docs/overview

"""
# pylint: disable=R0912
# pylint: disable=R0914
# pylint: disable=R0915

import argparse
import logging
import sys

import keyring
import logzero
from logzero import logger

import umbr_api
import umbr_api.management
import umbr_api.reporting
from umbr_api.add import add
from umbr_api.get import get_list
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
        formatter_class=argparse.RawDescriptionHelpFormatter,
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
        help='Bypass Domain Acceptance Process while adding',
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
        help='Remove a record from the block list',
    )
    parser_del.add_argument(
        '--key',
        help='Specify API key',
        type=str,
    )
    parser_del.add_argument(
        'record_id',
        help='DNS domain name or record ID to remove from the block list',
        type=str,
    )

    # networks command
    parser_networks = subparsers.add_parser(
        'networks',
        help='List of configured networks',
    )
    parser_networks.add_argument(
        '--limit',
        help='Limit number of records to return',
        type=int,
        default=10,
    )
    parser_networks.add_argument(
        '--page',
        help='Number of page to show',
        type=int,
        default=0,
    )

    # roamingcomputers command
    parser_roamingcomputers = subparsers.add_parser(
        'roamingcomputers',
        help='List of roaming computers',
    )
    parser_roamingcomputers.add_argument(
        '--limit',
        help='Limit number of records to return',
        type=int,
        default=10,
    )
    parser_roamingcomputers.add_argument(
        '--page',
        help='Number of page to show',
        type=int,
        default=0,
    )

    # internalnetworks command
    parser_internalnetworks = subparsers.add_parser(
        'internalnetworks',
        help='List of internal networks',
    )
    parser_internalnetworks.add_argument(
        '--limit',
        help='Limit number of records to return',
        type=int,
        default=10,
    )
    parser_internalnetworks.add_argument(
        '--page',
        help='Number of page to show',
        type=int,
        default=0,
    )

    # virtualappliances command
    parser_virtualappliances = subparsers.add_parser(
        'virtualappliances',
        help='List of virtual appliances',
    )
    parser_virtualappliances.add_argument(
        '--limit',
        help='Limit number of records to return',
        type=int,
        default=10,
    )
    parser_virtualappliances.add_argument(
        '--page',
        help='Number of page to show',
        type=int,
        default=0,
    )

    # sites command
    parser_sites = subparsers.add_parser(
        'sites',
        help='List of sites',
    )
    parser_sites.add_argument(
        '--limit',
        help='Limit number of records to return',
        type=int,
        default=10,
    )
    parser_sites.add_argument(
        '--page',
        help='Number of page to show',
        type=int,
        default=0,
    )

    # users command
    parser_users = subparsers.add_parser(
        'users',
        help='List of administrative users',
        )
    parser_users.add_argument(
        '--limit',
        help='Limit number of records to return',
        type=int,
        default=10,
    )
    parser_users.add_argument(
        '--page',
        help='Number of page to show',
        type=int,
        default=0,
    )

    # roles command
    parser_roles = subparsers.add_parser(
        'roles',
        help='List of user roles',
        )
    parser_roles.add_argument(
        '--limit',
        help='Limit number of records to return',
        type=int,
        default=10,
    )
    parser_roles.add_argument(
        '--page',
        help='Number of page to show',
        type=int,
        default=0,
    )

    # activity command
    parser_activity = subparsers.add_parser(
        'activity',
        help='Report the latest security activity',
        )
    parser_activity.add_argument(
        '--limit',
        help='Limit number of records to return',
        type=int,
        default=20,
    )
    parser_activity.add_argument(
        '--start',
        help='From time (epoch)',
        type=int,
    )
    parser_activity.add_argument(
        '--stop',
        help='Till time (epoch)',
        type=int,
    )

    # top command
    parser_top = subparsers.add_parser(
        'top',
        help='Report top10 identities for particular destination',
        )
    parser_top.add_argument(
        'destination',
        help='The destination must a domain specified'
             ' without any protocol or delimiters',
        type=str,
    )

    # recent command
    parser_recent = subparsers.add_parser(
        'recent',
        help='Report the most recent DNS requests for a particular '
             'destination from all identities',
        )
    parser_recent.add_argument(
        '--limit',
        help='Limit number of records to return',
        type=int,
        default=20,
    )
    parser_recent.add_argument(
        '--offset',
        help='Changes which index the list of returned orgs starts at',
        type=int,
    )
    parser_recent.add_argument(
        'destination',
        help='The destination must a domain specified'
             ' without any protocol or delimiters',
        type=str,
    )

    # keyring command
    parser_keyring = subparsers.add_parser(
        'keyring',
        help='Access to the system keyring service for credentials management',
    )
    group_keyring = parser_keyring.add_mutually_exclusive_group()
    group_keyring.add_argument(
        '--add-orgid',
        dest='orgid',
        help='Add Organization ID',
        type=str,
    )
    group_keyring.add_argument(
        '--show-orgid',
        help='Show Organization ID',
        action='store_true',
        default=False,
    )
    group_keyring.add_argument(
        '--add-enforcement',
        dest='key_to_add',
        help='Add Enforcement API key to the keyring',
        type=str,
    )
    group_keyring.add_argument(
        '--show-enforcement',
        help='Show Enforcement API key from the keyring',
        action='store_true',
        default=False,
    )
    group_keyring.add_argument(
        '--add-management',
        dest='management_credentials',
        help='Add Management API credentials to the keyring in format:'
             "'key:secret'",
        type=str,
    )
    group_keyring.add_argument(
        '--show-management',
        help='Show saved Enforcement API credentials',
        action='store_true',
        default=False,
    )
    group_keyring.add_argument(
        '--add-reporting',
        dest='reporting_credentials',
        help='Add Reporting API credentials to the keyring in format:'
        "'key:secret'",
        type=str,
    )
    group_keyring.add_argument(
        '--show-reporting',
        help='Show saved Reporting API credentials',
        action='store_true',
        default=False,
    )

    # print short usage description if no args was provided
    if len(sys.argv) == 1:
        parser.print_usage(sys.stderr)
        raise SystemExit(0)

    return parser.parse_args()


def save_key(key, name):
    """Save API credentials to the system keyring."""
    assert key
    assert name in ["enforcement", "management", "reporting", "orgid", "test"]
    logger.debug('Saving API credentials to the system keyring')
    keyring.set_password(umbr_api.__title__, name, key)
    read_key = keyring.get_password(umbr_api.__title__, name)
    print('Note: Any python program may have an access to this record '
          'in the keyring under your credentials.')
    if read_key == key:
        print('OK')
    else:
        print('Error: Provided credentials doesn''t match to saved.')
        logging.error('Provided credentials doesn''t match to saved key.')
    return 0 if read_key == key else 1


def show_key(name):
    """Read and show API credentials from the keyring."""
    logger.debug('Reading API credentials from keyring')
    try:
        read_key = keyring.get_password(umbr_api.__title__, name)
    except RuntimeError:
        read_key = None

    if read_key:
        print('API credentials:', read_key)
    else:
        logging.warning('No API credentials are accessible.')
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
            exit_code = save_key(
                args.key_to_add,
                "enforcement"
            )
        elif args.show_enforcement:
            exit_code = show_key("enforcement")

        elif args.management_credentials:
            exit_code = save_key(
                args.management_credentials,
                "management"
            )
        elif args.show_management:
            exit_code = show_key("management")

        elif args.reporting_credentials:
            exit_code = save_key(
                args.reporting_credentials,
                "reporting"
            )
        elif args.show_reporting:
            exit_code = show_key("reporting")

        elif args.orgid:
            exit_code = save_key(
                args.orgid,
                "orgid"
            )
        elif args.show_orgid:
            exit_code = show_key("orgid")

        raise SystemExit(exit_code)

    if args.command in ["get", "add", "del"]:
        if args.key is None:
            logger.debug('Reading API credentials from the system keyring')
            args.key = keyring.get_password(
                umbr_api.__title__,
                "enforcement"
            )

    if args.command in [
            "networks", "roamingcomputers", "internalnetworks",
            "virtualappliances", "sites", "users", "roles",
    ]:
        logger.debug('Reading OrgId from the system keyring')
        args.orgid = keyring.get_password(
            umbr_api.__title__,
            "orgid"
        )

        logger.debug('Reading credentials from the system keyring')
        args.key_management = keyring.get_password(
            umbr_api.__title__,
            "management"
        )

    if args.command in [
            "activity", "top", "recent",
    ]:
        logger.debug('Reading OrgId from the system keyring')
        args.orgid = keyring.get_password(
            umbr_api.__title__,
            "orgid"
        )

        logger.debug('Reading credentials from the system keyring')
        args.key_reporting = keyring.get_password(
            umbr_api.__title__,
            "reporting"
        )

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

    if args.command == 'networks':
        response = umbr_api.management.networks(
            orgid=args.orgid, cred=args.key_management, limit=args.limit,
            page=args.page
        )
        exit_code = response.status_code

    if args.command == 'roamingcomputers':
        response = umbr_api.management.roamingcomputers(
            orgid=args.orgid, cred=args.key_management, limit=args.limit,
            page=args.page
        )
        exit_code = response.status_code

    if args.command == 'internalnetworks':
        response = umbr_api.management.internalnetworks(
            orgid=args.orgid, cred=args.key_management, limit=args.limit,
            page=args.page
        )
        exit_code = response.status_code

    if args.command == 'virtualappliances':
        response = umbr_api.management.virtualappliances(
            orgid=args.orgid, cred=args.key_management, limit=args.limit,
            page=args.page
        )
        exit_code = response.status_code

    if args.command == 'sites':
        response = umbr_api.management.sites(
            orgid=args.orgid, cred=args.key_management, limit=args.limit,
            page=args.page
        )
        exit_code = response.status_code

    if args.command == 'users':
        response = umbr_api.management.users(
            orgid=args.orgid, cred=args.key_management, limit=args.limit,
            page=args.page
        )
        exit_code = response.status_code

    if args.command == 'roles':
        response = umbr_api.management.roles(
            orgid=args.orgid, cred=args.key_management, limit=args.limit,
            page=args.page
        )
        exit_code = response.status_code

    if args.command == 'activity':
        response = umbr_api.reporting.activity(
            orgid=args.orgid, cred=args.key_reporting, limit=args.limit,
            start=args.start, stop=args.stop
        )
        exit_code = response.status_code

    if args.command == 'top':
        response = umbr_api.reporting.top_identities(
            destination=args.destination, cred=args.key_reporting,
            orgid=args.orgid
        )
        exit_code = response.status_code

    if args.command == 'recent':
        response = umbr_api.reporting.recent(
            destination=args.destination, cred=args.key_reporting,
            orgid=args.orgid, limit=args.limit, offset=args.offset
        )
        exit_code = response.status_code

    logger.debug('Exit code: %d', exit_code)
    raise SystemExit(exit_code)


if __name__ == '__main__':
    main()
