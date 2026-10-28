# Instructions and heading

# generates headings (eg:---- heading ----)

def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Displays instructions
def instructions():
    statement_generator("Instructions","-")

    print('''
To use this program simply enter the which category you'd like to convert. 
Options are:
 - distance 
 - time
 - mass
Then, you may enter your starting unit and 
enter your target unit relating to your chosen category. The program 
will automatically calculate the conversion.

Important note:
Please ensure that all categories, units, and numbers are valid to get an
accurate result.

If at any time you would like to stop, simply enter 'xxx'.
    ''')

# Ask user for a number and loop until they
# enter a number that is more than zero
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:
        # ask the user for a number
        response = input(question).strip().lower()
        if response == 'xxx':
            return 'xxx'
        try:
            users_amount = float(response)
            if users_amount > 0:
                return users_amount

            else:
                print(error)
        except ValueError:
            print(error)

# Dictionaries

distance_dict = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000,
}
mass_dict = {
    "mg": 0.001,
    "g": 1,
    "kg": 1000,
    "t": 1000000,
}

time_dict = {
    "ms": 0.001,
    "sec": 1,
    "min": 60,
    "hr": 3600,
    "d": 86400,
}

# code
def unit_checker(question, dictionary):

    """
     Prompts the user with a question and ensures their input matches
     one of the keys in the provided dictionary. It also dynamically
     formats a clean error message based on the available options.

    """

    # Initialise an empty list to store all the keys from the dictionary
    key_list = list(dictionary.keys())

    # Slice the list to get all the keys EXCEPT the very last one
    most_keys = key_list[:-1]

    options= ""
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
        end_bit = f"{key_list[0]}or {key_list[1]}"

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
       if response == 'xxx':
           return 'xxx'

       # Check if the cleaned user response exits as a
       # key in the dictionary
       if response in dictionary:
           # If it is valid, return the response
           return response

       else:
           print(error)
           print()

# Main Routine

want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")


if want_instructions == "":
    instructions()

# Repeat question
want_instructions = input("Press any key to continue ")

# Break
while True:
    print()
    # Ask for which category
    category = input("Select your category: ")
    if category == 'xxx':
        break

    if category == 'distance':
        chosen_dict = distance_dict
    elif category == 'mass':
        chosen_dict = mass_dict
    elif category == 'time':
        chosen_dict = time_dict
    else:
        print("Your category is invalid. Please choose from distance, mass, or time.")
        continue

    # Check if user's input is valid
    print()
    amount = num_check("Amount: ")
    if amount == 'xxx':
        break

    # Check that user's input for 'From:' is also valid
    from_unit = unit_checker("From: ", chosen_dict)
    if from_unit == 'xxx':
        break

    # Check that user's input for 'To:' is also valid
    to_unit = unit_checker("To: ", chosen_dict)
    if to_unit == 'xxx':
        break

    # Multiply to get to our standard value...
    standard = amount * chosen_dict[from_unit]

    # Divide to get to our desired value
    answer = standard / chosen_dict[to_unit]

    print()
    print(f"{amount} {from_unit} is {answer} {to_unit} ")

print()
print("Thank you for using 'Ultimate Conversion Calculator'!")
