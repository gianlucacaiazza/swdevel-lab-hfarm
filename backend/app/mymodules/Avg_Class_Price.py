from df_integrations import flights
import pandas as pd

def calculate_average_price_airline(flights, airline):
    # Filter the DataFrame for the specified airline
    airline_data = flights[flights['Air Carrier'] == airline]

    # Retrieve unique travel classes present in the DataFrame
    travel_classes = airline_data['Travel Class'].unique()

    # Create a dictionary for the results
    results = {'Airline': airline}

    # Calculate the average price for each travel class
    for travel_class in travel_classes:
        # Filter data for the specific travel class
        class_data = airline_data[airline_data['Travel Class'] == travel_class]
        # Calculate the average price for the travel class
        average_price = class_data['Price in £'].mean()
        results[f'Average Price {travel_class}'] = average_price

    # Check if there is only one travel class
    if len(travel_classes) == 1:
        results['Info'] = f"The airline {airline} only has {travel_classes[0]} class flights"
    elif len(travel_classes) == 0:
        results['Info'] = f"The airline {airline} has no flights recorded in the DataFrame"

    # Return the results
    return results

'''
# Example usage
chosen_airline = 'Airline Name'
result = calculate_average_price_airline(flights, chosen_airline)

# Display available airlines and prompt user for input
chosen_airline = 'FLYBE'
# Example usage
result = calculate_average_price_airline(flights, chosen_airline)

print(result)
'''