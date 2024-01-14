"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd




from .mymodules.search_school import schools_by_province
from .mymodules.feature_2_best_school_in_town import best_school_in_town 
from .mymodules.feat_1_elenco_scuole_con_infrastrutture import elenco_scuole_con_infrastrutture


app = FastAPI()

# Dictionary of birthdays
birthdays_dictionary = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'
}

df = pd.read_csv('/app/app/employees.csv')

# Lettura del csv, si usa sep=';' poiche' questo file usa come separatore
# il punto e virgola e non la virgola.
veneto = pd.read_csv('/app/app/veneto.csv', sep=';')

@app.get('/csv_show')
def read_and_return_csv():
    return{veneto.to_string()}

@app.get('/')
def read_root():
    """
    Root endpoint for the backend.

    Returns:
        dict: A simple greeting.
    """
    return {"Hello": "World"}


@app.get('/query/{person_name}')
def read_item(person_name: str):
    """
    Endpoint to query birthdays based on person_name.

    Args:
        person_name (str): The name of the person.

    Returns:
        dict: Birthday information for the provided person_name.
    """
    person_name = person_name.title()  # Convert to title case for consistency
    birthday = birthdays_dictionary.get(person_name)
    if birthday:
        return {"person_name": person_name, "birthday": birthday}
    else:
        return {"error": "Person not found"}

# Restituisce tutte le scuole filtrare per provincia.
@app.get('/module/search/province/{province}')
def read_item_from_module(province: str):
    return JSONResponse(schools_by_province(province, veneto))


@app.get('/module/all')
def dump_all_birthdays():
    return {print_birthdays_str()}


@app.get('/get-date')
def get_date():
    """
    Endpoint to get the current date.

    Returns:
        dict: Current date in ISO format.
    """
    current_date = datetime.now().isoformat()
    return JSONResponse(content={"date": current_date})


@app.get('/best-school/{city}/{school_level}')
def get_best_school(city: str, school_level: str):
    return JSONResponse(best_school_in_town(veneto, city, school_level))
        

@app.get('/schools/{nome_provincia}/{infrastrutture}')
def get_schools(nome_provincia: str, infrastrutture: str):
    infrastrutture_list = infrastrutture.split(',')  # Crea una lista dalle stringhe separate da virgole
    result = elenco_scuole_con_infrastrutture(veneto, nome_provincia, infrastrutture_list)
    return JSONResponse(result)