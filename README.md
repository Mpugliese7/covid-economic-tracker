# covid-economic-tracker

An application designed to provide the user with data on unemployment rates by state to help monitor local labor marekts during the COVID-19 pandemic. 

Issue requests to the [St. Louis Federal Reserve's FRED API](https://fred.stlouisfed.org/) in order to provide an update on a state's labor market.

# Prerequisites
    Anaconda 3.7
    Python 3.7
    Pip

# Installation and Setup
Download this repository (https://github.com/Mpugliese7/covid-economic-tracker) onto your computer. Then navigate there from the command line. 

Create and activate a new Anaconda virtual environment named something like "covid-tracker-env". 
    ```conda create covid-tracker-env
    conda activate covid-tracker-env```

Pip install the required packages specificed in the "requirements.txt" file that was downloaded from the repository.
    pip install -r requirements.txt

Create a .env file and place your unique API key in the .env
    FRED_API_Key=123456789

Make sure there is a corresponding .gitignore file that prevents the .env file from being uploaded to github.
    # ignore secret environment variable values
    .env

# Running the program
To run the program
    python covid-economic-tracker.py

When prompted, enter a state abbreivation (2 A-Z characters). If the entered abbreviation does not meet those criteria, the program will not run and will print an error message. The user can try again after a failed attempt.

The outputs for this application should be a table that includes the state's current unemployment rate, the state's unemployment rate before COVID-19 (February 2020), the state's all-time high and all-time low unemployment rates, the national unemployment rate, and the +/- difference between the state unemployment rate and the national rate.

If the state's unemployment rate is higher than the national rate, a message will print warning the user that this state's labor market is in a weaker state and thus may have a higher need for economic assistance. 

If the state's unemployment rate is lower than the national rate, a message will print warning the user that this state's labor market is in a stronger state and thus may have a lower need for economic assistance. 

The program should also create two charts. A time series line chart of the state unemployment rate, and a time series line chart of the state and national unemployment rates. 