"""
CLI for finding the nearest airport

This module contains a Command Line Interface for finding the closest
airport. It contains a method for printing the result to the Console.

Typical Usage:
    $ airport --lat 51.012 --long 1.234
"""

import click
from rich.console import Console
from rich.table import Table

from search import Searcher


@click.command()
@click.option("--long")
@click.option("--lat")
def closest(long, lat):
    """
    Returns the closest airport based on co-ordinates

    This function returns the closest airport based on co-ordinates provided
    by the user. It renders a table containing the relevant data.

    Args:
        long -> Supplied longitude
        lat -> Supplied latitude

    Returns:
        None

    Raises:
        None
    """

    search = Searcher()
    search.find_distances(long, lat)
    data = search.find_closest_airport()

    table = Table(title="Closest Airport")
    table.add_column("Airport Name")
    table.add_column("ICAO")
    table.add_column("Latitude")
    table.add_column("Longitude")
    table.add_column("Distance (km)")

    table.add_row(
        str(data[0]), str(data[1]), str(data[2]), str(data[3]), f"{data[4]:.2f}"
    )

    console = Console()
    console.print(table)

    return 0
