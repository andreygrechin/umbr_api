#!/usr/bin/env python3
"""API call to Umbrella Enforcement API to get blocked domain list.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        >>> from umbr_api.get import get_list
        >>> response = get_list(key="KEY")
        >>> print(response.status_code)
        200

    PEP 484 type annotations are supported. If attribute, parameter, and
    return types are annotated according to PEP 484, they do not need to be
    included in the docstring:

Todo:
    * Add args to show all existing records without pagination.

References:
    https://docs.umbrella.com/developer/enforcement-api/domains2/

"""

import json
from datetime import datetime

from logzero import logger
from tabulate import tabulate

from umbr_api._http_requests import send_get
from umbr_api.credentials import get_key
from umbr_api.management import json_to_table


def get_list(page=1, limit=10, key=None, exclude=None, **kwargs):
    """Return response tuple as response to API call.

    Note:
        Up to 200 records can be returned by API.

    Args:
        page (int): Page # to request.
        limit (int): Limit number of records to request.
        key (str): API key, if not specify obtain via ``key`` module.

    Returns:
        Return ``requests.Response`` object.
        http://docs.python-requests.org/en/master/api/#requests.Response

    """
    assert isinstance(page, int)
    assert isinstance(limit, int)

    key = get_key(key=key)
    response = None

    api_uri = (
        "https://s-platform.api.opendns.com/1.0/"
        + "domains?customerKey="
        + key
    )
    api_uri += "&page={0}&limit={1}".format(page, limit)

    response = send_get(url=api_uri)

    format_response(
        response.status_code, json.loads(response.text), exclude, **kwargs
    )

    return response


def format_response(code, json_response, exclude, **kwargs):
    """Format results."""
    if code == 200:
        print(
            "Page: {}\nLimit: {}\n".format(
                json_response["meta"]["page"], json_response["meta"]["limit"]
            )
        )
        for idx, record in enumerate(json_response["data"]):
            time_str = datetime.fromtimestamp(record["lastSeenAt"]).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            json_response["data"][idx]["lastSeenAt"] = time_str

        table = json_to_table(json_response["data"], exclude_col=exclude)
        print(
            tabulate(
                table[1:], headers=table[0], tablefmt=kwargs.get("format")
            )
        )
    else:
        print("Error")
        try:
            for key, value in json_response.items():
                logger.error("%s %s", key, value)
        except KeyError as msg:
            print("Get abnormal code while read:", code)
            logger.exception(msg)


def main(test_key=None):
    """Test if executed directly."""
    # Standard request

    get_list(key=test_key, **{"format": "psql"})

    # Request with pagination
    get_list(page=2, limit=2, key=test_key)

    # Request with pagination, max limit is 200 records,
    # so the last one will fail with error 400
    get_list(page=1, limit=201, key=test_key)


if __name__ == "__main__":
    main()
