import pandas as pd

# Creating dataframes with pandas
attractions = pd.read_csv('Datasets/Locations.csv')
crime = pd.read_csv('Datasets/CrimeCount.csv')
stations = pd.read_csv('Datasets/Stations.csv')
trees = pd.read_csv('Datasets/Trees.csv')
zip = pd.read_csv('Datasets/zip_neighbourhood.csv')
bnb = pd.read_csv('Datasets/AirBnb.csv')

# Finds zipcodes that respects the criteria for the number of attractions
def corrZipAtt(min, max):
    counts_by_zipcode = attractions.groupby('Zipcode')['Tourist_Spot'].count().reset_index()
    filtered_locations = counts_by_zipcode[(counts_by_zipcode['Tourist_Spot'] >= min) & (counts_by_zipcode['Tourist_Spot'] <= max)]
    return filtered_locations['Zipcode'].tolist()
