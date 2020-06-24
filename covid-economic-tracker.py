# covid-19 economic tracker

import csv
import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

# Info Inputs

FRED_series_id = input("Please input a FRED series id: ")

# need an error check here

api_key = os.environ.get("FRED_API_KEY")

request_url = f"https://api.stlouisfed.org/fred/series/observations?series_id={FRED_series_id}&api_key={api_key}&file_type=json"

response = requests.get(request_url)

parsed_response = json.loads(response.text)

# need an error check here

last_value = parsed_response["observations"][-1]["value"]

print(str(last_value))