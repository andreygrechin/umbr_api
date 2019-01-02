#!/usr/bin/env python3
"""Example of using umbr_api.

References:
    Enforcement API
    https://docs.umbrella.com/developer/enforcement-api/
    https://docs.umbrella.com/developer/enforcement-api/limits-responses-and-errors/

"""
import json
from umbr_api.get import get_list


def main():
    """Test if executed directly."""
    response = get_list(key="YOUR-CUSTOMER-KEY-IS-HERE-0123456789")

    block_list_json = json.loads(response.text)
    print(response.status_code,
          json.dumps(dict(response.headers), indent=4),
          json.dumps(block_list_json, indent=4), sep='\n\n')

    for record in block_list_json['data']:
        print('ID: {}, Name: {}'.format(record['id'], record['name']))


if __name__ == '__main__':
    main()
