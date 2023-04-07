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
    data = {
        "id": id
    }
    electronic_object = electronic.Electronic.get_one_with_company(data)
    return render_template("view_electronic.html", this_electronic = electronic_object)

# Edit form for one electronic
@app.route("/electronics/<int:id>/edit")
def edit_electronic_page(id):
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    # Grab the electronic
    data = {
        "id": id
    }
    # Grab one electronic item AND all the companies (for dropdown)
    electronic_object = electronic.Electronic.get_one_with_company(data)
    all_companies = company.Company.get_all_companies()
    return render_template("edit_electronic.html", this_electronic = electronic_object, all_companies = all_companies)

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
    # Need data dictionary as we need to know the ID
    data = {
        "id": id
    }
    electronic.Electronic.delete_electronic(data)
    return redirect("/electronics")

# POST route to edit an electronic in the database
@app.route("/electronics/edit_in_db", methods=["POST"]) # Removed path variable to demo using an ID as a hidden input
def edit_electronic_in_db():
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    print(request.form) # Just to see what's in the form
    electronic.Electronic.edit_electronic_in_db(request.form) # Send form off - this includes the ID of the electronic we're editing
    return redirect(f"/electronics/{request.form['id']}") # Since there's no path variable in the route name, we can use the ID of the electronic from the form
