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
The code is currently set up to use a specific S3 bucket name and file name, which should be modified to before running the script.
To modify the S3 bucket name and file name, simply navigate to the relevant section of the code and update the values accordingly. It is important to ensure that the updated bucket name and file name are valid and accessible, and that any required permissions have been granted before running the code. Once the changes have been made, the code can be executed and the updated file will be uploaded to the specified S3 bucket.
