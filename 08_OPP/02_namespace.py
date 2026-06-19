class Tea:
    origin = 'shylet'

print(Tea.origin)
# Add propertities 
Tea.is_hot = True
print(Tea.is_hot)


# Creating object from Tea class 
masala = Tea()
print(masala.origin)
print(masala.is_hot)

masala.is_hot = False
print(Tea.is_hot) # class value
print(masala.is_hot) # Object value 

masala.flavour = 'Masala'
print(masala.flavour)