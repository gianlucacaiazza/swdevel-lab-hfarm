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


@app.route('/airlines_comparator', methods=['GET', 'POST'])
def airlines():
    form = QueryForm()
    response = requests.get(f'{FASTAPI_BACKEND_HOST}/get_airline')
    airlines = json.loads(response.json())
    form.airline.choices=airlines
    BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/{airlines}'
    if form.validate_on_submit():
        airlines = form.airline.data
        response = requests.get(f'{BACKEND_URL}/{airlines}')
        data = response.json()
        return render_template('airlines.html', form=form, result = data)
    else:
        return render_template('airlines.html', form=form, result = f'None')
    
@app.route('/result-air', methods=['GET', 'POST'])
def show_results():
    BACKEND_URL = f'{FASTAPI_BACKEND_HOST}'
    if request.method == 'POST':
        airlines = request.form['airline']
        try:
            response = requests.get(f'{BACKEND_URL}/{airlines}')
            if response.status_code == 200:
                data = response.json()
                if data:  # Check if there is a result
                    return render_template('results_air.html', result=data)
                else:
                    return render_template('results_air.html', message="No result")
            else:
                status = response.status_code
                return render_template('results_air.html', message="App not responding, response status = "f'{status}')
        except requests.exceptions.ConnectionError as e:
            return render_template('results_air.html', message=f"Connection error: {str(e)}")
    return redirect(url_for('airlines'))

@app.route('/image')
def image():
    return render_template('image.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
        
