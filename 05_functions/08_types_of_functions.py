def pure_tea(cups): # pure function
    return cups *10

total_tea = 0

# Not Recommended
def impure_tea(cups): # impure function
    global total_tea
    total_tea +=cups

# Recusrsive function = call itself inside its body
def pour_tea(n):
    if n==0:
        return 'All cups are pure'
    return pour_tea(n-1) 

print(pour_tea(3))


# Lamdas Function (annonumous function)
tea_types = ['Light', 'kadak', 'gingar', 'kadak']

strong_tea = list(filter(lambda tea: tea !='kadak',tea_types))
print(strong_tea)