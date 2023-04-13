from flask import Flask
app = Flask(__name__) # Create app (instance of Flask class) so we can make it available through project
app.secret_key = "thisisasecrettoeverybody" # Needed for session and flash messages