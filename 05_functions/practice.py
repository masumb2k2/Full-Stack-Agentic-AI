def order_datils(tea_type , cups, amount):
    return f"Tea type {tea_type}, cups {cups}, anount {amount}"

print(order_datils('gingar',12,120))
print(order_datils(tea_type='elachi',cups=5,amount=100))

def order_items(*items, **amount):
    return f"Iteams are {items} and amount are {amount}"

print(order_items('Tea', 'cooffee', tea_amount = 12, coffee_amount = 5))

# Null value handel 
def order_values(order = None):
    if order is None:
        order = []
    print(order)
order_values([12,3,4])
