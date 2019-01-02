#!/usr/bin/env python3
# pylint: disable=R0201
"""Test unit."""

import unittest
from offline_utils import FakeResponse


class TestCaseMocking(unittest.TestCase):
    """Main class."""

    def test_remove_activity(self):
        """Call main."""
        from unittest import mock
        from umbr_api.reporting import activity

        my_response = FakeResponse('data/templates/reporting/case1')

        with mock.patch('requests.request') as mock_requests_post:
            mock_requests_post.return_value = my_response
            response = activity(filename="umbrella_example.json")
        assert response.status_code == my_response.status_code

    def test_top_identities(self):
        """Call main."""
        from unittest import mock
        from umbr_api.reporting import top_identities

        my_response = FakeResponse('data/templates/reporting/case2')

        with mock.patch('requests.request') as mock_requests_post:
            mock_requests_post.return_value = my_response
            response = top_identities(
                "cisco.com", filename="umbrella_example.json"
            )
        assert response.status_code == my_response.status_code

    def test_recent(self):
        """Call main."""
        from unittest import mock
        from umbr_api.reporting import recent

        my_response = FakeResponse('data/templates/reporting/case3')

        with mock.patch('requests.request') as mock_requests_post:
            mock_requests_post.return_value = my_response
            response = recent(
                "cisco.com", filename="umbrella_example.json"
            )
        assert response.status_code == my_response.status_code


if __name__ == '__main__':
    unittest.main()
