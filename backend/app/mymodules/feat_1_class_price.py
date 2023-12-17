
'''
Feature 3 - Average Price Per Flight Class

This module provides functionality to calculate the average prices
for different types of flight classes offered by a specific airline.
'''


def calculate_average_price_airline(flights, airline):
    """
    Calculate the average price for each travel class of a specific airline.

    Parameters:
    - flights (DataFrame): A DataFrame containing flight data,
                          including columns 'Air Carrier',
                          'Travel Class', and 'Price in £'.
    - airline (str): The name of the airline for which to calculate avg prices.

    Returns:
    str: A string containing information about the average prices for each
         travel class of the specified airline.
         If the airline has only one travel class, additional information
         about the class is included.
         If the airline has no flights recorded in the DataFrame, appropriate
         information is provided.
    """
    # Filter the DataFrame for the specified airline
    airline_data = flights[flights['Air Carrier'] == airline]

    # Retrieve unique travel classes present in the DataFrame
    travel_classes = airline_data['Travel Class'].unique()

    # Initialize a string to store the results
    res_str = f''

    # Calculate the average price for each travel class
    for travel_class in travel_classes:
        # Filter data for the specific travel class
        class_data = airline_data[airline_data['Travel Class'] == travel_class]
        # Calculate the average price for the travel class
        average_price = class_data['Price in £'].mean()
        res_str += f'Average Price {travel_class}: {average_price:.2f} £'

    # Check if there is only one travel class
    if len(travel_classes) == 1:
        res_str += f" The airline only has {travel_classes[0]} class flights"

    # Return the results as a string
    return res_str
  