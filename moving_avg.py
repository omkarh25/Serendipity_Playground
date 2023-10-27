import pandas as pd
import yfinance as yf

# Load the Excel file
excel_file_path = r"C:\Users\serendipaty\OneDrive\Desktop\sweet.xlsx"
df = pd.read_excel(excel_file_path)

# Create new columns for 20 DMA, 50 DMA, and 200 DMA
df['20_DMA'] = None
df['50_DMA'] = None
df['200_DMA'] = None

# Fetch and update DMA values for each company
for index, row in df.iterrows():
    ticker = row['Yahoo Code']
    try:
        # Fetch historical data
        stock_data = yf.download(ticker, period="1y")
        
        # Calculate DMAs
        df.loc[index, '20_DMA'] = stock_data['Close'].rolling(window=20).mean().iloc[-1]
        df.loc[index, '50_DMA'] = stock_data['Close'].rolling(window=50).mean().iloc[-1]
        df.loc[index, '200_DMA'] = stock_data['Close'].rolling(window=200).mean().iloc[-1]
        
        print(f"Updated DMA for {ticker}")
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")

# Save the updated DataFrame back to the Excel file
df.to_excel(excel_file_path, index=False, engine='openpyxl')
print("Excel file updated successfully.")
