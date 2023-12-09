import json
from flask import Flask, render_template
import requests  # Import the requests library to make HTTP requests
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_HOST = 'http://backend'


class SeachBnBForm(FlaskForm):
    min_attr = SelectField('Min attractions?:',
                         choices=[0, 5, 10])
    max_attr = SelectField('Max attractions?:',
                         choices=[5, 10, 20])
    trees_bool = SelectField('Do you want to be in a green area:',
                             choices=['True', 'False'])
    crime_rate = SelectField('How much do you care for a crime-free area?:',
                             choices=[1, 2, 3, 4])

    submit = SubmitField('Search')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SeachBnBForm()
    error_message = None

    if form.validate_on_submit():
        crime_rate = form.crime_rate.data
        min_attr = form.min_attr.data
        max_attr = form.max_attr.data
        trees_bool = form.trees_bool.data

        response = requests.get(
            'http://backend/search',
            params={
                'min': min_attr,
                'max': max_attr,
                'trees_bool': trees_bool,
                'crime_rate': crime_rate
            }
        )

        if response.status_code == 200:
            data = response.json()
            data = json.loads(data)
            data = [elem for elem in data]
            return render_template('search.html',
                                   form=form,
                                   string_list=data,
                                   error_message=error_message)
        else:
            error_message = f'Error: Unable to fetch data from FastAPI Backend'

    return render_template('search.html', form=form, result=None,
                           error_message=error_message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)