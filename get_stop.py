import os
import requests
import json
import sys

#Check for API KEY
api_key = os.getenv("API_KEY")
if not api_key:
    raise RuntimeError("API_KEY is not set")

#Setup arguments for request
apiURL="https://external.transitapp.com/v3/public/nearby_stops"
headers = {
    "apiKey": api_key
}
params = {
    "lat":float(sys.argv[1]),
    "lon":float(sys.argv[2])
}

#Make request and print response
response=requests.get(apiURL,params,headers=headers)
print(response.json())