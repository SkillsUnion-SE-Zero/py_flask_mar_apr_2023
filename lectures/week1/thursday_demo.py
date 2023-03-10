# Loop through a list:
some_list = [3, 8, 2, 1, "Hello", True, "green", "Happy"]

# One way with indexes
for ind in range(len(some_list)): # Grabbing by taking each index, then referring to the list with that index
    print(some_list[ind])

# One way without indexes
for this_val in some_list: # Grabbing each value from the list directly (a "for-each" loop in other languages)
    print(this_val)

# Dictionaries
my_dictionary = {
    "name": "Adrian", # "key": value pairs, separated by commas
    "using_laptop": True,
    "age": 25
}

# Interactive question:
# Print the value linked to name for the dictionary on the screen.
print(my_dictionary["name"]) # ANSWER - accessing values in a dictionary is like a list, except we use the key instead of a number

# One way to loop through a dictionary 
for current_key in my_dictionary:
    print(current_key) # Print current key
    print(my_dictionary[current_key]) # Print value linked to the key

# Figure out the data type for these variables:
x1 = [{"id": 1}, {"id": 3}, {"id": 8}] # List - specifically a list of dictionaries
x2 = { # Dictionary
    "id": 1,
    "name": "John Doe",
    "classes": ["Python", "JavaScript"]
}
x3 = [[1, 8, 3], [3, 4, 2]] # List - list of lists (2-D array)
x4 = (8, 3, {"name":"Adrian"}) # Tuple

# Loop through x1 and grab each id's value
for val in x1:
    print(val["id"])

print(x1) # Entire list
print(x1[0]) # Specific item (dictionary) in the list
print(x1[0]["id"]) # Specific key from a specific dictionary nested inside the list