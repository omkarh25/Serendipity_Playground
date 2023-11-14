import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from openpyxl import load_workbook

def do_geocode(address, geolocator):
    try:
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        time.sleep(1)  # Retry after a short wait in case of timeout
        return do_geocode(address, geolocator)
    except GeocoderServiceError as e:
        print(f"Geocoder service error for address '{address}': {e}")
        return None

def main():
    file_path = r'C:\Users\91861\OneDrive\Desktop\bhoodevi\WebScraping\your_excel_file.xlsx'  # Update with your file name
    wb = load_workbook(file_path)
    sheet = wb.active
    geolocator = Nominatim(user_agent="geoapiExercises")

    for index, row in enumerate(sheet.iter_rows(min_row=1, max_col=1, values_only=True), start=1):
        if row[0] and isinstance(row[0], str) and row[0].strip():
            address = row[0]  # Assuming address is in the first column
            location = do_geocode(address, geolocator)
            if location:
                sheet.cell(row=index, column=2).value = location.latitude
                sheet.cell(row=index, column=3).value = location.longitude
            else:
                print(f"Location not found or error occurred for address: {address}")
        else:
            print(f"Empty or invalid address at row {index}")

    updated_file_path = r'C:\Users\91861\OneDrive\Desktop\bhoodevi\WebScraping\updated_your_excel_file.xlsx'
    wb.save(updated_file_path)  # Saves the workbook with coordinates

if __name__ == "__main__":
    main()
