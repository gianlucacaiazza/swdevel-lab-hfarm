
"""

Read a flights dataset from a CSV file and perform data cleaning operations.

Parameters:
- file_path (str): The path to the CSV file containing flights data.

Returns:
- DataFrame: A cleaned DataFrame with irrelevant columns removed, currency 
symbols removed
from the 'Total Cost ex VAT' column, and columns renamed for clarity.

"""

import pandas as pd


flights_data = pd.read_csv('/app/app/flights.csv', encoding='ISO-8859-1')

# Remove useless columns
df_clean = flights_data.drop(columns=["Number of Travellers", "Customer"])


def clean_cost(value):
    """

    Apply to column with '£' values.

    Replace '£' values with spaces for future modelling of value
    Returning float

    """
    if isinstance(value, str) and '£' in value:
        return float(value.replace('£', '').replace(',', '').strip())
    else:
        return float(value)


df_clean[' Total Cost ex VAT '] = df_clean[' Total Cost ex VAT '].apply(clean_cost)

# Renaming the columns for clarity
df_clean.rename(columns={' Total Cost ex VAT ': 'Price in £'}, inplace=True)
df_clean.rename(columns={'Journey Start Point': 'Departure'}, inplace=True)
df_clean.rename(columns={'Journey Finish Point': 'Arrival'}, inplace=True)

# Renaming an Air Carrier
plane = df_clean['Air Carrier']
plane = plane.replace('DO NOT USE - EASYJET - PLEASE ', 'EASYJET')
