def tea_flavours(flavour = 'masala'):
    """Return the flavour"""
    return flavour

# __dunder__
print(tea_flavours.__doc__)
print(tea_flavours.__name__)

def generate_bill(tea = 0, samosa = 0):
    """"
    Calculate the total bill of tea and samosa 
    : param tea: number of tea
    : parm: samosa : number of samosa
    : return toal
    """
    total = tea *10 +samosa*15
    return total, "Thank you"
