"""
For today, we will practice modularization and using Flask for these group exercises.
We won't yet tie in a database.  We'll do that in today's lecture.
"""

"""
Part 1: Creating a modularized project

1. Create a new project folder.
2. Go inside this new project folder.  Create a new folder called flask_app and a new Python file called server.py.
3. Install Flask.  (You can choose to install PyMySQL, but you don't need it for this exercise.)
4. Inside the flask_app folder, create the following:
    - config folder
    - controllers folder
    - models folder
    - static folder
    - templates folder
    - A new .py file called __init__.py - make sure you have two underscores _ on each side of "init"!
5. In your __init__.py file, make sure you have the following: creating the app variable, and creating a secret key for session.
6. In your server.py file, make sure you import the app and add the logic for running the app.

We will create a controller and import it in our server file soon.  Same with adding HTML.
"""

"""
Part 2: Adding some routes and HTML
For this exercise, you may use any route names you wish.
1. Create a new file in your controllers folder called "favorites.py".
2. Create the following:
    - An HTML file with a form where a user can enter a favorite food, favorite color and favorite band/artist.
      Feel free to add additional fields - especially other input types!  The solutions won't show this to encourage
      you to try this on your own.
    - A route that shows this HTML file in your controller, favorites.py.
3. Add a new route in your controller that will process the form and add each field separately into session.  Don't forget
   to add this route in your form!  What type of HTTP request method is this?
4. Add the following:
    - A new route that will display the results from your form.
    - A new HTML file that will display the results from your form.
    - Make sure you redirect properly to this route!

Make sure you test your project!  Don't forget to activate your virtual environment!
"""

"""
Part 3: More session practice (tricky challenges ahead)
Let's add some session variables that will show the *previous* values entered in the form, and display the previous and current
values in the page that displays the results.
1. In your route that will process the new form, start with the following:
    - Create new session variables that hold the old values from your form.  Where would you put this - before or after you grab
    the new values?
    - Can you think of a scenario where the code will break?  If so, how can we fix this?
2. Now go to the page with the results and display both the new values and the old values.  Make sure this works if it's the first
time the form was done (i.e. the form wasn't filled out beforehand) or if was filled out multiple times.
"""