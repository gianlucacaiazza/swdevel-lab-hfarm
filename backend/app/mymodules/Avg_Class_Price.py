

from df_integrations import flights
import pandas as pd


def calculate_average_price_airline(flights, airline):
    """ 
    Calculate the average price for each travel class of a specific airline.

    Parameters:
    - flights (DataFrame): A DataFrame containing flight data, including columns 'Air Carrier',
                          'Travel Class', and 'Price in £'.
    - airline (str): The name of the airline for which to calculate average prices.

    Returns:
    str: A string containing information about the average prices for each travel class of the specified airline.
         If the airline has only one travel class, additional information about the class is included.
         If the airline has no flights recorded in the DataFrame, appropriate information is provided.

    Example Usage:
    result = calculate_average_price_airline(flights, 'YourAirlineName')
    print(result)
    Average Price ECONOMY: 123.45 £
    Average Price BUSINESS: 789.60 £
    The airline only has ECONOMY class flights
    """
    # Filter the DataFrame for the specified airline
    airline_data = flights[flights['Air Carrier'] == airline]

    # Retrieve unique travel classes present in the DataFrame
    travel_classes = airline_data['Travel Class'].unique()

    # Initialize a string to store the results
    results_string = f''

    # Calculate the average price for each travel class
    for travel_class in travel_classes:
        # Filter data for the specific travel class
        class_data = airline_data[airline_data['Travel Class'] == travel_class]
        # Calculate the average price for the travel class
        average_price = class_data['Price in £'].mean()
        results_string += f'Average Price {travel_class}: {average_price:.2f} £'

    # Check if there is only one travel class
    if len(travel_classes) == 1:
        results_string += f" The airline only has {travel_classes[0]} class flights"


    # Return the results as a string
    return results_string
