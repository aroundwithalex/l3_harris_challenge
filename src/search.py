"""
Searches a CSV file for the closest long/lat match

This module contains methods that search a CSV file for the closest
longitude and latitude match. It then returns that match to the CLI.

Typical Usage:
    >>> from src.search import Searcher
    >>> search = Searcher()
    >>> search.find_closest_airport(51.091, 1.234)
"""
from os import path
import warnings

import pandas
from geopy import Point, distance


class Searcher:
    """
    Returns the closest airport to the users location

    This class contains various methods to match a users longitude and
    latitude to their closest airport. It then returns the result.

    Attributes:
        coords_df -> Airports co-ordinates DataFrame
        distances -> List of distances 
    """
    def __init__(self):
        """
        Constructor for Searcher object

        This method takes a file path and passes into Pandas so that a
        DataFrame can be created. It then saves this as an instance
        variable.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """

        file_path = path.join(path.abspath("."), "data", "uk_airport_coords.csv")
        if not path.exists(file_path):
            raise FileNotFoundError(f"{file_path} does not exist. Please add.")
        
        self.coords_df = pandas.read_csv(file_path)

        self.distances = []

    def find_distances(self, long, lat):
        """
        Finds distances between two co-ordinates

        This method finds the distance between two co-ordinates. It returns
        the value in kilometers and appends to a relevant list.

        Args:
            long -> Longitude
            lat -> Latitude

        Returns:
            Closest airport and related data

        Raises:
            None
        """
        
        user_location = Point(lat, long)
        latlong_df = self.coords_df[["Latitude", "Longitude"]]
        for row in latlong_df.iterrows():
            lat, long = row[1].values[0], row[1].values[1]
            airport_location = Point(lat, long)
            dist = distance.distance(user_location, airport_location).km
            self.distances.append(dist)

        return self.distances

    def find_closest_airport(self):
        """
        Returns the closest airport to the user

        This method returns the closest airport to the user. It does this by
        appending the distances to the DataFrame and finding the smallest one.

        Args:
            distances -> Distances to add to the DataFrame

        Returns:
            Closest airport


        Raises:
            None
        """

        self.coords_df["distance"] = self.distances
        closest_airport = self.coords_df.sort_values(by=["distance"]).iloc[0]

        return closest_airport.to_list()
