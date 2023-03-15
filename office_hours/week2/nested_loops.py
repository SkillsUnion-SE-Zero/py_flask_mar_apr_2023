my_dictionary = {
    "menu": ["Teriyaki","Rice","Pizza","Cheeseburger"],
    "employees": ["Adrian", "Jennifer", "Jane", "Jack", "Randy"]
}

# print(my_dictionary["menu"])

# Loop to go through each key in this dictionary
for this_key in my_dictionary: # Alternately could do "for this_key in my_dictionary.keys()" (other ways as well)
    print(this_key)
    print(my_dictionary[this_key])
    cur_list = my_dictionary[this_key] # Added for clarity to show that we're looking at a list linked to the current key right now
    for this_item in cur_list: # Alternately, "for this_index in range(len(my_dictionary[this_key])):"
        print(this_item)

