import pandas as pd
import requests
import statistics
import boto3
import os
import matplotlib.pyplot as plt
from io import StringIO, BytesIO

# Define the base URL for the CoinGecko API
base_url = "https://api.coingecko.com/api/v3/"

# Define the S3 bucket name and file name
bucket_name = "my-bucket-name"
file_name = "crypto_data.csv"


def get_historical_data(coin):
    url = f"{base_url}coins/{coin}/market_chart?vs_currency=usd&days=30"
    response = requests.get(url)
    if response.status_code != 200:
        print(
            f"Error: Could not retrieve data for {coin}. Status code: {response.status_code}."
        )
        return pd.DataFrame(), pd.DataFrame()
    data = response.json()
    prices_df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
    prices_df["timestamp"] = pd.to_datetime(prices_df["timestamp"], unit="ms")
    volume_df = pd.DataFrame(data["total_volumes"], columns=["timestamp", "volume"])
    volume_df["timestamp"] = pd.to_datetime(volume_df["timestamp"], unit="ms")
    return prices_df, volume_df


def clean_data(prices_df, volume_df):
    df = pd.merge(prices_df, volume_df, on="timestamp")
    df = df.set_index("timestamp").resample("D").mean().reset_index()
    return df


def get_stats(df):
    stats = {}
    q1 = df["price"].quantile(0.25)
    q3 = df["price"].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df["price"] < lower_bound) | (df["price"] > upper_bound)]
    stats["outliers"] = outliers
    stats["avg_price"] = df["price"].mean()
    stats["std_dev_price"] = statistics.stdev(df["price"])
    stats["min_price"] = df["price"].min()
    stats["max_price"] = df["price"].max()
    stats["avg_volume"] = df["volume"].mean()
    stats["std_dev_volume"] = statistics.stdev(df["volume"])
    stats["min_volume"] = df["volume"].min()
    stats["max_volume"] = df["volume"].max()
    return stats


def plot_prices(df, coin):
    plt.plot(df["timestamp"], df["price"], label=coin.capitalize())


def plot_volume(volume_df, coin):
    plt.plot(
        volume_df["timestamp"], volume_df["volume"], label=f"{coin.capitalize()} Volume"
    )

def upload_to_s3(bucket_name, file_name):
    s3 = boto3.client("s3")
    full_path = os.path.join(os.getcwd(), file_name) # or any other desired full path
    s3.upload_file(full_path, bucket_name, file_name)


def main():
    coins = ["bitcoin", "ethereum"]
    for coin in coins:
        prices_df, volume_df = get_historical_data(coin)
        if prices_df is None or volume_df is None:
            continue
        df = clean_data(prices_df, volume_df)
        if df.empty:
            print(f"Error: Data is empty for {coin}.")
            continue
        stats = get_stats(df)
        print(f"Stats for {coin.capitalize()} (past 30 days):\n")
        print(f"Number of data points: {len(df)}\n")
        print(f"Average Price: {stats['avg_price']}\n")
        print(f"Standard Deviation of Price: {stats['std_dev_price']}\n")
        print(f"Minimum Price: {stats['min_price']}\n")
        print(f"Maximum Price: {stats['max_price']}\n")
        print(f"Average Volume: {stats['avg_volume']}\n")
        print(f"Standard Deviation of Volume: {stats['std_dev_volume']}\n")
        print(f"Minimum Volume: {stats['min_volume']}\n")
        print(f"Maximum Volume: {stats['max_volume']}\n")
        # Plot the price and volume data
        plot_prices(df, coin)
        plot_volume(volume_df, coin)
        # Add legend and labels to the plot
        plt.legend()
        plt.title("Cryptocurrency Price and Volume")
        plt.xlabel("Date")
        plt.ylabel("Price / Volume (USD)")
        # Save the plot to a BytesIO buffer
        buf = BytesIO()
        plt.savefig(buf, format="png")
        # Upload the plot to S3
        buf.seek(0)
        upload_to_s3(bucket_name, file_name)
        s3 = boto3.resource("s3")
        s3.Object(bucket_name, file_name).put(Body=buf.getvalue())
        print(f"Plot saved to {bucket_name}/{file_name}.")


if __name__ == "__main__":
    main()



# This code performs data collection, cleaning, and analysis of historical price and volume data for two cryptocurrencies: Bitcoin and Ethereum.

# The get_historical_data function sends a GET request to the CoinGecko API for the specified cryptocurrency's market chart data for the past 30 days, in USD. If the request is successful, the function creates two pandas DataFrames, one for prices and one for volume, and returns them. If the request fails, empty DataFrames are returned.

# The clean_data function merges the price and volume DataFrames on the timestamp column, resamples the data to a daily frequency, and calculates the mean value for each column.

# The get_stats function takes the cleaned DataFrame as input and calculates several statistics for both price and volume data, including the average, standard deviation, minimum, and maximum values. It also identifies any data points that are considered outliers, using the interquartile range (IQR) method.

# The plot_prices and plot_volume functions use matplotlib to plot the daily price and volume data for each cryptocurrency, respectively. The main function iterates over each cryptocurrency in a list and collects, cleans, and analyzes the data using the above functions. It then prints the statistics for each cryptocurrency and saves a plot of the data to an S3 bucket using boto3.

# The code is currently set up to use a specific S3 bucket name and file name, which can be modified to suit the user's needs.
# To modify the S3 bucket name and file name, simply navigate to the relevant section of the code and update the values accordingly. It is important to ensure that the updated bucket name and file name are valid and accessible, and that any required permissions have been granted before running the code. Once the changes have been made, the code can be executed and the updated file will be uploaded to the specified S3 bucket.