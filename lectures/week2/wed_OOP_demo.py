class Company:
    # We go here when we create various Company instances
    def __init__(self, name, slogan, employee_count, location):
        self.name = name
        self.slogan = slogan # Ctrl/Cmd + D to highlight multiple instances of the first item you want to change
        self.employee_count = employee_count # Alt + Shift + Down to copy the current line below
        self.location = location # Alt + Shift + Down to copy the current line below
        self.revenue_more_than_1_billion = False # Every Company will be assumed for now to not make more than $1 billion in revenue
        self.electronics = [] # Empty list that will hold Electronics eventually

    def hire_employee(self): # Method to add an employee
        self.employee_count += 1
        return self # Allows for chaining
    
    def build_new_electronic(self, new_item): # new_item is going to be an Electronic
        self.electronics.append(new_item)

    
class Electronic:
    inspector = "FCC" # Class variable - tied directly to the class itself and not a specific Electronic

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

print(Electronic.inspector) # type()
Electronic.rename_inspector("IEEE") # Demo of class method
print(Electronic.inspector)
print(Electronic.is_examined_by_someone(False)) # Demo of static method

dell = Company("Dell","Innovation that stops at nothing.",20000,"Austin, TX")
alienware = Electronic("Alienware", 1024, "Desktop", 2015)
xps = Electronic("XPS",512, "Laptop", 2018)

# Linking classes together
dell.build_new_electronic(alienware) # Links the Electronic to the Company
alienware.company = dell # Links the Company to this Electronic

