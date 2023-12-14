"""
Frontend module for the Flask application.

This module defines a simple Flask application that serves as the frontend for the project.
"""

from flask import Flask, render_template, Request, redirect, url_for, request
app = Flask(__name__)

# ... [Altra configurazione necessaria, se presente] ...

import requests  # Import the requests library to make HTTP requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_HOST = 'http://backend:80'  # Replace with the actual URL of your FastAPI backend

class QueryForm(FlaskForm):
    Departure = SelectField('Departure: ')
    Arrival = SelectField('Arrival: ')
    submit = SubmitField('Result: ')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate_average_price', methods=['GET', 'POST'])
def calculate_average_price():
    # Extracting selected departure and arrival airports from the form
    form = QueryForm()
    response = requests.get(f'{FASTAPI_BACKEND_HOST}/get_airport')
    airports = json.loads(response.json())
    form.Departure.choices = airports
    form.Arrival.choices = airports
    Departure = airports
    Arrival =  airports
    BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/{Departure}/{Arrival}'
    if form.validate_on_submit():
        Departure = form.Departure.data
        Arrival = form.Arrival.data
        response = requests.get(f'{BACKEND_URL}/{Departure}/{Arrival}')
        data = response.json()
        return render_template('flights1.html', form = form, result = data)
    else:
        return render_template('flights1.html', form = form, data = f'None')
    
@app.route('/results-flights', methods = ['GET','POST'])
def resultshow():
    BACKEND_URL = f'{FASTAPI_BACKEND_HOST}'
    if request.method == 'POST':
        Departure = request.form['Departure']
        Arrival = request.form['Arrival']
        try:
            response = requests.get(f'{BACKEND_URL}/{Departure}/{Arrival}')
            if response.status_code == 200:
                data = response.json()
                if data:
                    return render_template('result_avg.html', result = data)
                else:
                    return render_template('result_avg.html', message = 'No Result')
            else:
                status = response.status_code
                return render_template('result_avg.html', message = 'App not Responding = ' f'{status}')
        except requests.exceptions.ConnectionError as e:
            return render_template('result_avg.html', message = f'Connection error: {str(e)}')
    return redirect(url_for('calculate_average_price'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
        
