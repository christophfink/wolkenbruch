#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Copyright (C) 2019 Christoph Fink, University of Helsinki
#
#   This program is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation; either version 3
#   of the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, see <http://www.gnu.org/licenses/>.
""" Checks the forecast precipitation rate for the next 14h and sends
    an e-mail to remind me to take my rain gear with me """

__all__ = [
    "main",
    "__version__"
]

from .__main__ import main
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
