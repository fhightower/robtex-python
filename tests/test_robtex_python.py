"""
test_robtex_python
----------------------------------

Tests for `robtex_python` module.
"""

import pytest

import robtex_python


@pytest.fixture
def command_line_args():
    """Function to simulate command line arguments using docopt."""
    args = dict()

    args['ip'] = "8.8.8.8"
    args['asn'] = "15169"
    args['host'] = "example.com"

    return args


def test_ip_query(command_line_args):
    """Test the ip query."""
    response = robtex_python.ip_query(command_line_args['ip'])

    assert response['status'] == "ok"
    assert response['city'] == "Mountain View"


def test_as_query(command_line_args):
    """Test the asn query."""
    response = robtex_python.as_query(command_line_args['asn'])

    assert response['status'] == "ok"


def test_pdns_forward_query(command_line_args):
    """Test the pdns forward query."""
    response = robtex_python.pdns_forward(command_line_args['host'])

    assert len(response) > 1
    assert response[0]['rrname'] == command_line_args['host']


def test_pdns_reverse_query(command_line_args):
    """Test the pdns reverse query."""
    response = robtex_python.pdns_reverse(command_line_args['ip'])

    assert len(response) > 1
    assert response[0]['rrdata'] == command_line_args['ip']
