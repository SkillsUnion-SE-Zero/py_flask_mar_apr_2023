# Write a function that takes in a list as input and returns the maximum value.  If the list is empty, return None.

this_list = [3, 4, 1, 8, 5]
another_list = [2, 10, 7]

def find_max_value(input_list):
    cur_max = input_list[0] # Start off with first value in list
    # Looping through the list, one value at a time
    for cur_list_value in input_list: # for this_index in range(len(input_list)):
        if cur_list_value > cur_max: # Checking to see whether the current value is bigger than the maximum found
            cur_max = cur_list_value # Setting the current value as the new maximum
    print(cur_max)
    return cur_max

max_from_this_list = find_max_value(this_list)
print(max_from_this_list)
print(find_max_value(another_list))

# Accessing values with mixed (combined) data types

this_dictionary = {
    "rooms": ["Kitchen", "Living room", "Dining room"],
    "owner": {
        "name": "Jack Doe",
        "age": 45,
        "occupation": "Very rich programmer"
    },
    "is_clean": True
}

print(this_dictionary)
# this_key = "rooms"
print(this_dictionary["rooms"]) # or [this_key] without the quotes
print(this_dictionary["rooms"][2])
print(this_dictionary["owner"]) # Accessing the owner dictionary
print(this_dictionary["owner"]["age"]) # A value within the nested owner dictionary
