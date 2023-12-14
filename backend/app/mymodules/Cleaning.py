import pandas as pd
import numpy as np

flights_data = pd.read_csv('/app/app/flights.csv', encoding='ISO-8859-1')

# Remove useless columns
flights_data_cleaned = flights_data.drop(columns=["Number of Travellers", "Customer"])

# Cleaning the 'Total Cost ex VAT' column
def clean_cost(value):
    if isinstance(value, str) and '£' in value:
        return float(value.replace('£', '').replace(',', '').strip())
    else:
        return value

# Apply the cleaning function to the column
flights_data_cleaned[' Total Cost ex VAT '] = flights_data_cleaned[' Total Cost ex VAT '].apply(clean_cost)

# Renaming the columns for clarity
flights_data_cleaned.rename(columns={' Total Cost ex VAT ':'Price in £'}, inplace=True)
flights_data_cleaned.rename(columns={'Journey Start Point':'Departure'}, inplace=True)
flights_data_cleaned.rename(columns={'Journey Finish Point':'Arrival'}, inplace=True)

print(flights_data_cleaned['Price in £'].values)



