#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys

import pictogram


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print("This is the main routine.")
    print("It should do something interesting.")

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.


if __name__ == "__main__":
    main()
