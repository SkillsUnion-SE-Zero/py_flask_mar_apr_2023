from flask_app import app
from flask import render_template, redirect, request, session
import requests # Import the requests package

@app.route("/")
def main_page():
    # Get JSON data from link using an API
    response_string= requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&start_date=2023-04-18")
    print(response_string.json())
    return render_template("index.html")