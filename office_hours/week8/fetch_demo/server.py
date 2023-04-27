from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def root_route():
    return render_template("index.html")

@app.route("/fetch")
def fetch():
    return jsonify({"name":"Adrian", "message": "Hello!"})
    
if __name__=="__main__":
    app.run(debug=True)