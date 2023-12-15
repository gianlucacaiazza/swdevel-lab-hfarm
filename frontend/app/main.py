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
    departure = SelectField('Departure:')
    submit1 = SubmitField('Where can i go?')
    airline = SelectField('Airlines:')
    submit2 = SubmitField('Get airlines')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/randomize', methods=['GET', 'POST'])
def randomize():
    form = QueryForm()
    response = requests.get(f'{FASTAPI_BACKEND_HOST}/get_departure')
    departures = json.loads(response.json())
    form.departure.choices=departures
    BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query'
    if form.validate_on_submit():
        departure = form.departure.data
        response = requests.get(f'{BACKEND_URL}/{departure}')
        data = response.json()
        return render_template('randomize.html', form=form, result = data)
    else:
        return render_template('randomize.html', form=form, result = f'None')

@app.route('/result', methods=['GET', 'POST'])
def show_result():
    BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/random'
    if request.method == 'POST':
        departure = request.form['departure']
        try:
            response = requests.get(f'{BACKEND_URL}/{departure}')
            if response.status_code == 200:
                data = response.json()
                data = ', '.join(data)
                if data:  # Check if there is a result
                    return render_template('result.html', result=data)
                else:
                    return render_template('result.html', message="No result")
            else:
                status = response.status_code
                return render_template('result.html', message="App not responding, response status = "f'{status}')
        except requests.exceptions.ConnectionError as e:
            return render_template('result.html', message=f"Connection error: {str(e)}")
    return redirect(url_for('randomize'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
        
