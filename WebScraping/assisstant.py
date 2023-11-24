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







import openai

def generate_text(prompt, model="text-davinci-003", api_key="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"):
    openai.api_key = api_key

    try:
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# Example usage
response = generate_text("Give the geocode of Rakesh Fantasy Garden", api_key="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")
print(response)
