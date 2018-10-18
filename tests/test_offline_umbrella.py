#!/usr/bin/env python3
"""Test unit."""

import unittest
from offline_utils import FakeResponse

FAKE_KEY = 'YOUR-CUSTOMER-KEY-IS-HERE-0123456789'


class TestCaseMocking(unittest.TestCase):
    """Main class."""

    def test_umbrella_main_get(self):
        """Call main."""
        import argparse
        from unittest import mock
        from umbr_api.umbrella import main

        my_response = FakeResponse('data/templates/get/case1')

        args = argparse.Namespace(
            command='get',
            key=FAKE_KEY,
            max_records=2,
            verbose=2,
            )

        with mock.patch('requests.request') as mock_requests_post:
            mock_requests_post.return_value = my_response

            with self.assertRaises(SystemExit) as expected_exc:
                main(args)
        self.assertEqual(expected_exc.exception.code, 200)

    def test_umbrella_main_keyring(self):
        """Call main."""
        import argparse
        from umbr_api.umbrella import main

        args = argparse.Namespace(
            command='keyring',
            key_to_add=None,
            show_enforcement=True,
            verbose=0,
            )

        with self.assertRaises(SystemExit) as expected_exc:
            main(args)
        self.assertTrue(
            expected_exc.exception.code == 0 or
            expected_exc.exception.code == 1
            )


if __name__ == '__main__':
    unittest.main()
