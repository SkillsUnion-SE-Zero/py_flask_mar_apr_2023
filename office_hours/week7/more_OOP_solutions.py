class Ship:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


class Sailor:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

sailor_results = [
    {"id": 1, "first_name": "Adrian", "last_name": "Barnard", "created_at": "???", "updated_at": "???", "ship_id": 3},
    {"id": 3, "first_name": "Jenny", "last_name": "Rocket", "created_at": "???", "updated_at": "???", "ship_id": 3},
    {"id": 4, "first_name": "John", "last_name": "Doe", "created_at": "???", "updated_at": "???", "ship_id": 2},
    {"id": 5, "first_name": "Penny", "last_name": "Lane", "created_at": "???", "updated_at": "???", "ship_id": 2},
]

ship_results = [
    {"id": 1, "name": "USS Oregon", "created_at": "???", "updated_at": "???"},
    {"id": 2, "name": "HMS London", "created_at": "???", "updated_at": "???"},
    {"id": 3, "name": "USS Michigan", "created_at": "???", "updated_at": "???"},
]

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