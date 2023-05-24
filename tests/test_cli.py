"""
Tests CLI commands

This module tests the CLI command that returns the result
of the closest airport search. 

Typical Usage
    $ pytest -v
"""

import os
from tempfile import TemporaryDirectory

import pytest

from click.testing import CliRunner
from src.cli import closest

@pytest.fixture
def setup():
    """
    Sets up the test environment

    Creates the CliRunner object so that it can be used
    in later tests:

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    runner = CliRunner()
    return runner

def test_closest_command(setup):
    """
    Tests the closest CLI command

    This method tests the closest CLI command. It ensures that
    it generates the correct output and exit code.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """

    result = setup.invoke(closest, ["--lat", "52.772078", "--long", "-1.664884"])
    assert "Closest Airport" in result.output
    assert result.exit_code == 0

def test_file_not_found_failure(setup):
    """
    Tests what happens if no co-ordinate file exists

    This test ensures that the CLI fails if no co-ordinate file is found
    in the expected place. 

    Args:
        setup -> pytest fixture
    
    Returns:
        None
    
    Raises:
        None
    """

    current_dir = os.getcwd()
    with TemporaryDirectory() as tempdir:
        os.chdir(tempdir)
        result = setup.invoke(closest, ["--lat", "52.772078", "--long", "-1.664884"])
        os.chdir(current_dir)
        assert "No such file" in result.output

def test_value_error_failure(setup):
    """
    Tests what happens if bad co-ordinates are passed

    This tests checks what happens when bad co-ordinates are passed to the CLI. IT
    ensures that an error is printed to the screen.
    
    Args:
        setup -> pytest fixture
    
    Returns:
        None
    
    Raises:
        None
    """

    result = setup.invoke(closest, ["--lat", "1000", "--long", "-10000"])
    assert "Error" in result.output

