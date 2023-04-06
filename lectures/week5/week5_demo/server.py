from flask_app import app # Bring in the app from the __init__.py file!
from flask_app.controllers import companies, electronics # import all your controllers!!!

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.