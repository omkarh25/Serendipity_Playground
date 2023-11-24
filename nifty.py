import pandas as pd
import requests
from bs4 import BeautifulSoup

# Read the Excel file from desktop
file_path = r"C:\Users\serendipaty\OneDrive\Desktop\esti.xlsx"
df = pd.read_excel(file_path)

# Function to fetch 1-year Target Estimate from Yahoo Finance
def fetch_1y_target_est(yahoo_code):
    try:
        url = f"https://finance.yahoo.com/quote/{yahoo_code}?p={yahoo_code}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Look for 1-year Target Estimate in the page content
        target_est_element = soup.find("td", {"data-test": "ONE_YEAR_TARGET_PRICE-value"})
        if target_est_element:
            return target_est_element.text
        return None
    except Exception as e:
        print(f"Error fetching for {yahoo_code}: {e}")
        return None

# Update the dataframe with 1-year Target Estimates
df['1y Target Est'] = df['Yahoo Code'].apply(fetch_1y_target_est)

# Save the updated dataframe back to Excel
df.to_excel(file_path, index=False)
