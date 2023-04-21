class Ship:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.sailors = [] # This will hold a bunch of Sailors, so we'll use an empty list

    # Grab all ships - no sailors 
    @classmethod
    def get_all_ships(cls):
        query = "SELECT * FROM ships;" # Query to grab all ships - no sailors linked
        # Simulated data - hard-coded to represent actual data from your database
        ship_results = [  # This is where you would actually connect to MySQL to grab the actual data
            {"id": 1, "name": "USS Oregon", "created_at": "???", "updated_at": "???"},
            {"id": 2, "name": "HMS London", "created_at": "???", "updated_at": "???"},
            {"id": 3, "name": "USS Michigan", "created_at": "???", "updated_at": "???"},
        ]
        ship_object_list = []
        # Loop through each dictionary from the list we got back from our query
        for each_ship_dictionary in ship_results:
            # Create Ship objects
            # Approach 1: Ship(each_ship_dictionary); Approach 2: cls(each_ship_dictionary)
            new_ship_object = cls(each_ship_dictionary) # cls() means call on the __init__ method in this class - the Ship class
            ship_object_list.append(new_ship_object) # Add this Ship to the list of Ship objects
        return ship_object_list
    
    # Grab one Ship with all Sailors linked
    @classmethod
    def get_one_ship_with_sailors(cls, data):
        query = """
        SELECT * FROM ships
        LEFT JOIN sailors
        ON ships.id = sailors.ship_id
        WHERE ships.id = %(id)s;
        """ # Need ??? because we want to make sure we grab the ship's info, regardless of the number of sailors linked
        one_ship_with_sailors_results = [
            {
                "id": 3, "name": "USS Michigan", "created_at": "???", "updated_at": "???",
                "sailors.id": 1, "first_name": "Adrian", "last_name": "Barnard", "sailors.created_at": "???", "sailors.updated_at": "???"
            },
            {
                "id": 3, "name": "USS Michigan", "created_at": "???", "updated_at": "???",
                "sailors.id": 3, "first_name": "Jenny", "last_name": "Rocket", "sailors.created_at": "???", "sailors.updated_at": "???"
            },
        ]
        # Create the Ship object
        this_ship = cls(one_ship_with_sailors_results[0])
        # Go through each dictionary
        for this_sailor_dictionary in one_ship_with_sailors_results:
            # Grab the sailor's info
            corrected_sailor_dictionary = {
                "id": this_sailor_dictionary["sailors.id"],
                "first_name": this_sailor_dictionary["first_name"],
                "last_name": this_sailor_dictionary["last_name"],
                "created_at": this_sailor_dictionary["sailors.created_at"],
                "updated_at": this_sailor_dictionary["sailors.updated_at"],
            }
            # Create the Sailor object
            this_sailor_object = Sailor(corrected_sailor_dictionary)
            # Link the Sailor to this Ship
            this_ship.sailors.append(this_sailor_object)
        return this_ship

