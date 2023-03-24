from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route("/") # Root route
def main_page():
    return render_template("index.html")

@app.route("/value_demo")
def passing_along_values():
    message = 'Hello world!'
    favorite_number = 25
    companies = [
        {"id": 1, "name": "HP"},
        {"id": 2, "name": "Dell"},
        {"id": 3, "name": "Apple"}
    ]
    return render_template('value_demo.html', server_message = message, num = favorite_number, company_list = companies)

# @app.route('/blogs/<int:id>') # This allows us to specify "id" as an int instead of the default of string (data type)
# def blog_page(id): # The <int:> converts the path variable to an integer directly
#     pass 
#     # return "This is blog " + id

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

