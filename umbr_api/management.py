#!/usr/bin/env python3
"""API calls to Umbrella Management API.

References:
    https://docs.umbrella.com/umbrella-api/v1.0/reference

"""

import json

from logzero import logger
from tabulate import tabulate

from umbr_api.credentials import get_base64, get_orgid
from umbr_api._http_requests import send_get


# pylint: disable = R0913
def management_api(
        command, orgid=None, cred=None, limit=10, page=1, **kwargs):
    """Send a command to Umbrella Management API."""
    assert command in [
        "networks",
        "roamingcomputers",
        "internalnetworks",
        "virtualappliances",
        "sites",
        "users",
        "roles"
    ]

    console = kwargs.get("console", True)
    cfg_file = kwargs.get("filename", "umbrella.json")

    api_uri = "https://management.api.umbrella.com/v1/organizations" + \
        "/{}/{}?limit={}&page={}".format(
            get_orgid(orgid, filename=cfg_file),
            command,
            limit,
            page,
        )
    response = send_get(
        url=api_uri,
        headers={
            "Authorization": "Basic {}".format(
                get_base64(cred=cred, filename=cfg_file, api="management")
            )
        },
    )

    if response.status_code == 200:
        if console:
            table = json_to_table(json.loads(response.text))
            print(tabulate(table[1:], headers=table[0], tablefmt="simple"))
    else:
        logger.error(
            'HTTP Status code: %s\n%s',
            response.status_code,
            response.text
        )
    return response


def json_to_table(_json):
    """Convert json object to table."""
    table = list()
    for row in _json:
        line = list()
        headers = list()
        for attribute, value in row.items():
            if isinstance(value, dict):
                for sub_element, sub_value in value.items():
                    headers.append("\n".join([attribute, sub_element]))
                    if isinstance(sub_value, list):
                        line.append('\n'.join(sub_value))
                    else:
                        line.append(sub_value)
            else:
                if isinstance(value, list):
                    line.append('\n'.join(value))
                else:
                    line.append(value)
                headers.append(attribute)
        table.append(line)
    table.insert(0, headers)
    return table


def networks(**kwargs):
    """Request networks info."""
    return management_api("networks", **kwargs)


def roamingcomputers(**kwargs):
    """Request roaming computers info."""
    return management_api("roamingcomputers", **kwargs)


def internalnetworks(**kwargs):
    """Request internal networks info."""
    return management_api("internalnetworks", **kwargs)


def virtualappliances(**kwargs):
    """Request virtual appliances info."""
    return management_api("virtualappliances", **kwargs)


def sites(**kwargs):
    """Request sites info."""
    return management_api("sites", **kwargs)


def users(**kwargs):
    """Request users info."""
    return management_api("users", **kwargs)


def roles(**kwargs):
    """Request roles info."""
    return management_api("roles", **kwargs)


def main():
    """Test if executed directly."""
    networks(limit=20, orgid="")
    # roamingcomputers()
    # internalnetworks()
    # virtualappliances()
    # sites()
    # users()
    # roles()


if __name__ == '__main__':
    main()
