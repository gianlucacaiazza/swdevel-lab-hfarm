from fastapi import FastAPI
from .mymodules import data_handling
import pandas as pd


app = FastAPI()


# Creating dataframes with pandas
attractions = pd.read_csv('Datasets/Locations.csv')
crime = pd.read_csv('Datasets/CrimeCount.csv')
stations = pd.read_csv('Datasets/Stations.csv')
trees = pd.read_csv('Datasets/Trees.csv')
zip = pd.read_csv('Datasets/zip_neighbourhood.csv')
bnb = pd.read_csv('Datasets/AirBnb.csv')


def convert_price(price_str):
    prezzo_float = float(price_str.replace('$', '').replace(',', ''))

    return int(prezzo_float)

bnb['price'] = bnb['price'].apply(convert_price)


@app.get('/search')
def search_bnb(min, max, trees_bool, crime_rate ):
    min = int(min)
    max = int(max)
    crime_rate = int(crime_rate)
    zipcodes_attr = data_handling.corrZipAtt(min, max)
    zipcodes_trees = data_handling.corrZipTrees(trees_bool)
    zipcodes_crime = data_handling.corrZipCrime(crime_rate)
    
    res = data_handling.commonZip(zipcodes_attr, zipcodes_crime, zipcodes_trees)

    val = data_handling.cheapestBnbPerZip(res, bnb)

    list_of_dicts = val.to_json(orient='records')

    return list_of_dicts