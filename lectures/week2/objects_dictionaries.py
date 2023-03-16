class Company:
    # Changed this to accept a dictionary
    def __init__(self, data_dictionary):
        self.name = data_dictionary["name"]
        self.slogan = data_dictionary["slogan"] # Ctrl/Cmd + D to highlight multiple instances of the first item you want to change
        self.employee_count = data_dictionary["employee_count"] # Alt + Shift + Down to copy the current line below
        self.location = data_dictionary["location"] # Alt + Shift + Down to copy the current line below
        self.revenue_more_than_1_billion = False # Every Company will be assumed for now to not make more than $1 billion in revenue
        self.electronics = [] # Empty list that will hold Electronics eventually

    def hire_employee(self): # Method to add an employee
        self.employee_count += 1
        return self # Allows for chaining
        
        # cls() means Company()
    
    def build_new_electronic(self, new_item): # new_item is going to be an Electronic
        self.electronics.append(new_item)

class Electronic:
    inspector = "FCC" # Class variable - tied directly to the class itself and not a specific Electronic

    # cls() means Electronic()

    # Due to time, didn't change this to accept a dictionary - try it yourself!
    def __init__(self, name, size, type, release_year):
        self.name = name
        self.size = size
        self.type = type
        self.release_year = release_year
        self.company = None # Placeholder that will eventually hold a Company

    # def add_company(self, company_object):
    #     self.company = company_object

    @classmethod
    def rename_inspector(cls, new_name):
        cls.inspector = new_name

    @staticmethod
    def is_examined_by_someone(is_inspected):
        if is_inspected == True:
            return "This item has been inspected"
        else:
            return "This item has not been inspected"
        
company_list = [
    {
        "name": "Dell",
        "slogan": "Innovation that stops at nothing.", # Ctrl/Cmd + D to highlight multiple instances of the first item you want to change
        "employee_count": 20000, # Alt + Shift + Down to copy the current line below
        "location": "Austin, TX"
    },
    {
        "name": "Apple",
        "slogan": "Think different.", # Ctrl/Cmd + D to highlight multiple instances of the first item you want to change
        "employee_count": 200000, # Alt + Shift + Down to copy the current line below
        "location": "Cupertino, CA"
    }
]

company_objects_list = []
for this_company_dictionary in company_list: # Go through list of dictionaries
    company_objects_list.append(Company(this_company_dictionary)) # Create new object, then add to list

for this_company_object in company_objects_list: # Go through list of objects (class instances)
    print(this_company_object.slogan) # Display slogan from object (note the . as this is an object, NOT a dictionary)