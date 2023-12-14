
import sys
sys.path.append('app/mymodules')

import pandas as pd

import sys
sys.path.append('app/mymodules')

from Cleaning import flights_data_cleaned
import datetime
import random
df = flights_data_cleaned

#changing travel date string into datetime format

df['Travel Date'] = pd.to_datetime(df['Travel Date'], format = '%d/%m/%Y')

#iterating over dataframe
add_rows = []
#create a condition (mask) that checks whether the value in the 'Ticket Single or Return' column is equal to 'Return'
mask = df['Ticket Single or Return'] == 'Return'
#slash price by half where mask value = TRUE
df.loc[mask, 'Price in £'] = df.loc[mask, 'Price in £'] / 2

# creating new row for return ticket 
new_row = df[mask].copy()
add_rows = df[mask].copy()

#switching departure with arrival to create return ticket, 1 to 3 days after, random
random_number = random.randint(1, 3)
add_rows['Departure'], add_rows['Arrival'] = add_rows['Arrival'], add_rows['Departure']
add_rows['Travel Date'] = add_rows['Travel Date'] + pd.Timedelta(days=random_number)

#adding the new roes to the dataframe
df = pd.concat([df, pd.DataFrame(add_rows)], ignore_index=True)

#sort by travel date
df = df.sort_values(by = 'Travel Date', ascending = True)

#drop column 'Ticket Single or Return', drop duplicates, reset indexes
df.drop(columns=['Ticket Single or Return'],inplace=True)
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)

#our final dataset to use for the project 
flights = df

