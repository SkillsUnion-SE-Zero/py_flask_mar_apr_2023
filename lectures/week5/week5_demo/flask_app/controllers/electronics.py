from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models import electronic, company # Import models

# Route to display new electronic form
@app.route("/electronics/new")
def new_electronic_form():
    # still need to check whether someone is logged in
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    all_companies = company.Company.get_all_companies()
    return render_template("add_electronic.html", all_companies = all_companies)

# View all electronics
@app.route("/electronics")
def all_electronics_page():
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    all_electronics = electronic.Electronic.get_all_electronics_with_companies()
    return render_template("all_electronics.html", all_electronics = all_electronics)

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
    # Let's use request.form to directly pass in the data as a dictionary (be careful if you use inputs like checkboxes and radio buttons)
    new_id = electronic.Electronic.add_one_electronic(request.form)
    return redirect(f"/electronics/{new_id}") # Redirect to new electronic's page

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
