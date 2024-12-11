from flask import Flask, render_template, request, redirect, url_for, session
import requests
import os
app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")
API_URL = "http://127.0.0.1:8000"

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/api/rides", methods=["GET"])
def list_rides():
    response = requests.get(f"{API_URL}/api/rides")
    if response.status_code == 200:
        rides = response.json().get("rides", [])
        return render_template("rides_list.html", rides=rides)
    else:
        return f"Failed to fetch rides: {response.status_code}", response.status_code

@app.route('/rides/new', methods=['GET', 'POST'])
def create_ride():
    if request.method == 'POST':
        if "token" not in session:
            return redirect(url_for('login'))

        ride_data = {
            "departure_location": request.form["departure_location"],
            "arrival_location": request.form["arrival_location"],
            "departure_time": request.form["departure_time"],
            "available_seats": int(request.form["available_seats"]),
            "driver_name": request.form["driver_name"]
        }
        headers = {"Authorization": f"Bearer {session['token']}"}
        response = requests.post(f"{API_URL}/api/rides", json=ride_data, headers=headers)
        if response.status_code == 201:
            return redirect(url_for('list_rides'))
        else:
            return f"Failed to create a ride: {response.json().get('detail', 'Unknown error')}", response.status_code

    return render_template('create_ride.html')

@app.route("/rides/<int:ride_id>/book", methods=["POST"])
def book_ride(ride_id):
    token = session.get("token")
    if not token:
        return redirect(url_for("login"))
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "passenger_name": session.get("username", "Anonymous")
    }
    response = requests.post(f"{API_URL}/auth/rides/{ride_id}/book", headers=headers, json=payload)
    if response.status_code == 200:
        return redirect(url_for("list_rides"))
    return f"Failed to book ride: {response.json().get('detail', 'Unknown error')}", response.status_code

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        response = requests.post(
            f"{API_URL}/auth/login",
            data={"username": username, "password": password},
            )
        if response.status_code == 200:
            session["token"] = response.json()["access_token"]
            
            return redirect(url_for("index"))

        else:
            return "login failed", 401
    return render_template("index.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    response = requests.post(
        f"{API_URL}/auth/register",
        json={"username": username, "email": email, "password": password},
    )
    if response.status_code == 200:
        return redirect(url_for("index"))
    else:
        return "Registration failed", 400


if __name__ == '__main__':
    app.run(debug=True)
