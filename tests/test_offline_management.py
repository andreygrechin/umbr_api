#!/usr/bin/env python3
# pylint: disable=no-self-use
"""Test unit."""

import unittest

from offline_utils import FakeResponse


class TestCaseMocking(unittest.TestCase):
    """Main class."""

    def test_management_networks(self):
        """Call main."""
        from unittest import mock
        from umbr_api.management import networks

        my_response = FakeResponse("data/templates/management/case2")

        with mock.patch("requests.request") as mock_requests_post:
            mock_requests_post.return_value = my_response
            response = networks(filename="umbrella_example.json")
        assert response.status_code == my_response.status_code

    def test_virtualappliances(self):
        """Call main."""
        from unittest import mock
        from umbr_api.management import virtualappliances

        my_response = FakeResponse("data/templates/management/case3")

        with mock.patch("requests.request") as mock_requests_post:
            mock_requests_post.return_value = my_response
            response = virtualappliances(filename="umbrella_example.json")
        assert response.status_code == my_response.status_code


if __name__ == "__main__":
    unittest.main()
