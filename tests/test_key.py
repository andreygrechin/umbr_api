#!/usr/bin/env python3
# pylint: disable=R0201
"""Test unit."""

import unittest


class TestCase(unittest.TestCase):
    """Main class."""

    def test_get_key_from_api_call(self):
        """Check if key returns."""
        from umbr_api._key import get_key
        assert get_key(key='123456789012345678901234567890123456') == \
            '123456789012345678901234567890123456'

    def test_get_key_from_file(self):
        """Check if key will be read from the file."""
        from umbr_api._key import get_key
        assert get_key(filename='customer_key_example.json') == \
            'YOUR-CUSTOMER-KEY-IS-HERE-0123456789'

    def test_key_incorrect_chars(self):
        """Check for incorrect chars in the key."""
        from umbr_api._key import get_key
        with self.assertRaises(SystemExit) as expected_exc:
            get_key(key='12345678901234567890123456789012345+')
        self.assertEqual(expected_exc.exception.code, 1)

    def test_wrong_file(self):
        """Check if non existing json file was provided."""
        from umbr_api._key import get_key
        with self.assertRaises(SystemExit) as expected_exc:
            get_key(key=None, filename='unique12345.json')
            # check exit code
        self.assertEqual(expected_exc.exception.code, 2)

    def test_key_length_1(self):
        """Check for a longer key."""
        from umbr_api._key import get_key
        with self.assertRaises(SystemExit) as expected_exc:
            get_key(key='1234567890123456789012345678901234567')
        self.assertEqual(expected_exc.exception.code, 1)

    def test_key_length_2(self):
        """Check for a shorter key."""
        from umbr_api._key import get_key
        with self.assertRaises(SystemExit) as expected_exc:
            get_key(key='12345678901234567890123456789012345')
        self.assertEqual(expected_exc.exception.code, 1)

    def test_key_1(self):
        """Check reading from file if empty key as a str."""
        from umbr_api._key import get_key
        assert get_key(key='', filename='customer_key_example.json') == \
            'YOUR-CUSTOMER-KEY-IS-HERE-0123456789'

    def test_key_2(self):
        """Check reading from file if key=None."""
        from umbr_api._key import get_key
        assert get_key(key=None, filename='customer_key_example.json') == \
            'YOUR-CUSTOMER-KEY-IS-HERE-0123456789'

    def test_incorrect_json(self):
        """Check if incorrect json was provided."""
        import os.path
        from unittest import mock

        from umbr_api._key import get_key

        json_test_file = os.path.join(os.path.dirname(__file__),
                                      'data', 'customer_key_incorrect.json')

        with mock.patch('os.path.join') as mock_path_join:
            mock_path_join.return_value = json_test_file

            with self.assertRaises(SystemExit) as expected_exc:
                get_key(filename='customer_key_incorrect.json')
                # check exit code
            self.assertEqual(expected_exc.exception.code, 1)

    def test_main(self):
        """Check main() from _key module."""
        from umbr_api._key import main
        main()


if __name__ == '__main__':
    unittest.main()
