# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# BASE_URL = "https://housing.com"
# START_URL = BASE_URL + "/in/buy/bangalore/bangalore"
# HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# def extract_details_from_page(url):
#     response = requests.get(url, headers=HEADERS)
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     # NOTE: These selectors are placeholders and may not work for the actual site.
#     property_elements = soup.find_all('div', class_='property-card') 

#     locations, prices, builtup_areas = [], [], []

#     for prop in property_elements:
#         # Location
#         loc_elem = prop.find('span', class_='property-location')
#         locations.append(loc_elem.text.strip() if loc_elem else 'N/A')
        
#         # Price
#         price_elem = prop.find('span', class_='property-price')
#         prices.append(price_elem.text.strip() if price_elem else 'N/A')
        
#         # Built-up Area
#         area_elem = prop.find('span', class_='property-area')
#         builtup_areas.append(area_elem.text.strip() if area_elem else 'N/A')

#     return locations, prices, builtup_areas

# all_locations, all_prices, all_builtup_areas = [], [], []

# current_page_url = START_URL

# while current_page_url:
#     print(f"Scraping page: {current_page_url}")
    
#     locations, prices, builtup_areas = extract_details_from_page(current_page_url)
#     all_locations.extend(locations)
#     all_prices.extend(prices)
#     all_builtup_areas.extend(builtup_areas)
    
#     # Check if there's a "Next" button to move to the next page
#     soup = BeautifulSoup(requests.get(current_page_url, headers=HEADERS).content, 'html.parser')
#     next_button = soup.find('a', rel='next')  # This might need modification based on the site's structure.
    
#     if next_button and 'href' in next_button.attrs:
#         current_page_url = BASE_URL + next_button['href']
#     else:
#         current_page_url = None

#     time.sleep(5)

# # Create the DataFrame with the combined lists
# df = pd.DataFrame({
#     'Location': all_locations,
#     'Price': all_prices,
#     'Built-up Area': all_builtup_areas
# })

# # Saving to Excel
# df.to_excel("housing.xlsx", index=False)
# print("housing.xlsx saved!")


# from selenium import webdriver
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# def extract_details_from_page(soup):
#     property_elements = soup.find_all('div', class_='property-card')

#     locations, prices, builtup_areas = [], [], []

#     for prop in property_elements:
#         loc_elem = prop.find('span', class_='property-location')
#         locations.append(loc_elem.text.strip() if loc_elem else 'N/A')

#         price_elem = prop.find('span', class_='property-price')
#         prices.append(price_elem.text.strip() if price_elem else 'N/A')

#         area_elem = prop.find('span', class_='property-area')
#         builtup_areas.append(area_elem.text.strip() if area_elem else 'N/A')

#     return locations, prices, builtup_areas

# # Initialize the browser
# browser = webdriver.Chrome()  # Make sure you have the ChromeDriver installed
# browser.get("https://housing.com/in/buy/bangalore/bangalore")

# all_locations, all_prices, all_builtup_areas = [], [], []

# # Scroll a set number of times (or adjust logic for when to stop scrolling)
# for _ in range(10):  # Adjust the range as needed
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)  # Wait for content to load

#     # Extract details after each scroll
#     page_source = browser.page_source
#     soup = BeautifulSoup(page_source, 'html.parser')
#     locations, prices, builtup_areas = extract_details_from_page(soup)
    
#     all_locations.extend(locations)
#     all_prices.extend(prices)
#     all_builtup_areas.extend(builtup_areas)

# # Create the DataFrame with the combined lists
# df = pd.DataFrame({
#     'Location': all_locations,
#     'Price': all_prices,
#     'Built-up Area': all_builtup_areas
# })

# # Saving to Excel
# df.to_excel("housing.xlsx", index=False)
# print("housing.xlsx saved!")

# # Close the browser
# browser.quit()
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# START_URL = "https://housing.com/in/buy/bangalore/bangalore"

# # Setup the driver
# driver = webdriver.Chrome()
# driver.get(START_URL)

# locations, prices, areas = [], [], []

# # Scroll a set number of times to load properties
# scroll_count = 20
# for _ in range(scroll_count):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(5)
    
