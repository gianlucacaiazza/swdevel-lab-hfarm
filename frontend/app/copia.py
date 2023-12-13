from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetching unique departure airports from the FastAPI backend
    departure_airports = requests.get('http://localhost:8000/departure_airports').json()

    return render_template('index.html', departure_airports=departure_airports)

@app.route('/calculate_average_price', methods=['POST'])
def calculate_average_price():
    # Extracting selected departure and arrival airports from the form
    departure_airport = request.form.get('departure_airport')
    arrival_airport = request.form.get('arrival_airport')

    # Sending a request to the FastAPI backend to calculate the average price
    response = requests.get(f'http://localhost:8000/{departure_airport}/{arrival_airport}')
    result = response.json()

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
