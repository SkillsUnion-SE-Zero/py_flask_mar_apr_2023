from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import flight

# Add routes here!
@app.route("/flights")
def all_flights_page():
    all_flights = flight.Flight.get_all_with_carriers()
    return render_template("all_flights.html", all_flights = all_flights)

@app.route("/flights/<int:id>")
def show_flight_page(id):
    data = {
        "id": id,
    }
    one_flight = flight.Flight.get_one_with_carrier(data)
    return render_template("view_flight.html", this_flight = one_flight)