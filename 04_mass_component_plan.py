mass_dict = {
    "mg": 0.001,
    "g": 1,
    "kg": 1000,
    "t": 1000000,
}

print()
# Get amount and units (assume they are valid)
amount = float(input("Amount: "))
from_unit = input("From: ")
to_unit = input("To: ")

# Multiply to get to our standard value...
standard = amount * mass_dict[from_unit]

# Divide to get to our desired value
answer = standard / mass_dict[to_unit]

print()
print(f"{amount} {from_unit} is {answer} {to_unit} ")