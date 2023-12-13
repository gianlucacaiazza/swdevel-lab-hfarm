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

    #we want also to include possible mispelling in the input of the user
        close_matches = difflib.get_close_matches(departure, unique_departures, n=5, cutoff=threshold)


    #    if not close_matches:
    #        return "No departure found"
    #    elif len(close_matches) > 1:
    #        print("Did you mean:")
    #        for i, match in enumerate(close_matches, start=1):
    #            print(f"{i}. {match}")
  #          choice = int(input("Choose the number correspondent to your departure: "))
          #  suggested_departure = close_matches[choice - 1]
     #   else:
     #       suggested_departure = close_matches[0]


        possible_destinations = df[df['Departure'] == departure]['Arrival'].unique()
    

        if possible_destinations.size > 0:
            chosen_destination = random.choice(possible_destinations)
            available_dates = df[(df['Departure'] == departure) & (df['Arrival'] == chosen_destination)]['Travel Date']
            available_dates = ', '.join(available_dates.astype(str))
            return f'Maybe you could go here {chosen_destination}', f'in this/these date(s): {available_dates}'
        else:
            return "We are sorry, but we don't have any flights from this departure"

# Esempio di utilizzo:
# departure = input("Enter your departure: ")
# result = randomize_destination(departure, your_dataframe)
# print(result)
departure = 'BROMEE'
df = flights
randomize_destination(departure, flights)


