menu_item = ['black','Gingar','Out of Stock','Lemon','Green','Discontinue','Tulsi']

for item in menu_item:
    if item == 'Out of Stock':
        continue
    if item == 'Discontinue':
        print(f"{item} is found in break")
        break
    print(f"{item} is found")
    