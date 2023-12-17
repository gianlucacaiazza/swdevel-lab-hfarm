
"""
Feature 1 - Average Flight Price Calculation

This module provides functionality to calculate the average flight ticket
price for a selected departure-arrival connection using the WePole software.
"""


def calculate_average_price(data, departure, arrival):
    """
    Calculate the average price for a given departure-arrival connection,
    regardless of the date.

    Parameters:
    - data (pd.DataFrame): DataFrame containing flight data.
    - departure (str): Departure airport.
    - arrival (str): Arrival airport.

    Returns:
    - float: Average price for the specified route.

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
