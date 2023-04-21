# Review of data types
some_list = [] # Lists are defined with the square brackets
list_of_trails = ["Pacific Crest Trail", "Appalachian Trail", "Oregon Trail"]
print(list_of_trails[2])

empty_dictionary = {} # Dictionaries are defined with the curly braces
oregon_trail = {
    "id": 1,
    "name": "Oregon Trail",
    "length": 1500,
    "highest_elevation": 9000,
    "created_at": "???",
    "updated_at": "???"
}
# Get the length of the Oregon Trail
print(oregon_trail["length"])
# Another way to grab a value
some_key = "highest_elevation"
print(oregon_trail[some_key])

class Trail:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.length = data["length"]
        self.highest_elevation = data["highest_elevation"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

# Create a Trail object
this_trail = Trail(
    {
        "id": 1, 
        "name": "Riverfront Trail", 
        "length": 10, 
        "highest_elevation": 100, 
        "created_at": "???", 
        "updated_at": "???"
    }
)

# Grab the name of this_trail:
print(this_trail.name)
# print(type(oregon_trail))

list_of_user_data = [
    {"id": 1, "first_name": "Adrian", "last_name": "Barnard", "created_at": "???", "updated_at": "???"},
    {"id": 2, "first_name": "Thomas", "last_name": "Kosta", "created_at": "???", "updated_at": "???"},
    {"id": 4, "first_name": "Bart", "last_name": "Simpson", "created_at": "???", "updated_at": "???"},
    {"id": 5, "first_name": "Ariana", "last_name": "Grande", "created_at": "???", "updated_at": "???"},
]

# Grabbing values
print(list_of_user_data)
print(list_of_user_data[2]) 
print(list_of_user_data[2]["last_name"]) # See the name Simpson
# list_of_user_data[???]

list_with_one_user = [
    {"id": 1, "first_name": "Adrian", "last_name": "Barnard", "created_at": "???", "updated_at": "???"},
]
# Create a User object with the variable list_with_one_user
new_user_object = User(list_with_one_user[0])
print(new_user_object.first_name)