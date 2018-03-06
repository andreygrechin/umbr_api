#!/usr/bin/env python3
# pylint: disable=R0201
"""Test unit."""

import unittest


class OnlineTestCase(unittest.TestCase):
    """Main class."""

    # def test_default(self):
    #     """Call get_list() with default args."""
    #     import umbr_api
    #     umbr_api.remove.remove(record_id=None, domain_name=None, key=None)

    def test_main(self):
        """Call main."""
        from umbr_api.remove import main
        main()


if __name__ == '__main__':
    unittest.main()
