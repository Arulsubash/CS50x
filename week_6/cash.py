from cs50 import get_float

# Getting input:
while True:
    change = get_float("How many doller you may have: ")
    if (change > 0 or type(change) is int):
        break
doller = round(change * 100)
# quarters calculation
counter_quarters = 0
while doller >= 25:
    doller = doller - 25
    counter_quarters += 1

# dimes calculation
counter_dimes = 0
while doller >= 10:
    doller = doller - 10
    counter_dimes += 1

# nickels calculation
counter_nickels = 0
while doller >= 5:
    doller = doller - 5
    counter_nickels += 1

# pennies calculation
counter_pennies = 0
while doller >= 1:
    doller = doller - 1
    counter_pennies += 1

balence = counter_quarters + counter_dimes + counter_nickels + counter_pennies

print(balence)
