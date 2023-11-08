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

# def scrape_quikr_properties():
#     base_url = "https://www.quikr.com/homes/property/residential-apartments-for-sale-in-bangalore-cid_23?page="
#     page_number = 1
#     all_data = []
#     max_pages = 150

#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }

#     while page_number <= max_pages:
#         print(f"Scraping page {page_number}...")
#         response = requests.get(base_url + str(page_number), headers=headers)
        
#         if response.status_code != 200:
#             print(f"Failed to retrieve page {page_number}.")
#             print(f"Status code: {response.status_code}")
#             print(response.text)
#             break

#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Extract data
#         locations = [loc.get_text().strip().split(" in ")[-1] for loc in soup.select('a.notclickb.projectname')]
#         prices = [convert_price(price.get_text().strip()) for price in soup.select('span') if "Lakh" in price.get_text() or "Crore" in price.get_text()]
#         builtup_areas = [int(area.get_text().split()[0]) for area in soup.select('span') if 'sq.ft.' in area.get_text() and area.get_text().split()[0].replace('.', '', 1).isdigit()]

#         page_data = list(zip(locations, prices, builtup_areas))
#         all_data.extend(page_data)

#         page_number += 1
#         time.sleep(2)

#     return all_data

# data = scrape_quikr_properties()

# # Convert data to DataFrame and save to a new Excel file
# df = pd.DataFrame(data, columns=["Location", "Price", "Built-up Area (sq.ft.)"])
# df.to_excel("scraped_data_new_v3.xlsx", index=False)
# print("Data saved to '.xlsx'")

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

# def scrape_quikr_properties():
#     base_url = "https://www.quikr.com/homes/property/residential-plots-for-sale-in-bangalore-cid_23?page="
#     page_number = 1
#     all_data = []
#     max_pages = 150

#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'en-US,en;q=0.9'
#     }

#     while page_number <= max_pages:
#         print(f"Scraping page {page_number}...")
#         response = requests.get(base_url + str(page_number), headers=headers)
        
#         if response.status_code != 200:
#             print(f"Failed to retrieve page {page_number}.")
#             print(f"Status code: {response.status_code}")
#             print(response.text)
#             break

#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Extract data
#         locations = [loc.get_text().strip().split(" in ")[-1] for loc in soup.select('a.notclickb.projectname')]
#         prices = [convert_price(price.get_text().strip()) for price in soup.select('span') if "Lakh" in price.get_text() or "Crore" in price.get_text()]
#         builtup_areas = [int(area.get_text().split()[0]) for area in soup.select('span') if 'sq.ft.' in area.get_text() and area.get_text().split()[0].replace('.', '', 1).isdigit()]

#         page_data = list(zip(locations, prices, builtup_areas))
#         all_data.extend(page_data)

#         page_number += 1
#         time.sleep(5)  # Increasing the delay

#     return all_data

# data = scrape_quikr_properties()

# # Convert data to DataFrame and save to a new Excel file
# df = pd.DataFrame(data, columns=["Location", "Price", "Built-up Area (sq.ft.)"])
# df.to_excel("residential_v2.xlsx", index=False)
# print("Data saved to 'residential_v2.xlsx'")


# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# def scrape_housing_properties(base_url, headers, pages_to_scrape):
#     all_data = []
#     for page in range(1, pages_to_scrape + 1):
#         print(f"Scraping page {page}...")
#         response = requests.get(f"{base_url}{page}", headers=headers)
#         if response.status_code != 200:
#             print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
#             continue

#         soup = BeautifulSoup(response.text, 'html.parser')
#         property_listings = soup.find_all('div', class_='css-xvyvcx')

#         for property_listing in property_listings:
#             location_element = property_listing.find('h1', class_='css-1hidc9c')
#             price_element = property_listing.find('div', class_='css-1rhznz4')
#             area_element = property_listing.find('div', class_='_h3yh40')

#             if location_element and price_element and area_element:
#                 location = location_element.text.strip()
#                 price = price_element.text.strip()
#                 area = area_element.text.strip().split(' ')[0]  # Get the first number only

#                 all_data.append({
#                     "Location": location,
#                     "Price": price,
#                     "Built-up Area (sq.ft.)": area
#                 })
#             else:
#                 print(f"Missing data for listing on page {page}, skipping...")

#         time.sleep(1)  # Polite scraping by adding a delay between requests

#     return all_data

# # URL and headers
# base_url = "https://housing.com/in/buy/bangalore/bangalore?page="
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }

# # Number of pages you want to scrape
# pages_to_scrape = 5  # Adjust this to the number of pages you want to scrape

# # Scrape the properties
# properties_data = scrape_housing_properties(base_url, headers, pages_to_scrape)

# # Convert data to DataFrame
# df = pd.DataFrame(properties_data)

# # Specify the path where you want to save the Excel file
# excel_path = 'C:\\Users\\91861\\OneDrive\\Desktop\\bhoodevi\\WebScraping\\housingg_data.xlsx'

