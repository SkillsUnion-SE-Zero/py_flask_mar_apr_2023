from flask_app.config.mysqlconnection import connectToMySQL # Don't forget to import this!

class Carrier:
    # Add class variable for schema here

    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.hq_city = data["hq_city"]
        self.year_founded = data["year_founded"]
        self.total_workers = data["total_workers"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]