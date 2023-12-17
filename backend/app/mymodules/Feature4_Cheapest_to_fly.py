import pandas as pd
import sys
sys.path.append('app/mymodules')
from df_integrations import flights


def cheapest_to_fly(data, arrival):

    arrival_flights = data[(data['Arrival'] == arrival)]

    df_media_prezzi = arrival_flights.groupby("Air Carrier")["Price in £"].mean().round(2).reset_index()

    df_media_prezzi.sort_values(by="Price in £",inplace=True)

    cheapest=df_media_prezzi.iloc[0]

    return cheapest


