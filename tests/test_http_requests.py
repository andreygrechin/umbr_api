#!/usr/bin/env python3
# pylint: disable=R0201
"""Test unit."""

import unittest


class TestCase(unittest.TestCase):
    """Main class."""

    def test_send_post(self):
        """Call incorrect send_post, get None."""  # import requests
        from umbr_api._http_requests import send_post

        response = send_post(" ")
        self.assertEqual(response, None)

    def test_send_get(self):
        """Call incorrect send_get, get None."""  # import requests
        from umbr_api._http_requests import send_get

        response = send_get(" ")
        self.assertEqual(response, None)

    def test_send_delete(self):
        """Call incorrect send_delete, get None."""  # import requests
        from umbr_api._http_requests import send_delete

        response = send_delete(" ")
        self.assertEqual(response, None)


if __name__ == "__main__":
    unittest.main()
