import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# 1. Read the Excel file
file_path = r"C:\Users\serendipaty\OneDrive\Desktop\money.xlsx"
df = pd.read_excel(file_path)

# Function to fetch current price and price from a year ago
def fetch_prices(ticker):
    stock = yf.Ticker(ticker)
    today = datetime.today().date()
    one_year_ago = today - timedelta(days=365)
    
    # Fetching historical data
    hist = stock.history(start=one_year_ago, end=today)
    
    # Getting the CMP and the price from a year ago
    cmp = hist['Close'].iloc[-1] if not hist.empty else None
    price_one_year_ago = hist['Close'].iloc[0] if not hist.empty else None
    
    return round(cmp, 2), round(price_one_year_ago, 2)

# Fetching the prices and updating the DataFrame
df['CMP'], df['a_year_ago'] = zip(*df['Yahoo Code'].apply(fetch_prices))

# Calculate the difference
df['difference'] = df["CMP"] - df["a_year_ago"]

# Update appreciation and depreciation columns based on the difference
df['appreciation'] = df['difference'].where(df['difference'] > 0, 0)
df['depreciation'] = (-df['difference']).where(df['difference'] < 0, 0)

# Calculate percentage return
df['percentage_return'] = (df['difference'] / df["a_year_ago"]) * 100
df['percentage_return'] = df['percentage_return'].round(2)  # Adjusting to two decimal places

# Save the updated DataFrame back to the Excel file
df.drop(columns=['difference'], inplace=True)  # Drop the temporary 'difference' column
df.to_excel(file_path, index=False)
