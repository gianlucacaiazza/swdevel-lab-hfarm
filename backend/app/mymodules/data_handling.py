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


# Finds zipcodes that respects the criteria for green areas
def corrZipTrees(trees_bool):
    if(trees_bool == 'True'):
        trees_mean = int(trees['count'].mean())
        zipcodes_trees = trees[trees['count'] >= trees_mean]['zipcode'].tolist()
    else:
        zipcodes_trees = trees['zipcode'].tolist()
    
    return zipcodes_trees


# Finds zipcodes that respects the criteria for crime rates
def corrZipCrime(crime_rate):
    if(crime_rate == 4):
        crime_threshold = int(((crime['count'].max()-crime['count'].min())/4)+crime['count'].min())
        zipcodes_crime = crime[crime['count'] <= crime_threshold]['zipcode'].tolist()
    elif(crime_rate == 3):
        crime_threshold = int(((crime['count'].max()-crime['count'].min())/2)+crime['count'].min())
        zipcodes_crime = crime[crime['count'] <= crime_threshold]['zipcode'].tolist()
    elif(crime_rate == 2):
        crime_threshold = int(((((crime['count'].max()-crime['count'].min())/4))*3)+crime['count'].min())
        zipcodes_crime = crime[crime['count'] <= crime_threshold]['zipcode'].tolist()
    elif(crime_rate == 1):
        zipcodes_crime = crime['zipcode'].tolist()

    return zipcodes_crime


# Finds common zipcodes among three lists
def commonZip(zip_1, zip_2, zip_3):
    res = set(zip_1) & set(zip_2) & set(zip_3)
    return list(res)
    

# Find the cheapest zipcode for each zipcode in the list
def cheapestBnbPerZip(zip_list, bnb_df):
    filtered_airbnb_df = bnb_df[bnb_df['zipcode'].isin(zip_list)]
    min_price_airbnb_df = filtered_airbnb_df.loc[filtered_airbnb_df.groupby('zipcode')['price'].idxmin()]
    
    return min_price_airbnb_df