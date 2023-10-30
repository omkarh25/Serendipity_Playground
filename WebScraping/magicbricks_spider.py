# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# BASE_URL = "https://www.magicbricks.com/property-for-sale-rent-in-Bangalore/residential-real-estate-Bangalore?ppinterface=google_paid_brand_bangalore&mbtracker=google_paid_brand_1_desk_bangalore&ccode=brand_1_sem&gclid=CjwKCAjwv-2pBhB-EiwAtsQZFM6RdcJ221f8UmVDfWdQRGFczkoytQrLzmqsnjpWm7d-6Wtbls27ZRoCoZgQAvD_BwE"
# START_URL = BASE_URL + "property-for-sale/residential-real-estate?bedroom=&proptype=Residential-Plot&cityName=Bangalore&areaUnit=12850"

# def extract_details_from_page(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     property_elements = soup.find_all('div', class_='mb-srp__card')

#     locations, prices, builtup_areas = [], [], []

#     for prop in property_elements:
#         # Location
#         loc_elem = prop.find('h2', class_='mb-srp__card--title')
#         locations.append(loc_elem.text.strip() if loc_elem else 'N/A')
        
#         # Price
#         price_elem = prop.find('div', class_='mb-srp__card__price--amount')
#         prices.append(price_elem.text.strip() if price_elem else 'N/A')
        
#         # Built-up Area
#         area_elem = prop.find('div', class_='mb-srp__card__summary--value')
#         builtup_areas.append(area_elem.text.strip() if area_elem else 'N/A')

#     return locations, prices, builtup_areas

# all_locations, all_prices, all_builtup_areas = [], [], []

# # Start scraping from the first page
# current_page_url = START_URL

# while current_page_url:
#     print(f"Scraping page: {current_page_url}")
    
#     locations, prices, builtup_areas = extract_details_from_page(current_page_url)
#     all_locations.extend(locations)
#     all_prices.extend(prices)
#     all_builtup_areas.extend(builtup_areas)
    
#     # Check if there's a "Next" button to move to the next page
#     soup = BeautifulSoup(requests.get(current_page_url).content, 'html.parser')
#     next_button = soup.find('a', rel='next')
    
#     if next_button and 'href' in next_button.attrs:
#         current_page_url = BASE_URL + next_button['href']
#     else:
#         current_page_url = None

# # Create the DataFrame with the combined lists
# df = pd.DataFrame({
#     'Location': all_locations,
#     'Price': all_prices,
#     'Built-up Area': all_builtup_areas
# })

# # Saving to Excel
# df.to_excel("housing.xlsx", index=False)
# print("housing.xlsx")


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://www.magicbricks.com"
START_URL = BASE_URL + "/independent-house-for-sale-in-bangalore-pppfs"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def extract_details_from_page(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    property_elements = soup.find_all('div', class_='m-srp-card')

    locations, prices, builtup_areas = [], [], []

    for prop in property_elements:
        # Location
        loc_elem = prop.find('h3', class_='m-srp-card__title')
        locations.append(loc_elem.text.strip() if loc_elem else 'N/A')
        
        # Price
        price_elem = prop.find('div', class_='m-srp-card__price')
        prices.append(price_elem.text.strip() if price_elem else 'N/A')
        
        # Built-up Area
        area_elem = prop.find('div', class_='m-srp-card__summary__info')
        builtup_areas.append(area_elem.text.strip() if area_elem else 'N/A')

    return locations, prices, builtup_areas

all_locations, all_prices, all_builtup_areas = [], [], []

current_page_url = START_URL

while current_page_url:
    print(f"Scraping page: {current_page_url}")
    
    locations, prices, builtup_areas = extract_details_from_page(current_page_url)
    all_locations.extend(locations)
    all_prices.extend(prices)
    all_builtup_areas.extend(builtup_areas)
    
    # Check if there's a "Next" button to move to the next page
    soup = BeautifulSoup(requests.get(current_page_url, headers=HEADERS).content, 'html.parser')
    next_button = soup.find('a', rel='next')
    
    if next_button and 'href' in next_button.attrs:
        current_page_url = BASE_URL + next_button['href']
    else:
        current_page_url = None

    time.sleep(5)

# Create the DataFrame with the combined lists
df = pd.DataFrame({
    'Location': all_locations,
    'Price': all_prices,
    'Built-up Area': all_builtup_areas
})

# Saving to Excel
df.to_excel("mg.xlsx", index=False)
print("mg.xlsx saved!")
