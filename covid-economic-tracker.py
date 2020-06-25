# covid-19 economic tracker

import csv
import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

### define a function that converts format to one decimal and a percent sign ###

api_key = os.environ.get("FRED_API_KEY")

# User Input and API Pull

try:
    state = input("Please input a state abbreviation: ")
    FRED_series_id = (state) + "UR"
    request_url = f"https://api.stlouisfed.org/fred/series/observations?series_id={FRED_series_id}&api_key={api_key}&file_type=json"
    response = requests.get(request_url)

    parsed_response = json.loads(response.text)

    total_observations = parsed_response["count"]

except KeyError:
    print("Hey, didn't find that location. Try again please.")
    exit()

# Getting the most recent value

last_value = float(parsed_response["observations"][total_observations-1]["value"]) # assumes oldest data point comes first, as is FRED standard

# Getting the all-time high/all-time low

all_values = []
index = -1

for v in parsed_response["observations"]:
    index = index + 1
    value = float(parsed_response["observations"][index]["value"])
    all_values.append(value)

all_time_high = max(all_values)
all_time_low = min(all_values)

# Getting the state's pre-COVID-19 unemployment rate

pre_covid_date = "2020-02-01"

matching_observations = [v for v in parsed_response["observations"] if v["date"] == pre_covid_date] 
matching_observation = matching_observations[0]
pre_covid_level = matching_observation["value"]

# pre_covid_level = 

# for v in parsed_response["observations"][index]["date"]:
#     index = index + 1
#     if v == "2020-02-01":
#         pre_covid_level = parsed_response["observations"][index]["value"]
#     else:
#         pass

# Getting the current national UR

# Information Output

print("Current UR: " + str(last_value))
print("February 2020 UR " + str(pre_covid_level))
print("All Time High UR: " + str(all_time_high))
print("All Time Low UR: " + str(all_time_low))
