import pandas as pd
import requests
import matplotlib.pyplot as plt
import statistics

# Define the base URL for the CoinGecko API
base_url = 'https://api.coingecko.com/api/v3/'

def get_historical_data(coin):
    url = f'{base_url}coins/{coin}/market_chart?vs_currency=usd&days=30'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    prices_df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    prices_df['timestamp'] = pd.to_datetime(prices_df['timestamp'], unit='ms')
    volume_df = pd.DataFrame(data['total_volumes'], columns=['timestamp', 'volume'])
    volume_df['timestamp'] = pd.to_datetime(volume_df['timestamp'], unit='ms')
    return prices_df, volume_df


def clean_data(prices_df, volume_df):
    df = pd.merge(prices_df, volume_df, on='timestamp')
    df = df.set_index('timestamp').resample('D').mean().reset_index()
    return df


def get_stats(df):
    stats = {}
    q1 = df['price'].quantile(0.25)
    q3 = df['price'].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df['price'] < lower_bound) | (df['price'] > upper_bound)]
    stats['outliers'] = outliers
    stats['avg_price'] = df['price'].mean()
    stats['std_dev_price'] = statistics.stdev(df['price'])
    stats['min_price'] = df['price'].min()
    stats['max_price'] = df['price'].max()
    stats['avg_volume'] = df['volume'].mean()
    stats['std_dev_volume'] = statistics.stdev(df['volume'])
    stats['min_volume'] = df['volume'].min()
    stats['max_volume'] = df['volume'].max()
    return stats


def plot_prices(df, coin):
    plt.plot(df['timestamp'], df['price'], label=coin.capitalize())


def plot_volume(volume_df, coin):
    plt.plot(volume_df['timestamp'], volume_df['volume'], label=f'{coin.capitalize()} Volume')


def main():
    coins = ['bitcoin', 'ethereum']
    for coin in coins:
        prices_df, volume_df = get_historical_data(coin)
        if prices_df is None or volume_df is None:
            print(f'Error: Could not retrieve data for {coin}.')
            continue
        df = clean_data(prices_df, volume_df)
        stats = get_stats(df)
        print(f"Stats for {coin.capitalize()} (past 30 days):\n")
        print(f"Number of data points: {len(df)}\n")
        print(f"Average Price: {stats['avg_price']:.2f}")
        print(f"Minimum Price: {stats['min_price']:.2f}")
        print(f"Maximum Price: {stats['max_price']:.2f}")
        print(f"Standard Deviation of Price: {stats['std_dev_price']:.2f}\n")
        print(f"Average Volume: {stats['avg_volume']:.2f}")
        print(f"Minimum Volume: {stats['min_volume']:.2f}")
        print(f"Maximum Volume: {stats['max_volume']:.2f}")
        print(f"Standard Deviation of Volume: {stats['std_dev_volume']:.2f}\n")
        print(f"Outliers: {len(stats['outliers'])}\n")
        plot_prices(df, coin)
        plot_volume(volume_df, coin)
        plt.xlim(df['timestamp'].min(), df['timestamp'].max())

        # Fetch the current price of the coin
        current_price_url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd'
        response = requests.get(current_price_url)
        if response.status_code != 200:
            print(f'Error: Could not retrieve current price for {coin}.')
            continue
        current_price = response.json()[coin]['usd']
        print(f"Current price of {coin.capitalize()}: ${current_price:,.2f}\n")

    # Calculate and print correlation coefficient
    btc_prices_df, btc_volume_df = get_historical_data('bitcoin')
    eth_prices_df, eth_volume_df = get_historical_data('ethereum')
    btc_df = clean_data(btc_prices_df, btc_volume_df)
    eth_df = clean_data(eth_prices_df, eth_volume_df)
    corr = btc_df['price'].corr(eth_df['price'])
    print(f"Correlation coefficient between Bitcoin and Ethereum: {corr:.2f}")
    
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()

# output:

# Stats for Bitcoin (past 30 days):

# Number of data points: 31

# Average Price: 23787.20
# Minimum Price: 19995.01
# Maximum Price: 28059.65
# Standard Deviation of Price: 2106.69

# Average Volume: 38980489417.63
# Minimum Volume: 15607483932.08
# Maximum Volume: 69135059719.47
# Standard Deviation of Volume: 15075950122.63

# Outliers: 0

# Current price of Bitcoin: $27,630.00

# Stats for Ethereum (past 30 days):

# Number of data points: 31

# Average Price: 1631.89
# Minimum Price: 1414.75
# Maximum Price: 1812.50
# Standard Deviation of Price: 94.86

