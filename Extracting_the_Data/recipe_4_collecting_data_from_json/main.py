import requests
import json

# collecting json from "https://quotes.rest/qod.json"
url = "https://quotes.rest/qod.json"

r = requests.get(url)

response = r.json()

print(json.dumps(response, indent=4))

# Extracting contents
quotes = response['contents']['quotes'][0]

print(quotes)

# Extracting only quote
print(quotes['quote'], '\n--', quotes['author'])

