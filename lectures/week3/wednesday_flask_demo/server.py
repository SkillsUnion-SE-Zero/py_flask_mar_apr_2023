from flask import Flask # If you see a squiggly line here, it's normal - don't worry about it
app = Flask(__name__)

@app.route("/hi") # Decorator that defines the route name - need the "/" at the start!!
def hello_route():
    return "Hello from Flask!" # Return this information to the client (later on HTML and other responses)

@app.route('/blog/<id>/<name>') # Path variables are enclosed within the <>
def view_blog(id, name): # Make sure you include path variables as parameters when you define your function
    return f"This is blog {id} by {name}"
    # return "This is blog " + id + " by " + name # Alternate way to display same result

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.