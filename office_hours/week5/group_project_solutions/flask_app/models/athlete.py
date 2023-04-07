from flask_app.config.mysqlconnection import connectToMySQL

class Athlete:
    db = "athletes_schema_apr_2023" # Put your schema name here!

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.sport = data["sport"]
        self.birthdate = data["birthdate"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # You will write your class methods here to add an athlete to the database and grab all athletes!

    # Class method to add the new athlete to the database
    @classmethod
    def add_athlete(cls, data):
        query = """
        INSERT INTO athletes
        (first_name, last_name, sport, birthdate, description)
        VALUES (%(first_name)s, %(last_name)s, %(sport)s, %(birthdate)s, %(description)s);
        """
        return connectToMySQL(cls.db).query_db(query, data)
    
    # Class method to grab all athletes
    @classmethod
    def get_all_athletes(cls):
        query = "SELECT * FROM athletes;"
        results = connectToMySQL(cls.db).query_db(query) # "results" variable is a LIST of DICTIONARIES
        all_athlete_objects = [] # List that will hold all Athlete objects created
        # Looping through each dictionary in the list of dictionaries from your database
        for this_athlete_dictionary in results:
            # cls() means create a class object from within the class - in this case, cls() means Athlete()
            new_athlete_object = cls(this_athlete_dictionary)
            all_athlete_objects.append(new_athlete_object) # Add Athlete object to new list
        return all_athlete_objects


