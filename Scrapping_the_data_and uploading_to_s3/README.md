# Cryptocurrency-Data-Analysis-and-Visualization
This Python script analyzes historical price and volume data for Bitcoin and Ethereum using the CoinGecko API. It cleans the data, calculates various statistics, and generates a plot of the data for each cryptocurrency. It also uploads the plot to an S3 bucket.
# Dependencies
pandas
requests
statistics
boto3
matplotlib
# Setup
Install the dependencies using pip install pandas requests statistics boto3 matplotlib
Replace my-bucket-name with your desired S3 bucket name in the bucket_name variable.
# Usage
Run the script using python script_name.py
The script analyzes the past 30 days of data for Bitcoin and Ethereum and prints out various statistics for each cryptocurrency.
The script generates a plot of the price and volume data for each cryptocurrency and saves it to an S3 bucket.
The script can be easily modified to analyze different cryptocurrencies or time periods by changing the coins list or the days parameter in the get_historical_data() function.