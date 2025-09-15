"""
This script interacts with the D-ID API to send audio-related requests.

It uses the `requests` library to make HTTP POST requests to the API endpoint.
Sensitive information such as the Bearer token and API key are securely loaded
from environment variables using the `python-dotenv` library.

Ensure that the `.env` file contains the following variables:
- BEARER_TOKEN: The authorization token for accessing the API.
- API_KEY: The API key for additional authentication.

Dependencies:
- python-dotenv: For loading environment variables from the `.env` file.
- requests: For making HTTP requests.

Usage:
1. Install the required dependencies using `pip install -r requirements.txt`.
2. Ensure the `.env` file is properly configured with the required variables.
3. Run the script to send a POST request to the D-ID API.
"""

from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Retrieve the Bearer token and API key from environment variables
bearer_token = os.getenv("BEARER_TOKEN")
api_key = os.getenv("API_KEY")

# Define the API endpoint URL
url = "https://api.d-id.com/audios"

# Set up the headers for the HTTP request
headers = {
    "accept": "application/json",
    "content-type": "multipart/form-data",
    "authorization": f"Bearer {bearer_token}"
}

# Send a POST request to the API endpoint
response = requests.post(url, headers=headers)

# Print the response from the API
print(response.text)
