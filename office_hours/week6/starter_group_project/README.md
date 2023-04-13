# This is starter code for the week 6 group challenge.

For this week, we will focus on reading stuff from the database and practice joining tables.  We will not focus on creating, updating or deleting through the app for this set of challenges due to time.  A lot of folks have struggled with grabbing data and creating objects, along with linking these objects together.

You're encouraged to add create, update and delete to this app on your own.

## Project set-up
1. Grab the .zip folder.  Create a new virtual environment by installing the needed packages - flask and pymysql.
2. Find a place to unzip this folder.
3. Take the schema in the folder named "ERD_folder" and forward-engineer that schema.  You may rename the schema if you wish.
4. If necessary, please go to your mysqlconnection.py file and change the password.  Also change the port number in your server.py file if needed.
5. Install as needed.

## SQL query practice
1. Add at least 3 carriers to your database.  You may use any values you wish.
2. Now add at least 2 flights to your database.  Make sure you link a carrier each time!
3. Write a query that grabs all flights with their carriers.
4. Write a query that grabs a single flight - AND the carrier linked to the flight.
5. Write a query that grabs a carrier with all its flights.  Make sure you can grab the carrier's info regardless of the number of flights linked.

## Flask practice
You will notice there are no HTML files.  Also, the controller files are basically empty except for some imports.  The models only initially contain the `__init__` method.

1. Create a route that will show all flights with their carriers.
2. Now create a class method to grab those flights with carriers.  You will need to add at least one new attribute in your init method.  Don't forget to add your schema name!
3. Create an HTML file that will display those flights and carriers.  For this exercise, make sure it includes a table with the following at a minimum:
- ID of the Flight
- Flight number
- Name of the carrier linked to this flight
Don't forget to pass this information to the HTML!

Now let's focus on grabbing one flight with a carrier.
1. Create a route that will show one flight with its carrier.
2. Now create a class method to grab the flight linked with its carrier.
3. Create an HTML file that will display the flight and carrier.  Display all information about the flight, excluding the created_at and updated_at columns, and show the name of the carrier.

Now let's grab one carrier and all its flights.
1. Create a new route that will show one carrier and all its flights.
2. Make a new class method to grab the carrier with its flights.
3. Now create a new HTML file to display the carrier and its flights.  Make sure you can display each flight's number, starting city and destination (ending) city.

