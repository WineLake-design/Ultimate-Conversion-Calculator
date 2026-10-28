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

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")


if want_instructions == "":
    instructions()

# Repeat question
want_instructions = input("Press any key to continue ")

