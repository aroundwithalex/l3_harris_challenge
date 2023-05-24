"""
Unit tests for search.py

This module contains unit tests for search.py. It ensures that the
methods work as expected.

Typical Usage:
    $ pytest -v
"""

import pytest

from src.search import Searcher

@pytest.fixture
def setup():
    """
    Creates an object for testing

    This method instantiates the Searcher object in memory
    so it can be used in relevant unit tests.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    search = Searcher()
    return search

def test_find_distances(setup):
    """
    Tests find_distances method

    This method tests the find_distances method. It ensures that
    the method finds the closest distance from longitude and latitude
    co-ordinates.

    Args:
        setup -> pytest fixture
    
    Returns:
        None
    
    Raises:
        None
    """

    lat = 52.772078
    long = -1.664884

    setup.find_distances(long, lat)

    assert len(setup.distances) == 59

def test_find_closest_airport(setup):
    """
    Tests find_closest_airport method

    This method tests the find_closest_airport method to ensure that
    it returns the closest airport to the co-ordinates.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """
    lat = 52.772078
    long = -1.664884

    setup.find_distances(long, lat)

    result = setup.find_closest_airport()
    assert isinstance(result, list) and len(result) == 5
