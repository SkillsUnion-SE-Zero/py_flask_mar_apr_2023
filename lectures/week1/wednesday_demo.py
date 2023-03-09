"""
Interactive question:

Given a variable x, where x is the name of some location as a string, print the following:
"I love <location here>!"  Your answer must use the variable x.

For example:
x = "Seattle"
# Print out "I love Seattle!" - make sure you use "x" - do NOT hard-code this!
"""
x = "Seattle" # Don't forget the quotes for a string
# print("I love "+x+"!") # No spaces are automatically entered if you use the "+"
# print("I love",x,"!") # If you use the commas "," spaces will automatically be inserted in between each item

# f-string
this_message = f"I love {x}, and my favorite number is {33+55}!"
# print(this_message) # Or could do print(f"I love {x}!")

# Lists
my_list = [] # Empty list
this_list = [1, 3, 8, 2] # List of integers
my_new_list = [True, 3, "Hello world!", [3, 1, 5]] # Mix data types

# Tuples - read-only - you can't change their values
my_tuple = (3, 8, 4) # Note the parentheses

print(this_list[2])
this_list.append(10) # Equivalent to .push() in JS
print(this_list)
# print(my_new_list[3][2])
print(my_new_list)
print(my_new_list[3])
# Printing stuff in reverse order
print([my_new_list[3],my_new_list[2]])
print(my_new_list[3:1:-1]) # Using slicing: starting_index:ending_index_to_exclude:increment

# Conditional statements
exit_number = 55

if exit_number < 51: # Don't forget about "and", "or" for combining conditions!
    print("Stay on freeway")
elif exit_number == 51:
    print("Get off the freeway now")
else:
    print("Get off at the next exit and make a U-turn!")


# Print values from 5 to 64 in steps of 3, so 5, 8, 11, etc., inclusively
for i in range(5, 65, 3):
    print(i)


# Functions are used to perform a set of operations.  Think of this as writing a recipe.

def greeting_message(name): # name is a parameter - placeholder that will hold a value
    return "Hello, " + name + "!"

this_message = greeting_message("Adrian") # Storing the result of the function into a variable so we can reuse the result
print(this_message+"!!!")