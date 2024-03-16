import requests

url = "https://the-one-api.dev/v2/book/5cf5805fb53e011a64671582"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
