#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Robtex Python.

Usage:
    # TODO: Add usage instructions here
    robtex_python ship new <name>...
    robtex_python ship <name> move <x> <y> [--speed=<kn>]
    robtex_python ship shoot <x> <y>
    robtex_python mine (set|remove) <x> <y> [--moored | --drifting]
    robtex_python (-h | --help)
    robtex_python --version

Options:
    -h --help     Show this screen.
    --version     Show version.
    # TODO: Add options here
    --speed=<kn>  Speed in knots [default: 10].
    --moored      Moored (anchored) mine.
    --drifting    Drifting mine.
"""

from docopt import docopt

from .__init__ import __version__ as VERSION


def main(args=None):
    """Console script for robtex_python"""
    arguments = docopt(__doc__, version=VERSION)
    print(arguments)
    print("You can modify the output of the CLI by making changes to robtex_python.cli.main .")


if __name__ == "__main__":
    main()