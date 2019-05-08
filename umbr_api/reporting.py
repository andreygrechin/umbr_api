#!/usr/bin/env python3
"""API calls to Umbrella Reporting API.

References:
    https://docs.umbrella.com/umbrella-api/docs/overview

"""

import json

from tabulate import tabulate

from umbr_api._http_requests import send_get
from umbr_api.credentials import get_base64, get_orgid
from umbr_api.management import json_to_table


def get_headers(cred=None, filename=None):
    """Return headers for basic HTTP authentication.

    Returns:
        str: Basic authorization header, including Base64 encoded
            username and password.

    """
    return {
        "Authorization": "Basic {}".format(
            get_base64(cred=cred, filename=filename, api="reporting")
        )
    }


def activity(cred=None, orgid=None, **kwargs):
    """Request the last security activities.

    Parameters:
        orgid (str): Cisco Umbrella organization ID
        limit (int): the number of results to return, from 1 to 500
        start (int): the start of the time window for which
            results are shown, specified as Unix (epoch)
            timestamp in seconds.
        stop (int): the stop of the time window for which
            results are shown, specified as Unix (epoch)
            timestamp in seconds
        _stop_timest (int): used for pagination and gathered
            from the output of the previous query, specified as
            Unix (epoch) timestamp in milliseconds. (not implemented)

    Returns:
        requests.Response: Return ``requests.Response`` class object

    """
    cfg_file = kwargs.get("filename", "umbrella.json")
    limit = kwargs.get("limit", 10)
    start = kwargs.get("start", None)
    stop = kwargs.get("stop", None)
    exclude = kwargs.get("exclude", None)

    if start and stop:
        time_filter = "&start={}&stop={}".format(start, stop)
    else:
        time_filter = ""
    api_uri = (
        "https://reports.api.umbrella.com/v1/organizations"
        + "/{}/security-activity?limit={}{}".format(
            get_orgid(orgid, filename=cfg_file), limit, time_filter
        )
    )
    activity_response = send_get(
        url=api_uri, headers=get_headers(cred, filename=cfg_file)
    )
    if activity_response.status_code == 200:
        table = json_to_table(
            json.loads(activity_response.text)["requests"], exclude_col=exclude
        )
        print(
            tabulate(
                table[1:], headers=table[0], tablefmt=kwargs.get("format")
            )
        )
    return activity_response


def top_identities(destination, cred=None, orgid=None, **kwargs):
    """Request top10 identities which send DNS requests to destination.

    Parameters:
        destination (str): a domain name specified without
            any protocol or delimiters
        orgid (str): Cisco Umbrella organization ID

    Returns:
        requests.Response: Return ``requests.Response`` class object

    """
    cfg_file = kwargs.get("filename", "umbrella.json")
    exclude = kwargs.get("exclude", None)

    api_uri = (
        "https://reports.api.umbrella.com/v1/organizations"
        + "/{}/destinations/{}/identities".format(
            get_orgid(orgid, filename=cfg_file), destination
        )
    )
    ident_response = send_get(
        url=api_uri, headers=get_headers(cred, filename=cfg_file)
    )
    if ident_response.status_code == 200:
        table = json_to_table(
            json.loads(ident_response.text)["identities"], exclude_col=exclude
        )
        print(
            tabulate(
                table[1:], headers=table[0], tablefmt=kwargs.get("format")
            )
        )
    return ident_response


def recent(destination, cred=None, orgid=None, offset=0, **kwargs):
    """Request the most recent DNS requests for a particular destination.

    Parameters:
        destination (str): a domain name specified without any
        orgid (str): Cisco Umbrella organization ID protocol or
            delimiters
        limit (int): number of requests for the specified
            destination returned
        offset (int): changes which index the list of returned
            orgs starts at. Default is 0, and orgs are listed in
            reverse alphabetical order. Offset essentially allows
            for pagination. If the first set of results shows 50,
            then offset=50 shows the next fifty and offset=100 shows
            the next fifty after that.

    Returns:
        requests.Response: Return ``requests.Response`` class object

    """
    cfg_file = kwargs.get("filename", "umbrella.json")
    exclude = kwargs.get("exclude", None)
    limit = kwargs.get("limit", 10)

    api_uri = (
        "https://reports.api.umbrella.com/v1/organizations"
        + "/{}/destinations/{}/activity?limit={}&offset={}".format(
            get_orgid(orgid, filename=cfg_file), destination, limit, offset
        )
    )
    recent_response = send_get(
        url=api_uri, headers=get_headers(cred, filename=cfg_file)
    )
    if recent_response.status_code == 200:
        table = json_to_table(
            json.loads(recent_response.text)["requests"], exclude_col=exclude
        )
        print(
            tabulate(
                table[1:], headers=table[0], tablefmt=kwargs.get("format")
            )
        )
    return recent_response


def main():
    """Test if executed directly."""
    activity()
    # top_identities("github.com", filename="umbrella.json")
    # recent("discordapp.com", orgid=None, limit=20, filename="umbrella.json")


if __name__ == "__main__":
    main()
