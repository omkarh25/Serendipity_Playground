import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from openpyxl import load_workbook

def do_geocode(address):
    try:
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        time.sleep(1)
        return do_geocode(address)
    except GeocoderServiceError as e:
        print(f"Geocoder service error for address '{address}': {e}")
        return None

wb = load_workbook(r'C:\Users\91861\OneDrive\Desktop\bhoodevi\qucikrr11.xlsx')
sheet = wb.active

geolocator = Nominatim(user_agent="geoapiExercises")

for index, row in enumerate(sheet.iter_rows(min_row=1, max_col=1, values_only=True), start=1):
    if row[0] and isinstance(row[0], str) and row[0].strip():
        address = row[0] + ", Bangalore, India"
        location = do_geocode(address)
        if location:
            sheet.cell(row=index, column=2).value = location.latitude
            sheet.cell(row=index, column=3).value = location.longitude
        else:
            print(f"Location not found or error occurred for address: {address}")
    else:
        print(f"Empty or invalid address at row {index}")

wb.save(r'C:\Users\91861\OneDrive\Desktop\bhoodevi\qucikrr11_with_coords.xlsx')
