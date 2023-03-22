# Cryptocurrency-Data-Analysis-and-Visualization
# Introduction
This code is a collection of functions and tests to help get historical stock price and volume data, clean and process it, and generate some basic statistics and visualizations. It also includes a test to verify that data can be read from and written to an S3 bucket.

# Requirements
This code requires the following packages to be installed:

pandas
numpy
statistics
requests
matplotlib
boto3

# Usage
The my_module module contains the following functions:


clean_data(df) - cleans and processes the data returned by get_historical_data().
get_stats(df) - calculates basic statistics for the cleaned data.
plot_prices(df) - generates a line plot of the cleaned price data.
plot_volume(df) - generates a line plot of the cleaned volume data.
# The TestHistoricalData class in the my_module module contains a test to verify that data can be read from and written to an S3 bucket.

# Testing
The code includes a unit test for the TestHistoricalData class. To run the test, simply execute the my_module module. The test will be executed automatically.