from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route("/")
def start_journey():
    story_message = "In a very distant galaxy, there was a coder working on writing a program to recycle air inside their ship as it navigates between Planet X and Titania.  Suddenly air starts to decompress from one of the noncritical bays of your ship.  What do you do?"
    left_route_name = "stopleak"
    right_route_name = "letgo"
    left_text = "Attempt to stop the leak"
    right_text = "Let the air from that bay go into space"
    return render_template("story.html", left_link = left_route_name, right_link = right_route_name, msg = story_message, left_text = left_text, right_text = right_text)

# @app.route("/stopleak") # Left option from start of story
# def stop_leak():
#     story_message = "You go in and successfully fix the leak.  However, another leak appears in another bay in your ship.  Now what do you?"
#     left_route_name = "stopleak"
#     right_route_name = "letgo"
#     left_text = "Attempt to stop the leak"
#     right_text = "Let the air from that bay go into space"
#     return render_template("story.html", left_link = left_route_name, right_link = right_route_name, msg = story_message, left_text = left_text, right_text = right_text)

# @app.route("/letgo") # Right option - let air be
# def let_air_go():
#     story_message = "You decided the air was nonessential and let that air go out into the vacuum of space.  Now a warning message appears as you continue to write your algorithm to recycle your air more efficiently.  The message says that you now may not have enough air to get to Titania.  What do you do now?"
#     left_route_name = "turnback"
#     right_route_name = "continue"
#     left_text = "Turn the ship back"
#     right_text = "Continue to write on the algorithm"
#     return render_template("story.html", left_link = left_route_name, right_link = right_route_name, msg = story_message, left_text = left_text, right_text = right_text)

@app.route("/<option>") # Path variable
def story_page(option):
    if option == "stopleak": # /stopleak route
        story_message = "You go in and successfully fix the leak.  However, another leak appears in another bay in your ship.  Now what do you?"
        left_route_name = "stopleak"
        right_route_name = "letgo"
        left_text = "Attempt to stop the leak"
        right_text = "Let the air from that bay go into space"
    elif option == "letgo": # /letgo route
        story_message = "You decided the air was nonessential and let that air go out into the vacuum of space.  Now a warning message appears as you continue to write your algorithm to recycle your air more efficiently.  The message says that you now may not have enough air to get to Titania.  What do you do now?"
        left_route_name = "turnback"
        right_route_name = "continue"
        left_text = "Turn the ship back"
        right_text = "Continue to write on the algorithm"
    return render_template("story.html", left_link = left_route_name, right_link = right_route_name, msg = story_message, left_text = left_text, right_text = right_text)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.