from flask_app.config.mysqlconnection import connectToMySQL # Don't forget to import this!
from flask_app.models import flight

class Carrier:
    db = "carrier_schema" # Add class variable for schema here

    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.hq_city = data["hq_city"]
        self.year_founded = data["year_founded"]
        self.total_workers = data["total_workers"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # New attribute to link Flights
        self.flights = [] # Empty list that will hold many Flights

    # Grab one Carrier with all its flights
    @classmethod
    def get_one_with_flights(cls, data):
        query = """
        SELECT * FROM carriers
        LEFT JOIN flights
        ON carriers.id = flights.carrier_id
        WHERE carriers.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results) # List of dictionaries!
        print(results[0]) # Dictionary!
        # Create the Carrier object
        carrier_object = cls(results[0]) # pass in the dictionary at index 0, then create Carrier with cls() = Carrier()
        # Loop through each flight and create a Flight object to link to this Carrier
        for each_flight_dictionary in results:
            # Grab flight's info and put it in a new dictionary
            new_flight_dictionary = {
                "id": each_flight_dictionary["flights.id"], # ID is duplicate column name
                "number": each_flight_dictionary["number"],
                "starting_city": each_flight_dictionary["starting_city"],
                "ending_city": each_flight_dictionary["ending_city"],
                "created_at": each_flight_dictionary["flights.created_at"], # Duplicate column name
                "updated_at": each_flight_dictionary["flights.updated_at"], # Duplicate column name
            }
            # Create the Flight object
            new_flight_object = flight.Flight(new_flight_dictionary)
            # Link this Flight to this Carrier
            carrier_object.flights.append(new_flight_object)
        print(carrier_object.flights[0].starting_city) # For testing purposes
        return carrier_object