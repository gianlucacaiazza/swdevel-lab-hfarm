"""
This is the module for Feature 1 of the WePole software.

The calculate_average_price function computes the
average flight ticket price for a selected flight connection.

"""

import pandas as pd
from df_integrations import flights


def calculate_average_price(data, departure, arrival):
    """
    Calculate the average price for a given departure-arrival connection,
    regardless of the date.

    Parameters:
    - data (pd.DataFrame): DataFrame containing flight data.
    - departure (str): Departure airport code.
    - arrival (str): Arrival airport code.

    Returns:
    - Average price for the specified route.
    """
    # Filter DataFrame based on the departure and arrival airports
    dep_arr_flights = data[(data['Departure'] == departure) &
                           (data['Arrival'] == arrival)]

    # Check if there are valid entries for the given route
    if len(dep_arr_flights) == 0:
        return None  # No data for the specified route

    # Calculate the average price for the given route
    average_price = dep_arr_flights['Price in £'].mean()

    return average_price
