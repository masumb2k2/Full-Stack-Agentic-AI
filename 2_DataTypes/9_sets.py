essentiaal_item = {'Rice', 'Potatoo', 'onion','Garlic'}
optional_item = {'Garlic','soap','shampoo'}

# Union operation --|
all_shop_item = essentiaal_item | optional_item
print(f"All shop item : {all_shop_item}")

# common Item // & - intersection 
common_item = essentiaal_item & optional_item
print(f"Common Items : {common_item}")

# differece 
diffence = essentiaal_item - optional_item
print(f"diffrence Items : {diffence}")

# membership testing 
print(f"is 'Garlic' in essential item : {'Garlic' in essentiaal_item}")