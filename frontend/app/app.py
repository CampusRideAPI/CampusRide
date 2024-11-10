from flask import Flask, render_template, request, redirect, url_for
import requests


app = Flask(__name__)
API_URL = "http://localhost:8000"


@app.route('/')
def list_rides():
    response = requests.get(f"{API_URL}/rides")
    return render_template("list_rides.html", rides=response.json())

