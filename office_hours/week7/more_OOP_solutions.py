class Ship:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_ships(cls):
        query = "SELECT * FROM ships;"
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

class Sailor:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

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


# In your controller file, you would do something like this to call on the class method:
sailor_list = Sailor.get_all_sailors() # or sailor.Sailor.get_all_sailors() if you import the entire model file ("sailor.py" file with the model called "Sailor")
# Loop through each sailor and display their full name (good practice for when you do it in your HTML):
for each_sailor in sailor_list:
    print(each_sailor.first_name + " " + each_sailor.last_name)

# In controller, grab from database by calling on the model
ship_list = Ship.get_all_ships()
for each_ship in ship_list: # Print each ship's name
    print(each_ship.name)

one_sailor_with_ship_results = [
    {
        "id": 1, "first_name": "Adrian", "last_name": "Barnard", "created_at": "???", "updated_at": "???", 
        "ships.id": 3, "name": "USS Michigan", "ships.created_at": "???", "ships.updated_at": "???"
    }
]

sailors_with_ships_results = [
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