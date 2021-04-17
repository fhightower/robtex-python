"""
test_robtex_cli
----------------------------------

Tests for `robtex_python` cli interface.
"""

import docopt
import pytest

from robtex_python import cli


@pytest.fixture
def command_line_args():
    """Function to simulate command line arguments using docopt."""
    args = dict()

    args['ip'] = "8.8.8.8"
    args['asn'] = "15169"
    args['host'] = "example.com"

    return args


def test_blank_command_line():
    """Test the command line usage of this project."""
    with pytest.raises(docopt.DocoptExit) as exc_info:
        cli.main()

    # get the error message
    error_message = exc_info.value
    # make sure the error message contains the expected usage output
    assert "Usage:" in str(error_message)


def test_ip_query():
    """Test the command line usage of this project."""
    output = cli.main({'--ip': "8.8.8.8"})

    assert output['status'] == "ok"
    assert output['city'] == "Mountain View"


def test_as_query():
    """Test the asn query."""
    output = cli.main({'--as': "15169"})

    assert output['status'] == "ok"


def test_pdns_forward_query(command_line_args):
    """Test the pdns forward query."""
    output = cli.main({'--pdns-forward': "example.com"})

    assert len(output) > 1
    assert output[0]['rrname'] == command_line_args['host']


def test_pdns_reverse_query(command_line_args):
    """Test the pdns reverse query."""
    output = cli.main({'--pdns-reverse': "8.8.8.8"})

    assert len(output) > 1
    assert output[0]['rrdata'] == command_line_args['ip']
