import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os

# Function to safely load CSV files
def load_csv(filepath):
    if os.path.exists(filepath):
        return pd.read_csv(filepath)
    else:
        print(f"File not found: {filepath}")
        return pd.DataFrame()  # Return an empty DataFrame if file is not found

# Question 1: Use yfinance to Extract Tesla Stock Data
# Extracting Tesla Stock Data
tesla_data = yf.download('TSLA', start='2010-01-01', end='2021-01-01')
tesla_data.reset_index(inplace=True)
print("Tesla Stock Data - First Five Rows:")
print(tesla_data.head())

# Question 2: Use Webscraping to Extract Tesla Revenue Data
tesla_revenue = load_csv('tesla_revenue.csv')
if not tesla_revenue.empty:
    print("Tesla Revenue Data - Last Five Rows:")
    print(tesla_revenue.tail())

# Question 3: Use yfinance to Extract GameStop Stock Data
# Extracting GameStop Stock Data
gme_data = yf.download('GME', start='2010-01-01', end='2021-01-01')
gme_data.reset_index(inplace=True)
print("GameStop Stock Data - First Five Rows:")
print(gme_data.head())

# Question 4: Use Webscraping to Extract GME Revenue Data
gme_revenue = load_csv('gme_revenue.csv')
if not gme_revenue.empty:
    print("GameStop Revenue Data - Last Five Rows:")
    print(gme_revenue.tail())

# Function to plot the stock data
def make_graph(data, title):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Close'])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Close Price USD')
    plt.show()

# Question 5: Plot Tesla Stock Graph
make_graph(tesla_data, 'Tesla Stock Price 2010-2020')

# Question 6: Plot GameStop Stock Graph
make_graph(gme_data, 'GameStop Stock Price 2010-2020')
