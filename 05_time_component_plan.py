time_dict = {
    "ms": 0.001,
    "sec": 1,
    "min": 60,
    "hr": 3600,
    "d": 86400,
}

print()
# Get amount and units (assume they are valid)
amount = float(input("Amount: "))
from_unit = input("From: ")
to_unit = input("To: ")

# Multiply to get to our standard value...
standard = amount * time_dict[from_unit]

# Divide to get to our desired value
answer = standard / time_dict[to_unit]

print()
print(f"{amount} {from_unit} is {answer} {to_unit} ")