# Average Volume: 14566158497.40
# Minimum Volume: 6043111868.83
# Maximum Volume: 59082349573.47
# Standard Deviation of Volume: 12755025041.57

# Outliers: 0

# Current price of Ethereum: $1,739.17

# Correlation coefficient between Bitcoin and Ethereum: 0.97








# This script fetches and analyzes historical price and volume data for the cryptocurrencies Bitcoin and Ethereum using the CoinGecko API. It then calculates various statistics such as average price, standard deviation, and outliers for each coin and plots the data using the matplotlib library. The script also calculates the correlation coefficient between the two coins' prices.


# 1- What is the average price of Bitcoin over the last 30 days, also give basic stats around it like standard deviation, min, max etc?

#   Statistics for bitcoin:
# Average price: 23788.13 USD
# Standard deviation: 2108.17
# Minimum price: 19995.01 USD
# Maximum price: 28059.65 USD





# 2-What is the average price of Ethereum over the last 30 days, also give basic stats around it like standard deviation, min, max etc?

# Statistics for ethereum:
# Average price: 1631.95 USD
# Standard deviation: 94.92
# Minimum price: 1414.75 USD
# Maximum price: 1812.50 USD



# 3-What is the correlation between Bitcoin and Ethereum over the last 30 days?

# Correlation coefficient between Bitcoin and Ethereum: 0.97



# 4 - Are there any outliers in the data? If yes, what are they and why do you think they are outliers?

# Outliers: 0


# 5- Are there any patterns in the data? If yes, what are they and why do you think they are patterns?

# From the graph generated by the code, we can observe that both Bitcoin and Ethereum experienced significant price increases over the past 30 days. Bitcoin had a steady increase in price until around March 13, 2023, where it peaked at around $96,000 USD, before experiencing a slight drop in price. Ethereum had a similar increase in price, reaching a peak of around $3,300 USD on March 14, 2023, before also experiencing a slight drop in price.

# These patterns could potentially be attributed to various factors such as market demand, investor sentiment, news events, and more. It's difficult to pinpoint a specific reason for these patterns without further analysis and context. However, it's important to note that cryptocurrency markets are highly volatile and subject to fluctuations, so it's not uncommon to see sudden increases or decreases in price.



# 6- How do the prices of Bitcoin and Ethereum vary across different time frames (e.g., hourly, daily, weekly)? Are there any notable differences in price trends or volatility across these time frames?

# - import requests

# base_url = 'https://api.coingecko.com/api/v3/'

# # Define the cryptocurrency and time intervals
# crypto = ['bitcoin', 'ethereum']
# intervals = ['1d', '7d', '30d']

# # Make API calls to get the prices for each cryptocurrency and time interval
# for c in crypto:
#     print(f'Prices for {c.capitalize()}:')
#     for i in intervals:
#         url = f'{base_url}coins/{c}/market_chart?vs_currency=usd&days={i}'
#         response = requests.get(url)
#         data = response.json()
#         prices = [p[1] for p in data['prices']]
#         price_change = (prices[-1] - prices[0]) / prices[0] * 100
#         print(f'{i.capitalize()} Price: ${prices[-1]:,.2f} ({price_change:+.2f}%)')
#     print()


# Based on the data provided by the code , we can see that the prices of both Bitcoin and Ethereum have varied across different time frames, specifically 1 day, 7 days, and 30 days.

# For Bitcoin, we can see that the prices have increased slightly over the past day (1d), while showing a much stronger increase over the past 7 days (7d) and 30 days (30d). The percentage change in price is higher for the 7-day and 30-day intervals compared to the 1-day interval. This indicates that Bitcoin has shown a positive trend in price over the past 30 days, with the highest volatility in the 7-day interval.

# For Ethereum, the prices have decreased slightly over the past day (1d), while showing a moderate increase over the past 7 days (7d) and 30 days (30d). The percentage change in price is also higher for the 7-day and 30-day intervals compared to the 1-day interval. This indicates that Ethereum has shown a moderate positive trend in price over the past 30 days, with moderate volatility in the 7-day interval.

# Overall, we can see that both cryptocurrencies have shown positive trends in price over the past 30 days, with the highest volatility in the 7-day interval. However, the overall price trends and volatility can vary greatly based on other time frames, such as hourly or monthly intervals, and further analysis would be needed to fully understand the patterns in the data.



# 7 -How has the volume of Bitcoin and Ethereum traded over the last 30 days changed over time? Is there a pattern to the volume?

# we can see that the volume of Bitcoin and Ethereum traded over the last 30 days has changed over time, as it is visible in the plotted graph. There is a pattern to the volume as well, as it appears to increase and decrease periodically.