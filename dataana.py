import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Read the Excel file
file_path =  r"C:\Users\serendipaty\OneDrive\Desktop\percent.xlsx"  # Replace with your file path
df = pd.read_excel(file_path, engine='openpyxl')

# Check if the required columns exist, if not, create them
columns_to_add = ['start_date', 'last_date', 'percentage_up', 'start_price', 'last_price']
for col in columns_to_add:
    if col not in df.columns:
        df[col] = None

# Get today's date and 50 days ago
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=50)).strftime('%Y-%m-%d')

# Loop through each stock ticker in the Yahoo Code column
for index, row in df.iterrows():
    ticker = row['Yahoo Code']
    
    # Fetch the stock data
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    
    if not stock_data.empty:
        # Get the closing price on the start and end dates
        start_price_val = stock_data.iloc[0]['Close']
        end_price_val = stock_data.iloc[-1]['Close']
        
        # Calculate the percentage change
        percentage_change = ((end_price_val - start_price_val) / start_price_val) * 100
        
        # If the stock has moved above 20%, update the columns
        if percentage_change > 5:
            df.at[index, 'start_date'] = start_date
            df.at[index, 'last_date'] = end_date
            df.at[index, 'percentage_up'] = percentage_change
            df.at[index, 'start_price'] = start_price_val
            df.at[index, 'last_price'] = end_price_val

# Save the updated DataFrame back to the Excel file
df.to_excel(file_path, index=False, engine='openpyxl')
