# generates headings (eg:---- heading ----)

def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Displays instructions
def instructions():
    statement_generator("Instructions","-")

    print('''
To use this program simply enter your starting unit and 
enter your target unit. The program will automatically
calculate the conversion.

Please ensure that all units and numbers are valid to get an
accurate result.

To exit the program, please type 'xxx'.
    ''')

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")


if want_instructions == "":
    instructions()

# Repeat question
want_instructions = input("Press any key to continue ")

