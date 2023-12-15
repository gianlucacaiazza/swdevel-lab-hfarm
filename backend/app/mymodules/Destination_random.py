import pandas as pd
from df_integrations import flights
import random
import difflib


#We want to create a "surprise me" function where you only need to input the departure airport and it gives a list 
#of possible destinations + dates

def randomize_destination(departure, df):
    '''
    parameters:
    - departure -> the airport desidered by the user, should be chosen from a list in the frontend
    - df -> in our case "flights", should work with analog df with analog values
    Returns:
    - string with {random-destination} and {available dates}'''
    departure = departure.upper()

    if df.empty == True:
        return f'data are not available for this dataset'
    else:
    #first we want to check and format the list of airports of departures
        unique_departures = [str(d) for d in df['Departure'].unique() if pd.notna(d)]

        possible_destinations = df[df['Departure'] == departure]['Arrival'].unique()
    

        if possible_destinations.size > 0:
            random_destination = random.choice(possible_destinations)
            available_dates = df[(df['Departure'] == departure) & (df['Arrival'] == random_destination)]['Travel Date']
            available_dates = ', '.join(available_dates.astype(str))
            return f'{random_destination}', f'AVAILABLE DATES: {available_dates}'
        else:
            return "We are sorry, but we don't have any flights from this departure"



