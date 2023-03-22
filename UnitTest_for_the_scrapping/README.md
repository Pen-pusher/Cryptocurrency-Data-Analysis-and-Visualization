# README file for UnitTest


This test suite is designed to test the functionality of various functions in my_module, which is a Python module for retrieving, cleaning, analyzing and plotting historical financial data using the Pandas library.

# Test Functions
The test suite consists of the following test functions:

# test_get_historical_data_returns_dataframe()
This function tests whether get_historical_data() returns two Pandas dataframes when a successful API response is received.

# test_get_historical_data_returns_empty_dataframe()
This function tests whether get_historical_data() returns two empty dataframes when a 404 status code is received from the API.

# test_clean_data_returns_dataframe()


This function tests whether clean_data() returns a combined dataframe containing the price and volume data from two separate dataframes.

# test_get_stats_returns_dict()
This function tests whether get_stats() returns a dictionary containing various statistical measures calculated from the input dataframe.

# test_plot_prices_does_not_raise_error()
This function tests whether plot_prices() raises an error when given a dataframe with price and volume data.

# test_plot_volume_does_not_raise_error()
This function tests whether plot_volume() raises an error when given a dataframe with price and volume data.

# Test Environment
The test suite requires the following Python modules to be installed:

unittest
pandas
numpy
statistics
requests
io
In addition, the following functions from my_module are imported for testing:

get_historical_data
clean_data
get_stats
plot_prices
plot_volume
The test suite can be executed by running the unittest.main() function.

# Test Results
The test suite provides feedback on whether each test function passes or fails. If a test function fails, an error message will be printed to the console. Otherwise, a message confirming that the test passed will be printed.
