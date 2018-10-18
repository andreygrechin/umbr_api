#!/usr/bin/env python3
"""Wrapper for request module calls."""

import json

import requests
from logzero import logger


def send_get(url, headers=None):
    """Send HTTP GET request via 'requests' module."""
    return send_any('GET', url, headers)


def send_any(method, url, headers=None, data=None):
    """Send HTTP request via 'requests' module."""
    assert url
    assert isinstance(url, str)
    logger.info('Requesting: %s', url)
    if headers:
        logger.debug('Headers to send: %s', str(headers))
    if data:
        logger.debug('Data to send: %s', str(data))

    try:
        response = requests.request(method, url, headers=headers, data=data)
    except requests.exceptions.RequestException as err_msg:
        logger.exception(err_msg)
        response = None
    else:
        if not response.ok:
            logger.warning('Response code: %d', response.status_code)
            logger.warning('Response body: %d', response.text)
            logger.warning('Response headers: %d', response.headers)
        response_logging(response)

    return response


def send_post(url, data=None, headers=None):
    """Send HTTP POST request via 'requests' module."""
    return send_any('POST', url, data=data, headers=headers)


def send_delete(url, headers=None):
    """Send HTTP DELETE request via 'requests' module."""
    return send_any('DELETE', url, headers=headers)


def response_logging(response):
    """Log responses."""
    logger.info('Response code: %d', response.status_code)
    logger.info('Response headers: %s', str(response.headers)[:100])
    logger.debug(
        'Response headers:\n%s',
        json.dumps(dict(response.headers), indent=4)
        )
    logger.info('Response: %s', response.text[:100])
    if response.text:
        logger.debug(
            'Response:\n%s',
            json.dumps(json.loads(response.text), indent=4)
            )
    else:
        logger.debug('Response: <empty>')


if __name__ == '__main__':
    pass
