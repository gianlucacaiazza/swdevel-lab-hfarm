import pandas as pd
from df_integrations import flights
import json



def get_destinations(departure):
    for i in flights['Departure']:
        if i == departure:
            possible_destination = flights[flights['Departure'] == departure]['Arrival'].unique()
    # Convert to DataFrame
            df = pd.DataFrame(possible_destination, columns=['Destination'])
            return df.to_json(orient='records')
    else:
        possible_destination = f'not available'
    return possible_destination

print(get_destinations('LONDON - LGW'))

