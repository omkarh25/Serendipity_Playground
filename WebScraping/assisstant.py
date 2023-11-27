# import requests

# def query_openai_assistant(prompt, model="text-davinci-003", api_key="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"):
#     """
#     Send a query to the OpenAI Assistant API.

#     :param prompt: The prompt or question to ask the AI.
#     :param model: The model to use. Defaults to 'text-davinci-003'.
#     :param api_key: Your API key for OpenAI.
#     :return: The response from the AI.
#     """
#     url = "https://api.openai.com/v1/assistants/YOUR_ASSISTANT_ID/messages"
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "model": model,
#         "messages": [{"role": "system", "content": "This is a test"}]
#     }

#     response = requests.post(url, headers=headers, json=data)
#     return response.json()

# # Example usage
# response = query_openai_assistant("What is the capital of France?")
# print(response)
# asst_uhQlHg2Zelg1Fsxl4cFBLiUv



# import openai

# def generate_text(prompt, model="text-davinci-003", api_key="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"):
#     openai.api_key = api_key

#     try:
#         response = openai.Completion.create(
#             model=model,
#             prompt=prompt,
#             max_tokens=150
#         )
#         return response.choices[0].text.strip()
#     except Exception as e:
#         return str(e)

# # Example usage
# response = generate_text("Give the geocode of Rakesh Fantasy Garden", api_key="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")
# print(response)




# import openai
# import pandas as pd

# def generate_text(prompt, model="text-davinci-003", api_key="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"):
#     openai.api_key = api_key

#     try:
#         response = openai.Completion.create(
#             model=model,
#             prompt=prompt,
#             max_tokens=150
#         )
#         return response.choices[0].text.strip()
#     except Exception as e:
#         return str(e)

# def get_geocodes_from_excel(file_path, api_key):
#     # Read the Excel file
#     df = pd.read_excel(file_path)

#     # Print the column names for troubleshooting
#     print("Columns in the file:", df.columns.tolist())

#     # Check if 'location' column exists (note the lowercase 'l')
#     if 'location' not in df.columns:
#         return "The Excel file does not have a 'location' column."

#     # Create a new column for geocodes
#     df['Geocode'] = ''

#     # Iterate over each location and get the geocode
#     for index, row in df.iterrows():
#         location = row['location']  # Use 'location' with lowercase 'l'
#         prompt = f"Give the geocode of {location}"
#         geocode = generate_text(prompt, api_key=api_key)
#         df.at[index, 'Geocode'] = geocode

#     # Save the results to a new Excel file
#     output_file = 'geocodes_output1.xlsx'
#     df.to_excel(output_file, index=False)

#     return f"Geocodes saved to {output_file}"

# # Example usage
# file_path = r'C:\Users\91861\OneDrive\Desktop\bhoodevi\WebScraping\coo.xlsx'  # Use the correct file path
# api_key = "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"  # Replace with your actual OpenAI API key
# result = get_geocodes_from_excel(file_path, api_key)
# print(result)
# import openai
# import pandas as pd

# def generate_text(prompt, api_key, model="text-davinci-003"):
#     openai.api_key = api_key

#     try:
#         response = openai.Completion.create(
#             model=model,
#             prompt=prompt,
#             max_tokens=150
#         )
#         return response.choices[0].text.strip()
#     except Exception as e:
#         return f"Error: {str(e)}"

# def get_geocodes_from_excel(file_path, api_key):
#     try:
#         # Read the Excel file
#         df = pd.read_excel(file_path)
#     except Exception as e:
#         return f"Error reading the Excel file: {str(e)}"

#     # Print the column names for troubleshooting
#     print("Columns in the file:", df.columns.tolist())

#     # Check if 'location' column exists
#     if 'location' not in df.columns:
#         return "The Excel file does not have a 'location' column."

#     # Create a new column for geocodes
#     df['Geocode'] = ''

#     # Iterate over each location and get the geocode
#     for index, row in df.iterrows():
#         location = row['location']
#         prompt = f"Give the geocode of {location}"
#         geocode = generate_text(prompt, api_key=api_key, model="text-davinci-003")
#         df.at[index, 'Geocode'] = geocode
#         print(f"Processed location: {location} - Geocode: {geocode}")  # Print each geocode for verification

