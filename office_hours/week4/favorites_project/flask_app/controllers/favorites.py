from flask_app import app
from flask import render_template, redirect, request, session

@app.route("/")
def main_page():
    return render_template("favorite_form.html")

@app.route('/process_form', methods=["POST"])
def process_form():
    # print("Request object:")
    # print(request.__dict__)
    print("Request.form data:")
    print(request.form)
    # Saving the previous values, but only if this is the 2nd time or later,
    # as the first time session variables won't exist yet, hence the need to check
    if "favorite_band" in session:
        session["old_favorite_band"] = session["favorite_band"]
    if "favorite_color" in session:
        session["old_favorite_color"] = session["favorite_color"]
    if "favorite_food" in session:
        session["old_favorite_food"] = session["favorite_food"]
    # Saving the new values
    session["favorite_band"] = request.form["favorite_band"]
    session["favorite_color"] = request.form["favorite_color"]
    session["favorite_food"] = request.form["favorite_food"]
    return redirect("/results")

@app.route("/results")
def results_page():
    return render_template("results.html")

# Temporary route to reset session for debugging purposes
@app.route("/reset")
def clear_session():
    session.clear()
    return redirect("/")