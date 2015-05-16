#!/usr/bin/env python
# -*- coding: utf-8 -*-

# AUTHOR: Roberto Gea (Alquimista) <robertogea@openmailbox.org>
# VERSION: 0.1.0
# WEB: https://bitbucket.com/alquimista/pictogram
import os
import sys
print(os.path.abspath(".."))
try:
    from pictogram.filters import default
except ImportError:
    sys.path.insert(0, os.path.abspath(".."))
    from pictogram.filters import default


blur2 = default.blur()
