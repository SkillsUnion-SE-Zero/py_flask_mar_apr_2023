from flask_app import app
from flask import render_template, redirect, request, session
import requests, os # Import the requests and os packages

@app.route("/search", methods=["POST"])
def search_api_one_image():
    # print("Value of one environmental variable:")
    # print(os.environ.get("NASA_API_KEY"))
    api_link = f"https://api.nasa.gov/planetary/apod?api_key={os.environ.get('NASA_API_KEY')}&date={request.form['date']}"
    # Get JSON data from link using an API
    response_string= requests.get(api_link)
    raw_data = response_string.json()
    session["date"] = raw_data["date"]
    session["description"] = raw_data["explanation"]
    session["image_link"] = raw_data["hdurl"]
    return redirect("/results")

@app.route('/search/multiple', methods=["POST"])
def search_api_multiple_images():
    api_link = f"https://api.nasa.gov/planetary/apod?api_key={os.environ.get('NASA_API_KEY')}&start_date={request.form['starting_date']}&end_date={request.form['ending_date']}"
    # Get JSON data from link using an API
    response_string= requests.get(api_link)
    raw_data = response_string.json()
    # print(raw_data)
    session.modified = True # To allow us to modify lists in session
    session["results"] = []
    # Go through each object in list
    for each_result in raw_data:
        # Save raw data into dictionary
        new_dictionary = {
            "date": each_result["date"],
            "description": each_result["explanation"],
            "image_link": each_result["hdurl"],
        }
        session["results"].append(new_dictionary)
    return redirect("/results/multiple")

@app.route("/")
def search_page():
    return render_template("image_search.html")

@app.route("/results")
def results_page():
    return render_template("search_results.html")

@app.route("/results/multiple")
def multiple_results_page():
    return render_template("multi_search_results.html")