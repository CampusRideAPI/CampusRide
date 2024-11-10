from flask import Flask, render_template, request, redirect, url_for
import requests
app = Flask(__name__)
API_URL = "http://localhost:8000"

@app.route('/')
def list_rides():
    response = requests.get(f"{API_URL}/rides")
    rides = response.json()["rides"]
    return render_template('rides_list.html', rides=rides)

@app.route('/rides/new', methods=['GET', 'POST'])
def create_ride():
    if request.method == 'POST':
        ride_data = {
            "departure_location": request.form["departure_location"],
            "arrival_location": request.form["arrival_location"],
            "departure_time": request.form["departure_time"],
            "available_seats": int(request.form["available_seats"]),
            "driver_name": request.form["driver_name"]
        }
        response = requests.post(f"{API_URL}/rides", json=ride_data)
        return redirect(url_for('list_rides'))
    return render_template('create_ride.html')

@app.route('/rides/<int:ride_id>/book', methods=['POST'])
def book_ride(ride_id):
    booking_data = {
        "passenger_name": request.form["passenger_name"]
    }
    
    response = requests.post(
        f"{API_URL}/rides/{ride_id}/book",
        json=booking_data
    )
    
    return redirect(url_for('list_rides'))


if __name__ == '__main__':
    app.run(debug=True)