#     # Parse the current page source with BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, 'html.parser')

#     # Extract data for each property
#     properties = soup.select('div.property-card')
    
#     for prop in properties:
#         loc_elem = prop.select_one('h1.css-1hidc9c')
#         price_elem = prop.select_one('span.css-19rl1ms')
#         area_elem = prop.select_one('div._h3yh40')

#         if loc_elem and loc_elem.text.strip() not in locations:
#             locations.append(loc_elem.text.strip())
#             prices.append(price_elem.text.strip() if price_elem else 'N/A')
#             areas.append(area_elem.text.strip() if area_elem else 'N/A')

# # Close the Selenium browser
# driver.quit()

# # Save the extracted data to an Excel file
# df = pd.DataFrame({
#     'Location': locations,
#     'Price': prices,
#     'Built-up Area': areas
# })
# df.to_excel("housing.xlsx", index=False)
# print("housing.xlsx saved!")

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# BASE_URL = "https://www.commonfloor.com"
# START_URL = "https://www.commonfloor.com/bangalore-property/for-sale"
# HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# def extract_details_from_page(url):
#     response = requests.get(url, headers=HEADERS)
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     property_elements = soup.find_all('div', class_='snb-tile')

#     locations, prices, builtup_areas = [], [], []

#     for prop in property_elements:
#         # Location
#         loc_elem = prop.find('a', href=True, title=True)
#         locations.append(loc_elem['title'].replace('Apartment for Sale in ', '') if loc_elem else 'N/A')
        
#         # Price
#         price_elem = prop.find('span', class_='s_p')
#         prices.append(price_elem.text.strip() if price_elem else 'N/A')
        
#         # Built-up Area
#         area_elem = prop.find('span')
#         builtup_areas.append(area_elem.contents[0].strip() if area_elem else 'N/A')

#     return locations, prices, builtup_areas

# all_locations, all_prices, all_builtup_areas = [], [], []
# current_page_url = START_URL

# while current_page_url:
#     print(f"Scraping page: {current_page_url}")
    
#     locations, prices, builtup_areas = extract_details_from_page(current_page_url)
#     all_locations.extend(locations)
#     all_prices.extend(prices)
#     all_builtup_areas.extend(builtup_areas)
    
#     # Check for the next page link
#     soup = BeautifulSoup(requests.get(current_page_url, headers=HEADERS).content, 'html.parser')
#     next_page_link = soup.find('a', {'rel': 'next'})
    
#     if next_page_link:
#         current_page_url = BASE_URL + next_page_link.get('href')
#     else:
#         current_page_url = None
    
#     time.sleep(5)

# # Create the DataFrame with the combined lists
# df = pd.DataFrame({
#     'Location': all_locations,
#     'Price': all_prices,
#     'Built-up Area': all_builtup_areas
# })

# # Save to Excel
# df.to_excel("commonfloor.xlsx", index=False)
# print("commonfloor.xlsx saved!")


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://www.quikr.com"
START_URL = "https://www.quikr.com/homes/property/residential-apartments-for-sale-in-bangalore-cid_23"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def extract_details_from_page(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    property_elements = soup.find_all('a', class_='listtitle notclickb')

    locations, prices, builtup_areas = [], [], []

    for prop in property_elements:
        # Location
        locations.append(prop.text.strip())

        # Since price and built-up area are in separate spans, we need to navigate back to their parent to find them
        parent_div = prop.find_parent()

        # Price
        price_elem = parent_div.find('span')  # Assuming price is the first span
        prices.append(price_elem.text.strip() if price_elem else 'N/A')
        
        # Built-up Area
        all_spans = parent_div.find_all('span')
        if len(all_spans) > 1:
            area_elem = all_spans[1]  # Accessing the second span only if it exists
            builtup_areas.append(area_elem.text.strip() if area_elem else 'N/A')
        else:
            builtup_areas.append('N/A')

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
    next_button = soup.find('a', rel='next')  # This might need modification based on the site's structure.
    
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
df.to_excel("quickrr.xlsx", index=False)
print("quickrr.xlsx saved!")
