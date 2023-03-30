class Company:
    # Put the database name in somewhere
    def __init__(self, data): # Note the data parameter - it's a dictionary from your database
        # Make sure column names match up with those in your tables in your schema in MySQL Workbench!
        self.id = data["id"]
        self.name = data["name"]
        self.slogan = data["slogan"]
        self.location = data["location"] 
        self.over_one_billion = data["over_one_billion"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
        # We will revisit the attribute below next week
        # self.electronics = [] # Empty list that will hold Electronics eventually