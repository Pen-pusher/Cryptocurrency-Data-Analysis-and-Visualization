# Cryptocurrency-Data-Analysis-and-Visualization
The code is a Python script that retrieves historical price and volume data for two cryptocurrencies (Bitcoin and Ethereum) from the CoinGecko API, performs some data cleaning and analysis, and then generates a plot of the price and volume data. The plot is saved as a PNG file and uploaded to an Amazon S3 bucket.

# Here is a more detailed breakdown of what the script is doing:

# The script imports several libraries, including Pandas, Requests, Matplotlib, and Boto3.
# The script defines the base URL for the CoinGecko API, as well as the name of the S3 bucket and file name where the plot will be stored.
# The script defines several functions, including get_historical_data(), clean_data(), get_stats(), plot_prices(), plot_volume(), and upload_to_s3().
# The get_historical_data() function retrieves historical price and volume data for a specified cryptocurrency from the CoinGecko API, using the requests library to make HTTP requests and the pd.DataFrame() function from the Pandas library to store the data in a Pandas DataFrame. The function returns two DataFrames: one for the price data and one for the volume data.
# The clean_data() function merges the price and volume DataFrames, resamples the data to daily intervals, and computes the mean price and volume for each day. The function returns a new DataFrame with the cleaned and aggregated data.
# The get_stats() function computes various statistics on the cleaned DataFrame, including the average price, standard deviation of price, minimum and maximum price, average volume, standard deviation of volume, minimum and maximum volume, and any outliers in the price data. The function returns a dictionary with these statistics.
# The plot_prices() and plot_volume() functions use the Matplotlib library to plot the price and volume data, respectively, for a specified cryptocurrency. The functions add the plot to the current Matplotlib figure.
# The upload_to_s3() function uses the Boto3 library to upload a file to an S3 bucket. The function takes the name of the bucket and file as input.
# The main() function is the main part of the script. It loops through the two cryptocurrencies (Bitcoin and Ethereum), retrieves the historical data, cleans and analyzes the data, generates a plot, saves the plot to a BytesIO buffer, and uploads the plot to the S3 bucket using the upload_to_s3() function. The function also prints out some statistics on the data and the location of the saved plot.
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
