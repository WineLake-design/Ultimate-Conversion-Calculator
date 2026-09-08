# Ask user for a number and loop until they
# enter a number that is more than zero
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Main Routine
for item in range(0, 2):
    from_unit = num_check("How much? ")
    print(from_unit)

