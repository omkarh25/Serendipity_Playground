import pandas as pd
import googlemaps
import time
import os
from dotenv import load_dotenv

load_dotenv(r"C:\Users\91861\OneDrive\Desktop\bhoodevi\WebScraping\.env")

def geocode_with_google(file_path, api_key):
    df = pd.read_excel(file_path)
    gmaps = googlemaps.Client(key=api_key)

    for index, row in df.iterrows():
        try:
            geocode_result = gmaps.geocode(row['Location'])
            if geocode_result:
                location = geocode_result[0]['geometry']['location']
                df.at[index, 'Latitude'] = location['lat']
                df.at[index, 'Longitude'] = location['lng']
            else:
                df.at[index, 'Latitude'] = 'N/A'
                df.at[index, 'Longitude'] = 'N/A'
            print(f"Processed: {row['Location']}")
        except Exception as e:
            print(f"Error: {e}")
            df.at[index, 'Latitude'] = 'N/A'
            df.at[index, 'Longitude'] = 'N/A'
        time.sleep(1)  # To prevent exceeding query limit

    output_file = 'geocoded_with_google4.xlsx'
    df.to_excel(output_file, index=False)
    print(f"Data saved to {output_file}")

# Replace with your file path and API key
file_path = r'C:\Users\91861\OneDrive\Desktop\bhoodevi\WebScraping\coo1.xlsx'
api_key = os.getenv("Google2_api_key")
geocode_with_google(file_path, api_key)      
 