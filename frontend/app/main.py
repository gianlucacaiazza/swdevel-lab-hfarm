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
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'


class QueryForm(FlaskForm):
    province = StringField('Province:')
    submit = SubmitField('Get province from FastAPI Backend')


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



@app.route('/internal', methods=['GET', 'POST'])
def internal():
    """
    Render the internal page.

    Returns:
        str: Rendered HTML content for the internal page.
    """
    form = QueryForm()
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
            
            # Call your function to find the best school in town
            best_school_info = best_school_in_town(data, province, 'scuola_level')  # Replace 'scuola_level' with the actual school level
            
            return render_template('internal.html', form=form, result=result, error_message=error_message, best_school_info=best_school_info)
        else:
            error_message = f'Error: Unable to fetch province for {province} from FastAPI Backend'

    return render_template('internal.html', form=form, result=None, error_message=error_message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_HOST = 'https://vscode.dev/github/KlementinaYlli/M.E.K.E-Group/blob/KlementinaYlli_module/backend/app/main.py'  

class QueryForm(FlaskForm):
    province = StringField('Province:')
    infrastructures = SelectMultipleField('Choose Infrastructures:', choices=[('Mensa', 'Cafeteria'), ('PalestraPiscina', 'GYM and POOL')])
    submit = SubmitField('Find Schools')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = QueryForm()
    schools = None
    error_message = None

    if form.validate_on_submit():
        province = form.province.data
        infrastructures = ','.join(form.infrastructures.data)
        schools, error_message = fetch_schools(province, infrastructures)

    return render_template('index.html', form=form, schools=schools, error_message=error_message)

def fetch_schools(province, infrastructures):
    """
    Fetch schools based on the province and infrastructure requirements.

    Args:
        province (str): The province to search in.
        infrastructures (str): Comma-separated string of infrastructures.

    Returns:
        tuple: Tuple containing the schools (if any) and an error message (if any).
    """
    backend_url = f'{FASTAPI_BACKEND_HOST}/schools/{province}/{infrastructures}'
    try:
        response = requests.get(backend_url)
        if response.status_code == 200:
            return response.json(), None
        else:
            return None, f"Error: Backend responded with status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return None, f"Error: Could not connect to backend. Exception: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)


