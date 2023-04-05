from flask import render_template, request, redirect, session
from flask_app import app
# Import models

# Route to display new electronic form
@app.route("/electronics/new")
def new_electronic_form():
    # still need to check whether someone is logged in
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    pass

# View all electronics
@app.route("/electronics")
def all_electronics_age():
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    pass

# View one electronic
@app.route("/electronics/<int:id>")
def view_electronics_page(id):
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    pass

# Edit form for one electronic
@app.route("/electronics/<int:id>/edit")
def edit_electronic_page(id):
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    pass

# POST route for adding new electronic to database
@app.route("/electronics/add_to_db", methods=["POST"])
def add_electronic_to_db():
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    pass

# Route to delete an electronic from the database
@app.route("/electronics/<int:id>/delete")
def delete_electronic(id):
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    pass

# POST route to edit an electronic in the database
@app.route("/electronics/<int:id>/edit_in_db", methods=["POST"])
def edit_electronic_in_db(id):
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    pass
