from flask_app import app # Don't forget to import the app
from flask_app.controllers import carriers, flights # Remember to import ALL your controllers!

if __name__=="__main__":
    app.run(debug=True)