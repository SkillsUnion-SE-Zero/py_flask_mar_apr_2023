from flask_app.config.mysqlconnection import connectToMySQL # Don't forget to import this!

class Flight:
    # Create a class variable here for your schema name

    def __init__(self, data):
        self.id = data["id"]
        self.number = data["number"]
        self.starting_city = data["starting_city"]
        self.ending_city = data["ending_city"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # Don't forget one more attribute!!