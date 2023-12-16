
import pandas as pd
'''import inquirer'''
import sys 
#sys.path.append('/app/mymodules/df_integrations')
from df_integrations import flights

def calculate_average_price(data, departure, arrival):
    """
    Calculate the average price for a given departure-arrival connection, regardless of the date.

    Parameters:
    - data (pd.DataFrame): DataFrame containing flight data.
    - departure (str): Departure airport code.
    - arrival (str): Arrival airport code.

    Returns:
    - float: Average price for the specified route.
    """
    # Filter DataFrame based on the departure and arrival airports
    dep_arr_flights = data[(data['Departure'] == departure) & (data['Arrival'] == arrival)]

    # Check if there are valid entries for the given route
    if len(dep_arr_flights) == 0:
        return None  # No data for the specified route

    # Calculate the average price for the given route
    average_price = dep_arr_flights['Price in £'].mean()

    return average_price

'''ef prompt_for_airports(flights_data):
    # Extract unique departure airports
    departure_airports = list(flights_data['Departure'].unique())

    # Create a list of questions for inquirer
    departure_question = [
        inquirer.List('departure_airport',
                      message="Select Departure Airport:",
                      choices=departure_airports,
                      ),
    ]

    # Prompt the user to select the departure airport
    answers = inquirer.prompt(departure_question)
    departure_airport = answers['departure_airport']

    # Extract possible arrival airports based on the selected departure airport
    possible_arrival_airports = list(flights_data[flights_data['Departure'] == departure_airport]['Arrival'].unique())

    # Create a list of questions for inquirer
    arrival_question = [
        inquirer.List('arrival_airport',
                      message="Select Arrival Airport:",
                      choices=possible_arrival_airports,
                      ),
    ]

    # Prompt the user to select the arrival airport
    answers = inquirer.prompt(arrival_question)
    arrival_airport = answers['arrival_airport']

    return departure_airport, arrival_airport'''



def filter_destinations(data, departure_airport):
    """
    Filter function to find all possible destinations from a given departure airport.
    
    :param data: DataFrame containing flight information.
    :param departure_airport: The departure airport to filter by.
    :return: A list of unique destinations from the given departure airport.
    """
    # Filter the data for the given departure airport
    filtered_data = data[data['Departure'] == departure_airport]

    # Get the list of unique destinations
    destinations = filtered_data['Arrival'].unique()

    return destinations