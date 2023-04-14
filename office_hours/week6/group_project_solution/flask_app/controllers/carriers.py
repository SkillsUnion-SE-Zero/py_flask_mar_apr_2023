from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import carrier
# Add routes here!
@app.route("/carriers/<int:id>")
def view_carrier_page(id):
    data = {
        "id": id
    }
    this_carrier = carrier.Carrier.get_one_with_flights(data)
    return render_template("view_carrier.html", this_carrier = this_carrier)