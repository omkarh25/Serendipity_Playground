from geopy.geocoders import Nominatim
import pandas as pd

# Correctly formatted file path
file_path = r'C:\Users\91861\OneDrive\Desktop\bhoodevi\WebScraping\bhoodevi 2.xlsx'  # Raw string to handle file path

# Load the Excel file
addresses_df = pd.read_excel(file_path)

# Initialize geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

# Function to geocode address
def geocode_address(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except Exception as e:
        return None, None

# Geocode each address in the dataframe
addresses_df['Coordinates'] = addresses_df['Location'].apply(geocode_address)

# Splitting the coordinates into latitude and longitude
addresses_df[['Geo Latitude', 'Geo Longitude']] = pd.DataFrame(addresses_df['Coordinates'].tolist(), index=addresses_df.index)

# Save the updated results to a new Excel file
addresses_df.to_excel('geocoded_addresses_updated.xlsx', index=False)

print("Geocoding complete. Updated results saved to 'geocoded_addresses_updated.xlsx'.")
