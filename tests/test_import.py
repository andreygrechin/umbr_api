#!/usr/bin/env python3
# pylint: disable=R0201, W0612
"""Test unit."""

import unittest


class TestKey(unittest.TestCase):
    """Main class."""

    def test_import_package(self):
        """Import of the package."""
        import umbr_api

    def test_import_modules(self):
        """Import of modules."""
        import umbr_api.add
        import umbr_api.get
        import umbr_api.remove

    def test_import_func(self):
        """Import of modules."""
        from umbr_api.add import add
        from umbr_api.get import get_list
        from umbr_api.remove import remove


if __name__ == '__main__':
    unittest.main()
