import pandas as pd
import requests
from bs4 import BeautifulSoup

# Read the Excel file from desktop
file_path = r"C:\Users\serendipaty\OneDrive\Desktop\sweet.xlsx"
df = pd.read_excel(file_path)

# Function to fetch ex-dividend date from Yahoo Finance
def fetch_ex_dividend_date(yahoo_code):
    try:
        url = f"https://finance.yahoo.com/quote/{yahoo_code}?p={yahoo_code}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Look for ex-dividend date in the page content
        ex_dividend_date_element = soup.find("td", {"data-test": "EX_DIVIDEND_DATE-value"})
        if ex_dividend_date_element:
            return ex_dividend_date_element.text
        return None
    except Exception as e:
        print(f"Error fetching for {yahoo_code}: {e}")
        return None

# Update the dataframe with ex-dividend dates
df['Ex-Dividend Date'] = df['Yahoo Code'].apply(fetch_ex_dividend_date)

# Save the updated dataframe back to Excel
df.to_excel(file_path, index=False)
