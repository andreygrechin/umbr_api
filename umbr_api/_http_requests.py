#!/usr/bin/env python3
"""Wrapper for request module calls."""

import requests
from logzero import logger


def send_get(url):
    """Send HTTP GET request via 'requests' module."""
    assert url
    assert isinstance(url, str)
    logger.info('Requesting: %s', url)

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as err_msg:
        logger.exception(err_msg)
        response = None
    else:
        response_logging(response)

    return response


def send_post(url, data=None, headers=None):
    """Send HTTP POST request via 'requests' module."""
    assert url
    assert isinstance(url, str)
    logger.info('Requesting: %s', url)
    logger.debug('Data to send: %s', str(data))
    logger.debug('Headers to send: %s', str(headers))
    try:
        response = requests.post(url,
                                 data=data,
                                 headers=headers)
    except requests.exceptions.RequestException as err_msg:
        logger.exception(err_msg)
        response = None
    else:
        response_logging(response)

    return response


def send_delete(url, headers=None):
    """Send HTTP DELETE request via 'requests' module."""
    assert url
    assert isinstance(url, str)
    logger.info('Requesting: %s', url)
    logger.debug('Headers to send: %s', str(headers))
    try:
        response = requests.delete(url, headers=headers)
    except requests.exceptions.RequestException as err_msg:
        logger.exception(err_msg)
        response = None
    else:
        response_logging(response)

    return response


def response_logging(response):
    """Log responses."""
    logger.info('Response code: %d', response.status_code)
    logger.info('Response headers: %s', str(response.headers)[:100])
    logger.debug('Response headers:\n%s', str(response.headers))
    logger.info('Response: %s', response.text[:100])
    logger.debug('Response:\n%s', response.text)


if __name__ == '__main__':
    pass
