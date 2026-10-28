distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": .001,
}

print()
# Get amount and units (assume they are valid)
amount = float(input("Amount: "))
from_unit = input("From: ")
to_unit = input("To: ")

# Multiply to get to our standard value...
multiply_by = distance_dict[to_unit]
standard = amount * multiply_by

# Divide to get to our desired value
divide_by = distance_dict[from_unit]
answer = standard / divide_by

print(f"{amount} {from_unit} is {answer} {to_unit} ")