class Sailor:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ship = None # Hold only ONE Ship object, so a placeholder of None will do

    @classmethod
    def get_all_sailors(cls):
        # Query to grab all sailors (no ships linked yet)
        query = "SELECT * FROM sailors;"
        # Simulated data - hard-coded to represent actual data from your database
        sailor_results = [ # This is where you would actually connect to MySQL to grab the actual data
            {"id": 1, "first_name": "Adrian", "last_name": "Barnard", "created_at": "???", "updated_at": "???", "ship_id": 3},
            {"id": 3, "first_name": "Jenny", "last_name": "Rocket", "created_at": "???", "updated_at": "???", "ship_id": 3},
            {"id": 4, "first_name": "John", "last_name": "Doe", "created_at": "???", "updated_at": "???", "ship_id": 2},
            {"id": 5, "first_name": "Penny", "last_name": "Lane", "created_at": "???", "updated_at": "???", "ship_id": 2},
        ]
        print(sailor_results)
        sailor_object_list = [] # Hold a bunch of Sailor objects
        # Create a bunch of Sailor objects (class instances)
        for each_sailor_dictionary in sailor_results:
            print(each_sailor_dictionary)
            # Create Sailor objects
            # Approach 1: Sailor(each_sailor_dictionary); Approach 2: cls(each_sailor_dictionary)
            new_sailor_object = cls(each_sailor_dictionary) # cls() means call on the __init__ method in this class - the Sailor class
            print("ID = " + str(new_sailor_object.id))
            print(f"First name of sailor: {new_sailor_object.first_name}")
            sailor_object_list.append(new_sailor_object)
        return sailor_object_list # Make sure you indent correctly!  Notice this is NOT inside your for loop
    
    # Grab one Sailor with a Ship linked
    @classmethod
    def get_one_sailor_with_ship(cls, data):
        query = """
        SELECT * FROM sailors
        JOIN ships
        ON ships.id = sailors.ship_id
        WHERE sailors.id = %(id)s;
        """
        one_sailor_with_ship_results = [ # SIMULATED (HARD-CODED) data that would come from your database
            {
                "id": 1, "first_name": "Adrian", "last_name": "Barnard", "created_at": "???", "updated_at": "???", 
                "ships.id": 3, "name": "USS Michigan", "ships.created_at": "???", "ships.updated_at": "???"
            }
        ]
        # Create the Sailor object
        sailor_object = cls(one_sailor_with_ship_results[0])
        print("Entire list:")
        print(one_sailor_with_ship_results)
        print("First dictionary in the list:")
        print(one_sailor_with_ship_results[0])
        # Create the Ship object
        new_ship_dictionary = {
            "id": one_sailor_with_ship_results[0]["ships.id"], # Remember how to access values in lists vs. dictionaries!
            "name": one_sailor_with_ship_results[0]["name"],
            "created_at": one_sailor_with_ship_results[0]["ships.created_at"],
            "updated_at": one_sailor_with_ship_results[0]["ships.updated_at"],
        }
        ship_object = Ship(new_ship_dictionary) # In your models, you may have to do ship.Ship
        sailor_object.ship = ship_object # Linking the Ship to this Sailor
        print(f"Name of sailor: {sailor_object.first_name} {sailor_object.last_name}")
        print(f"Assigned to the ship {sailor_object.ship.name}")
        return sailor_object

    # Grab all sailors with ships
    @classmethod
    def get_all_sailors_with_ships(cls):
        query = """
        SELECT * FROM sailors
        JOIN ships
        ON ships.id = sailors.ship_id;
        """
        sailors_with_ships_results = [ # HARD-CODED EXAMPLE OF DATA that would come from your database
            {
                "id": 1, "first_name": "Adrian", "last_name": "Barnard", "created_at": "???", "updated_at": "???", 
                "ships.id": 3, "name": "USS Michigan", "ships.created_at": "???", "ships.updated_at": "???"
            },
            {
                "id": 3, "first_name": "Jenny", "last_name": "Rocket", "created_at": "???", "updated_at": "???",
                "ships.id": 3, "name": "USS Michigan", "ships.created_at": "???", "ships.updated_at": "???"
            },
            {
                "id": 4, "first_name": "John", "last_name": "Doe", "created_at": "???", "updated_at": "???",
                "ships.id": 2, "name": "HMS London", "ships.created_at": "???", "ships.updated_at": "???"
            },
            {
                "id": 5, "first_name": "Penny", "last_name": "Lane", "created_at": "???", "updated_at": "???",
                "ships.id": 2, "name": "HMS London", "ships.created_at": "???", "ships.updated_at": "???"
            },
        ]
        all_sailor_objects = [] # Hold a bunch of Sailors
        # Loop through your list of sailor dictionaries
        for sailor_dictionary in sailors_with_ships_results:
            print(sailor_dictionary)
            # Create the Sailor object
            sailor_object = cls(sailor_dictionary)
            # Create the Ship object
            new_ship_dictionary = {
                "id": sailor_dictionary["ships.id"], # Remember how to access values in lists vs. dictionaries!
                "name": sailor_dictionary["name"],
                "created_at": sailor_dictionary["ships.created_at"],
                "updated_at": sailor_dictionary["ships.updated_at"],
            }
            ship_object = Ship(new_ship_dictionary) # In your models, you may have to do ship.Ship
            sailor_object.ship = ship_object # Linking the Ship to this Sailor
            print(f"Name of sailor: {sailor_object.first_name} {sailor_object.last_name}")
            print(f"Assigned to the ship {sailor_object.ship.name}")
            # add this Sailor to the list of Sailor objects
            all_sailor_objects.append(sailor_object)
        return all_sailor_objects # Make sure this is NOT in your for loop

# In your controller file, you would do something like this to call on the class method:
sailor_list = Sailor.get_all_sailors() # or sailor.Sailor.get_all_sailors() if you import the entire model file ("sailor.py" file with the model called "Sailor")
# Loop through each sailor and display their full name (good practice for when you do it in your HTML):
for each_sailor in sailor_list:
    print(each_sailor.first_name + " " + each_sailor.last_name)

# In controller, grab from database by calling on the model
ship_list = Ship.get_all_ships()
for each_ship in ship_list: # Print each ship's name
    print(each_ship.name)

# Grabbing one sailor with a ship
# Disclaimer: In your controller, you would have to pass in an ID of some sort
one_sailor_with_ship = Sailor.get_one_sailor_with_ship({"id": 1})
print(one_sailor_with_ship.first_name)
print(one_sailor_with_ship.ship.name)

# Grabbing all sailors with ships
all_sailors_with_ships = Sailor.get_all_sailors_with_ships()
for each_sailor in all_sailors_with_ships:
    print(each_sailor.first_name)
    print(each_sailor.ship.name)

# Grabbing one ship with salors
print("One ship with sailors:")
one_ship_with_sailors = Ship.get_one_ship_with_sailors({'id': 3})
print(one_ship_with_sailors.name)
for each_sailor in one_ship_with_sailors.sailors:
    print(each_sailor.first_name)