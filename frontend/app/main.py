"""
Frontend module for the Flask application.

This module defines a simple Flask application that serves as the frontend for the project.
"""

from flask import Flask, render_template
import requests  # Import the requests library to make HTTP requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_HOST = 'http://backend'  # Replace with the actual URL of your FastAPI backend


<<<<<<< Updated upstream
=======
class ProviderForm(FlaskForm):
    provider_name = StringField('Provider Name:')
    submit = SubmitField('Search')

class QueryForm(FlaskForm):
    street_name = StringField('Street name:')
    submit = SubmitField('Get number of columns from FastAPI Backend')


>>>>>>> Stashed changes
@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: Rendered HTML content for the index page.
    """
    # Fetch the date from the backend
    date_from_backend = fetch_date_from_backend()
    return render_template('index.html', date_from_backend=date_from_backend)

def fetch_date_from_backend():
    """
    Function to fetch the current date from the backend.

    Returns:
        str: Current date in ISO format.
    """
    backend_url = 'http://backend/get-date'  # Adjust the URL based on your backend configuration
    try:
        response = requests.get(backend_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json().get('date', 'Date not available')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching date from backend: {e}")
        return 'Date not available'


<<<<<<< Updated upstream
=======
@app.route('/provider', methods=['GET', 'POST'])
def provider():
    form = ProviderForm()
    form.provider_name.label = 'Select the name of your provider'
    error_message = None  # Initialize error message

    if form.validate_on_submit():
        provider_name = form.provider_name.data
        fastapi_url = f'{FASTAPI_BACKEND_HOST}/module/lookfor/{provider_name}'
        response = requests.get(fastapi_url)
        if response.status_code == 200:
            data = response.json()
            #charging_points = data.get('Available charging points', f'Error: charging points not available for {provider_name}')
            
            return render_template('provider.html', form=form, result=data, error_message=error_message)
        else:
            error_message = f'Error: Unable to fetch data for {provider_name} from FastAPI Backend'
    return render_template('provider.html', form=form, result=None, error_message=error_message)

'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

'''


@app.route('/number_stations', methods=['GET', 'POST'])
def number_stations():
    """
    Render the internal page.

    Returns:
        str: Rendered HTML content for the index page.
    """
    form = QueryForm()
    error_message = None  # Initialize error message

    if form.validate_on_submit():
        street_name = form.street_name.data

        # Make a GET request to the FastAPI backend
        fastapi_url = f'{FASTAPI_BACKEND_HOST}/get_charging_stations/{street_name}'
        response = requests.get(fastapi_url)

        if response.status_code == 200:
            # Extract and display the result from the FastAPI backend
            data = response.json()
            return render_template('number_stations.html', form=form, result=data, error_message=error_message)
        else:
            error_message = f'Error: Unable to fetch dict_vie for {street_name} from FastAPI Backend'

    return render_template('number_stations.html', form=form, result=None, error_message=error_message)

>>>>>>> Stashed changes
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
