#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_robtex_python
----------------------------------

Tests for `robtex_python` module.
"""

import os
import docopt
import pytest



from robtex_python import robtex_python
from robtex_python import cli


@pytest.fixture
def absolute_path():
    """Return an absolute path (which is useful for running tests)."""
    # return os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(absolute_path, response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
@pytest.fixture
def command_line_args():
    """Function to simulate command line arguments using docopt."""
    args = dict()

    # TODO: Add command line arguments here (see: https://github.com/docopt/docopt#api)

    return args


def test_command_line_interface(command_line_args):
    """Test the command line usage of this project."""
    # TODO: Add more robust testing here
    with pytest.raises(docopt.DocoptExit) as exc_info:
        cli.main()

    # get the error message
    error_message = exc_info.value
    # make sure the error message contains the expected usage output
    assert "Usage:" in str(error_message)
