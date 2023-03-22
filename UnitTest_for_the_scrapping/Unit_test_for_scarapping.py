import unittest
from unittest.mock import Mock
import pandas as pd
import numpy as np
import statistics
import requests
from io import StringIO
from pandas.testing import assert_frame_equal
from my_module import (
    get_historical_data,
    clean_data,
    get_stats,
    plot_prices,
    plot_volume,
)

class TestHistoricalData(unittest.TestCase):
    def test_get_historical_data_returns_dataframe(self):
        response_mock = Mock(status_code=200)
        response_mock.json.return_value = {
            "prices": [
                [1647100529299, 54116.04469027418],
                [1647104631781, 54598.25920111847],
            ],
            "total_volumes": [
                [1647100529299, 4.088759921396482],
                [1647104631781, 3.4729554076966823],
            ],
        }
        with unittest.mock.patch("requests.get", return_value=response_mock):
            prices_df, volume_df = get_historical_data("bitcoin")
            self.assertIsInstance(prices_df, pd.DataFrame)
            self.assertIsInstance(volume_df, pd.DataFrame)

    def test_get_historical_data_returns_empty_dataframe(self):
        response_mock = Mock(status_code=404)
        with unittest.mock.patch("requests.get", return_value=response_mock):
            prices_df, volume_df = get_historical_data("bitcoin")
            self.assertTrue(prices_df.empty)
            self.assertTrue(volume_df.empty)

    def test_clean_data_returns_dataframe(self):
        prices_df = pd.DataFrame(
            {
                "timestamp": [pd.Timestamp("2022-03-01"), pd.Timestamp("2022-03-02")],
                "price": [100, 200],
            }
        )
        volume_df = pd.DataFrame(
            {
                "timestamp": [pd.Timestamp("2022-03-01"), pd.Timestamp("2022-03-02")],
                "volume": [10, 20],
            }
        )
        expected_df = pd.DataFrame(
            {
                "timestamp": [pd.Timestamp("2022-03-01"), pd.Timestamp("2022-03-02")],
                "price": [100, 200],
                "volume": [10, 20],
            }
        )
        expected_df["timestamp"] = pd.to_datetime(expected_df["timestamp"])
        result_df = clean_data(prices_df, volume_df)
        assert_frame_equal(result_df, expected_df)

 
    def test_get_stats_returns_dict(self):
        df = pd.DataFrame(
            {
                "timestamp": [pd.Timestamp("2022-03-01"), pd.Timestamp("2022-03-02")],
                "price": [100, 200],
                "volume": [10, 20],
            }
        )
        expected_stats = {
            "mean_price": 150.0,
            "median_price": 150.0,
            "std_price": 70.71067811865476,
            "mean_volume": 15.0,
            "median_volume": 15.0,
            "std_volume": 5.0,
            "min_price": 100,
            "max_price": 200,
            "min_volume": 10,
            "max_volume": 20,
            "correlation": 1.0,
            "covariance": 150.0,
        }
        result_stats = get_stats(df)
        self.assertDictEqual(result_stats, expected_stats)

    def test_plot_prices_does_not_raise_error(self):
        
        df = pd.DataFrame(
            {
                "timestamp": [pd.Timestamp("2022-03-01"), pd.Timestamp("2022-03-02")],
                "price": [100, 200],
                "volume": [10, 20],
            }
        )
        try:
            plot_prices(df)
        except Exception:
            self.fail("plot_prices raised an exception unexpectedly!")


    def test_plot_volume_does_not_raise_error(self):
        df = pd.DataFrame(
            {
                "timestamp": [pd.Timestamp("2022-03-01"), pd.Timestamp("2022-03-02")],
                "price": [100, 200],
                "volume": [10, 20],
            }
        )
        try:
            plot_volume(df)
        except Exception:
            self.fail("plot_volume raised an exception unexpectedly!")


if __name__ == "__main__":
    unittest.main()






# This code is a unit test suite for a module that includes functions for retrieving historical data of Bitcoin prices and volumes, cleaning the data, getting statistics on the data, and plotting the prices and volumes.

# The unit tests check that:

# get_historical_data returns dataframes when a valid response is received and empty dataframes when a 404 status code is returned.
# clean_data returns a cleaned dataframe with the expected columns and data types.
# get_stats returns a dictionary with the expected statistics.
# plot_prices and plot_volume do not raise any exceptions.