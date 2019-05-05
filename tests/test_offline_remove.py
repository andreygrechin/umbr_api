#!/usr/bin/env python3
# pylint: disable=R0201
"""Test unit."""

import unittest

from offline_utils import FakeResponse

FAKE_KEY = "YOUR-CUSTOMER-KEY-IS-HERE-0123456789"


class TestCaseMocking(unittest.TestCase):
    """Main class."""

    def test_remove_main(self):
        """Call main."""
        from unittest import mock
        from umbr_api.remove import main

        my_response = FakeResponse("data/templates/remove/case1")

        with mock.patch("requests.request") as mock_requests_post:
            mock_requests_post.return_value = my_response
            main(test_key=FAKE_KEY)

    def test_remove(self):
        """Call main."""
        from unittest import mock
        import umbr_api

        my_response = FakeResponse("data/templates/remove/case1")

        with mock.patch("requests.request") as mock_requests_post:
            mock_requests_post.return_value = my_response
            response = umbr_api.remove(record_id="29765170", key=FAKE_KEY)
        assert response.status_code == my_response.status_code

    def test_remove_fail(self):
        """Call add to fail."""
        from unittest import mock
        import umbr_api

        my_response = FakeResponse("data/templates/remove/case2")

        with mock.patch("requests.request") as mock_requests_post:
            mock_requests_post.return_value = my_response
            response = umbr_api.remove(
                record_id="www.example.com", key=FAKE_KEY
            )
        assert response.status_code == my_response.status_code


if __name__ == "__main__":
    unittest.main()
