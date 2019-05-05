#!/usr/bin/env python3
# pylint: disable=R0201
"""Test unit."""

import unittest


class OnlineKeyringTestCase(unittest.TestCase):
    """Test the keyring."""

    def test_keyring_general_online(self):
        """Save a key in the keyring, read back and compare."""
        import keyring

        keyring.set_password("umbr_api_test", "username2", "password123")
        read = keyring.get_password("umbr_api_test", "username2")
        assert read == "password123"


if __name__ == "__main__":
    unittest.main()
