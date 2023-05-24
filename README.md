# L3Harris Technical Challenge

## Introduction

This repository contains the codebase for the L3Harris Technical Challenge. It locates the nearest
airport to a user based upon their provided co-ordinates, and prints the closest airport to the user
to the terminal.

## How to download the code

To download the code, you can clone the repository to your local machine by using `git clone`. To
install the repository locally, create a virtual environment within the root directory and install
the package using `pip install .`.  The required dependencies should be installed automatically. 

## How to run the code

To run the code after installation, you should be able to utilise the following command: -

`$ airports --lat 51.123 --long -1.23455`

This should cause a table to be printed to your console, which contains details about the airport
including longitude, latitude, airport name, relevant codes and the distance from the users location
to the airport. 

## How to run the test suite

The test suite has been written utilising pytest. When you install the codebase, pytest should be
installed automatically as a required dependency.  Therefore, you should be able to run the test
suite using `pytest -v`. Code coverage currently sits at 100%.