#     # Save the results to a new Excel file
#     try:
#         output_file = r'C:\Users\91861\OneDrive\Desktop\bhoodevi\WebScraping\geocodes_output1.xlsx'
#         df.to_excel(output_file, index=False)
#         return f"Geocodes saved to {output_file}"
#     except Exception as e:
#         return f"Error saving the Excel file: {str(e)}"

# # Example usage
# file_path = r'C:\Users\91861\OneDrive\Desktop\bhoodevi\WebScraping\coo.xlsx'
# api_key = "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"
# result = get_geocodes_from_excel(file_path, api_key)
# print(result)

# import openai
# import pandas as pd

# def generate_text(prompt, api_key, model="text-davinci-003"):
#     openai.api_key = api_key

#     try:
#         response = openai.Completion.create(
#             model=model,
#             prompt=prompt,
#             max_tokens=150
#         )
#         return response.choices[0].text.strip()
#     except Exception as e:
#         return f"Error: {str(e)}"

# def parse_geocode(geocode):
#     # Assuming the geocode format is "latitude, longitude"
#     try:
#         latitude, longitude = geocode.split(", ")
#         return float(latitude), float(longitude)
#     except Exception as e:
#         return None, None

# def get_geocodes_from_excel(file_path, api_key):
#     try:
#         # Read the Excel file
#         df = pd.read_excel(file_path)
#     except Exception as e:
#         return f"Error reading the Excel file: {str(e)}"

#     # Check if 'location' column exists
#     if 'location' not in df.columns:
#         return "The Excel file does not have a 'location' column."

#     # Create new columns for latitude and longitude
#     df['Latitude'] = ''
#     df['Longitude'] = ''

#     # Iterate over each location and get the geocode
#     for index, row in df.iterrows():
#         location = row['location']
#         prompt = f"Give the geocode of {location}"
#         geocode = generate_text(prompt, api_key=api_key, model="text-davinci-003")
#         latitude, longitude = parse_geocode(geocode)
#         df.at[index, 'Latitude'] = latitude
#         df.at[index, 'Longitude'] = longitude

#     # Save the results to a new Excel file
#     try:
#         output_file = r'C:\Users\91861\OneDrive\Desktop\bhoodevi\WebScraping\geocodes_output1.xlsx'
#         df.to_excel(output_file, index=False)
#         return f"Geocodes saved to {output_file}"
#     except Exception as e:
#         return f"Error saving the Excel file: {str(e)}"

# # Example usage
# file_path = r'C:\Users\91861\OneDrive\Desktop\bhoodevi\WebScraping\coo.xlsx'
# api_key = "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"
# result = get_geocodes_from_excel(file_path, api_key)
# print(result)

import openai
import pandas as pd

def generate_text(prompt, api_key, model="text-davinci-003"):
    openai.api_key = api_key

    try:
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def parse_geocode(geocode):
    # Assuming the geocode format is "latitude, longitude"
    try:
        latitude, longitude = geocode.split(", ")
        return float(latitude), float(longitude)
    except Exception as e:
        return None, None

def get_geocodes_from_excel(file_path, api_key):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)

        # Check if 'location' column exists
        if 'location' not in df.columns:
            return "The Excel file does not have a 'location' column."

        # Create new columns for latitude and longitude
        df['Latitude'] = ''
        df['Longitude'] = ''

        # Iterate over each location and get the geocode
        for index, row in df.iterrows():
            location = row['location']
            prompt = f"Give the geocode of {location}"
            geocode = generate_text(prompt, api_key=api_key, model="text-davinci-003")
            latitude, longitude = parse_geocode(geocode)
            df.at[index, 'Latitude'] = latitude
            df.at[index, 'Longitude'] = longitude

        # Save the results to a new Excel file
        output_file = 'geocodes_output33.xlsx'  # Change the path if needed
        df.to_excel(output_file, index=False)
        return f"Geocodes saved to {output_file}"

    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
file_path = 'C:\Users\91861\OneDrive\Desktop\bhoodevi\WebScraping\coo.xlsx'  # Replace with your actual file path
api_key = "your-api-key-here"  # Replace with your actual OpenAI API key
result = get_geocodes_from_excel(file_path, api_key)
print(result)
