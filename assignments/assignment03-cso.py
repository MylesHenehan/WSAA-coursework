import requests
import json
url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en'
response = requests.get(url) # using .get() to fetch data
data = response.json() # using .json() to parse and convert to a Python dict 
with open("cso.json", 'w') as file:
    json.dump(data, file, indent=4)
print("Data has been successfully saved to the file cso.json")

# Looking at the json file that's saved, the format doesn't look very nice, so I went back and added the indent parameter (source: https://www.digitalocean.com/community/tutorials/python-pretty-print-json)
