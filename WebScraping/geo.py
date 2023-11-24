# import pandas as pd
# from geopy.geocoders import Nominatim
# from geopy.exc import GeocoderTimedOut
# from time import sleep

# # Function to geocode a location
# def geocode_location(location, geolocator):
#     try:
#         geocoded_location = geolocator.geocode(location)
#         if geocoded_location:
#             return geocoded_location.latitude, geocoded_location.longitude
#         else:
#             return None, None
#     except GeocoderTimedOut:
#         return None, None

# # Load the Excel file
# file_path = 'C:/users/91861/OneDrive/Desktop/bhoodevi/WebScraping/bhoodevi 2.xlsx'
# # Read all sheets
# xls = pd.ExcelFile(file_path)
# sheet_names = xls.sheet_names

# # Initialize Nominatim Geocoder
# geolocator = Nominatim(user_agent="JohnDoePersonalProject")

# # Process each sheet
# for sheet_name in sheet_names:
#     df = pd.read_excel(file_path, sheet_name=sheet_name)
#     location_column = 'Location'  # Replace with your actual location column name

#     # Check if location column exists
#     if location_column in df.columns:
#         # Geocode each location
#         for index, row in df.iterrows():
#             location = row[location_column]
#             lat, lng = geocode_location(location, geolocator)
#             df.at[index, 'Latitude'] = lat
#             df.at[index, 'Longitude'] = lng
#             sleep(1)  # Respect Nominatim's usage limit

#         # Save the results back to a new sheet in the same Excel file
#         with pd.ExcelWriter('geocoded_output.xlsx', mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
#             df.to_excel(writer, sheet_name=sheet_name, index=False)

# print("Geocoding complete.")