# # Save the DataFrame to an Excel file
# df.to_excel(excel_path, index=False)

# print(f"Data saved to '{excel_path}'")

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# # Function to scrape property details from a single page
# def get_property_details(url, headers):
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     properties = []
#     # Update the class name if the website's layout has changed
#     cards = soup.find_all('div', class_='snb-tile')  # Ensure this is the correct class for property cards

#     for card in cards:
#         # Extract the location
#         location_tag = card.find('a', class_='gtpnd')
#         location = location_tag.text.strip() if location_tag else 'N/A'
        
#         # Extract the price
#         price_tag = card.find('span', class_='s_p')
#         price = price_tag.get_text(strip=True).replace(u'\xa0', u' ') if price_tag else 'N/A'
        
#         # Extract the built-up area
#         area_tag = card.find('span', class_='s_p').find_next('span')  # Modified to find the next span tag
#         area = area_tag.get_text(strip=True).split(' ')[0] if area_tag and area_tag.get_text(strip=True).split() else 'N/A'

#         properties.append({
#             'Location': location,
#             'Price': price,
#             'Built-up Area': area
#         })

#     return properties, response

# # Function to scrape multiple pages
# def scrape_commonfloor(max_pages):
#     base_url = "https://www.commonfloor.com/bangalore-property/for-sale"
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }
    
#     all_properties = []
#     for page in range(1, max_pages + 1):
#         print(f"Scraping page: {page}")
#         current_url = f"{base_url}?page={page}"
#         properties, response = get_property_details(current_url, headers)
#         all_properties.extend(properties)
#         time.sleep(1)  # Polite delay between page requests

#         # Check for the 'Next' button
#         soup = BeautifulSoup(response.content, 'html.parser')
#         next_button = soup.select_one('a[name="Next"]')
#         if not next_button:
#             print("No more pages left to scrape.")
#             break

#     return all_properties

# # Set the number of pages you want to scrape
# max_pages = 10

# # Scrape the properties
# property_list = scrape_commonfloor(max_pages)

# # Create DataFrame and save to Excel
# df = pd.DataFrame(property_list)
# excel_file_path = "C:\\Users\\91861\\OneDrive\\Desktop\\bhoodevi\\WebScraping\\commonfloor_properties.xlsx"  # Change the path as needed for your environment
# df.to_excel(excel_file_path, index=False)

# print(f"Data saved to {excel_file_path}")


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Function to convert price string to integer
def convert_price(price_str):
    price_str = price_str.replace(' ', '').replace(',', '')
    if 'L' in price_str:
        return int(float(price_str.split('L')[0]) * 1e5)
    elif 'Cr' in price_str:
        return int(float(price_str.split('Cr')[0]) * 1e7)
    return None  # None for no match, you can add more conditions if needed

# Function to scrape property details from a single page
def get_property_details(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    properties = []
    cards = soup.find_all('div', class_='snb-tile')  # Ensure this is the correct class for property cards

    for card in cards:
        # Extract the location
        location_tag = card.find('a', class_='gtpnd')
        location = location_tag.text.strip() if location_tag else 'N/A'
        
        # Extract the price and convert it
        price_tag = card.find('span', class_='s_p')
        price = convert_price(price_tag.get_text(strip=True).replace(u'\xa0', u' ')) if price_tag else 'N/A'
        
        # Extract the built-up area
        area_tag = card.find('span', class_='s_p').find_next('span')
        area = area_tag.get_text(strip=True).split(' ')[0] if area_tag and area_tag.get_text(strip=True).split() else 'N/A'

        properties.append({
            'Location': location,
            'Price': price,
            'Built-up Area': area
        })

    return properties, response

# Function to scrape multiple pages
def scrape_commonfloor(max_pages):
    base_url = "https://www.commonfloor.com/bangalore-property/for-sale"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    all_properties = []
    for page in range(1, max_pages + 1):
        print(f"Scraping page: {page}")
        current_url = f"{base_url}?page={page}"
        properties, response = get_property_details(current_url, headers)
        all_properties.extend(properties)
        time.sleep(1)  # Polite delay between page requests

        # Check for the 'Next' button
        soup = BeautifulSoup(response.content, 'html.parser')
        next_button = soup.select_one('a[name="Next"]')
        if not next_button:
            print("No more pages left to scrape.")
            break

    return all_properties

# Set the number of pages you want to scrape
max_pages =200

# Scrape the properties
property_list = scrape_commonfloor(max_pages)

# Create DataFrame and save to Excel
df = pd.DataFrame(property_list)
excel_file_path = "C:\\Users\\91861\\OneDrive\\Desktop\\bhoodevi\\WebScraping\\common_floor 22.xlsx"  # Change the path as needed for your environment
df.to_excel(excel_file_path, index=False)

print(f"Data saved to {excel_file_path}")
