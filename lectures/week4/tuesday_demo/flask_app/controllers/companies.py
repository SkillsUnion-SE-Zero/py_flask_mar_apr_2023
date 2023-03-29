from flask import render_template, request, redirect, session
from flask_app import app

@app.route("/")
def login_page(): # View the login page
    return render_template("login.html")

@app.route("/companies/new")
def new_company_page(): # showing the new company page
    pass

@app.route("/companies")
def all_companies_page(): # all companies page
    # Question for Wednesday - how can we check to see
    # whether a user actually filled out the form to log in?
    # Hint: take a look at the login route to get you started,
    # then figure out what logic you'll need here (and in other routes).
    print("Now in companies route")
    print(request.form) # Form data is now gone from logging in!
    return render_template("all_companies.html")

@app.route("/login", methods=["POST"])
def login_user(): # Logging in a user
    # print(request.form)
    session["name"] = request.form["your_name"] # Save user in session (temporary log-in)
    return redirect("/companies")

@app.route("/logout")
def logout_user(): # Logging out a user
    # How do we clear session?
    pass

@app.route("/companies/add", methods=["POST"])
def add_company(): # Adding a company
    pass
