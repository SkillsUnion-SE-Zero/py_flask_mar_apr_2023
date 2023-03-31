from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models import company # Import the file so we can call on the class methods (need file to avoid circular imports)
@app.route("/")
def login_page(): # View the login page
    return render_template("login.html")

@app.route("/companies/new")
def new_company_page(): # showing the new company page
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    return render_template("add_company.html")

@app.route("/companies")
def all_companies_page(): # all companies page
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    # Now grabbing info from DB instead of using session
    all_company_objects = company.Company.get_all_companies()
    # print(request.form) # Form data is now gone from logging in!
    return render_template("all_companies.html", list_of_company_objects = all_company_objects)

@app.route("/login", methods=["POST"])
def login_user(): # Logging in a user
    print(session)
    # print(request.form)
    session["name"] = request.form["your_name"] # Save user in session (temporary log-in)
    print(session)
    return redirect("/companies")

@app.route("/logout")
def logout_user(): # Logging out a user
    session.pop("name")
    # session.clear() # Remove all key-value pairs from session
    return redirect("/") # Send back to login route

@app.route("/companies/add", methods=["POST"])
def add_company(): # Adding a company
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    # Put data from form into this new dictionary (will be more useful
    # in update and view queries)
    form_results = {
        "name": request.form["name"],
        "slogan": request.form["slogan"],
        "location": request.form["location"],
        "over_one_billion": request.form["over_one_billion"],
    }
    # NEW: We're now calling on a class method to create the company
    # in the database - importing the file, so file_name.ClassName.method_name()
    company.Company.create_company(form_results)
    return redirect("/companies")

@app.route("/companies/<int:id>") # Viewing one company
def view_one_company(id):
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    # Need data dictionary as we need the ID of the company
    data = {
        "id": id
    }
    # Grab the company
    this_company = company.Company.get_one_company(data)
    return render_template("view_company.html", this_company = this_company)

@app.route("/companies/<int:id>/edit") # Showing the edit page - NOT for editing in DB
def edit_one_company_page(id):
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    pass

@app.route("/companies/<int:id>/delete") # Delete company from DB
def delete_one_company(id):
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    pass

@app.route("/companies/<int:id>/update", methods=["POST"]) # Take form data and edit company in DB
def update_company_in_db(id):
    if "name" not in session:
        print("Not logged in - going back to root route")
        return redirect("/")
    pass