#!/usr/bin/env python3
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

    # pylint: disable=R0914
    def test_umbrella_main(self):
        """Call main."""
        import argparse
        from unittest import mock
        from umbr_api.umbrella import main

        status_code_file = os.path.join(os.path.dirname(__file__),
                                        'data/templates/get/case1',
                                        'code.txt')
        body_file = os.path.join(os.path.dirname(__file__),
                                 'data/templates/get/case1',
                                 'body.json')
        headers_file = os.path.join(os.path.dirname(__file__),
                                    'data/templates/get/case1',
                                    'headers.json')
        with open(status_code_file) as file:
            status_code = int(file.read())
        with open(headers_file) as file:
            headers = literal_eval(file.read())
        with open(body_file) as file:
            body_text = file.read()

        my_response = FakeResponse(status_code, headers, body_text)

        args = argparse.Namespace(add=None, get_list=2,
                                  key=['YOUR-CUSTOMER-KEY-IS-HERE-0123456789'],
                                  keyring_add=None, remove_domain=None,
                                  remove_id=None, verbose=2, version=False)

        with mock.patch('requests.request') as mock_requests_post:
            mock_requests_post.return_value = my_response

            with self.assertRaises(SystemExit) as expected_exc:
                main(args)
        self.assertEqual(expected_exc.exception.code, 200)


if __name__ == '__main__':
    unittest.main()
