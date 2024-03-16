import requests
import os
from dotenv import load_dotenv 

load_dotenv()  
API_KEY = os.getenv("API_KEY_Lord")

url = "https://the-one-api.dev/v2/chapter"

payload = {}
headers = {
  'Authorization': f"Bearer {API_KEY}", 
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
