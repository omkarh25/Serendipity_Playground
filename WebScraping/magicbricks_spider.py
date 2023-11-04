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
import time
import pandas as pd

def convert_price(price_str):
    try:
        price_str = price_str.strip().replace(",", "")
        if "Lakh" in price_str:
            return int(float(price_str.replace("Lakh", "").strip()) * 1e5)
        elif "Crore" in price_str:
            return int(float(price_str.replace("Crore", "").strip()) * 1e7)
        else:
            return int(price_str)
    except ValueError:
        return None

def scrape_quikr_properties():
    base_url = "https://www.quikr.com/homes/property/residential-apartments-for-sale-in-bangalore-cid_23?page="
    page_number = 1
    all_data = []
    max_pages = 150

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    while page_number <= max_pages:
        print(f"Scraping page {page_number}...")
        response = requests.get(base_url + str(page_number), headers=headers)
        
        if response.status_code != 200:
            print(f"Failed to retrieve page {page_number}.")
            print(f"Status code: {response.status_code}")
            print(response.text)
            break

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data
        locations = [loc.get_text().strip().split(" in ")[-1] for loc in soup.select('a.notclickb.projectname')]
        prices = [convert_price(price.get_text().strip()) for price in soup.select('span') if "Lakh" in price.get_text() or "Crore" in price.get_text()]
        builtup_areas = [int(area.get_text().split()[0]) for area in soup.select('span') if 'sq.ft.' in area.get_text() and area.get_text().split()[0].replace('.', '', 1).isdigit()]

        page_data = list(zip(locations, prices, builtup_areas))
        all_data.extend(page_data)

        page_number += 1
        time.sleep(2)

    return all_data

data = scrape_quikr_properties()

# Convert data to DataFrame and save to a new Excel file
df = pd.DataFrame(data, columns=["Location", "Price", "Built-up Area (sq.ft.)"])
df.to_excel("qucikrr11.xlsx", index=False)
print("Data saved to 'qucikrr11.xlsx'")

# import requests
# from bs4 import BeautifulSoup
# import time
# import pandas as pd

# def convert_price(price_str):
#     try:
#         price_str = price_str.strip().replace(",", "")
#         if "Lakh" in price_str:
#             return int(float(price_str.replace("Lakh", "").strip()) * 1e5)
#         elif "Crore" in price_str:
#             return int(float(price_str.replace("Crore", "").strip()) * 1e7)
#         else:
#             return int(price_str)
#     except ValueError:
#         return None

# def is_number(s):
#     try:
#         int(s)
#         return True
#     except ValueError:
#         return False

# def scrape_quikr_properties():
#     base_url = "https://www.quikr.com/homes/property/residential-builderfloors-for-sale-in-bangalore-cid_23"
#     all_data = []
#     max_pages = 100
#     current_page = 1

#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }

#     while current_page <= max_pages:
#         print(f"Scraping page {current_page}...")
#         response = requests.get(base_url + "?page=" + str(current_page), headers=headers)
        
#         if response.status_code != 200:
#             print(f"Failed to retrieve page {current_page}.")
#             print(f"Status code: {response.status_code}")
#             print(response.text)
#             current_page += 1
#             continue

#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Extract data
#         locations = [loc.get_text().strip().split(" in ")[-1] for loc in soup.select('a.listtitle.notclickb')]
#         prices = [convert_price(price.get_text().strip()) for price in soup.select('span') if "Lakh" in price.get_text() or "Crore" in price.get_text()]
#         builtup_areas = [int(area.get_text().split()[0]) for area in soup.select('span') if 'sq.ft.' in area.get_text() and is_number(area.get_text().split()[0])]

#         # Add data to our list
#         page_data = list(zip(locations, prices, builtup_areas))
#         all_data.extend(page_data)

#         current_page += 1
#         time.sleep(2)

#     return all_data

# data = scrape_quikr_properties()

# # Convert data to DataFrame and save to a new Excel file
# df = pd.DataFrame(data, columns=["Location", "Price", "Built-up Area (sq.ft.)"])
# df.to_excel("scraped_data_new4.xlsx", index=False)
# print("Data saved to 'scraped_data_new4.xlsx'")
