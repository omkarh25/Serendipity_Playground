import pandas as pd

# Load the Excel file from Desktop
file_path = r"C:\Users\serendipaty\OneDrive\Desktop\infy.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')

# Ensure the 'Close' column exists
if 'Close' not in df.columns:
    print("Column 'Close' not found in the Excel file.")
    exit()

# Calculate the 200-week moving average
df['200W MA'] = df['Close'].rolling(window=200).mean()

# Save the updated dataframe back to the same Excel file
df.to_excel(file_path, index=False, engine='openpyxl')
print("Updated Excel file with 200-week moving average.")
