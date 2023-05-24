"""
Tests CLI commands

This module tests the CLI command that returns the result
of the closest airport search. 

Typical Usage
    $ pytest -v
"""

from click.testing import CliRunner
from src.cli import closest
from src.search import Searcher

def test_closest_command():
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

    runner = CliRunner()
    result = runner.invoke(closest, ["--lat", "52.772078", "--long", "-1.664884"])
    assert "Closest Airport" in result.output
    assert result.exit_code == 0
