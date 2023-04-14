from flask_app.config.mysqlconnection import connectToMySQL # Don't forget to import this!
from flask_app.models import carrier # For creating Carrier objects

class Flight:
    db = "carrier_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.number = data["number"]
        self.starting_city = data["starting_city"]
        self.ending_city = data["ending_city"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # Don't forget one more attribute!!
        self.carrier = None # We'll use None as a placeholder as it'll hold only one Carrier

    @classmethod
    def get_all_with_carriers(cls):
        query = """
            SELECT * FROM flights 
            JOIN carriers
            ON flights.carrier_id = carriers.id;
        """
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        flight_object_list = []
        # Loop through this list of dictionaries (rows of data)
        for this_flight_dictionary in results:
            print(this_flight_dictionary)
            # Create Flight object
            new_flight_object = cls(this_flight_dictionary) # cls() in this case means Flight()
            # Create the Carrier object
            # Step 1: Grab the carrier's info and put it in a new dictionary
            carrier_dictionary = {
                "id": this_flight_dictionary["carriers.id"], # ID column is duplicated in flights table
                "name": this_flight_dictionary["name"],
                "hq_city": this_flight_dictionary["hq_city"],
                "year_founded": this_flight_dictionary["year_founded"],
                "total_workers": this_flight_dictionary["total_workers"],
                "created_at": this_flight_dictionary["carriers.created_at"], # Timestamp column is duplicated in flights table
                "updated_at": this_flight_dictionary["carriers.updated_at"], # Timestamp column is duplicated in flights table
            }
            # Step 2: Create the Carrier object itself
            carrier_object = carrier.Carrier(carrier_dictionary)
            # Link the Carrier and Flight
            new_flight_object.carrier = carrier_object
            # Print statement to test attributes - especially when linking classes
            print(new_flight_object.carrier.name)
            # Add this new Flight to the list of Flights
            flight_object_list.append(new_flight_object)
        return flight_object_list

    @classmethod
    def get_one_with_carrier(cls, data):
        query = """
        SELECT * FROM flights 
        JOIN carriers
        ON flights.carrier_id = carriers.id
        WHERE flights.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        # Loop through this list of dictionaries (rows of data)
        print(results[0]) # results is a list, while results at index 0 is a dictionary
        this_flight_dictionary = results[0]
        # Create Flight object
        new_flight_object = cls(this_flight_dictionary) # cls() in this case means Flight()
        # Create the Carrier object
        # Step 1: Grab the carrier's info and put it in a new dictionary
        carrier_dictionary = {
            "id": this_flight_dictionary["carriers.id"], # ID column is duplicated in flights table
            "name": this_flight_dictionary["name"],
            "hq_city": this_flight_dictionary["hq_city"],
            "year_founded": this_flight_dictionary["year_founded"],
            "total_workers": this_flight_dictionary["total_workers"],
            "created_at": this_flight_dictionary["carriers.created_at"], # Timestamp column is duplicated in flights table
            "updated_at": this_flight_dictionary["carriers.updated_at"], # Timestamp column is duplicated in flights table
        }
        # Step 2: Create the Carrier object itself
        carrier_object = carrier.Carrier(carrier_dictionary)
        # Link the Carrier and Flight
        new_flight_object.carrier = carrier_object
        # Print statement to test attributes - especially when linking classes
        print(new_flight_object.carrier.name)
        return new_flight_object