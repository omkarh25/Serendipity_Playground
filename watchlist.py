import yfinance as yf
import pandas as pd
import os

# Define the path to the tan.xlsx file on the desktop
file_path = r"C:/Users/serendipaty/OneDrive/Desktop/tan.xlsx"
df = pd.read_excel(file_path)

# Ensure the column name is correct
if 'Yahoo Code' not in df.columns:
    raise ValueError("Yahoo Code column not found in the Excel file!")

# Fetch historical data for each company
end_date = pd.Timestamp.now()
start_date = end_date - pd.DateOffset(years=1)

data = []

for code in df['Yahoo Code']:
    try:
        stock = yf.Ticker(code)
        hist = stock.history(start=start_date, end=end_date)
        
        if not hist.empty:
            a_year_ago_price = hist.iloc[0]['Close']
            cmp_price = hist.iloc[-1]['Close']
            
            # Calculate percentage return
            percentage_return = ((cmp_price - a_year_ago_price) / a_year_ago_price) * 100
            
            data.append({
                'Companies': code,
                '1_year_ago_price': round(a_year_ago_price, 2),
                'cmp': round(cmp_price, 2),
                'percentage_return': round(percentage_return, 2)
            })
    except Exception as e:
        print(f"Error fetching data for {code}: {e}")

# Convert the data to a DataFrame and sort by 'percentage_return' column to get top 20 companies
watchlist_df = pd.DataFrame(data).sort_values(by='percentage_return', ascending=False).head(20)

# Define the path to save the WatchList.xlsx file on the OneDrive desktop
output_path = "C:/Users/serendipaty/OneDrive/Desktop/WatchList.xlsx"
watchlist_df.to_excel(output_path, index=False, engine='openpyxl')

print(f"Watchlist saved to {output_path}")
