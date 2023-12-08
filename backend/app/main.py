"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd

import sys

# Aggiungi il percorso della directory al sys.path
sys.path.append('/app/app/mymodules/')

# Ora puoi importare il modulo Cleaning
from mymodules.Cleaning import flights_data_cleaned
from mymodules.df_integrations import flights
from mymodules.Destination_random import randomize_destination



app = FastAPI()


@app.get('/')
def read_root():
    """
    Root endpoint for the backend.
    Returns:
        dict: A simple greeting.
    """
    return {"Hello": "World"}


#@app.get('/query/{person_name}')
#def read_item(person_name: str):
#    """
#    Endpoint to query birthdays based on person_name.

#    Args:
#        person_name (str): The name of the person.

#    Returns:
#        dict: Birthday information for the provided person_name.
#    """
#    person_name = person_name.title()  # Convert to title case for consistency
#    birthday = birthdays_dictionary.get(person_name)
#    if birthday:
#        return {"person_name": person_name, "birthday": birthday}
#    else:
#        return {"error": "Person not found"}


#@app.get('/module/search/{person_name}')
#def read_item_from_module(person_name: str):
#    return {return_birthday(person_name)}


#@app.get('/module/all')
#def dump_all_birthdays():
#    return {print_birthdays_str()}


#@app.get('/get-date')
#def get_date():
#    """
#    Endpoint to get the current date.

#    Returns:
#        dict: Current date in ISO format.
#    """
#    current_date = datetime.now().isoformat()
#    return JSONResponse(content={"date": current_date})



#from mymodules.Cleaning import flights_data 

@app.get('/randomize')
def randomzie():
    return randomize_destination(input(), flights)

