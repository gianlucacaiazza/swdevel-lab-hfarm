
"""
Frontend module for the Flask application.

This module defines a simple Flask application that serves as the frontend for the project.
"""


from flask import Flask, render_template, request
import requests  # Import the requests library to make HTTP requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_HOST = 'http://backend'  # Replace with the actual URL of your FastAPI backend
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'


app = Flask(__name__)
app.secret_key = 'your_secret_key'  

FASTAPI_BACKEND_HOST = 'http://backend'  

class AddressesForm(FlaskForm):
    area_name = SelectField('Area name:', choices=[
        ('DUOMO', 'DUOMO'),
        ('MAGENTA - S. VITTORE', 'MAGENTA - S. VITTORE'),
        ('CENTRALE', 'CENTRALE'),
        ("CITTA' STUDI", "CITTA' STUDI"),
        ('BARONA', 'BARONA'),
        ('GUASTALLA', 'GUASTALLA'),
        ('GIARDINI PORTA VENEZIA','GIARDINI PORTA VENEZIA'),
        ('ISOLA','ISOLA'),
        ('BUENOS AIRES', 'BUENOS AIRES'),
        ('PORTA ROMANA', 'PORTA ROMANA'),
        ('VIGENTINA', 'VIGENTINA'),
        ('TORTONA', 'TORTONA'),
        ('NAVIGLI', 'NAVIGLI'),
        ('PAGANO','PAGANO'),
        ('TRE TORRI', 'TRE TORRI'),
        ('BOVISA', 'BOVISA'),
        ('GARIBALDI REPUBBLICA', 'GARIBALDI REPUBBLICA'),
        ('BICOCCA', 'BICOCCA'),
        ('TICINESE', 'TICINESE'),
        ('LODI - CORVETTO', 'LODI - CORVETTO'),
        ('TIBALDI', 'TIBALDI'),
        ('UMBRIA - MOLISE', 'UMBRIA - MOLISE'),
        ('DE ANGELI - MONTE ROSA', 'DE ANGELI - MONTE ROSA'),
        ('BRERA', 'BRERA'),
        ('GRECO', 'GRECO'),
        ('SCALO ROMANA', 'SCALO ROMANA'),
        ('LORENTEGGIO', 'LORENTEGGIO'),
        ('GIAMBELLINO', 'GIAMBELLINO'),
        ('SARPI', 'SARPI'),
        ('PARCO LAMBRO - CIMIANO', 'PARCO LAMBRO - CIMIANO'),
        ('MACIACHINI - MAGGIOLINA', 'MACHIACHINI - MAGGIOLINA'),
        ('LORETO', 'LORETO'),
        ('PADOVA', 'PADOVA'),
        ('XXII MARZO', 'XXII MARZO'),
        ('RIPAMONTI', 'RIPAMONTI'),
        ('BANDE NERE', 'BANDE NERE'),
        ('S. SIRO', 'S. SIRO'),
        ('QUARTO OGGIARO', 'QUARTO OGGIARO'),
        ('FARINI', 'FARINI'),
        ("NIGUARDA - CA' GRANDA", "NIGUARDA - CA' GRANDA"),
        ('ENERMIA', 'ENERMIA'),
        ('EX OM - MORIVIONE', 'EX OM - MORIVIONE'),
        ('S. CRISTOFORO', 'S. CRISTOFORO'),
        ('LAMBRATE', 'LAMBRATE'),
        ('PARCO FORLANINI - ORTICA', 'PARCO FORLANINI - ORTICA'),
        ('VIALE MONZA', 'VIALE MONZA'),
        ('STADERS', 'STADERA'),
        ('WASHINGTON', 'WASHINGTON'),
        ('PORTELLO', 'PORTELLO'),
        ('FORZE ARMATE', 'FORZE ARMATE'),
        ('GALLARATESE', 'GALLARATESE'),
        ('AFFORI', 'AFFORI'),
        ('QT 8', 'QT 8'),
        ('VILLAPIZZONE', 'VILLAPIZZONE'),
        ('GHISOLFA', 'GHISOLFA'),
        ('ORTOMERCATO', 'ORTOMERCATO'),
        ('DERGANO', 'DERGANO'),
        ('CORSICA', 'CORSICA')

    ])
    submit = SubmitField('Get Area_name from FastAPI Backend')

