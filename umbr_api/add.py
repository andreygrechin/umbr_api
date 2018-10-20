#!/usr/bin/env python3
# pylint: disable=C0301
"""API call to add a record via Umbrella Enforcement API.

Note:
    When posting data to the Security Platform API, the following steps are
    taken before the domain appears in a customer's block list. The optional
    parameter "disableDstSafeguards" can be used to bypass parts of this
    process as outlined in the Generic Event Format Field Descriptions.
    The domain acceptance process is outlined from start to finish here:

        1. An external source identifies malicious activity occurring when
        a user visits a particular URL. This source could be a third party
        vendor’s data feed, an entry in one of your security logs or something
        identified as malicious on a security related website.

        2. The event is sent to the Umbrella Security Platform API via
        a POST request, following the steps and syntax outlined earlier in
        this documentation.

        3. Before the domain included API POST event is added to the specified
        Umbrella customer’s block list, the following checks are performed:

            a) Does the domain already exist in the Umbrella Security global
               block list under one of the Security Categories?

            b) Is the domain considered benign, or safe, under the Cisco
               Umbrella Investigate?

            c) Is the status of the domain uncategorized?

            d) Is the domain already present on the customer’s allow list
               within the organization?

        4. If the domain is then added to the customer’s domain list, then
        any domains in that list will be blocked in accordance with that
        customer’s Umbrella policy security settings.

References:
    https://docs.umbrella.com/developer/enforcement-api/events2/
    https://docs.umbrella.com/developer/enforcement-api/domain-acceptance-process2/

"""

import json
from datetime import datetime
from urllib.parse import urlparse

from logzero import logger

import umbr_api
from umbr_api._http_requests import send_post
from umbr_api.credentials import get_key


def add(domain=None, url=None, key=None, bypass=False):
    """Add domain name to block list."""
    assert domain and url
    assert isinstance(domain, str)
    assert isinstance(url, str)

    if domain != url:
        if url[0:7] == 'http://' or url[0:8] == 'https://':
            check_url = urlparse(url).hostname
        else:
            check_url = urlparse('http://' + url).hostname

        if domain != check_url:
            logger.warning('Domain name part from URL '
                           'doesn\'t match DNS domain name')
            logger.warning('DNS domain name: %s', domain)
            logger.warning('URL domain name: %s', check_url)

    key = get_key(key=key)
    response = None

    time_str = (datetime.utcnow()).isoformat(sep='T') + 'Z'
    api_uri = 'https://s-platform.api.opendns.com/1.0/events?customerKey=' + \
              key

    if bypass:
        bypass_str = 'true'
    else:
        bypass_str = 'false'

    block_request_txt = """
    {{
        "alertTime": "{alertTime}",
        "deviceId": "ba6a59f4-e692-4724-ba36-c28132a761de",
        "deviceVersion": "{deviceVersion}",
        "dstDomain": "{dstDomain}",
        "dstUrl": "{dstUrl}",
        "eventTime": "{eventTime}",
        "protocolVersion": "1.0a",
        "providerName": "Security Platform",
        "disableDstSafeguards": {disableDstSafeguards}
    }}""".format(alertTime=time_str,
                 deviceVersion=umbr_api.__version__,
                 dstDomain=domain,
                 dstUrl=url,
                 eventTime=time_str,
                 disableDstSafeguards=bypass_str)

    response = send_post(api_uri,
                         data=block_request_txt,
                         headers={'Content-Type': 'application/json'})
    format_response(response)

    return response


def format_response(response):
    """Format results."""
    if response.status_code == 202:
        print('OK')
    else:
        print('Error')
        try:
            json_response = json.loads(response.text)
            for key, value in json_response.items():
                logger.error('%s %s', key, value)
        except KeyError as msg:
            print('Get abnormal code while adding:',
                  response.status_code)
            logger.exception(msg)


def main(test_key=None):
    """Test if executed directly."""
    result = add(
        domain='www.example.com',
        url='https://www.example.com/test',
        key=test_key,
        )
    assert result.status_code == 202

    result = add(
        domain='www.example.com',
        url='www.example.com',
        key=test_key,
        )
    assert result.status_code == 202


if __name__ == '__main__':
    main()
