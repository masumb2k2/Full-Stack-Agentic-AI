# tea = 'Gingar Tea'

# def prepare_tea(order):
#     print(f"Prepring: {order}")

# prepare_tea(tea)

tea = [1,2,3]
def edit_tea(cup):
    cup[1]=42

edit_tea(tea)
print(tea) 


def make_tea(tea, milk, sugar):
    print(tea,milk, sugar)

make_tea('Dhaka','yes', 'Low') # positional
make_tea(tea='green', milk='Medium',sugar='high') # Keyword

# Args and *Kwargs
def special_tea(*ingredients , **extras):
    print("Ingredients", ingredients)
    print("Extras",extras)

special_tea("Cinamon", 'Cardmom' , sweetner= 'Honey', foam= "soap")

# def tea_orders(order = []):
#     order.append('Masala')
#     print(order)
# tea_orders()

def tea_orders(order = None):
    if order is None:
        order= []
    print(order)
tea_orders()
tea_orders()