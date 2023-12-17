'''We want to create a "surprise me" function where you only need to input the departure airport and it gives a list 
   of possible destinations + dates'''

import pandas as pd
from df_integrations import flights
import random
import difflib

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
        possible_destinations = df[df['Departure'] == departure]['Arrival'].unique()

        if possible_destinations.size > 0:
            chosen_destination = random.choice(possible_destinations)

        def give_output(chosen_destination, df):
            if chosen_destination:    
                available_dates = df[(df['Departure'] == departure) & (df['Arrival'] == chosen_destination)]['Travel Date']
                available_dates = ', '.join(available_dates.astype(str))
                return f'{chosen_destination}', f'AVAILABLE DATES: {available_dates}'
            else:
                return "We are sorry, but we don't have any flights from this departure"
    def arrivalcity():
        return chosen_destination
    return {
        'give_output': give_output(chosen_destination, df),
        'arrivalcity': arrivalcity()
    }










