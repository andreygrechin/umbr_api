#!/usr/bin/env python3
# pylint: disable=R0201
"""Test unit."""

import unittest
from ast import literal_eval
import os

FAKE_KEY = 'YOUR-CUSTOMER-KEY-IS-HERE-0123456789'


# pylint: disable=R0903
class FakeResponse():
    """To mimic ``requests`` response obj."""

    def __init__(self, code, headers, body_txt):
        """Create fake class."""
        self.status_code = code
        self.headers = headers
        self.text = body_txt


class TestCaseMocking(unittest.TestCase):
    """Main class."""

    def test_add_main(self):
        """Call main."""
        from unittest import mock
        from umbr_api.add import main

        status_code_file = os.path.join(os.path.dirname(__file__),
                                        'data/templates/add/case1',
                                        'code.txt')
        body_file = os.path.join(os.path.dirname(__file__),
                                 'data/templates/add/case1',
                                 'body.json')
        headers_file = os.path.join(os.path.dirname(__file__),
                                    'data/templates/add/case1',
                                    'headers.json')
        with open(status_code_file) as file:
            status_code = int(file.read())
        with open(headers_file) as file:
            headers = literal_eval(file.read())
        with open(body_file) as file:
            body_text = file.read()

        my_response = FakeResponse(status_code, headers, body_text)

        with mock.patch('requests.request') as mock_requests_post:
            mock_requests_post.return_value = my_response
            main(test_key=FAKE_KEY)

    def test_add(self):
        """Call main."""
        from unittest import mock
        import umbr_api

        status_code_file = os.path.join(os.path.dirname(__file__),
                                        'data/templates/add/case1',
                                        'code.txt')
        body_file = os.path.join(os.path.dirname(__file__),
                                 'data/templates/add/case1',
                                 'body.json')
        headers_file = os.path.join(os.path.dirname(__file__),
                                    'data/templates/add/case1',
                                    'headers.json')
        with open(status_code_file) as file:
            status_code = int(file.read())
        with open(headers_file) as file:
            headers = literal_eval(file.read())
        with open(body_file) as file:
            body_text = file.read()

        my_response = FakeResponse(status_code, headers, body_text)

        with mock.patch('requests.request') as mock_requests_post:
            mock_requests_post.return_value = my_response
            response = umbr_api.add(domain='example.com', url='example.com',
                                    key=FAKE_KEY,
                                    bypass=False)
        assert response.status_code == status_code

    def test_add_fail(self):
        """Call add to fail."""
        from unittest import mock
        import umbr_api

        status_code_file = os.path.join(os.path.dirname(__file__),
                                        'data/templates/add/case2',
                                        'code.txt')
        body_file = os.path.join(os.path.dirname(__file__),
                                 'data/templates/add/case2',
                                 'body.json')
        headers_file = os.path.join(os.path.dirname(__file__),
                                    'data/templates/add/case2',
                                    'headers.json')
        with open(status_code_file) as file:
            status_code = int(file.read())
        with open(headers_file) as file:
            headers = literal_eval(file.read())
        with open(body_file) as file:
            body_text = file.read()

        my_response = FakeResponse(status_code, headers, body_text)

        with mock.patch('requests.request') as mock_requests_post:
            mock_requests_post.return_value = my_response
            response = umbr_api.add(domain='example.com', url='2example.com',
                                    key=FAKE_KEY,
                                    bypass=True)
        assert response.status_code == status_code


if __name__ == '__main__':
    unittest.main()
