from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import company # Importing other model file to prevent circular imports

class Electronic:
    db_name = "company_electronic_schema" # NEW: Class variable to save schema name in one spot

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.size = data["size"]
        self.type = data["type"]
        self.release_date = data["release_date"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # We're linking ONE Company to this Electronic object
        self.company = None # This will eventually hold a Company object

    @classmethod
    def add_one_electronic(cls, data):
        query = """
        INSERT INTO electronics
        (name, size, type, release_date, company_id)
        VALUES (%(name)s, %(size)s, %(type)s, %(release_date)s, %(company_id)s);
        """ # IMPORTANT: You need the foreign key in here - company_id!!!
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_all_electronics_with_companies(cls):
        query = """
        SELECT * FROM electronics
        JOIN companies
        ON electronics.company_id = companies.id;
        """
        results = connectToMySQL(cls.db_name).query_db(query)
        all_electronic_objects = [] # Hold a bunch of Electronics
        if len(results) == 0: # Return empty list if there's no electronics
            return [] 
        else: # At least one electronic found
            # Go through each item in this list - a dictionary
            for this_electronic_dictionary in results:
                print(this_electronic_dictionary) # Showing the dictionary (so you can see what it looks like in the terminal)
                # Create the Electronic object
                new_electronic_object = cls(this_electronic_dictionary) # cls() here means Electronic()
                # Create the Company object - need new dictionary to remove table names from columns whose names are duplicates
                new_company_dictionary = {
                    "id": this_electronic_dictionary['companies.id'], # Duplicate column name when joining tables
                    "name": this_electronic_dictionary['companies.name'], # Duplicate column name when joining tables
                    "slogan": this_electronic_dictionary['slogan'],
                    "location": this_electronic_dictionary['location'],
                    "over_one_billion": this_electronic_dictionary['over_one_billion'],
                    "created_at": this_electronic_dictionary['companies.created_at'], # Duplicate column name when joining tables
                    "updated_at": this_electronic_dictionary['companies.updated_at'], # Duplicate column name when joining tables
                }
                new_company_object = company.Company(new_company_dictionary) # Do NOT use cls() here - we need to create a Company object!
                # Link the Company object to this new Electronic object
                new_electronic_object.company = new_company_object
                # Add this new Electronic to this list
                all_electronic_objects.append(new_electronic_object)
            return all_electronic_objects