import yfinance as yf
import pandas as pd

def get_stock_data(tickers):
    data = yf.download(tickers, period="2d")['Close']
    return data

def update_stock_data(df, data):
    df['yest_close'] = None
    df['today_close'] = None
    df['%rise'] = None
    
    

    for ticker in df['Yahoo Code']:
        if ticker in data.columns:
            previous_close = data[ticker].iloc[0]
            today_close = data[ticker].iloc[1]
            percentage_rise = ((today_close - previous_close) / previous_close) * 100

            if percentage_rise > 2:
                df.loc[df['Yahoo Code'] == ticker, 'yest_close'] = round(previous_close, 2)
                df.loc[df['Yahoo Code'] == ticker, 'today_close'] = round(today_close, 2)
                df.loc[df['Yahoo Code'] == ticker, '%rise'] = round(percentage_rise, 2)

    return df

if __name__ == "__main__":
    # Read tickers from Excel file
    file_path = r"C:\Users\serendipaty\OneDrive\Desktop\autom.xlsx"  # Replace with your file path
    df = pd.read_excel(file_path)
    tickers = df['Yahoo Code'].tolist()

    data = get_stock_data(tickers)
    updated_df = update_stock_data(df, data)

    # Save the updated DataFrame back to the Excel file
    updated_df.to_excel(file_path, index=False)
    

