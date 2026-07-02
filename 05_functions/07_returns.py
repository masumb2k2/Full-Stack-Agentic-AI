# def make_tea():
#     return "Here is your Masala tea"

# return_value = make_tea()
# print(return_value)


# When nothing its return none 
def ideal_teaseller():
    pass
print(ideal_teaseller())

# One Value return
def solde_cups():
    return 120
total = solde_cups()
print(total)

# Early from a function return
def tea_status(cups_left):
    if cups_left == 0:
        return "Sorry, Tea over"
    return "Tea is ready"
print(tea_status(cups_left=1))


# Return Multiple value
def tea_report():
    return 100,200 # sold & remain
sold, remaining = tea_report()
print(f"sold: {sold} Remaining: {remaining}")

# handle multiple valaue
def tea_report():
    return 100,200 , 300 # sold & remain
sold, remaining, _ = tea_report()
print(f"sold: {sold} Remaining: {remaining}")