from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Retrieve the Bearer token and API key from environment variables
bearer_token = os.getenv("BEARER_TOKEN")
api_key = os.getenv("API_KEY")

url = "https://api.d-id.com/audios"

headers = {
    "accept": "application/json",
    "content-type": "multipart/form-data",
    "authorization": f"Bearer {bearer_token}"
}

response = requests.post(url, headers=headers)

print(response.text)
