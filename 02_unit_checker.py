# measurement dictionary
measurement_dict = {
    "mm": "millimeter",
    "cm":"centimeter",
    "m":"meter",
    "km":"kilometer",
    "ms":"millisecond",
    "sec":"second",
    "min":"minute",
    "hr":"hour",
    "d":"day",
    "mg": "milligram",
    "g": "gram",
    "kg": "kilogram",
    "t": "tonnes",
}

# code
def unit_checker(question, dictionary):

    """
     Prompts the user with a question and ensures their input matches
     one of the keys in the provided dictionary. It also dynamically
     formats a clean error message based on the available options.

    """

    # Initialise an empty string to accumulate the first few dictionary keys
    options = ""

    # Initialise an empty list to store all the keys from the dictionary
    key_list = []

    # Loop through the dictionary to extract
    # all of its keys and add each key.
    for key in dictionary:
        key_list.append(key)

    # Slice the list to get all the keys EXCEPT the very last one
    most_keys = key_list[:-1]

    # Grab just the very last key from the list
    last_key = key_list[-1]

    # Loop through all keys except the last one
    for thing in most_keys:
        options += f"{thing}, "

    # --- Formatting the Error Message ---
    # Case 1: If there is only 1 item in the dictionary
    if len(dictionary) == 1:
        end_bit = key_list[0]

    # Case 2: If there are exactly 2 items
    elif len(dictionary) == 2:
        end_bit = f"{key_list[0]} or {key_list[1]}"

    # Case 3: If there are 3 or more items
    # (e.g. "a, b, or c")
    else:
        end_bit = f"{options} or {last_key}"

    # final error message
    error = f"Your unit is invalid. Please choose an option from: {end_bit}."
    # --- Input Validation Loop ---
    while True:
       # Ask the user the question
       response = input(question).strip().lower()

       # Check if the cleaned user response exits as a
       # key in the dictionary
       if response in dictionary or response in dictionary.values():
           # If it is valid, return the response
           return response

       else:
           print(error)
           print()


# Main Routine goes here
print()
users_unit = unit_checker("Unit: ", measurement_dict)

if users_unit in measurement_dict:
    abbreviation = users_unit
    full_name = measurement_dict[users_unit]

    print(f"'{abbreviation}' refers to '{full_name}'")
    print(f"'{full_name} is your chosen unit")

else:
    full_name = users_unit
    print(f"'{full_name}' is your chosen unit")
