#!/usr/bin/env python3
"""API call to Umbrella Enforcement API to remove a policy record.

References:
    https://docs.umbrella.com/developer/enforcement-api/domain2/

"""

import json
from urllib.parse import quote
from logzero import logger
from umbr_api._key import get_key
from umbr_api._http_requests import send_delete

APP_JSON = {'Content-Type': 'application/json'}


def remove(record_id=None, domain_name=None, key=None):
    """Remove a record from the policy."""
    key = get_key(key=key)
    response = None

    if record_id and domain_name:
        logger.warning('Both arguments are used. "id" is preferred.')

    if record_id:
        api_uri = """https://s-platform.api.opendns.com/1.0/domains/""" + \
                  """{0}?customerKey={1}""".format(record_id, key)
        response = send_delete(api_uri, headers=APP_JSON)
    elif domain_name and not record_id:
        safe_url = quote(domain_name, safe='')

        api_uri = """https://s-platform.api.opendns.com/1.0/domains/""" + \
                  """{0}?customerKey={1}""".format(safe_url, key)
        response = send_delete(api_uri, headers=APP_JSON)

    format_response(response)

    return response


def format_response(response):
    """Format results."""
    if response.status_code == 204:
        print('OK')
    else:
        print('Error')
        json_response = json.loads(response.text)
        logger.error('%s', json_response['message'])

        try:
            for key, value in json_response['errors'].items():
                logger.error('%s %s', key, value)
        except KeyError:
            pass

        try:
            logger.error('Code: %s', json_response['code'])
        except KeyError:
            pass

        logger.error('Status code: %d', json_response['statusCode'])


def main():
    """Test if executed directly."""
    response = remove(record_id='29765170')
    print(response.status_code,
          json.dumps(dict(response.headers), indent=4), sep='\n\n')

    # response = remove(record_id=29765171)
    # print(response.status_code,
    #       json.dumps(dict(response.headers), indent=4), sep='\n\n')

    # response = remove(domain_name='www.shopdisney.com')
    # print(response.status_code,
    #       json.dumps(dict(response.headers), indent=4), sep='\n\n')


if __name__ == '__main__':
    main()
