# covid-19 economic tracker

import csv
import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

### define a function that converts format to one decimal and a percent sign ###

# Info Inputs

state = input("Please input a state abbreviation: ")

FRED_series_id = (state) + "UR"

### need an error check here ###

# API Pull

api_key = os.environ.get("FRED_API_KEY")

request_url = f"https://api.stlouisfed.org/fred/series/observations?series_id={FRED_series_id}&api_key={api_key}&file_type=json"

response = requests.get(request_url)

parsed_response = json.loads(response.text)

### need an error check here ###

# Getting the most recent value

total_observations = parsed_response["count"]

last_value = parsed_response["observations"][total_observations-1]["value"] # assumes oldest data point comes first, as is FRED standard

print(last_value)

# Getting the all-time high/all-time low

all_values = []
index = -1

for v in parsed_response["observations"]:
    index = index + 1
    value = parsed_response["observations"][index]["value"]
    all_values.append(value)

all_time_high = max(all_values)
all_time_low = min(all_values)

print(all_time_high)
print(all_time_low)

# Getting the pre-COVID-19 state UR

# Getting the current national UR

# Information Output