# coding=utf-8
from __future__ import absolute_import, division, print_function, \
  unicode_literals

DEFAULT_PORT = 14265

# Make some imports accessible from the top level of the package.
# noinspection PyUnresolvedReferences
from .adapter import *
# noinspection PyUnresolvedReferences
from .api import *


# Don't forget to update version number in setup.py!
__version__ = '1.0.0'