class ProviderForm(FlaskForm):
    provider_name = SelectField()

    
class QueryForm(FlaskForm):
    street_name = StringField('Street name:')
    submit = SubmitField('Get number of columns from FastAPI Backend')


class ProviderstreetnameForm(FlaskForm):
    street_name = StringField('Street Name:')
    submit = SubmitField('Search')

    
class ZoneForm(FlaskForm):
    zone_name=StringField('Zone name')
    submit=SubmitField('Get types of sockets from FASTAPI Backend')
    
@app.route('/')
def index():
    date_from_backend = fetch_date_from_backend()
    return render_template('index.html', date_from_backend=date_from_backend)
  

def fetch_date_from_backend():
    backend_url = 'http://backend/get-date'
    try:
        response = requests.get(backend_url)
        response.raise_for_status()
        return response.json().get('date', 'Date not available')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching date from backend: {e}")
        return 'Area name not available'

@app.route('/addresses', methods=['GET', 'POST'])
def addresses():
    form = AddressesForm()
    error_message = None 

    if form.validate_on_submit():
        selected_area = form.area_name.data

        fastapi_url = f'{FASTAPI_BACKEND_HOST}/addresses/{selected_area}'
        response = requests.get(fastapi_url)

        if response.status_code == 200:
            return render_template('addresses.html', form=form, result=response.text, error_message=error_message)
        else:
            error_message = f'Error: Unable to fetch area_name for {selected_area} from FastAPI Backend'

    return render_template('addresses.html', form=form, result=None, error_message=error_message)


@app.route('/provider', methods=['GET', 'POST'])
def provider():
    error_message = None  # Initialize error message
    form = None  # Initialize form as None

    if request.method == 'POST':
        provider_name = request.form.get('provider_name')
        fastapi_url = f'{FASTAPI_BACKEND_HOST}/module/lookfor/{provider_name}'
        response = requests.get(fastapi_url)
        
        if response.status_code == 200:
            data = response.json()
            form = ProviderForm()  # Reinitialize form if needed
            return render_template('provider.html', form=form, result=data, error_message=error_message)
        else:
            error_message = f'Error: Unable to fetch data for {provider_name} from FastAPI Backend'

    form = ProviderForm()  # Initialize form for initial GET request
    return render_template('provider.html', form=form, result=None, error_message=error_message)

@app.route('/street_name', methods=['GET','POST'])
def provider_street_name():
    form = ProviderstreetnameForm()
    error_message= None

    if form.validate_on_submit():
        street_name = form.street_name.data
        fastapi_url = f'{FASTAPI_BACKEND_HOST}/module/search/{street_name}'
        response = requests.get(fastapi_url)
        if response.status_code == 200:
            data = response.json()
            return render_template('street_name1.html', form=form, result=data, error_message=error_message)
        else:
            error_message = f'Error: Unable to fetch data for {street_name} form FastAPI backend'
    return render_template('street_name1.html', form=form, result=None, error_message=error_message)




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

    
@app.route('/socket_types', methods=['GET', 'POST'])
def socket_types():
    error_message = None
    form = None

    if request.method == 'POST':
        zone_name = request.form.get('zone_name')
        fastapi_url = f'{FASTAPI_BACKEND_HOST}/socket_types_by_zone/{zone_name}'
        response = requests.get(fastapi_url)

        if response.status_code == 200:
            data = response.json()
            form = ZoneForm()
            return render_template('socket_types.html', form=form, result=data, error_message=error_message)
        else:
            error_message = f'Error: Unable to fetch data for {zone_name} from FASTAPI backend'

    form = ZoneForm()
    return render_template('socket_types.html', form=form, result=None, error_message=error_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

