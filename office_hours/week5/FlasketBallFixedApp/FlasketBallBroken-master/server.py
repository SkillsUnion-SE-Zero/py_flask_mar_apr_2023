from flask import Flask, request, redirect, session, flash, render_template
app = Flask(__name__)
app.secret_key = "unicorns"


@app.route('/') 
def index():

    return render_template("index.html") # Minor fix: removed the comma as it's not needed

@app.route('/leaderboard')
def leaderBoard():

    return render_template("leaderboard.html")


# Bug fix 7: Added "int:" to ensure that the path variable is
# converted to an integer, otherwise it comes back as a string
# by default, and '1' != 1
@app.route('/show/<int:rank>')
def show(rank):

    if rank == 1: 
        name = session['first']
    elif rank == 2:
        name = session['second']
    else:
        name = session['third']

    return render_template("showFriend.html", rank=rank, name=name)



@app.route('/enter', methods = ['POST'])
def enter():
    print(request.form)
    # Bug fix 2: Fixed the fields inside the quotes
    name = request.form["first_name"] + " " + request.form["last_name"]
    # Bug fix 3: Changed key in quotes from "user_name" to "name" to match up
    # with the h1 tag in line 20 of leaderboard.html
    session['name'] = name
    return redirect('/leaderboard')


# Bug fix 4: Need methods=["POST"] as we're handling form data
@app.route("/changeRanks", methods=["POST"])
def changeRanks():
    # Bug fix 6: Need to save these in session
    session["first"] = request.form['first']
    session["second"] = request.form['second']
    session["third"] = request.form['third']
    # Bug fix 5: You can't pass variables along when you redirect
    # no "first = first", "second = second", "third = third"
    return redirect('/leaderboard')

    

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)