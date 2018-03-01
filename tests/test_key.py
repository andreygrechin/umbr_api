#!/usr/bin/env python3
# pylint: disable=R0201
"""Test unit."""

import unittest


class TestKey(unittest.TestCase):
    """Main class."""

    def test_get_key_direct(self):
        """Check if key returns."""
        from umbr_api._key import get_key
        assert get_key(key='123456789012345678901234567890123456') == \
            '123456789012345678901234567890123456'

    def test_get_key_from_file(self):
        """Check if key will be read from the file."""
        from umbr_api._key import get_key
        assert get_key(filename='customer_key_example.json') == \
            'YOUR-CUSTOMER-KEY-IS-HERE-0123456789'

    def test_strings_a_3(self):
        """Check for incorrect chars in the key."""
        from umbr_api._key import get_key
        self.assertRaises(AssertionError, get_key,
                          key='12345678901234567890123456789012345+')

    def test_strings_a_4(self):
        """Check for a longer key."""
        from umbr_api._key import get_key
        self.assertRaises(AssertionError, get_key,
                          key='1234567890123456789012345678901234567')

    def test_strings_a_5(self):
        """Check for a shorter key."""
        from umbr_api._key import get_key
        self.assertRaises(AssertionError, get_key,
                          key='12345678901234567890123456789012345')


if __name__ == '__main__':
    unittest.main()
