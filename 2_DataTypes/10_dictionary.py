item_description = dict(type= 'Biscuit', weight= 250,amount=34)
print(f"Item Description : {item_description}")

# item add
item_order = {}
item_order['Grocery'] = ['Rice','onion']
item_order['Snacks'] = 'cake'
# print(f"Order items : {item_order}")

# delete item 
del item_order['Snacks']
print(f"Order items : {item_order}")

# new dictionary
item_description = {
    'name': "cake",
    'weight': 250,
    'amount': 8
}
# membership testing
print(f"is weight in description: {'weight' in item_description}")

# key , value , item separately access
# print(f"keys of Description : {item_description.keys()}")
# print(f"values of Description : {item_description.values()}")
# print(f"items of Description : {item_description.items()}")

# pop item from dictionary
last_added = item_description.popitem()
print(f"Last added item : {last_added}")

print(f"item description: {item_description}")

# update Dictionary 
old_item ={
    'Grocery': 'Rice',
    'Snacks' : 'Cake'
}

new_item = {
    'beauty' : 'soap',
    'cleaning': 'wheeel'
}
old_item.update(new_item)
print(f"Updated Old item : {old_item}")


# new dictionary
item_description = {
    'name': "cake",
    'weight': 250,
    'amount': 8
}
# Getting specific value
# item_amount = item_description['color']
# print(f"Item amount: {item_amount}")

item_color = item_description.get("color","no color")
print(f"Item color is : {item_color}")
