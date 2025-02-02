import requests
import json
import os

api_key = os.environ.get('KEY')


def call_gemini_api():
    # Define the API endpoint
    print(api_key)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

    # Define the headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Define the payload (data to be sent in the POST request)
    payload = {
        "contents": [{
            "parts": [{"text": """
I have data on subjects including the number of trees planted, air quality, happiness score, and number of mailboxes. I want to determine which pairs of these variables are most likely to be correlated, and explain the reasoning behind these potential correlations. Please provide the output as a JSON array of objects, where each object has the following structure:

{
  "datasheet1": "Name of the first variable (e.g., Number of trees planted)",
  "datasheet2": "Name of the second variable (e.g., Air quality)",
  "reason": "Explanation of why these two variables might be correlated. Include whether you expect a positive or negative correlation, and mention any potential confounding variables or spurious correlations. Focus on meaningful relationships and avoid suggesting correlations that are likely to be due to chance."
}
                """}]
        }]
    }

    # Convert the payload to JSON
    json_payload = json.dumps(payload)

    # Make the POST request
    response = requests.post(url, headers=headers, data=json_payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        print(response.json())
        return response.json()
    else:
        # Handle errors
        print(f"Error: {response.status_code}")
        print(response)
        print(response.json())
        return None
