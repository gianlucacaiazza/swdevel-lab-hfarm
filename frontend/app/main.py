"""
Frontend module for the Flask application.

This module defines a simple Flask application that serves as the frontend for the project.
"""

from flask import Flask, render_template
import requests  # Import the requests library to make HTTP requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_HOST = 'http://backend'  # Replace with the actual URL of your FastAPI backend
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'


class QueryForm(FlaskForm):
    person_name = StringField('Person Name:')
    submit = SubmitField('Get Birthday from FastAPI Backend')

class MoodForm(FlaskForm):
    mood = SelectField('Choose a Mood', choices=[
        ('chill', 'Chill'),
        ('workout', 'Workout'),
        ('passion', 'Passion'),
        ('party', 'Party'),
        ('discover','Discover')
    ], validators=[DataRequired()])


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


@app.route('/mood', methods=['GET', 'POST'])
def mood():
    form = MoodForm()
    error_message = None
    songs = None

    if form.validate_on_submit():
        selected_mood = form.mood.data
        fastapi_url = f'{FASTAPI_BACKEND_HOST}/mood/{selected_mood}'
        response = requests.get(fastapi_url)
        if response.status_code == 200:    
            songs = response.json()
        else:
            error_message = f'Error: Failed to retrive playlist for {selected_mood} from FastAPI Backend'

    return render_template('mood.html', form=form, songs=songs, error_message=error_message)

@app.route('/info')
def info():
    error_message = None
    data = {}

    info_list = ["c_songs", "genre", "p_genre"]

    backend_url = f'{FASTAPI_BACKEND_HOST}/info/'

    for info in info_list:
        response = requests.get(backend_url + info)
        if response.status_code == 200:
            data[info] = response.json()
        else:
            error_message = f"Error: Unable to retrieve {info} from the backend."

    return render_template('info.html', data=data, error_message=error_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
