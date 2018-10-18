#!/usr/bin/env python3
# pylint: disable=R0201
"""Test unit."""

import unittest


class OfflineTestCase(unittest.TestCase):
    """Main class."""

    def test_base64(self):
        """Test."""
        from umbr_api.credentials import get_base64

        assert get_base64(
            cred="Aladdin:OpenSesame",
            api="management"
        ) == "QWxhZGRpbjpPcGVuU2VzYW1l"

        assert get_base64(
            filename="umbrella_example.json",
            api="management"
        ) == "WW91cktleUlzSGVyZTpZb3VyU2VjcmV0SXNIZXJl"

        assert get_base64(
            cred="Aladdin:OpenSesame",
            filename="umbrella_example.json",
            api="management"
        ) == "QWxhZGRpbjpPcGVuU2VzYW1l"

    def test_get_orgid(self):
        """Test."""
        from umbr_api.credentials import get_orgid

        assert get_orgid(filename='umbrella_example.json') == \
            '0000000'

        assert get_orgid(
            orgid="TestTest",
            filename="umbrella_example.json"
        ) == 'TestTest'


if __name__ == '__main__':
    unittest.main()
