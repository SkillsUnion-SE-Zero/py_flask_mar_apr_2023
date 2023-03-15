# Draft 1 - hard-coded example

class TelevisionOld: # Names of classes are PascalCase - each word is capitalized
    def __init__(self):
        self.screen_size = 50
        self.brand_name = "Samsung"

my_tv = TelevisionOld()
print(my_tv.screen_size)

# Draft 2 - better version
class Television:
    def __init__(self, screen_size, this_brand):
        self.screen_size = screen_size
        self.brand_name = this_brand # Notice these don't match - that's okay; the parameter has to match the right-hand size

another_tv = Television(75,"Sony")
print(another_tv.screen_size)


class Company:
    # We go here when we create various Company instances
    def __init__(self, name, slogan, employee_count, location):
        self.name = name
        self.slogan = slogan # Ctrl/Cmd + D to highlight multiple instances of the first item you want to change
        self.employee_count = employee_count # Alt + Shift + Down to copy the current line below
        self.location = location # Alt + Shift + Down to copy the current line below

    def hire_employee(self): # Method to add an employee
        self.employee_count += 1
        return self # Allows for chaining


frys = Company("Fry's", "Your best buys are always at Fry's", 5000, "Portland")
print(frys.location)
# Change the location to "Los Angeles"
frys.location = "Los Angeles"
print(frys.location)
print(frys.employee_count)
frys.hire_employee().hire_employee()
print(frys.employee_count)