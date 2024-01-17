"""
Frontend module for the Flask application.

This module defines a simple Flask application that serves as the frontend for the project.
"""

from flask import Flask, render_template
import requests  # Import the requests library to make HTTP requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_HOST = 'http://backend'  # Replace with the actual URL of your FastAPI backend
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'


class ScoolbyProvince(FlaskForm):
    province = SelectField('Province:', choices=[])
    submit = SubmitField('Get all schools')

class BestSchoolForm(FlaskForm):
    city = SelectField('City:', choices=[])
    type = SelectField('Type:', choices=[])
    
    submit = SubmitField('Get best school')
    
class SchoolInfrastructuresForm(FlaskForm):
    province = SelectField('Province:', choices=[])
    infrastructure = SelectField('Infrastructures:', choices=[])
    
    submit = SubmitField('Get all schools')

@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: Rendered HTML content for the index page.
    """
    # Fetch the date from the backend
    return render_template('index.html')


@app.route('/school-by-province', methods=['GET', 'POST'])
def school_by_province():
    """
    Render the internal page.

    Returns:
        str: Rendered HTML content search school by province page.
    """
    form = ScoolbyProvince()
    form.province.choices = make_tuples(list('provinces'))
    
    error_message = None  # Initialize error message

    if form.validate_on_submit():
        province = form.province.data

        # Make a GET request to the FastAPI backend
        fastapi_url = f'{FASTAPI_BACKEND_HOST}/module/search/province/{province}'
        response = requests.get(fastapi_url)

        if response.status_code == 200:
            # Extract and display the result from the FastAPI backend
            data = response.json()
            result = data.get('result', f'Error: province not available for {province}')
            return render_template('school_by_province.html', form=form, result=result, error_message=error_message)
        else:
            error_message = f'Error: Unable to fetch province for {province} from FastAPI Backend'

    return render_template('school_by_province.html', form=form, result=None, error_message=error_message)


@app.route('/best-school', methods=['GET', 'POST'])
def best_school():
    """
    Render the best school page.

    Returns:
        str: Rendered HTML content best school section.
    """
    form = BestSchoolForm()
    
    cities = list('cities')
    types = list('school_types')

    form.city.choices = make_tuples(cities)
    form.type.choices = make_tuples(types)
    
    error_message = None  # Initialize error message

    if form.validate_on_submit():
        city = form.city.data
        type = form.type.data
        
        # Make a GET request to the FastAPI backend
        fastapi_url = f'{FASTAPI_BACKEND_HOST}/module/search/rank/{city}/{type}'
        response = requests.get(fastapi_url)

        if response.status_code == 200:
            # Extract and display the result from the FastAPI backend
            data = response.json()
            
            result = data.get('result', [])
            return render_template('best_school.html', form=form, result=result, error_message=error_message)
        else:
            error_message = f'Error: Unable to fetch'

    return render_template('best_school.html', form=form, result=None, error_message=error_message)


@app.route('/school-with-infrastructures', methods=['GET', 'POST'])
def shool_with_infrastructures():
    """
    Render the best school with infrastructures page.

    Returns:
        str: Rendered HTML content best school with infrastructures section.
    """
    form = SchoolInfrastructuresForm()
    
    provinces = list('provinces')

    form.province.choices = make_tuples(provinces)
    form.infrastructure.choices = [
        ("Spazi Didattici", "Spazi Didattici"),
        ("Auditorium Aula Magna", "Auditorium Aula Magna"),
        ("Mensa", "Mensa"),
        ("Palestra Piscina", "Palestra Piscina"),
        ("Spazi Amministrativi", "Spazi Amministrativi")
	]
    
    error_message = None  # Initialize error message

    if form.validate_on_submit():
        province = form.province.data
        infrastructure = form.infrastructure.data
        
        # Make a GET request to the FastAPI backend
        fastapi_url = f'{FASTAPI_BACKEND_HOST}/module/search/infrastructure/{province}/{infrastructure}'
        response = requests.get(fastapi_url)

        if response.status_code == 200:
            # Extract and display the result from the FastAPI backend
            data = response.json()
            
            result = data.get('result', [])
            return render_template('school_with_infrastructures.html', form=form, result=result, error_message=error_message)
        else:
            error_message = f'Error: Unable to fetch'

    return render_template('school_with_infrastructures.html', form=form, result=None, error_message=error_message)

def list(element):
    """
    Function to list a column of the csv file.

    Returns:
        list: List of unique values of the requested column.
    """
    backend_url = f'{FASTAPI_BACKEND_HOST}/all/{element}'
    try:
        response = requests.get(backend_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json().get('elements', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching date from backend: {e}")
        return 'Date not available'


def make_tuples(element):
    result = []
    for x in element:
        result.append((x, x))
    return result


if __name__ == '__main__':    app.run(host='0.0.0.0', port=80, debug=True)
