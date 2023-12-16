import pandas as pd
from df_integrations import flights
import random
import difflib


#We want to create a "surprise me" function where you only need to input the departure airport and it gives a list 
#of possible destinations + dates

import difflib
import random
import pandas as pd

def randomize_destination(departure, df, threshold=0.6):

    departure = departure.upper()

    if df.empty == True:
        return f'data are not available for this dataset'
    else:
    #first we want to check and format the list of airports of departures
        unique_departures = [str(d) for d in df['Departure'].unique() if pd.notna(d)]

        possible_destinations = df[df['Departure'] == departure]['Arrival'].unique()
    

        if possible_destinations.size > 0:
            chosen_destination = random.choice(possible_destinations)
            available_dates = df[(df['Departure'] == departure) & (df['Arrival'] == chosen_destination)]['Travel Date']
            available_dates = ', '.join(available_dates.astype(str))
            return f'{chosen_destination}', f'AVAILABLE DATES: {available_dates}'
        else:
            return "We are sorry, but we don't have any flights from this departure"



