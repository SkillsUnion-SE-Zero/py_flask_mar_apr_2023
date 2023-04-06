from flask_app.config.mysqlconnection import connectToMySQL

class Company:
    db_name = "company_electronic_schema" # NEW: Class variable to save schema name in one spot
    def __init__(self, data): # Note the data parameter - it's a dictionary from your database
        # Make sure column names match up with those in your tables in your schema in MySQL Workbench!
        self.id = data["id"]
        self.name = data["name"]
        self.slogan = data["slogan"]
        self.location = data["location"] 
        self.over_one_billion = data["over_one_billion"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.electronics = [] # NEW: Empty list that will hold MANY Electronics eventually

    @classmethod
    def create_company(cls, data):
        query = """
        INSERT INTO companies (name, slogan, location, over_one_billion) 
        VALUES (%(name)s, %(slogan)s, %(location)s, %(over_one_billion)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_all_companies(cls): # No data parameter needed because the query doesn't require specific values (e.g. id)
        query = "SELECT * FROM companies;"
        results = connectToMySQL(cls.db_name).query_db(query)
        list_of_company_objects = [] # This will hold a bunch of Company objects
        if len(results) == 0: # Nothing in DB
            return [] # Return an empty list - nothing to get
        else: # At least one company found
            # Need to take the data and create objects
            for this_company_dictionary in results:
                # Create the Company object
                new_company_object = cls(this_company_dictionary) # cls() means create an Object inside this class - in this case, Company()
                list_of_company_objects.append(new_company_object) # Add Company object to list
            # Return these objects
            return list_of_company_objects
        
    @classmethod
    def get_one_company(cls, data): # Need a data dictionary as we need to put a value inside our query
        query = "SELECT * FROM companies WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0: # Nothing in DB
            return None # Return an empty list - nothing to get
        else: # At least one company found
            # Create the Company object
            # NOTE: The variable "results" is a LIST, but we must pass in a DICTIONARY, so we
            # need a specific dictionary - in this case, at index 0
            new_company_object = cls(results[0]) # cls() means create an Object inside this class - in this case, Company()
            # Return this one object
            return new_company_object
        
    @classmethod
    def update_company(cls, data):
        query = """
        UPDATE companies SET name = %(name)s, 
        location = %(location)s, 
        slogan = %(slogan)s,
        over_one_billion = %(over_one_billion)s
        WHERE id = %(id)s;
        """ # Don't for the ID - important!!
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def delete_company(cls, data):
        query = "DELETE FROM companies WHERE id = %(id)s;" # IMPORTANT - need id!!!
        return connectToMySQL(cls.db_name).query_db(query, data)
