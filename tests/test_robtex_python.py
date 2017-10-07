#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_robtex_python
----------------------------------

Tests for `robtex_python` module.
"""

import docopt
import pytest

from robtex_python import robtex_python
from robtex_python import cli


@pytest.fixture
def command_line_args():
    """Function to simulate command line arguments using docopt."""
    args = dict()

    args['ip'] = "8.8.8.8"
    args['asn'] = "15169"
    args['host'] = "example.com"

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


def test_ip_query(command_line_args):
    """Test the command line usage of this project."""
    response = robtex_python.ip_query(command_line_args['ip'])

    assert response['status'] == "ok"
    assert response['city'] == "Mountain View"


def test_as_query(command_line_args):
    """Test the command line usage of this project."""
    response = robtex_python.as_query(command_line_args['asn'])

    assert response['status'] == "ok"


def test_pdns_forward_query(command_line_args):
    """Test the command line usage of this project."""
    response = robtex_python.pdns_forward(command_line_args['host'])

    assert len(response) > 1
    assert response[0]['rrname'] == command_line_args['host']


def test_pdns_reverse_query(command_line_args):
    """Test the command line usage of this project."""
    response = robtex_python.pdns_reverse(command_line_args['ip'])

    assert len(response) > 1
    assert response[0]['rrdata'] == command_line_args['ip']
