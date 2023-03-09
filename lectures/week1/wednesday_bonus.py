"""
Given a list of integers as input, each of which is 0 to 100, inclusively, return a new list, 
where each item in the list is one of the following strings:
    - "Congratulations on earning a score of < score goes here >!" when the number is 90 or more.  
    For example, "Congratulations on earning a score of 95!"
    - "You did well with a score of < score here >!" when the number is 80-89, inclusively.
    - "You did fine with a score of < score here >!" when the number is 70-79, inclusively.
    - "It's okay!  You'll do better next time!" when the number is less than 70.
For example, if you got [85, 92, 73], you'll return:
    [
        "You did well with a score of 85!", 
        "Congratulations on earning a score of 92!", 
        "You did fine with a score of 73!"
    ]
"""

def get_list_of_messages(score_list):
    message_list = [] # Empty list
    # For loop to go through each score
    for i in range(len(score_list)): # don't use x - use the parameter name!
        # Grabbing the current score
        this_score = score_list[i]
        # Determine which message to use based on the score
        if this_score >= 90:
            this_message = f"Congratulations on earning a score of {this_score}!"
        elif this_score >= 80:
            this_message = f"You did well with a score of {this_score}!"
        elif this_score >= 70:
            this_message = f"You did fine with a score of {this_score}!"
        else:
            this_message = "It's okay!  You'll do better next time!"
        message_list.append(this_message)
    return message_list

x = [100, 80, 70, 90, 85]
print(x)
print(get_list_of_messages(x))