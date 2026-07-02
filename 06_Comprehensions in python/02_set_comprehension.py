favoutire_teas = [
    'Masala Tea',
    'Green Tea',
    'Masala Tea',
    'Lemon Tea',
    'Green Tea',
    'Eleaichi Tea'
]

# unique_tea = {tea for tea in favoutire_teas }
# print(f"Uniue tea: {unique_tea}")

unique_tea = {tea for tea in favoutire_teas if len(tea) < 8 }
print(f"Uniue tea: {unique_tea}")


recipes = {
    'Masala Tea': ['ginger' ,'cardimom' ,'clove'],
    'Elechi Tea': ['Cardimon' ,'milk'],
    'Spicy Tea': ['ginger' , 'black pepper', 'clove']
}

unique_spices = {spice for ingredinets in recipes.values() for spice in ingredinets}
print(f"Unique Spices: {unique_spices}")