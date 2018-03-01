#!/usr/bin/env python3
"""API call to add a record via Umbrella Enforcement API.

References:
    https://docs.umbrella.com/developer/enforcement-api/events2/

"""

import json
from datetime import datetime
from urllib.parse import urlparse
from logzero import logger
from umbr_api._key import get_key
from umbr_api._http_requests import send_post


def add(domain=None, url=None, key=None):
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

    time_str = (datetime.utcnow()).isoformat(sep='T',
                                             timespec='milliseconds') + 'Z'
    api_uri = 'https://s-platform.api.opendns.com/1.0/events?customerKey=' + \
              key
    block_request_txt = """
    {{
        "alertTime": "{alertTime}",
        "deviceId": "ba6a59f4-e692-4724-ba36-c28132a761de",
        "deviceVersion": "10.13.3",
        "dstDomain": "{dstDomain}",
        "dstUrl": "{dstUrl}",
        "eventTime": "{eventTime}",
        "protocolVersion": "1.0a",
        "providerName": "umbr api call"
    }}""".format(alertTime=time_str,
                 dstDomain=domain,
                 dstUrl=url,
                 eventTime=time_str)

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
        json_response = json.loads(response.text)
        logger.error('%s', json_response['message'])
        for key, value in json_response['errors'].items():
            logger.error('%s %s', key, value)
        logger.error('Status code: %d', json_response['statusCode'])


def main():
    """Test if executed directly."""
    response = add(domain='www.shopdisney.com',
                   url='https://www.shopdisney.com/test')
    print(response.status_code,
          json.dumps(dict(response.headers), indent=4),
          json.dumps(json.loads(response.text), indent=4), sep='\n\n')


if __name__ == '__main__':
    main()
