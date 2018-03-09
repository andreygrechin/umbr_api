#!/usr/bin/env python3
"""Init."""

from .__about__ import (
    __author__, __copyright__, __email__, __license__, __summary__, __title__,
    __uri__, __version__
)
from .get import get_list
from .add import add
from .remove import remove

__all__ = (
    '__title__', '__summary__', '__uri__', '__version__', '__author__',
    '__email__', '__license__', '__copyright__',
)
