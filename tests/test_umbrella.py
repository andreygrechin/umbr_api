#!/usr/bin/env python3
# pylint: disable=R0201
"""Test unit."""

import unittest


class TestCase(unittest.TestCase):
    """Main online class."""

    def test_with_empty_args(self):
        """User passes no args, should exit with SystemExit."""
        from umbr_api.umbrella import create_parser

        # pylint: disable=W0612
        with self.assertRaises(SystemExit) as expected_exc:
            create_parser()
        # cannot use for tests under diff environments
        self.assertIsNotNone(expected_exc.exception.code)

    def test_verbose_level(self):
        """User passes no args, should exit with SystemExit."""
        import argparse
        from unittest import mock
        from umbr_api.umbrella import main

        args = argparse.Namespace(command=None, verbose=1)

        with mock.patch(
            "umbr_api.umbrella.create_parser"
        ) as mock_create_parser:

            mock_create_parser.return_value = args
            with self.assertRaises(SystemExit) as expected_exc:
                main()
            self.assertEqual(expected_exc.exception.code, 0)


class OnlineTestCase(unittest.TestCase):
    """Main online class."""

    def test_keyring_general(self):
        """Save a key in the keyring, read back and compare."""
        import keyring
        import umbr_api
        from umbr_api.umbrella import save_key
        from umbr_api.credentials import get_key

        # check existing key
        old_key = get_key(keyring.get_password("python", umbr_api.__title__))

        # save new test key
        code = save_key("YOUR-CUSTOMER-KEY-IS-HERE-0123456789", "test")
        assert code == 0

        code = save_key(old_key, "test")
        assert code == 0

    def test_get(self):
        """User passes '--get', should exit with SystemExit(0)."""
        import argparse
        from unittest import mock
        from umbr_api.umbrella import main

        args = argparse.Namespace(
            command="get", key=None, max_records=5, verbose=2
        )

        with mock.patch(
            "umbr_api.umbrella.create_parser"
        ) as mock_create_parser:

            mock_create_parser.return_value = args
            with self.assertRaises(SystemExit) as expected_exc:
                main()
            self.assertEqual(expected_exc.exception.code, 200)

    def test_get_fail(self):
        """User passes '--get 201', should exit with SystemExit(400)."""
        import argparse
        from unittest import mock
        from umbr_api.umbrella import main

        args = argparse.Namespace(
            command="get", key=None, max_records=201, verbose=2
        )

        with mock.patch(
            "umbr_api.umbrella.create_parser"
        ) as mock_create_parser:

            mock_create_parser.return_value = args
            with self.assertRaises(SystemExit) as expected_exc:
                main()
            self.assertEqual(expected_exc.exception.code, 400)


if __name__ == "__main__":
    unittest.main()
